from typing import Any, List, Tuple, Optional
from hub.core.meta.encode.base_encoder import Encoder, LAST_SEEN_INDEX_COLUMN
from hub.constants import ENCODING_DTYPE
from hub.util.exceptions import (
    ChunkIdEncoderError,
    OutOfChunkCountError,
    OutOfSampleCountError,
)
from hub.core.storage.hub_memory_object import HubMemoryObject
import numpy as np
from hub.core.serialize import serialize_chunkids, deserialize_chunkids
from hub.util.generate_id import generate_id

CHUNK_ID_COLUMN = 0


class ChunkIdEncoder(Encoder, HubMemoryObject):
    @staticmethod
    def name_from_id(id: ENCODING_DTYPE) -> str:
        """Returns the hex of `id` with the "0x" prefix removed. This is the chunk's name and should be used to determine the chunk's key.
        Can convert back into `id` using `id_from_name`. You can get the `id` for a chunk using `__getitem__`."""

        return hex(id)[2:]

    @staticmethod
    def id_from_name(name: str):
        """Returns the 64-bit integer from the hex `name` generated by `name_from_id`."""

        return int("0x" + name, 16)

    def get_name_for_chunk(self, chunk_index: int) -> str:
        """Gets the name for the chunk at index `chunk_index`. If you need to get the name for a chunk from a sample index, instead
        use `__getitem__`, then `name_from_id`."""

        chunk_id = self._encoded[:, CHUNK_ID_COLUMN][chunk_index]
        return ChunkIdEncoder.name_from_id(chunk_id)

    def get_id_for_chunk(self, chunk_index: int) -> str:
        """Gets the if for the chunk at index `chunk_index`. If you need to get the name for a chunk from a sample index, instead
        use `__getitem__`, then `name_from_id`."""

        return self._encoded[:, CHUNK_ID_COLUMN][chunk_index]

    @property
    def num_chunks(self) -> int:
        if self.num_samples == 0:
            return 0
        return len(self._encoded)

    def get_next_chunk_id(self, row) -> Optional[str]:
        if (
            self.num_chunks is None
            or self._encoded is None
            or not row < self.num_chunks - 1
        ):
            return None

        return self._encoded[row + 1][0]

    def get_prev_chunk_id(self, row) -> Optional[str]:
        if self.num_chunks is None or self._encoded is None or row == 0:
            return None

        return self._encoded[row - 1][0]

    def decrease_samples(self, row: int = 0, num_samples: int = 0):
        """Decrease sample count from encoder

        Args:
            row (int): row of the chunk
            num_samples (int): number of samples to be reduced

        Raises:
            OutOfSampleCountError: when num_samples are exeeding sample count
            OutOfChunkCountError: When the row is out of chunk bounds
        """
        if self.num_samples_at(row) < num_samples:
            raise OutOfSampleCountError()

        if self.num_chunks < row + 1:
            raise OutOfChunkCountError()

        self._encoded[row][LAST_SEEN_INDEX_COLUMN] -= num_samples

        self.is_dirty = True

    def delete_chunk_id(self, row):
        """Delete row from encoder

        Args:
            row (int): the row of chunk that needs to be deleted

        Raises:
            OutOfChunkCountError: When the row is out of chunk bounds
        """
        if row > self.num_chunks:
            raise OutOfChunkCountError

        self._encoded = np.delete(self._encoded, row, axis=0)
        self.is_dirty = True

    def generate_chunk_id(
        self, register: Optional[bool] = True, row: Optional[int] = None
    ) -> ENCODING_DTYPE:
        """Generates a random 64bit chunk ID using uuid4. Also prepares this ID to have samples registered to it.
        This method should be called once per chunk created.

        Args:
            register (Optional, bool): Whether the generated chunk id should be added to the encoder. Default True.
            row (Optional, int): Iterator position where the new generated id should be inserted

        Returns:
            ENCODING_DTYPE: The random chunk ID.

        Raises:
            OutOfChunkCountError: When the row is out of chunk bounds
        """

        id = generate_id(ENCODING_DTYPE)
        if register:
            if self.num_samples == 0:
                assert row is None
                self._encoded = np.array([[id, -1]], dtype=ENCODING_DTYPE)

            else:
                if row is not None and row < self.num_chunks:
                    new_entry = np.array(
                        [id, self._encoded[row][LAST_SEEN_INDEX_COLUMN]]
                    )
                    self._encoded = np.insert(self._encoded, row + 1, new_entry, axis=0)
                    return id
                if row is not None and row != self.num_chunks:
                    raise OutOfChunkCountError()
                last_index = self.num_samples - 1

                new_entry = np.array(
                    [[id, last_index]],
                    dtype=ENCODING_DTYPE,
                )
                self._encoded = np.concatenate([self._encoded, new_entry])
        return id

    def register_samples(self, num_samples: int, row: Optional[int] = None):  # type: ignore
        """Registers samples to the chunk ID that was generated last with the `generate_chunk_id` method.
        This method should be called at least once per chunk created.

        Args:
            num_samples (int): The number of samples the last chunk ID should have added to it's registration.
            row (int, Optional): The row of chunk to register the samples in.

        Raises:
            ValueError: `num_samples` should be non-negative.
            ChunkIdEncoderError: Must call `generate_chunk_id` before registering samples.
            ChunkIdEncoderError: `num_samples` can only be 0 if it is able to be a sample continuation accross chunks.
        """

        super().register_samples(None, num_samples, row=row)

    def translate_index_relative_to_chunks(self, global_sample_index: int) -> int:
        """Converts `global_sample_index` into a new index that is relative to the chunk the sample belongs to.

        Example:
            Given: 2 sampes in chunk 0, 2 samples in chunk 1, and 3 samples in chunk 2.
            >>> self.num_samples
            7
            >>> self.num_chunks
            3
            >>> self.translate_index_relative_to_chunks(0)
            0
            >>> self.translate_index_relative_to_chunks(1)
            1
            >>> self.translate_index_relative_to_chunks(2)
            0
            >>> self.translate_index_relative_to_chunks(3)
            1
            >>> self.translate_index_relative_to_chunks(6)
            2

        Args:
            global_sample_index (int): Index of the sample relative to the containing tensor.

        Returns:
            int: local index value between 0 and the amount of samples the chunk contains - 1.
        """

        ls = self.__getitem__(global_sample_index, return_row_index=True)  # type: ignore

        assert len(ls) == 1, len(
            ls
        )  # this method should only be called for non tiled samples
        chunk_index = ls[0][1]

        if chunk_index == 0:
            return global_sample_index

        current_entry = self._encoded[chunk_index - 1]  # type: ignore
        last_num_samples = current_entry[LAST_SEEN_INDEX_COLUMN] + 1

        return int(global_sample_index - last_num_samples)

    def _validate_incoming_item(self, _, num_samples: int):
        if num_samples < 0:
            raise ValueError(
                f"Cannot register negative num samples. Got: {num_samples}"
            )

        if len(self.array) == 0:
            raise ChunkIdEncoderError(
                "Cannot register samples because no chunk IDs exist."
            )

        if num_samples == 0 and self.num_chunks < 2:
            raise ChunkIdEncoderError(
                "Cannot register 0 num_samples (signifying a partial sample continuing the last chunk) when no last chunk exists."
            )

        # note: do not call super() method (num_samples can be 0)

    def _derive_next_last_index(self, last_index: ENCODING_DTYPE, num_samples: int):
        # this operation will trigger an overflow for the first addition, so supress the warning
        np.seterr(over="ignore")
        new_last_index = last_index + ENCODING_DTYPE(num_samples)
        np.seterr(over="warn")

        return new_last_index

    def _combine_condition(self, *args) -> bool:
        """Always returns True because sample registration can always be done. Used in base encoder `register_samples`."""

        return True

    def _derive_value(self, row: np.ndarray, *_) -> np.ndarray:
        return row[CHUNK_ID_COLUMN]

    def __setitem__(self, *args):
        raise NotImplementedError(
            "There is no reason for ChunkIdEncoder to be updated now."
        )

    def __getitem__(
        self, local_sample_index: int, return_row_index: bool = False
    ) -> Any:
        """Derives the value at `local_sample_index`.

        Args:
            local_sample_index (int): Index of the sample for the desired value.
            return_row_index (bool): If True, the index of the row that the value was derived from is returned as well.
                Defaults to False.

        Returns:
            Any: Either just a singular derived value, or a tuple with the derived value and the row index respectively.
        """

        if local_sample_index < 0:
            local_sample_index += self.num_samples

        row_index = self.translate_index(local_sample_index)
        output: List[Any] = []
        value = self._derive_value(
            self._encoded[row_index], row_index, local_sample_index
        )
        if return_row_index:
            output.append((value, row_index))
        else:
            output.append(value)

        row_index += 1

        while row_index < len(self._encoded):
            if self._encoded[row_index][LAST_SEEN_INDEX_COLUMN] == local_sample_index:
                self.last_row = row_index
                value = self._derive_value(
                    self._encoded[row_index], row_index, local_sample_index
                )
                if return_row_index:
                    output.append((value, row_index))
                else:
                    output.append(value)
                row_index += 1
            else:
                break
        return output

    def _num_samples_in_last_chunk(self):
        return self._num_samples_in_last_row()

    def pop(
        self, index: Optional[int] = None
    ) -> Tuple[List[ENCODING_DTYPE], List, bool]:
        """Pops the last sample added to the encoder and returns ids of chunks to be deleted from storage.
        Returns:
            Tuple of list of affected chunk ids, their rows and boolean specifying whether those chunks should be deleted
        """
        if index is None:
            index = self.get_last_index_for_pop()
        out = self.__getitem__(index, return_row_index=True)  # type: ignore
        chunk_ids = [out[i][0] for i in range(len(out))]
        rows = [out[i][1] for i in range(len(out))]
        if len(chunk_ids) > 1:  # tiled sample
            self._encoded[rows[-1] + 1 :, LAST_SEEN_INDEX_COLUMN] -= 1
            self._encoded = np.delete(self._encoded, rows, axis=0)
            to_delete = True
        else:
            row = rows[0]
            prev = -1 if row == 0 else self._encoded[row - 1][LAST_SEEN_INDEX_COLUMN]
            num_samples_in_chunk = self.array[row][LAST_SEEN_INDEX_COLUMN] - prev

            if num_samples_in_chunk == 1:
                self._encoded = np.delete(self._encoded, row, axis=0)
                to_delete = True
            elif num_samples_in_chunk > 1:
                self._encoded[row:, LAST_SEEN_INDEX_COLUMN] -= 1
                to_delete = False
            else:
                raise ValueError("No samples to pop")

        self.is_dirty = True
        return chunk_ids, rows, to_delete

    def _replace_chunks_for_tiled_sample(
        self, global_sample_index: int, chunk_ids: List[ENCODING_DTYPE]
    ):
        current_chunk_ids_and_rows = self.__getitem__(  # type: ignore
            global_sample_index, return_row_index=True
        )
        start_row = current_chunk_ids_and_rows[0][1]
        end_row = current_chunk_ids_and_rows[-1][1]
        if len(current_chunk_ids_and_rows) == len(chunk_ids):
            # inplace update
            self._encoded[start_row : end_row + 1, CHUNK_ID_COLUMN] = chunk_ids
        else:
            top = self._encoded[:start_row]
            bottom = self._encoded[end_row + 1 :]
            mid = np.empty((len(chunk_ids), 2), dtype=ENCODING_DTYPE)
            mid[:, CHUNK_ID_COLUMN] = chunk_ids
            mid[:, LAST_SEEN_INDEX_COLUMN] = global_sample_index
            self._encoded = np.concatenate([top, mid, bottom], axis=0)
        self.is_dirty = True

    @classmethod
    def frombuffer(cls, buffer: bytes):
        instance = cls()
        if not buffer:
            return instance
        version, ids = deserialize_chunkids(buffer)
        if ids.nbytes:
            instance._encoded = ids
        instance.version = version
        instance.is_dirty = False
        return instance

    def tobytes(self) -> memoryview:
        return serialize_chunkids(self.version, [self._encoded])
