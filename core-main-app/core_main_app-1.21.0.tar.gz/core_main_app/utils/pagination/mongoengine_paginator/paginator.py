""" Mongoengine paginator
"""
import inspect
import logging

from django.core.paginator import Paginator as DjangoPaginator
from django.utils.functional import cached_property

logger = logging.getLogger(__name__)


class MongoenginePaginator(DjangoPaginator):
    @cached_property
    def count(self):
        """Return the total number of objects, across all pages. Override for mongoengine compatibility.

        Explanation:
            count method in /django/core/paginator.py checks method_has_no_args(c)
            where c is queryset.count() method.

            count method in /mongoengine/queryset/queryset.py has a with_limit_and_skip arg, thus the test fails and
            this results in len(queryset) being called (bad for performances)
        """
        c = getattr(self.object_list, "count", None)
        if callable(c) and not inspect.isbuiltin(c):
            return c()

        logger.warning("count() function was not called. Calling len() instead.")
        return len(self.object_list)
