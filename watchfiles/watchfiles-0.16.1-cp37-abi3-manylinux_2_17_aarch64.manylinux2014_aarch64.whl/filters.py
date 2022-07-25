import logging
import os
import re
from pathlib import Path
from typing import TYPE_CHECKING, Optional, Sequence, Union

__all__ = 'BaseFilter', 'DefaultFilter', 'PythonFilter'
logger = logging.getLogger('watchfiles.watcher')


if TYPE_CHECKING:
    from .main import Change


class BaseFilter:
    """
    Useful base class for creating filters. `BaseFilter` should be inherited and configured, rather than used
    directly.

    The class supports ignoring files in 3 ways:
    """

    __slots__ = '_ignore_dirs', '_ignore_entity_regexes', '_ignore_paths'
    ignore_dirs: Sequence[str] = ()
    """Full names of directories to ignore, an obvious example would be `.git`."""
    ignore_entity_patterns: Sequence[str] = ()
    """
    Patterns of files or directories to ignore, these are compiled into regexes.

    "entity" here refers to the specific file or directory - basically the result of `path.split(os.sep)[-1]`,
    an obvious example would be `r'\\.py[cod]$'`.
    """
    ignore_paths: Sequence[Union[str, Path]] = ()
    """
    Full paths to ignore, e.g. `/home/users/.cache` or `C:\\Users\\user\\.cache`.
    """

    def __init__(self) -> None:
        self._ignore_dirs = set(self.ignore_dirs)
        self._ignore_entity_regexes = tuple(re.compile(r) for r in self.ignore_entity_patterns)
        self._ignore_paths = tuple(map(str, self.ignore_paths))

    def __call__(self, change: 'Change', path: str) -> bool:
        """
        Instances of `BaseFilter` subclasses can be used as callables.
        Args:
            change: The type of change that occurred, see [`Change`][watchfiles.Change].
            path: the raw path of the file or directory that changed.

        Returns:
            True if the file should be included in changes, False if it should be ignored.
        """
        parts = path.lstrip(os.sep).split(os.sep)
        if any(p in self._ignore_dirs for p in parts):
            return False

        entity_name = parts[-1]
        if any(r.search(entity_name) for r in self._ignore_entity_regexes):
            return False
        elif self._ignore_paths and path.startswith(self._ignore_paths):
            return False
        else:
            return True

    def __repr__(self) -> str:
        args = ', '.join(f'{k}={getattr(self, k, None)!r}' for k in self.__slots__)
        return f'{self.__class__.__name__}({args})'


class DefaultFilter(BaseFilter):
    """
    The default filter, which ignores files and directories that you might commonly want to ignore.
    """

    ignore_dirs: Sequence[str] = (
        '__pycache__',
        '.git',
        '.hg',
        '.svn',
        '.tox',
        '.venv',
        'site-packages',
        '.idea',
        'node_modules',
    )
    """Directory names to ignore."""

    ignore_entity_patterns: Sequence[str] = (
        r'\.py[cod]$',
        r'\.___jb_...___$',
        r'\.sw.$',
        '~$',
        r'^\.\#',
        r'^\.DS_Store$',
        r'^flycheck_',
    )
    """File/Directory name patterns to ignore."""

    def __init__(
        self,
        *,
        ignore_dirs: Optional[Sequence[str]] = None,
        ignore_entity_patterns: Optional[Sequence[str]] = None,
        ignore_paths: Optional[Sequence[Union[str, Path]]] = None,
    ) -> None:
        """
        Args:
            ignore_dirs: if not `None`, overrides the `ignore_dirs` value set on the class.
            ignore_entity_patterns: if not `None`, overrides the `ignore_entity_patterns` value set on the class.
            ignore_paths: if not `None`, overrides the `ignore_paths` value set on the class.
        """
        if ignore_dirs is not None:
            self.ignore_dirs = ignore_dirs
        if ignore_entity_patterns is not None:
            self.ignore_entity_patterns = ignore_entity_patterns
        if ignore_paths is not None:
            self.ignore_paths = ignore_paths

        super().__init__()


class PythonFilter(DefaultFilter):
    """
    A filter for Python files, since this class inherits from [`DefaultFilter`][watchfiles.DefaultFilter]
    it will ignore files and directories that you might commonly want to ignore as well as filtering out
    all changes except in Python files (files with extensions `('.py', '.pyx', '.pyd')`).
    """

    def __init__(
        self,
        *,
        ignore_paths: Optional[Sequence[Union[str, Path]]] = None,
        extra_extensions: Sequence[str] = (),
    ) -> None:
        """
        Args:
            ignore_paths: The paths to ignore, see [`BaseFilter`][watchfiles.BaseFilter].
            extra_extensions: extra extensions to ignore.

        `ignore_paths` and `extra_extensions` can be passed as arguments partly to support [CLI](../cli.md) usage where
        `--ignore-paths` and `--extensions` can be passed as arguments.
        """
        self.extensions = ('.py', '.pyx', '.pyd') + tuple(extra_extensions)
        super().__init__(ignore_paths=ignore_paths)

    def __call__(self, change: 'Change', path: str) -> bool:
        return path.endswith(self.extensions) and super().__call__(change, path)
