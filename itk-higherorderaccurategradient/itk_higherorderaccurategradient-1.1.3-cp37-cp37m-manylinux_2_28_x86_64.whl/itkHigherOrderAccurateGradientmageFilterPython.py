# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")


from . import _HigherOrderAccurateGradientPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkHigherOrderAccurateGradientmageFilterPython
else:
    import _itkHigherOrderAccurateGradientmageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHigherOrderAccurateGradientmageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHigherOrderAccurateGradientmageFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkImageToImageFilterBPython
import itk.itkVectorImagePython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkIndexPython
import itk.itkRGBPixelPython
import itk.itkImageRegionPython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython

def itkHigherOrderAccurateGradientImageFilterID2DD_New():
    return itkHigherOrderAccurateGradientImageFilterID2DD.New()

class itkHigherOrderAccurateGradientImageFilterID2DD(itk.itkImageToImageFilterBPython.itkImageToImageFilterID2ICVD22):
    r"""Proxy of C++ itkHigherOrderAccurateGradientImageFilterID2DD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_Clone)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_GetUseImageSpacing)
    UseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_UseImageSpacingOff)
    InputConvertibleToOutputCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_InputConvertibleToOutputCheck
    
    OutputHasNumericTraitsCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_OutputHasNumericTraitsCheck
    
    SetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_SetUseImageDirection)
    GetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_GetUseImageDirection)
    UseImageDirectionOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_UseImageDirectionOn)
    UseImageDirectionOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_UseImageDirectionOff)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_GetOrderOfAccuracy)
    __swig_destroy__ = _itkHigherOrderAccurateGradientmageFilterPython.delete_itkHigherOrderAccurateGradientImageFilterID2DD
    cast = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateGradientImageFilterID2DD

        Create a new object of the class itkHigherOrderAccurateGradientImageFilterID2DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateGradientImageFilterID2DD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateGradientImageFilterID2DD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateGradientImageFilterID2DD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateGradientImageFilterID2DD in _itkHigherOrderAccurateGradientmageFilterPython:
_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_swigregister(itkHigherOrderAccurateGradientImageFilterID2DD)
itkHigherOrderAccurateGradientImageFilterID2DD___New_orig__ = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD___New_orig__
itkHigherOrderAccurateGradientImageFilterID2DD_cast = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID2DD_cast


def itkHigherOrderAccurateGradientImageFilterID3DD_New():
    return itkHigherOrderAccurateGradientImageFilterID3DD.New()

class itkHigherOrderAccurateGradientImageFilterID3DD(itk.itkImageToImageFilterBPython.itkImageToImageFilterID3ICVD33):
    r"""Proxy of C++ itkHigherOrderAccurateGradientImageFilterID3DD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_Clone)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_GetUseImageSpacing)
    UseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_UseImageSpacingOff)
    InputConvertibleToOutputCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_InputConvertibleToOutputCheck
    
    OutputHasNumericTraitsCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_OutputHasNumericTraitsCheck
    
    SetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_SetUseImageDirection)
    GetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_GetUseImageDirection)
    UseImageDirectionOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_UseImageDirectionOn)
    UseImageDirectionOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_UseImageDirectionOff)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_GetOrderOfAccuracy)
    __swig_destroy__ = _itkHigherOrderAccurateGradientmageFilterPython.delete_itkHigherOrderAccurateGradientImageFilterID3DD
    cast = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateGradientImageFilterID3DD

        Create a new object of the class itkHigherOrderAccurateGradientImageFilterID3DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateGradientImageFilterID3DD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateGradientImageFilterID3DD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateGradientImageFilterID3DD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateGradientImageFilterID3DD in _itkHigherOrderAccurateGradientmageFilterPython:
_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_swigregister(itkHigherOrderAccurateGradientImageFilterID3DD)
itkHigherOrderAccurateGradientImageFilterID3DD___New_orig__ = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD___New_orig__
itkHigherOrderAccurateGradientImageFilterID3DD_cast = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID3DD_cast


def itkHigherOrderAccurateGradientImageFilterID4DD_New():
    return itkHigherOrderAccurateGradientImageFilterID4DD.New()

class itkHigherOrderAccurateGradientImageFilterID4DD(itk.itkImageToImageFilterBPython.itkImageToImageFilterID4ICVD44):
    r"""Proxy of C++ itkHigherOrderAccurateGradientImageFilterID4DD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_Clone)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_GetUseImageSpacing)
    UseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_UseImageSpacingOff)
    InputConvertibleToOutputCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_InputConvertibleToOutputCheck
    
    OutputHasNumericTraitsCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_OutputHasNumericTraitsCheck
    
    SetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_SetUseImageDirection)
    GetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_GetUseImageDirection)
    UseImageDirectionOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_UseImageDirectionOn)
    UseImageDirectionOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_UseImageDirectionOff)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_GetOrderOfAccuracy)
    __swig_destroy__ = _itkHigherOrderAccurateGradientmageFilterPython.delete_itkHigherOrderAccurateGradientImageFilterID4DD
    cast = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateGradientImageFilterID4DD

        Create a new object of the class itkHigherOrderAccurateGradientImageFilterID4DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateGradientImageFilterID4DD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateGradientImageFilterID4DD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateGradientImageFilterID4DD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateGradientImageFilterID4DD in _itkHigherOrderAccurateGradientmageFilterPython:
_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_swigregister(itkHigherOrderAccurateGradientImageFilterID4DD)
itkHigherOrderAccurateGradientImageFilterID4DD___New_orig__ = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD___New_orig__
itkHigherOrderAccurateGradientImageFilterID4DD_cast = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterID4DD_cast


def itkHigherOrderAccurateGradientImageFilterIF2FF_New():
    return itkHigherOrderAccurateGradientImageFilterIF2FF.New()

class itkHigherOrderAccurateGradientImageFilterIF2FF(itk.itkImageToImageFilterBPython.itkImageToImageFilterIF2ICVF22):
    r"""Proxy of C++ itkHigherOrderAccurateGradientImageFilterIF2FF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_Clone)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_GetUseImageSpacing)
    UseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_UseImageSpacingOff)
    InputConvertibleToOutputCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_InputConvertibleToOutputCheck
    
    OutputHasNumericTraitsCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_OutputHasNumericTraitsCheck
    
    SetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_SetUseImageDirection)
    GetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_GetUseImageDirection)
    UseImageDirectionOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_UseImageDirectionOn)
    UseImageDirectionOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_UseImageDirectionOff)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_GetOrderOfAccuracy)
    __swig_destroy__ = _itkHigherOrderAccurateGradientmageFilterPython.delete_itkHigherOrderAccurateGradientImageFilterIF2FF
    cast = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateGradientImageFilterIF2FF

        Create a new object of the class itkHigherOrderAccurateGradientImageFilterIF2FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateGradientImageFilterIF2FF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateGradientImageFilterIF2FF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateGradientImageFilterIF2FF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateGradientImageFilterIF2FF in _itkHigherOrderAccurateGradientmageFilterPython:
_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_swigregister(itkHigherOrderAccurateGradientImageFilterIF2FF)
itkHigherOrderAccurateGradientImageFilterIF2FF___New_orig__ = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF___New_orig__
itkHigherOrderAccurateGradientImageFilterIF2FF_cast = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF2FF_cast


def itkHigherOrderAccurateGradientImageFilterIF3FF_New():
    return itkHigherOrderAccurateGradientImageFilterIF3FF.New()

class itkHigherOrderAccurateGradientImageFilterIF3FF(itk.itkImageToImageFilterBPython.itkImageToImageFilterIF3ICVF33):
    r"""Proxy of C++ itkHigherOrderAccurateGradientImageFilterIF3FF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_Clone)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_GetUseImageSpacing)
    UseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_UseImageSpacingOff)
    InputConvertibleToOutputCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_InputConvertibleToOutputCheck
    
    OutputHasNumericTraitsCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_OutputHasNumericTraitsCheck
    
    SetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_SetUseImageDirection)
    GetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_GetUseImageDirection)
    UseImageDirectionOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_UseImageDirectionOn)
    UseImageDirectionOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_UseImageDirectionOff)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_GetOrderOfAccuracy)
    __swig_destroy__ = _itkHigherOrderAccurateGradientmageFilterPython.delete_itkHigherOrderAccurateGradientImageFilterIF3FF
    cast = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateGradientImageFilterIF3FF

        Create a new object of the class itkHigherOrderAccurateGradientImageFilterIF3FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateGradientImageFilterIF3FF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateGradientImageFilterIF3FF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateGradientImageFilterIF3FF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateGradientImageFilterIF3FF in _itkHigherOrderAccurateGradientmageFilterPython:
_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_swigregister(itkHigherOrderAccurateGradientImageFilterIF3FF)
itkHigherOrderAccurateGradientImageFilterIF3FF___New_orig__ = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF___New_orig__
itkHigherOrderAccurateGradientImageFilterIF3FF_cast = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF3FF_cast


def itkHigherOrderAccurateGradientImageFilterIF4FF_New():
    return itkHigherOrderAccurateGradientImageFilterIF4FF.New()

class itkHigherOrderAccurateGradientImageFilterIF4FF(itk.itkImageToImageFilterBPython.itkImageToImageFilterIF4ICVF44):
    r"""Proxy of C++ itkHigherOrderAccurateGradientImageFilterIF4FF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_Clone)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_GetUseImageSpacing)
    UseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_UseImageSpacingOn)
    UseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_UseImageSpacingOff)
    InputConvertibleToOutputCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_InputConvertibleToOutputCheck
    
    OutputHasNumericTraitsCheck = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_OutputHasNumericTraitsCheck
    
    SetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_SetUseImageDirection)
    GetUseImageDirection = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_GetUseImageDirection)
    UseImageDirectionOn = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_UseImageDirectionOn)
    UseImageDirectionOff = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_UseImageDirectionOff)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_GetOrderOfAccuracy)
    __swig_destroy__ = _itkHigherOrderAccurateGradientmageFilterPython.delete_itkHigherOrderAccurateGradientImageFilterIF4FF
    cast = _swig_new_static_method(_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateGradientImageFilterIF4FF

        Create a new object of the class itkHigherOrderAccurateGradientImageFilterIF4FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateGradientImageFilterIF4FF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateGradientImageFilterIF4FF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateGradientImageFilterIF4FF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateGradientImageFilterIF4FF in _itkHigherOrderAccurateGradientmageFilterPython:
_itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_swigregister(itkHigherOrderAccurateGradientImageFilterIF4FF)
itkHigherOrderAccurateGradientImageFilterIF4FF___New_orig__ = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF___New_orig__
itkHigherOrderAccurateGradientImageFilterIF4FF_cast = _itkHigherOrderAccurateGradientmageFilterPython.itkHigherOrderAccurateGradientImageFilterIF4FF_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def higher_order_accurate_gradient_image_filter(*args: itkt.ImageLike,  use_image_spacing: bool=..., use_image_direction: bool=..., order_of_accuracy: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for HigherOrderAccurateGradientImageFilter"""
    import itk

    kwarg_typehints = { 'use_image_spacing':use_image_spacing,'use_image_direction':use_image_direction,'order_of_accuracy':order_of_accuracy }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HigherOrderAccurateGradientImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def higher_order_accurate_gradient_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.HigherOrderAccurateGradient.HigherOrderAccurateGradientImageFilter
    higher_order_accurate_gradient_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    higher_order_accurate_gradient_image_filter.__doc__ = filter_object.__doc__




