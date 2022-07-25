"""
This module contains essential stuff that should've come with Python itself ;)
"""
import gc
import os
import re
import inspect
import weakref
import errno
import six
from functools import partial, wraps
from itertools import chain
import sys

from scrapy.utils.decorators import deprecated


def flatten(x):
    """flatten(sequence) -> list

    Returns a single, flat list which contains all elements retrieved
    from the sequence and all recursively contained sub-sequences
    (iterables).

    Examples:
    >>> [1, 2, [3,4], (5,6)]
    [1, 2, [3, 4], (5, 6)]
    >>> flatten([[[1,2,3], (42,None)], [4,5], [6], 7, (8,9,10)])
    [1, 2, 3, 42, None, 4, 5, 6, 7, 8, 9, 10]
    >>> flatten(["foo", "bar"])
    ['foo', 'bar']
    >>> flatten(["foo", ["baz", 42], "bar"])
    ['foo', 'baz', 42, 'bar']
    """
    return list(iflatten(x))


def iflatten(x):
    """iflatten(sequence) -> iterator

    Similar to ``.flatten()``, but returns iterator instead"""
    for el in x:
        if is_listlike(el):
            for el_ in iflatten(el):
                yield el_
        else:
            yield el


def is_listlike(x):
    """
    >>> is_listlike("foo")
    False
    >>> is_listlike(5)
    False
    >>> is_listlike(b"foo")
    False
    >>> is_listlike([b"foo"])
    True
    >>> is_listlike((b"foo",))
    True
    >>> is_listlike({})
    True
    >>> is_listlike(set())
    True
    >>> is_listlike((x for x in range(3)))
    True
    >>> is_listlike(six.moves.xrange(5))
    True
    """
    return hasattr(x, "__iter__") and not isinstance(x, (six.text_type, bytes))


def unique(list_, key=lambda x: x):
    """efficient function to uniquify a list preserving item order"""
    seen = set()
    result = []
    for item in list_:
        seenkey = key(item)
        if seenkey in seen:
            continue
        seen.add(seenkey)
        result.append(item)
    return result


def to_unicode(text, encoding=None, errors='strict'):
    """Return the unicode representation of a bytes object ``text``. If
    ``text`` is already an unicode object, return it as-is."""
    if isinstance(text, six.text_type):
        return text
    if not isinstance(text, (bytes, six.text_type)):
        raise TypeError('to_unicode must receive a bytes, str or unicode '
                        'object, got %s' % type(text).__name__)
    if encoding is None:
        encoding = 'utf-8'
    return text.decode(encoding, errors)


def to_bytes(text, encoding=None, errors='strict'):
    """Return the binary representation of ``text``. If ``text``
    is already a bytes object, return it as-is."""
    if isinstance(text, bytes):
        return text
    if not isinstance(text, six.string_types):
        raise TypeError('to_bytes must receive a unicode, str or bytes '
                        'object, got %s' % type(text).__name__)
    if encoding is None:
        encoding = 'utf-8'
    return text.encode(encoding, errors)


def to_native_str(text, encoding=None, errors='strict'):
    """ Return str representation of ``text``
    (bytes in Python 2.x and unicode in Python 3.x). """
    if six.PY2:
        return to_bytes(text, encoding, errors)
    else:
        return to_unicode(text, encoding, errors)


def re_rsearch(pattern, text, chunk_size=1024):
    """
    This function does a reverse search in a text using a regular expression
    given in the attribute 'pattern'.
    Since the re module does not provide this functionality, we have to find for
    the expression into chunks of text extracted from the end (for the sake of efficiency).
    At first, a chunk of 'chunk_size' kilobytes is extracted from the end, and searched for
    the pattern. If the pattern is not found, another chunk is extracted, and another
    search is performed.
    This process continues until a match is found, or until the whole file is read.
    In case the pattern wasn't found, None is returned, otherwise it returns a tuple containing
    the start position of the match, and the ending (regarding the entire text).
    """
    def _chunk_iter():
        offset = len(text)
        while True:
            offset -= (chunk_size * 1024)
            if offset <= 0:
                break
            yield (text[offset:], offset)
        yield (text, 0)

    if isinstance(pattern, six.string_types):
        pattern = re.compile(pattern)

    for chunk, offset in _chunk_iter():
        matches = [match for match in pattern.finditer(chunk)]
        if matches:
            start, end = matches[-1].span()
            return offset + start, offset + end
    return None


def memoizemethod_noargs(method):
    """Decorator to cache the result of a method (without arguments) using a
    weak reference to its object
    """
    cache = weakref.WeakKeyDictionary()
    @wraps(method)
    def new_method(self, *args, **kwargs):
        if self not in cache:
            cache[self] = method(self, *args, **kwargs)
        return cache[self]
    return new_method


_BINARYCHARS = {six.b(chr(i)) for i in range(32)} - {b"\0", b"\t", b"\n", b"\r"}
_BINARYCHARS |= {ord(ch) for ch in _BINARYCHARS}

@deprecated("scrapy.utils.python.binary_is_text")
def isbinarytext(text):
    """ This function is deprecated.
    Please use scrapy.utils.python.binary_is_text, which was created to be more
    clear about the functions behavior: it is behaving inverted to this one. """
    return not binary_is_text(text)


def binary_is_text(data):
    """ Returns ``True`` if the given ``data`` argument (a ``bytes`` object)
    does not contain unprintable control characters.
    """
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes, got '%s'" % type(data).__name__)
    return all(c not in _BINARYCHARS for c in data)


def _getargspec_py23(func):
    """_getargspec_py23(function) -> named tuple ArgSpec(args, varargs, keywords,
                                                        defaults)

    Identical to inspect.getargspec() in python2, but uses
    inspect.getfullargspec() for python3 behind the scenes to avoid
    DeprecationWarning.

    >>> def f(a, b=2, *ar, **kw):
    ...     pass

    >>> _getargspec_py23(f)
    ArgSpec(args=['a', 'b'], varargs='ar', keywords='kw', defaults=(2,))
    """
    if six.PY2:
        return inspect.getargspec(func)

    return inspect.ArgSpec(*inspect.getfullargspec(func)[:4])


def get_func_args(func, stripself=False):
    """Return the argument name list of a callable"""
    if inspect.isfunction(func):
        func_args, _, _, _ = _getargspec_py23(func)
    elif inspect.isclass(func):
        return get_func_args(func.__init__, True)
    elif inspect.ismethod(func):
        return get_func_args(func.__func__, True)
    elif inspect.ismethoddescriptor(func):
        return []
    elif isinstance(func, partial):
        return [x for x in get_func_args(func.func)[len(func.args):]
                if not (func.keywords and x in func.keywords)]
    elif hasattr(func, '__call__'):
        if inspect.isroutine(func):
            return []
        elif getattr(func, '__name__', None) == '__call__':
            return []
        else:
            return get_func_args(func.__call__, True)
    else:
        raise TypeError('%s is not callable' % type(func))
    if stripself:
        func_args.pop(0)
    return func_args


def get_spec(func):
    """Returns (args, kwargs) tuple for a function
    >>> import re
    >>> get_spec(re.match)
    (['pattern', 'string'], {'flags': 0})

    >>> class Test(object):
    ...     def __call__(self, val):
    ...         pass
    ...     def method(self, val, flags=0):
    ...         pass

    >>> get_spec(Test)
    (['self', 'val'], {})

    >>> get_spec(Test.method)
    (['self', 'val'], {'flags': 0})

    >>> get_spec(Test().method)
    (['self', 'val'], {'flags': 0})
    """

    if inspect.isfunction(func) or inspect.ismethod(func):
        spec = _getargspec_py23(func)
    elif hasattr(func, '__call__'):
        spec = _getargspec_py23(func.__call__)
    else:
        raise TypeError('%s is not callable' % type(func))

    defaults = spec.defaults or []

    firstdefault = len(spec.args) - len(defaults)
    args = spec.args[:firstdefault]
    kwargs = dict(zip(spec.args[firstdefault:], defaults))
    return args, kwargs


def equal_attributes(obj1, obj2, attributes):
    """Compare two objects attributes"""
    # not attributes given return False by default
    if not attributes:
        return False

    temp1, temp2 = object(), object()
    for attr in attributes:
        # support callables like itemgetter
        if callable(attr):
            if attr(obj1) != attr(obj2):
                return False
        elif getattr(obj1, attr, temp1) != getattr(obj2, attr, temp2):
            return False
    # all attributes equal
    return True


class WeakKeyCache(object):

    def __init__(self, default_factory):
        self.default_factory = default_factory
        self._weakdict = weakref.WeakKeyDictionary()

    def __getitem__(self, key):
        if key not in self._weakdict:
            self._weakdict[key] = self.default_factory(key)
        return self._weakdict[key]


@deprecated
def stringify_dict(dct_or_tuples, encoding='utf-8', keys_only=True):
    """Return a (new) dict with unicode keys (and values when "keys_only" is
    False) of the given dict converted to strings. ``dct_or_tuples`` can be a
    dict or a list of tuples, like any dict constructor supports.
    """
    d = {}
    for k, v in six.iteritems(dict(dct_or_tuples)):
        k = k.encode(encoding) if isinstance(k, six.text_type) else k
        if not keys_only:
            v = v.encode(encoding) if isinstance(v, six.text_type) else v
        d[k] = v
    return d


@deprecated
def is_writable(path):
    """Return True if the given path can be written (if it exists) or created
    (if it doesn't exist)
    """
    if os.path.exists(path):
        return os.access(path, os.W_OK)
    else:
        return os.access(os.path.dirname(path), os.W_OK)


@deprecated
def setattr_default(obj, name, value):
    """Set attribute value, but only if it's not already set. Similar to
    setdefault() for dicts.
    """
    if not hasattr(obj, name):
        setattr(obj, name, value)


def retry_on_eintr(function, *args, **kw):
    """Run a function and retry it while getting EINTR errors"""
    while True:
        try:
            return function(*args, **kw)
        except IOError as e:
            if e.errno != errno.EINTR:
                raise


def without_none_values(iterable):
    """Return a copy of ``iterable`` with all ``None`` entries removed.

    If ``iterable`` is a mapping, return a dictionary where all pairs that have
    value ``None`` have been removed.
    """
    try:
        return {k: v for k, v in six.iteritems(iterable) if v is not None}
    except AttributeError:
        return type(iterable)((v for v in iterable if v is not None))


def global_object_name(obj):
    """
    Return full name of a global object.

    >>> from scrapy import Request
    >>> global_object_name(Request)
    'scrapy.http.request.Request'
    """
    return "%s.%s" % (obj.__module__, obj.__name__)


if hasattr(sys, "pypy_version_info"):
    def garbage_collect():
        # Collecting weakreferences can take two collections on PyPy.
        gc.collect()
        gc.collect()
else:
    def garbage_collect():
        gc.collect()


class MutableChain(object):
    """
    Thin wrapper around itertools.chain, allowing to add iterables "in-place"
    """
    def __init__(self, *args):
        self.data = chain(*args)

    def extend(self, *iterables):
        self.data = chain(self.data, *iterables)

    def __iter__(self):
        return self.data.__iter__()

    def __next__(self):
        return next(self.data)

    next = __next__
