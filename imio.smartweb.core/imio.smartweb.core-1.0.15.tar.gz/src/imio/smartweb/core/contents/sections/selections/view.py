# -*- coding: utf-8 -*-

from imio.smartweb.core.contents.sections.views import CarouselOrTableSectionView
from imio.smartweb.core.utils import batch_results

import logging

logger = logging.getLogger("imio.smartweb.core")


class SelectionsView(CarouselOrTableSectionView):
    """Selection Section view"""

    def items(self):
        image_scale = self.image_scale
        items = [rel.to_object for rel in self.context.selected_items]
        results = []
        for item in items:
            if item is None:
                # TODO we need to understand why relations break and fix that
                logger.warning(
                    f"Broken selection item in {self.context.absolute_url()}"
                )
                continue
            url = item.absolute_url()
            description = item.description or ""
            has_image = True if getattr(item.aq_base, "image", None) else False
            results.append(
                {
                    "title": item.title,
                    "description": description.replace("**", ""),
                    "url": url,
                    "image": f"{url}/@@images/image/{image_scale}",
                    "has_image": has_image,
                }
            )
        return batch_results(results, self.context.nb_results_by_batch)
