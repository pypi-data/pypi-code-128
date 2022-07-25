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
    from . import _itkHigherOrderAccurateDerivativeImageFilterPython
else:
    import _itkHigherOrderAccurateDerivativeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHigherOrderAccurateDerivativeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHigherOrderAccurateDerivativeImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterAPython
import itk.itkImagePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.pyBasePython
import itk.stdcomplexPython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkRGBPixelPython
import itk.ITKCommonBasePython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython

def itkHigherOrderAccurateDerivativeImageFilterID2ID2_New():
    return itkHigherOrderAccurateDerivativeImageFilterID2ID2.New()

class itkHigherOrderAccurateDerivativeImageFilterID2ID2(itk.itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkHigherOrderAccurateDerivativeImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_Clone)
    SignedOutputPixelType = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_SetOrder)
    GetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_GetOrder)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_GetOrderOfAccuracy)
    SetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_GetUseImageSpacing)
    __swig_destroy__ = _itkHigherOrderAccurateDerivativeImageFilterPython.delete_itkHigherOrderAccurateDerivativeImageFilterID2ID2
    cast = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateDerivativeImageFilterID2ID2

        Create a new object of the class itkHigherOrderAccurateDerivativeImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateDerivativeImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateDerivativeImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateDerivativeImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateDerivativeImageFilterID2ID2 in _itkHigherOrderAccurateDerivativeImageFilterPython:
_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_swigregister(itkHigherOrderAccurateDerivativeImageFilterID2ID2)
itkHigherOrderAccurateDerivativeImageFilterID2ID2___New_orig__ = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2___New_orig__
itkHigherOrderAccurateDerivativeImageFilterID2ID2_cast = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID2ID2_cast


def itkHigherOrderAccurateDerivativeImageFilterID3ID3_New():
    return itkHigherOrderAccurateDerivativeImageFilterID3ID3.New()

class itkHigherOrderAccurateDerivativeImageFilterID3ID3(itk.itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkHigherOrderAccurateDerivativeImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_Clone)
    SignedOutputPixelType = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_SetOrder)
    GetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_GetOrder)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_GetOrderOfAccuracy)
    SetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_GetUseImageSpacing)
    __swig_destroy__ = _itkHigherOrderAccurateDerivativeImageFilterPython.delete_itkHigherOrderAccurateDerivativeImageFilterID3ID3
    cast = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateDerivativeImageFilterID3ID3

        Create a new object of the class itkHigherOrderAccurateDerivativeImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateDerivativeImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateDerivativeImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateDerivativeImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateDerivativeImageFilterID3ID3 in _itkHigherOrderAccurateDerivativeImageFilterPython:
_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_swigregister(itkHigherOrderAccurateDerivativeImageFilterID3ID3)
itkHigherOrderAccurateDerivativeImageFilterID3ID3___New_orig__ = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3___New_orig__
itkHigherOrderAccurateDerivativeImageFilterID3ID3_cast = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID3ID3_cast


def itkHigherOrderAccurateDerivativeImageFilterID4ID4_New():
    return itkHigherOrderAccurateDerivativeImageFilterID4ID4.New()

class itkHigherOrderAccurateDerivativeImageFilterID4ID4(itk.itkImageToImageFilterAPython.itkImageToImageFilterID4ID4):
    r"""Proxy of C++ itkHigherOrderAccurateDerivativeImageFilterID4ID4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_Clone)
    SignedOutputPixelType = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_SetOrder)
    GetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_GetOrder)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_GetOrderOfAccuracy)
    SetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_SetDirection)
    GetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_GetUseImageSpacing)
    __swig_destroy__ = _itkHigherOrderAccurateDerivativeImageFilterPython.delete_itkHigherOrderAccurateDerivativeImageFilterID4ID4
    cast = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateDerivativeImageFilterID4ID4

        Create a new object of the class itkHigherOrderAccurateDerivativeImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateDerivativeImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateDerivativeImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateDerivativeImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateDerivativeImageFilterID4ID4 in _itkHigherOrderAccurateDerivativeImageFilterPython:
_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_swigregister(itkHigherOrderAccurateDerivativeImageFilterID4ID4)
itkHigherOrderAccurateDerivativeImageFilterID4ID4___New_orig__ = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4___New_orig__
itkHigherOrderAccurateDerivativeImageFilterID4ID4_cast = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterID4ID4_cast


def itkHigherOrderAccurateDerivativeImageFilterIF2IF2_New():
    return itkHigherOrderAccurateDerivativeImageFilterIF2IF2.New()

class itkHigherOrderAccurateDerivativeImageFilterIF2IF2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkHigherOrderAccurateDerivativeImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_Clone)
    SignedOutputPixelType = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_SetOrder)
    GetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_GetOrder)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_GetOrderOfAccuracy)
    SetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_GetUseImageSpacing)
    __swig_destroy__ = _itkHigherOrderAccurateDerivativeImageFilterPython.delete_itkHigherOrderAccurateDerivativeImageFilterIF2IF2
    cast = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateDerivativeImageFilterIF2IF2

        Create a new object of the class itkHigherOrderAccurateDerivativeImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateDerivativeImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateDerivativeImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateDerivativeImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateDerivativeImageFilterIF2IF2 in _itkHigherOrderAccurateDerivativeImageFilterPython:
_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_swigregister(itkHigherOrderAccurateDerivativeImageFilterIF2IF2)
itkHigherOrderAccurateDerivativeImageFilterIF2IF2___New_orig__ = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2___New_orig__
itkHigherOrderAccurateDerivativeImageFilterIF2IF2_cast = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF2IF2_cast


def itkHigherOrderAccurateDerivativeImageFilterIF3IF3_New():
    return itkHigherOrderAccurateDerivativeImageFilterIF3IF3.New()

class itkHigherOrderAccurateDerivativeImageFilterIF3IF3(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkHigherOrderAccurateDerivativeImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_Clone)
    SignedOutputPixelType = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_SetOrder)
    GetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_GetOrder)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_GetOrderOfAccuracy)
    SetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_GetUseImageSpacing)
    __swig_destroy__ = _itkHigherOrderAccurateDerivativeImageFilterPython.delete_itkHigherOrderAccurateDerivativeImageFilterIF3IF3
    cast = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateDerivativeImageFilterIF3IF3

        Create a new object of the class itkHigherOrderAccurateDerivativeImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateDerivativeImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateDerivativeImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateDerivativeImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateDerivativeImageFilterIF3IF3 in _itkHigherOrderAccurateDerivativeImageFilterPython:
_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_swigregister(itkHigherOrderAccurateDerivativeImageFilterIF3IF3)
itkHigherOrderAccurateDerivativeImageFilterIF3IF3___New_orig__ = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3___New_orig__
itkHigherOrderAccurateDerivativeImageFilterIF3IF3_cast = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF3IF3_cast


def itkHigherOrderAccurateDerivativeImageFilterIF4IF4_New():
    return itkHigherOrderAccurateDerivativeImageFilterIF4IF4.New()

class itkHigherOrderAccurateDerivativeImageFilterIF4IF4(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF4IF4):
    r"""Proxy of C++ itkHigherOrderAccurateDerivativeImageFilterIF4IF4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_Clone)
    SignedOutputPixelType = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_SignedOutputPixelType
    
    SetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_SetOrder)
    GetOrder = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_GetOrder)
    SetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_SetOrderOfAccuracy)
    GetOrderOfAccuracy = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_GetOrderOfAccuracy)
    SetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_SetDirection)
    GetDirection = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_GetDirection)
    SetUseImageSpacingOn = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_SetUseImageSpacingOn)
    SetUseImageSpacingOff = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_SetUseImageSpacingOff)
    SetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_SetUseImageSpacing)
    GetUseImageSpacing = _swig_new_instance_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_GetUseImageSpacing)
    __swig_destroy__ = _itkHigherOrderAccurateDerivativeImageFilterPython.delete_itkHigherOrderAccurateDerivativeImageFilterIF4IF4
    cast = _swig_new_static_method(_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkHigherOrderAccurateDerivativeImageFilterIF4IF4

        Create a new object of the class itkHigherOrderAccurateDerivativeImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHigherOrderAccurateDerivativeImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHigherOrderAccurateDerivativeImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHigherOrderAccurateDerivativeImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHigherOrderAccurateDerivativeImageFilterIF4IF4 in _itkHigherOrderAccurateDerivativeImageFilterPython:
_itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_swigregister(itkHigherOrderAccurateDerivativeImageFilterIF4IF4)
itkHigherOrderAccurateDerivativeImageFilterIF4IF4___New_orig__ = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4___New_orig__
itkHigherOrderAccurateDerivativeImageFilterIF4IF4_cast = _itkHigherOrderAccurateDerivativeImageFilterPython.itkHigherOrderAccurateDerivativeImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def higher_order_accurate_derivative_image_filter(*args: itkt.ImageLike,  order: int=..., order_of_accuracy: int=..., direction: int=..., use_image_spacing: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for HigherOrderAccurateDerivativeImageFilter"""
    import itk

    kwarg_typehints = { 'order':order,'order_of_accuracy':order_of_accuracy,'direction':direction,'use_image_spacing':use_image_spacing }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HigherOrderAccurateDerivativeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def higher_order_accurate_derivative_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.HigherOrderAccurateGradient.HigherOrderAccurateDerivativeImageFilter
    higher_order_accurate_derivative_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    higher_order_accurate_derivative_image_filter.__doc__ = filter_object.__doc__




