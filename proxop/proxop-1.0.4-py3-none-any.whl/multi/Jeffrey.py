"""
Version : 1.0 ( 06-22-2022).

DEPENDENCIES:
     -'newton.py' in the folder 'utils'
     -'lambert_W.py' in the folder 'utils'

Author  : Mbaye Diongue

Copyright (C) 2022

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

from typing import Union, Tuple
import numpy as np
from proxop.utils.newton import newton_
from proxop.utils.lambert_W import lambert_W


class Jeffrey:
    r"""Compute the proximity operator and the evaluation of gamma*D.

    Where D is the function defined as:


                  /  (x-y) * log(x/y)                 if x > 0 and y > 0
        D(x,y) = |   0                                if x=y=0
                 \   + inf                            otherwise

    'gamma' is the scale factor

            When the inputs are arrays, the outputs are computed element-wise
    INPUTS
    ========
    x          - scalar or ND array
    y          - scalar or ND array with the same size as 'x'
    gamma      - scalar or ND array compatible with the blocks of 'y' [default: gamma=1]
    """

    def __init__(
            self
    ):
        pass

    def prox(
            self,
            x: np.ndarray,
            y: np.ndarray,
            gamma: Union[float, np.ndarray] = 1
    ) -> Tuple[np.ndarray, np.ndarray]:
        self._check(x, gamma)
        if np.size(x) != np.size(y):
            raise Exception("'x' and 'y' must have the same size")
        # scalar-like inputs handling
        if np.size(x) <= 1:
            x = np.reshape(x, (-1))
        if np.size(y) <= 1:
            y = np.reshape(y, (-1))

        # 2nd branch
        sz = np.shape(x)
        prox_p = np.zeros(sz)
        prox_q = np.zeros(sz)

        # branch selection
        # when the input is too big, we use a taylor approximation of the
        # LambertW function to avoid divergence
        u1 = 1 - x / gamma
        u2 = 1 - y / gamma
        lw_x, lw_y = np.zeros(sz), np.zeros(sz)
        # With x ...
        mask_u = u1 > 100
        lw_x[mask_u] = u1[mask_u] - u1[mask_u] / (1 + u1[mask_u]) * np.log(u1[mask_u])

        # we use the Lambert_W function otherwise
        mask_u = np.logical_not(mask_u)
        lw_x[mask_u] = lambert_W(np.exp(1 - x / gamma))
        # With y ...
        mask_u = u2 > 100
        lw_y[mask_u] = u2[mask_u] - u2[mask_u] / (1 + u2[mask_u]) * np.log(u2[mask_u])

        # we use the Lambert_W function otherwise
        mask_u = np.logical_not(mask_u)
        lw_y[mask_u] = lambert_W(np.exp(1 - y / gamma))

        mask = lw_x * lw_y < 1
        gg = gamma
        if np.size(gamma) > 1:
            gg = gamma[mask]
        xx = x[mask]
        yy = y[mask]

        # newton's method

        def fun_phi(u):
            return (
                    (u + 1) * np.log(u) - 1 / u + u ** 2 + (xx / gg - 1) * u + 1
                    - yy / gg
            )

        def der_fun_phi(u):
            return np.log(u) + 1 / u + 1 / u ** 2 + 2 * u + xx / gg

        # root finding
        eps = 1e-10
        low = lw_x + eps
        high = 1 / (lw_y + eps)
        t = (low + high) / 2
        t = newton_(fun_phi, fp=der_fun_phi, x0=t, low=low, high=high)

        # 1st branch
        prox_p[mask] = xx + gg * (np.log(t) + t - 1)
        prox_q[mask] = yy - gg * (np.log(t) - 1 / t + 1)

        return tuple([prox_p, prox_q])

    def __call__(self, x: np.ndarray, y: np.ndarray) -> np.float:
        if np.size(x) != np.size(y):
            raise Exception("'x' and 'y' must have the same size")
        if (
                np.any(x < 0)
                or np.any(y < 0)
                or np.any((x == 0) * (y != 0))
                or np.any((y == 0) * (x != 0))
        ):
            return np.inf
        if np.size(x) <= 1:
            x = np.reshape(x, (-1))
            y = np.reshape(y, (-1))
        mask = y > 0
        res = (x[mask] - y[mask]) * np.log(x[mask] / y[mask])
        return np.sum(res)

    def _check(self, x, gamma=1):
        if np.any(gamma <= 0):
            raise Exception("'gamma'  must be strictly positive")
        if np.size(gamma) > 1 and np.size(gamma) != np.size(x):
            ValueError(
                "'gamma' must be positive scalars or positive ND arrays" +
                " with the same size as 'x'"
            )
