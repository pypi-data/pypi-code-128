"""
Version : 1.0 ( 06-21-2022).

DEPENDENCIES:
     - 'fun_svd.py' located in the folder 'utils'
     - 'prox_svd.py' located in the folder 'utils'

Author  : Mbaye Diongue

Copyright (C) 2022

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

import numpy as np
from proxop.utils.prox_svd import prox_svd
from proxop.utils.fun_svd import fun_svd


class NuclearLogDet:
    r"""Compute the proximity operator and the evaluation of gamma*f.

    Where f is the function defined as:

               /  -log( det(X) ) + mu*||X||_N     if X is a symmetric positive
         f(x)=|                                   definite matrix
              \   + inf                           otherwise

    where
           * X = U*diag(s)*U.T \in R^{N*N}  spectral decomposition of the symmetric
           matrix X

           * det(X) is the determinant of the matrix X

           * ||X||_N = ||s||_1  the nuclear norm of X

           * 'gamma' is the scale factor

     Note:
    No checking is performed to verify whether X is symmetric or not when computing
    the proximity operator with the method 'prox'. X is assumed to
    be symmetric.

     INPUTS
    ========
     x          -  (N,N) -array_like ( representing an M*N symmetric matrix )
     mu         - positive scalar
    gamma      - positive scalar  [default: gamma=1]
    """

    def __init__(
            self,
            mu: float = 1
    ):
        if np.any(mu < 0) or np.size(mu) > 1:
            raise Exception("'mu'  must be a positive scalar")
        self.mu = mu

    def prox(self, x: np.ndarray, gamma: float = 1) -> np.ndarray:
        self._check(x, gamma)
        mu = self.mu

        def prox_phi(s, gam):
            return 0.5 * (s - gam * mu + np.sqrt((s - mu * gam) ** 2 + 4 * gam))

        return prox_svd(x, gamma, prox_phi, hermitian=True)

    def __call__(self, x: np.ndarray) -> np.float:
        self._check(x)
        tol = 1e-12
        # Check if the matrix is symmetric
        if not np.allclose(x, np.transpose(x)):
            return np.inf

        def fun_phi(s):
            if np.any(s <= tol):
                return np.inf
            return -np.log(np.prod(s)) + self.mu * np.sum(np.abs(s))

        return fun_svd(x, 1, fun_phi)

    def _check(self, x, gamma=1):
        if np.any(gamma <= 0) or np.size(gamma) > 1:
            raise Exception("'gamma'  must be a strictly positive scalar")
        if len(np.shape(x)) != 2:
            raise ValueError(
                "'x' must be an (M,N) -array_like ( representing an M*N matrix )"
            )
