# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
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
"""Corpus of domain names scraped from Common Crawl and manually annotated to add word boundaries (e.g. "commoncrawl" to "common crawl")."""


import datasets


# Find for instance the citation on arxiv or on the dataset repo/website
_CITATION = """\
@inproceedings{zrs2020urlsegmentation,
  title={Semi-supervised URL Segmentation with Recurrent Neural Networks Pre-trained on Knowledge Graph Entities},
  author={Hao Zhang and Jae Ro and Richard William Sproat},
  booktitle={The 28th International Conference on Computational Linguistics (COLING 2020)},
  year={2020}
}
"""


_DESCRIPTION = """Corpus of domain names scraped from Common Crawl and manually annotated to add word boundaries (e.g. "commoncrawl" to "common crawl"). Breaking domain names such as "openresearch" into component words "open" and "research" is important for applications such as Text-to-Speech synthesis and web search. Common Crawl is an open repository of web crawl data that can be accessed and analyzed by anyone. Specifically, we scraped the plaintext (WET) extracts for domain names from URLs that contained diverse letter casing (e.g. "OpenBSD"). Although in the previous example, segmentation is trivial using letter casing, this was not always the case (e.g. "NASA"), so we had to manually annotate the data. The dataset is stored as plaintext file where each line is an example of space separated segments of a domain name. The examples are stored in their original letter casing, but harder and more interesting examples can be generated by lowercasing the input first."""

_HOMEPAGE = "https://github.com/google-research-datasets/common-crawl-domain-names"

_LICENSE = "MIT License"


# The HuggingFace dataset library don't host the datasets but only point to the original files
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
_URLs = {
    "train": "https://raw.githubusercontent.com/google-research-datasets/common-crawl-domain-names/master/data/train.txt",
    "test": "https://raw.githubusercontent.com/google-research-datasets/common-crawl-domain-names/master/data/test.txt",
    "dev": "https://raw.githubusercontent.com/google-research-datasets/common-crawl-domain-names/master/data/eval.txt",
}


class CrawlDomain(datasets.GeneratorBasedBuilder):
    """Corpus of domain names scraped from Common Crawl and manually annotated to add word boundaries (e.g. "commoncrawl" to "common crawl")."""

    VERSION = datasets.Version("1.0.0")

    def _info(self):

        features = datasets.Features(
            {"example": datasets.Value("string")}  # These are the features of your dataset like images, labels ...
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=None,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""

        train_path = dl_manager.download_and_extract(_URLs["train"])
        test_path = dl_manager.download_and_extract(_URLs["test"])
        dev_path = dl_manager.download_and_extract(_URLs["dev"])

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": train_path,
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={"filepath": test_path, "split": "test"},
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": dev_path,
                    "split": "dev",
                },
            ),
        ]

    def _generate_examples(self, filepath, split):
        """Yields examples."""
        with open(filepath, encoding="utf-8") as f:
            for id_, row in enumerate(f):
                yield id_, {
                    "example": row.rstrip(),
                }
