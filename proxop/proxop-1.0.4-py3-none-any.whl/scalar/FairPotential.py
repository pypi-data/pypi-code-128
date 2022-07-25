"""
Version : 1.0 (06-09-2022).

Author  : Mbaye DIONGUE

Copyright (C) 2022

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

from typing import Union
import numpy as np


class FairPotential:
    r"""Compute the proximity operator and the evaluation of gamma*f.

    Where f is 'Fair Potential' function f defined as:

           f(x)=-  w*|x| - log(1+w|x|)

     with w > 0
    'gamma' is the scale factor

    When the input 'x' is an array, the output is computed element-wise :

    -When calling the function (and not the proximity operator) the result
    is computed element-wise SUM. So the command >>>FairPotential()(x) will
    return a scalar even if x is a vector.

    - But for the proximity operator (method 'prox'), the output has the
    same shape as the input 'x'. So, the command >>>FairPotential().prox(x)
    will return an array with the same shape as 'x'


     INPUTS
    ========
     x     - scalar or array
     w     - positive , scalar or array with the same size as 'x'
     gamma  - positive, scalar or array with the same size as 'x' [default: gamma=1]

     =======
    Examples
    ========

     Evaluate the 'direct' function :

     >>> FairPotential()( 2 )
     0.9013877113318902

      Compute the result element-wise for vector inputs :
     >>> FairPotential(gamma=2)( [-1, 0, 3, np.e] )
     6.6511571985219735

     Compute the proximity operator at a given point :

     >>> FairPotential().prox(  [-2, 3, 4, np.e] )
     array([-1.5       ,  2.5       ,  3.5       ,  2.21828183])

     Use a scale factor 'gamma'>0 to compute the proximity operator of
     the function 'gamma*f'

     >>> FairPotential().prox( [-2, 3, 4, np.e ], gamma=2.5)
     array([-0.68614066,  1.5       ,  2.38600094,  1.26147065])
    """

    def __init__(self, w: Union[float, np.ndarray] = 1):
        if np.size(w) > 1 and (not isinstance(w, np.ndarray)):
            w = np.array(w)
        if np.any(w <= 0):
            raise ValueError(
                "'w' (or all of its components if it is an array) must be strictly"
                + " positive"
            )
        self.w = w

    def prox(self, x: np.ndarray, gamma: Union[float, np.ndarray] = 1) -> np.ndarray:
        if np.size(x) > 1 and (not isinstance(x, np.ndarray)):
            x = np.array(x)
        if np.size(gamma) > 1 and (not isinstance(gamma, np.ndarray)):
            gamma = np.array(gamma)
        if np.size(x) <= 1:
            x = np.reshape(x, (-1))

        self._check(x, gamma)
        w = self.w
        sign_x = np.sign(x)
        abs_x = np.abs(x)
        prox_x = (
            w * abs_x
            - w**2 * gamma
            - 1
            + np.sqrt((w * abs_x - w**2 * gamma) ** 2 + 4 * w * abs_x)
        )
        prox_x = sign_x * prox_x / (2 * w)
        return prox_x

    def __call__(self, x: np.ndarray) -> np.float:
        return np.sum(self.w * np.abs(x) - np.log(1 + self.w * np.abs(x)))

    def _check(self, x, gamma):
        if np.any(gamma <= 0):
            raise ValueError(
                "'gamma' (or all of its elements if it is an array)"
                + "must be strictly positive"
            )
        if (np.size(gamma) > 1) and (np.size(gamma) != np.size(x)):
            raise ValueError("gamma' must be either scalar or the same size as 'x'")
