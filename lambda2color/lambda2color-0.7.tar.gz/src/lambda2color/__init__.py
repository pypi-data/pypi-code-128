"""Lambda2color

This is a simple library to transform a given light wavelength into the corresponding RGB color.

We adapt code from https://scipython.com/blog/converting-a-spectrum-to-a-colour/
such that we may obtain a RGB value fro a given wavelength

"""

# The version of this package. There's no comprehensive, official list of other
# magic constants, so we stick with this one only for now. See also this conversation:
# https://stackoverflow.com/questions/38344848/is-there-a-comprehensive-table-of-pythons-magic-constants
__version__ = "0.7"

from typing import Any

import numpy as np
import numpy.typing as npt


def xyz_from_xy(x_value: float, y_value: float) -> np.ndarray:
    """Return the vector (x, y, 1-x-y)."""
    return np.array((x_value, y_value, 1 - x_value - y_value))


class Lambda2color:
    """A class representing a colour system.

    A colour system defined by the CIE x, y and z=1-x-y coordinates of
    its three primary illuminants and its "white point".

    """

    def __init__(
        self, red: npt.ArrayLike, green: npt.ArrayLike, blue: npt.ArrayLike, white: npt.ArrayLike):
        """Initialise the ColourSystem object.

        Pass vectors (ie NumPy arrays of shape (3,)) for each of the
        red, green, blue  chromaticities and the white illuminant
        defining the colour system.

        """
        # Chromaticities
        self.red, self.green, self.blue = red, green, blue
        self.white = white
        # The chromaticity matrix (rgb -> xyz) and its inverse
        self.chromaticity_matrix = np.vstack((self.red, self.green, self.blue)).T
        self.inv_chromaticity_matrix = np.linalg.inv(self.chromaticity_matrix)
        # White scaling array
        self.wscale = self.inv_chromaticity_matrix.dot(self.white)

        # xyz -> rgb transformation matrix
        self.transformation_matrix = self.inv_chromaticity_matrix / self.wscale[:, np.newaxis]

        # the CIE colour matching function for 380 - 780 nm in 5 nm intervals
        cmf_str = """380 0.0014 0.0000 0.0065
        385 0.0022 0.0001 0.0105
        390 0.0042 0.0001 0.0201
        395 0.0076 0.0002 0.0362
        400 0.0143 0.0004 0.0679
        405 0.0232 0.0006 0.1102
        410 0.0435 0.0012 0.2074
        415 0.0776 0.0022 0.3713
        420 0.1344 0.0040 0.6456
        425 0.2148 0.0073 1.0391
        430 0.2839 0.0116 1.3856
        435 0.3285 0.0168 1.6230
        440 0.3483 0.0230 1.7471
        445 0.3481 0.0298 1.7826
        450 0.3362 0.0380 1.7721
        455 0.3187 0.0480 1.7441
        460 0.2908 0.0600 1.6692
        465 0.2511 0.0739 1.5281
        470 0.1954 0.0910 1.2876
        475 0.1421 0.1126 1.0419
        480 0.0956 0.1390 0.8130
        485 0.0580 0.1693 0.6162
        490 0.0320 0.2080 0.4652
        495 0.0147 0.2586 0.3533
        500 0.0049 0.3230 0.2720
        505 0.0024 0.4073 0.2123
        510 0.0093 0.5030 0.1582
        515 0.0291 0.6082 0.1117
        520 0.0633 0.7100 0.0782
        525 0.1096 0.7932 0.0573
        530 0.1655 0.8620 0.0422
        535 0.2257 0.9149 0.0298
        540 0.2904 0.9540 0.0203
        545 0.3597 0.9803 0.0134
        550 0.4334 0.9950 0.0087
        555 0.5121 1.0000 0.0057
        560 0.5945 0.9950 0.0039
        565 0.6784 0.9786 0.0027
        570 0.7621 0.9520 0.0021
        575 0.8425 0.9154 0.0018
        580 0.9163 0.8700 0.0017
        585 0.9786 0.8163 0.0014
        590 1.0263 0.7570 0.0011
        595 1.0567 0.6949 0.0010
        600 1.0622 0.6310 0.0008
        605 1.0456 0.5668 0.0006
        610 1.0026 0.5030 0.0003
        615 0.9384 0.4412 0.0002
        620 0.8544 0.3810 0.0002
        625 0.7514 0.3210 0.0001
        630 0.6424 0.2650 0.0000
        635 0.5419 0.2170 0.0000
        640 0.4479 0.1750 0.0000
        645 0.3608 0.1382 0.0000
        650 0.2835 0.1070 0.0000
        655 0.2187 0.0816 0.0000
        660 0.1649 0.0610 0.0000
        665 0.1212 0.0446 0.0000
        670 0.0874 0.0320 0.0000
        675 0.0636 0.0232 0.0000
        680 0.0468 0.0170 0.0000
        685 0.0329 0.0119 0.0000
        690 0.0227 0.0082 0.0000
        695 0.0158 0.0057 0.0000
        700 0.0114 0.0041 0.0000
        705 0.0081 0.0029 0.0000
        710 0.0058 0.0021 0.0000
        715 0.0041 0.0015 0.0000
        720 0.0029 0.0010 0.0000
        725 0.0020 0.0007 0.0000
        730 0.0014 0.0005 0.0000
        735 0.0010 0.0004 0.0000
        740 0.0007 0.0002 0.0000
        745 0.0005 0.0002 0.0000
        750 0.0003 0.0001 0.0000
        755 0.0002 0.0001 0.0000
        760 0.0002 0.0001 0.0000
        765 0.0001 0.0000 0.0000
        770 0.0001 0.0000 0.0000
        775 0.0001 0.0000 0.0000
        780 0.0000 0.0000 0.0000"""
        cmf = np.zeros((len(cmf_str.split("\n")), 4))
        for i, line in enumerate(cmf_str.split("\n")):
            cmf[i, :] = np.fromstring(line, sep=" ")
        self.cmf = cmf

    def xyz_to_rgb(self, xyz: npt.ArrayLike) -> Any:
        """Transform from xyz to rgb representation of colour.

        The output rgb components are normalized on their maximum
        value. If xyz is out the rgb gamut, it is desaturated until it
        comes into gamut.

        Fractional rgb components are returned.

        """
        # rgb = self.transformation_matrix.dot(xyz)
        rgb = np.tensordot(xyz, self.transformation_matrix.T, axes=1)

        if np.any(rgb < 0):
            # We're not in the RGB gamut: approximate by desaturating
            rgb -= np.min(rgb)
        if not np.all(rgb == 0):
            # Normalize the rgb vector
            rgb /= np.max(rgb)
        return rgb

    def spec_to_xyz(self, spec: Any) -> Any:
        """Convert a spectrum to an xyz point.

        The last dimension of the spectrum *must* be on the same grid of
        points as the colour-matching function self.cmf, that is,

                    380-780 nm in 5 nm steps.

        """
        # xyz = np.sum(spec[:, np.newaxis] * self.cmf[:, 1:], axis=0)
        xyz = np.tensordot(spec, self.cmf[:, 1:], axes=1)
        den = np.sum(xyz)
        if den == 0.0:
            return xyz
        return xyz / den

    def spec_to_rgb(self, spec: npt.ArrayLike) -> Any:
        """Convert a spectrum to an rgb value.

        The last dimension of the spectrum *must* be on the same grid of
        points as the colour-matching function self.cmf, that is,

                    380-780 nm in 5 nm steps.

        """
        xyz = self.spec_to_xyz(spec)
        return self.xyz_to_rgb(xyz)
