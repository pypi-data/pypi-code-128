from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.deno_to_jsonschema_response_200_args_item_typ_type_0 import DenoToJsonschemaResponse200ArgsItemTypType0
from ..models.deno_to_jsonschema_response_200_args_item_typ_type_1 import DenoToJsonschemaResponse200ArgsItemTypType1
from ..models.deno_to_jsonschema_response_200_args_item_typ_type_2 import DenoToJsonschemaResponse200ArgsItemTypType2
from ..types import UNSET, Unset

T = TypeVar("T", bound="DenoToJsonschemaResponse200ArgsItem")


@attr.s(auto_attribs=True)
class DenoToJsonschemaResponse200ArgsItem:
    """ """

    name: str
    typ: Union[
        DenoToJsonschemaResponse200ArgsItemTypType0,
        DenoToJsonschemaResponse200ArgsItemTypType1,
        DenoToJsonschemaResponse200ArgsItemTypType2,
    ]
    has_default: Union[Unset, bool] = UNSET
    default: Union[Unset, None] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        if isinstance(self.typ, DenoToJsonschemaResponse200ArgsItemTypType0):
            typ = self.typ.value

        elif isinstance(self.typ, DenoToJsonschemaResponse200ArgsItemTypType1):
            typ = self.typ.to_dict()

        else:
            typ = self.typ.to_dict()

        has_default = self.has_default
        default = None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "typ": typ,
            }
        )
        if has_default is not UNSET:
            field_dict["has_default"] = has_default
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_typ(
            data: object,
        ) -> Union[
            DenoToJsonschemaResponse200ArgsItemTypType0,
            DenoToJsonschemaResponse200ArgsItemTypType1,
            DenoToJsonschemaResponse200ArgsItemTypType2,
        ]:
            try:
                typ_type_0: DenoToJsonschemaResponse200ArgsItemTypType0
                if not isinstance(data, str):
                    raise TypeError()
                typ_type_0 = DenoToJsonschemaResponse200ArgsItemTypType0(data)

                return typ_type_0
            except:  # noqa: E722
                pass
            try:
                typ_type_1: DenoToJsonschemaResponse200ArgsItemTypType1
                if not isinstance(data, dict):
                    raise TypeError()
                typ_type_1 = DenoToJsonschemaResponse200ArgsItemTypType1.from_dict(data)

                return typ_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            typ_type_2: DenoToJsonschemaResponse200ArgsItemTypType2
            typ_type_2 = DenoToJsonschemaResponse200ArgsItemTypType2.from_dict(data)

            return typ_type_2

        typ = _parse_typ(d.pop("typ"))

        has_default = d.pop("has_default", UNSET)

        default = None

        deno_to_jsonschema_response_200_args_item = cls(
            name=name,
            typ=typ,
            has_default=has_default,
            default=default,
        )

        deno_to_jsonschema_response_200_args_item.additional_properties = d
        return deno_to_jsonschema_response_200_args_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
