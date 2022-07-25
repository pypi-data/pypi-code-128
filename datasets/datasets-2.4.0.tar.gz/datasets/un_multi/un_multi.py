# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""MultiUN: Multilingual UN Parallel Text 2000—2009"""


import itertools
import os

import datasets


_CITATION = """\
@inproceedings{eisele-chen-2010-multiun,
    title = "{M}ulti{UN}: A Multilingual Corpus from United Nation Documents",
    author = "Eisele, Andreas  and
      Chen, Yu",
    booktitle = "Proceedings of the Seventh International Conference on Language Resources and Evaluation ({LREC}'10)",
    month = may,
    year = "2010",
    address = "Valletta, Malta",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2010/pdf/686_Paper.pdf",
    abstract = "This paper describes the acquisition, preparation and properties of a corpus extracted from the official documents of the United Nations (UN). This corpus is available in all 6 official languages of the UN, consisting of around 300 million words per language. We describe the methods we used for crawling, document formatting, and sentence alignment. This corpus also includes a common test set for machine translation. We present the results of a French-Chinese machine translation experiment performed on this corpus.",
}

@InProceedings{TIEDEMANN12.463,
  author = {J�rg Tiedemann},
  title = {Parallel Data, Tools and Interfaces in OPUS},
  booktitle = {Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC'12)},
  year = {2012},
  month = {may},
  date = {23-25},
  address = {Istanbul, Turkey},
  editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Mehmet Ugur Dogan and Bente Maegaard and Joseph Mariani and Jan Odijk and Stelios Piperidis},
  publisher = {European Language Resources Association (ELRA)},
  isbn = {978-2-9517408-7-7},
}
"""


_DESCRIPTION = """\
This is a collection of translated documents from the United Nations. \
This corpus is available in all 6 official languages of the UN, \
consisting of around 300 million words per language
"""


_HOMEPAGE = "http://www.euromatrixplus.net/multi-un/"

_LANGUAGES = ["ar", "de", "en", "es", "fr", "ru", "zh"]
_LANGUAGE_PAIRS = list(itertools.combinations(_LANGUAGES, 2))

_BASE_URL = "http://opus.nlpl.eu/download.php?f=MultiUN/v1/moses"
_URLS = {f"{l1}-{l2}": f"{_BASE_URL}/{l1}-{l2}.txt.zip" for l1, l2 in _LANGUAGE_PAIRS}


class UnMulti(datasets.GeneratorBasedBuilder):
    """MultiUN: Multilingual UN Parallel Text 2000—2009"""

    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(name=f"{l1}-{l2}", version=datasets.Version("1.0.0"), description=f"MultiUN {l1}-{l2}")
        for l1, l2 in _LANGUAGE_PAIRS
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {"translation": datasets.features.Translation(languages=tuple(self.config.name.split("-")))}
            ),
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        lang_pair = self.config.name.split("-")
        data_dir = dl_manager.download_and_extract(_URLS[self.config.name])
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "source_file": os.path.join(data_dir, f"MultiUN.{self.config.name}.{lang_pair[0]}"),
                    "target_file": os.path.join(data_dir, f"MultiUN.{self.config.name}.{lang_pair[1]}"),
                },
            ),
        ]

    def _generate_examples(self, source_file, target_file):
        source, target = tuple(self.config.name.split("-"))
        with open(source_file, encoding="utf-8") as src_f, open(target_file, encoding="utf-8") as tgt_f:
            for idx, (l1, l2) in enumerate(zip(src_f, tgt_f)):
                result = {"translation": {source: l1.strip(), target: l2.strip()}}
                yield idx, result
