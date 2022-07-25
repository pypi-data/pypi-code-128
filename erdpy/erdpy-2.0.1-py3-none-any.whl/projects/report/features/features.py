from typing import List

from erdpy.projects.report.features.report_option import ReportFeature
from erdpy.projects.report.features.size import Size
from erdpy.projects.report.features.twiggy_paths_check import TwiggyPathsCheck


def get_default_report_features() -> List[ReportFeature]:
    return [
        Size("size"),
        TwiggyPathsCheck("has-allocator", pattern="wee_alloc::"),
        TwiggyPathsCheck("has-format", pattern="core::fmt"),
    ]
