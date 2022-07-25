# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")


from . import _StrainPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkStrainImageFilterPython
else:
    import _itkStrainImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkStrainImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkStrainImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkImageToImageFilterAPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageToImageFilterBPython
class itkImageToImageFilterIVD22ISSRTD22(itk.itkImageSourcePython.itkImageSourceISSRTD22):
    r"""Proxy of C++ itkImageToImageFilterIVD22ISSRTD22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_SetInput)
    GetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_GetInput)
    PushBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_PushBackInput)
    PopBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_PopBackInput)
    PushFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_PushFrontInput)
    PopFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_PopFrontInput)
    SetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_GetDirectionTolerance)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkImageToImageFilterIVD22ISSRTD22
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_cast)

# Register itkImageToImageFilterIVD22ISSRTD22 in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_swigregister(itkImageToImageFilterIVD22ISSRTD22)
itkImageToImageFilterIVD22ISSRTD22_cast = _itkStrainImageFilterPython.itkImageToImageFilterIVD22ISSRTD22_cast

class itkImageToImageFilterIVD33ISSRTD33(itk.itkImageSourcePython.itkImageSourceISSRTD33):
    r"""Proxy of C++ itkImageToImageFilterIVD33ISSRTD33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_SetInput)
    GetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_GetInput)
    PushBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_PushBackInput)
    PopBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_PopBackInput)
    PushFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_PushFrontInput)
    PopFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_PopFrontInput)
    SetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_GetDirectionTolerance)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkImageToImageFilterIVD33ISSRTD33
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_cast)

# Register itkImageToImageFilterIVD33ISSRTD33 in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_swigregister(itkImageToImageFilterIVD33ISSRTD33)
itkImageToImageFilterIVD33ISSRTD33_cast = _itkStrainImageFilterPython.itkImageToImageFilterIVD33ISSRTD33_cast

class itkImageToImageFilterIVD44ISSRTD44(itk.itkImageSourcePython.itkImageSourceISSRTD44):
    r"""Proxy of C++ itkImageToImageFilterIVD44ISSRTD44 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_SetInput)
    GetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_GetInput)
    PushBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_PushBackInput)
    PopBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_PopBackInput)
    PushFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_PushFrontInput)
    PopFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_PopFrontInput)
    SetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_GetDirectionTolerance)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkImageToImageFilterIVD44ISSRTD44
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_cast)

# Register itkImageToImageFilterIVD44ISSRTD44 in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_swigregister(itkImageToImageFilterIVD44ISSRTD44)
itkImageToImageFilterIVD44ISSRTD44_cast = _itkStrainImageFilterPython.itkImageToImageFilterIVD44ISSRTD44_cast

class itkImageToImageFilterIVF22ISSRTF22(itk.itkImageSourcePython.itkImageSourceISSRTF22):
    r"""Proxy of C++ itkImageToImageFilterIVF22ISSRTF22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_SetInput)
    GetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_GetInput)
    PushBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_PushBackInput)
    PopBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_PopBackInput)
    PushFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_PushFrontInput)
    PopFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_PopFrontInput)
    SetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_GetDirectionTolerance)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkImageToImageFilterIVF22ISSRTF22
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_cast)

# Register itkImageToImageFilterIVF22ISSRTF22 in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_swigregister(itkImageToImageFilterIVF22ISSRTF22)
itkImageToImageFilterIVF22ISSRTF22_cast = _itkStrainImageFilterPython.itkImageToImageFilterIVF22ISSRTF22_cast

class itkImageToImageFilterIVF33ISSRTF33(itk.itkImageSourcePython.itkImageSourceISSRTF33):
    r"""Proxy of C++ itkImageToImageFilterIVF33ISSRTF33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_SetInput)
    GetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_GetInput)
    PushBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_PushBackInput)
    PopBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_PopBackInput)
    PushFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_PushFrontInput)
    PopFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_PopFrontInput)
    SetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_GetDirectionTolerance)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkImageToImageFilterIVF33ISSRTF33
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_cast)

# Register itkImageToImageFilterIVF33ISSRTF33 in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_swigregister(itkImageToImageFilterIVF33ISSRTF33)
itkImageToImageFilterIVF33ISSRTF33_cast = _itkStrainImageFilterPython.itkImageToImageFilterIVF33ISSRTF33_cast

class itkImageToImageFilterIVF44ISSRTF44(itk.itkImageSourcePython.itkImageSourceISSRTF44):
    r"""Proxy of C++ itkImageToImageFilterIVF44ISSRTF44 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_SetInput)
    GetInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_GetInput)
    PushBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_PushBackInput)
    PopBackInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_PopBackInput)
    PushFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_PushFrontInput)
    PopFrontInput = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_PopFrontInput)
    SetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_SetCoordinateTolerance)
    GetCoordinateTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_GetCoordinateTolerance)
    SetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_SetDirectionTolerance)
    GetDirectionTolerance = _swig_new_instance_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_GetDirectionTolerance)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkImageToImageFilterIVF44ISSRTF44
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_cast)

# Register itkImageToImageFilterIVF44ISSRTF44 in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_swigregister(itkImageToImageFilterIVF44ISSRTF44)
itkImageToImageFilterIVF44ISSRTF44_cast = _itkStrainImageFilterPython.itkImageToImageFilterIVF44ISSRTF44_cast


def itkStrainImageFilterIVD22DD_New():
    return itkStrainImageFilterIVD22DD.New()

class itkStrainImageFilterIVD22DD(itkImageToImageFilterIVD22ISSRTD22):
    r"""Proxy of C++ itkStrainImageFilterIVD22DD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD___New_orig__)
    Clone = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_Clone)
    SetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_SetGradientFilter)
    GetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_GetGradientFilter)
    SetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_SetVectorGradientFilter)
    GetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_GetVectorGradientFilter)
    StrainFormType_INFINITESIMAL = _itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_StrainFormType_INFINITESIMAL
    
    StrainFormType_GREENLAGRANGIAN = _itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_StrainFormType_GREENLAGRANGIAN
    
    StrainFormType_EULERIANALMANSI = _itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_StrainFormType_EULERIANALMANSI
    
    SetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_SetStrainForm)
    GetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_GetStrainForm)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkStrainImageFilterIVD22DD
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_cast)

    def New(*args, **kargs):
        """New() -> itkStrainImageFilterIVD22DD

        Create a new object of the class itkStrainImageFilterIVD22DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStrainImageFilterIVD22DD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStrainImageFilterIVD22DD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStrainImageFilterIVD22DD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStrainImageFilterIVD22DD in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_swigregister(itkStrainImageFilterIVD22DD)
itkStrainImageFilterIVD22DD___New_orig__ = _itkStrainImageFilterPython.itkStrainImageFilterIVD22DD___New_orig__
itkStrainImageFilterIVD22DD_cast = _itkStrainImageFilterPython.itkStrainImageFilterIVD22DD_cast


def itkStrainImageFilterIVD33DD_New():
    return itkStrainImageFilterIVD33DD.New()

class itkStrainImageFilterIVD33DD(itkImageToImageFilterIVD33ISSRTD33):
    r"""Proxy of C++ itkStrainImageFilterIVD33DD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD___New_orig__)
    Clone = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_Clone)
    SetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_SetGradientFilter)
    GetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_GetGradientFilter)
    SetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_SetVectorGradientFilter)
    GetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_GetVectorGradientFilter)
    StrainFormType_INFINITESIMAL = _itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_StrainFormType_INFINITESIMAL
    
    StrainFormType_GREENLAGRANGIAN = _itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_StrainFormType_GREENLAGRANGIAN
    
    StrainFormType_EULERIANALMANSI = _itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_StrainFormType_EULERIANALMANSI
    
    SetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_SetStrainForm)
    GetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_GetStrainForm)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkStrainImageFilterIVD33DD
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_cast)

    def New(*args, **kargs):
        """New() -> itkStrainImageFilterIVD33DD

        Create a new object of the class itkStrainImageFilterIVD33DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStrainImageFilterIVD33DD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStrainImageFilterIVD33DD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStrainImageFilterIVD33DD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStrainImageFilterIVD33DD in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_swigregister(itkStrainImageFilterIVD33DD)
itkStrainImageFilterIVD33DD___New_orig__ = _itkStrainImageFilterPython.itkStrainImageFilterIVD33DD___New_orig__
itkStrainImageFilterIVD33DD_cast = _itkStrainImageFilterPython.itkStrainImageFilterIVD33DD_cast


def itkStrainImageFilterIVD44DD_New():
    return itkStrainImageFilterIVD44DD.New()

class itkStrainImageFilterIVD44DD(itkImageToImageFilterIVD44ISSRTD44):
    r"""Proxy of C++ itkStrainImageFilterIVD44DD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD___New_orig__)
    Clone = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_Clone)
    SetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_SetGradientFilter)
    GetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_GetGradientFilter)
    SetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_SetVectorGradientFilter)
    GetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_GetVectorGradientFilter)
    StrainFormType_INFINITESIMAL = _itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_StrainFormType_INFINITESIMAL
    
    StrainFormType_GREENLAGRANGIAN = _itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_StrainFormType_GREENLAGRANGIAN
    
    StrainFormType_EULERIANALMANSI = _itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_StrainFormType_EULERIANALMANSI
    
    SetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_SetStrainForm)
    GetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_GetStrainForm)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkStrainImageFilterIVD44DD
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_cast)

    def New(*args, **kargs):
        """New() -> itkStrainImageFilterIVD44DD

        Create a new object of the class itkStrainImageFilterIVD44DD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStrainImageFilterIVD44DD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStrainImageFilterIVD44DD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStrainImageFilterIVD44DD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStrainImageFilterIVD44DD in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_swigregister(itkStrainImageFilterIVD44DD)
itkStrainImageFilterIVD44DD___New_orig__ = _itkStrainImageFilterPython.itkStrainImageFilterIVD44DD___New_orig__
itkStrainImageFilterIVD44DD_cast = _itkStrainImageFilterPython.itkStrainImageFilterIVD44DD_cast


def itkStrainImageFilterIVF22FF_New():
    return itkStrainImageFilterIVF22FF.New()

class itkStrainImageFilterIVF22FF(itkImageToImageFilterIVF22ISSRTF22):
    r"""Proxy of C++ itkStrainImageFilterIVF22FF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF___New_orig__)
    Clone = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_Clone)
    SetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_SetGradientFilter)
    GetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_GetGradientFilter)
    SetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_SetVectorGradientFilter)
    GetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_GetVectorGradientFilter)
    StrainFormType_INFINITESIMAL = _itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_StrainFormType_INFINITESIMAL
    
    StrainFormType_GREENLAGRANGIAN = _itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_StrainFormType_GREENLAGRANGIAN
    
    StrainFormType_EULERIANALMANSI = _itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_StrainFormType_EULERIANALMANSI
    
    SetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_SetStrainForm)
    GetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_GetStrainForm)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkStrainImageFilterIVF22FF
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_cast)

    def New(*args, **kargs):
        """New() -> itkStrainImageFilterIVF22FF

        Create a new object of the class itkStrainImageFilterIVF22FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStrainImageFilterIVF22FF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStrainImageFilterIVF22FF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStrainImageFilterIVF22FF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStrainImageFilterIVF22FF in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_swigregister(itkStrainImageFilterIVF22FF)
itkStrainImageFilterIVF22FF___New_orig__ = _itkStrainImageFilterPython.itkStrainImageFilterIVF22FF___New_orig__
itkStrainImageFilterIVF22FF_cast = _itkStrainImageFilterPython.itkStrainImageFilterIVF22FF_cast


def itkStrainImageFilterIVF33FF_New():
    return itkStrainImageFilterIVF33FF.New()

class itkStrainImageFilterIVF33FF(itkImageToImageFilterIVF33ISSRTF33):
    r"""Proxy of C++ itkStrainImageFilterIVF33FF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF___New_orig__)
    Clone = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_Clone)
    SetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_SetGradientFilter)
    GetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_GetGradientFilter)
    SetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_SetVectorGradientFilter)
    GetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_GetVectorGradientFilter)
    StrainFormType_INFINITESIMAL = _itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_StrainFormType_INFINITESIMAL
    
    StrainFormType_GREENLAGRANGIAN = _itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_StrainFormType_GREENLAGRANGIAN
    
    StrainFormType_EULERIANALMANSI = _itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_StrainFormType_EULERIANALMANSI
    
    SetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_SetStrainForm)
    GetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_GetStrainForm)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkStrainImageFilterIVF33FF
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_cast)

    def New(*args, **kargs):
        """New() -> itkStrainImageFilterIVF33FF

        Create a new object of the class itkStrainImageFilterIVF33FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStrainImageFilterIVF33FF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStrainImageFilterIVF33FF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStrainImageFilterIVF33FF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStrainImageFilterIVF33FF in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_swigregister(itkStrainImageFilterIVF33FF)
itkStrainImageFilterIVF33FF___New_orig__ = _itkStrainImageFilterPython.itkStrainImageFilterIVF33FF___New_orig__
itkStrainImageFilterIVF33FF_cast = _itkStrainImageFilterPython.itkStrainImageFilterIVF33FF_cast


def itkStrainImageFilterIVF44FF_New():
    return itkStrainImageFilterIVF44FF.New()

class itkStrainImageFilterIVF44FF(itkImageToImageFilterIVF44ISSRTF44):
    r"""Proxy of C++ itkStrainImageFilterIVF44FF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF___New_orig__)
    Clone = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_Clone)
    SetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_SetGradientFilter)
    GetGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_GetGradientFilter)
    SetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_SetVectorGradientFilter)
    GetVectorGradientFilter = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_GetVectorGradientFilter)
    StrainFormType_INFINITESIMAL = _itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_StrainFormType_INFINITESIMAL
    
    StrainFormType_GREENLAGRANGIAN = _itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_StrainFormType_GREENLAGRANGIAN
    
    StrainFormType_EULERIANALMANSI = _itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_StrainFormType_EULERIANALMANSI
    
    SetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_SetStrainForm)
    GetStrainForm = _swig_new_instance_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_GetStrainForm)
    __swig_destroy__ = _itkStrainImageFilterPython.delete_itkStrainImageFilterIVF44FF
    cast = _swig_new_static_method(_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_cast)

    def New(*args, **kargs):
        """New() -> itkStrainImageFilterIVF44FF

        Create a new object of the class itkStrainImageFilterIVF44FF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStrainImageFilterIVF44FF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStrainImageFilterIVF44FF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStrainImageFilterIVF44FF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStrainImageFilterIVF44FF in _itkStrainImageFilterPython:
_itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_swigregister(itkStrainImageFilterIVF44FF)
itkStrainImageFilterIVF44FF___New_orig__ = _itkStrainImageFilterPython.itkStrainImageFilterIVF44FF___New_orig__
itkStrainImageFilterIVF44FF_cast = _itkStrainImageFilterPython.itkStrainImageFilterIVF44FF_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def image_to_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ImageToImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ImageToImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def image_to_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.Strain.ImageToImageFilter
    image_to_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    image_to_image_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def strain_image_filter(*args: itkt.ImageLike,  gradient_filter=..., vector_gradient_filter=..., strain_form=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for StrainImageFilter"""
    import itk

    kwarg_typehints = { 'gradient_filter':gradient_filter,'vector_gradient_filter':vector_gradient_filter,'strain_form':strain_form }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.StrainImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def strain_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.Strain.StrainImageFilter
    strain_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    strain_image_filter.__doc__ = filter_object.__doc__




