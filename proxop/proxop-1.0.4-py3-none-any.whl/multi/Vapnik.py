"""
Version : 1.0 ( 06-13-2022).

Author  : Mbaye Diongue

Copyright (C) 2022

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

from typing import Union, Optional
import numpy as np


class Vapnik:
    r"""Compute the proximity operator and the evaluation of gamma*f.

    Where f is the function defined as:

                        f(x) = max( ||x||_2 -epsilon, 0)


    'gamma' is the scale factor

    INPUTS
    ========
     x         - ND array
     epsilon   - positive, scalar or ND array compatible with the blocks of 'x'
     gamma     - positive, scalar or ND array compatible with the blocks of 'x'
                 [default: gamma=1]
     axis      - None or int, axis of block-wise processing [default: axis=None]
                  axis = None --> 'x' is processed as a single vector [DEFAULT] In this
                  case 'gamma' must be a scalar.
                  axis >=0   --> 'x' is processed block-wise along the specified axis
                  (0 -> rows, 1-> columns ect. In this case 'gamma' and 'epsilon' must
                  be singletons along 'axis'.
    """

    def __init__(
            self,
            epsilon: Union[float, np.ndarray],
            axis: Optional[int] = None
    ):
        if np.any(epsilon <= 0):
            raise ValueError(
                "'epsilon' (or all of its components if it is an array)" +
                " must be strictly positive"
            )
        if (axis is not None) and (axis < 0):
            axis = None
        self.epsilon = epsilon
        self.axis = axis

    def prox(self, x: np.ndarray, gamma: Union[float, np.ndarray] = 1) -> np.ndarray:
        self._check(x, gamma)
        axis = self.axis
        epsilon = self.epsilon

        if np.size(x) <= 1:
            x = np.reshape(x, (-1))

        sz = np.shape(x)
        sz = np.array(sz, dtype=int)
        sz[axis] = 1
        if np.size(gamma) > 1:
            gamma = np.reshape(gamma, sz)
        if np.size(epsilon) > 1:
            epsilon = np.reshape(epsilon, sz)

        # preliminaries
        l2_x = np.linalg.norm(x, ord=2, axis=axis).reshape(sz)

        # First branch
        prox_x = 1.0 * x

        # 2nd branch
        mask_ones = np.ones(np.shape(x), dtype=bool)
        mask = mask_ones * (l2_x - epsilon > 0) * (l2_x - epsilon <= gamma)
        prox_x[mask] = (epsilon / l2_x * x)[mask]

        # 3rd branch
        mask = mask_ones * (l2_x - epsilon > gamma)
        prox_x[mask] = ((1 - gamma / l2_x) * x)[mask]

        return prox_x

    def __call__(self, x: np.ndarray) -> float:
        if np.size(x) <= 1:
            x = np.reshape(x, (-1))
        l2_x = np.linalg.norm(x, ord=2, axis=self.axis)
        return np.sum(np.maximum(l2_x - self.epsilon, 0))

    def _check(self, x, gamma):
        if np.any(gamma <= 0):
            raise ValueError(
                "'gamma' (or all of its components if it is an array)" +
                " must be strictly positive"
            )
        if self.axis is None and np.size(gamma) > 1:
            raise ValueError(
                "'gamma' must be scalars when the" +
                " argument 'axis' is equal to 'None'"
            )
        if np.size(gamma) <= 1:
            return
        sz = np.shape(x)
        if len(sz) <= 1:
            self.axis = None
        if len(sz) <= 1:
            raise ValueError(
                "'gamma' must be scalar when 'x' is one dimensional"
            )
        if len(sz) > 1 and self.axis is not None:
            sz = np.array(sz, dtype=int)
            sz[self.axis] = 1
            if np.prod(sz) != np.size(gamma):
                raise ValueError(
                    "The dimension 'gamma' is not compatible" +
                    " with the blocks of 'x'"
                )
