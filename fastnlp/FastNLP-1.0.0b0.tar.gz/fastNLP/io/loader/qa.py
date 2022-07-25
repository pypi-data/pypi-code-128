r"""
该文件中的 **Loader** 主要用于读取问答式任务的数据
"""


from .loader import Loader
import json
from fastNLP.core.dataset import DataSet, Instance

__all__ = ['CMRC2018Loader']


class CMRC2018Loader(Loader):
    r"""
    **CMRC2018** 数据集的 **Loader** ，如果您使用了本数据，请引用
    A Span-Extraction Dataset for Chinese Machine Reading Comprehension. Yiming Cui, Ting Liu, etc.
    
    请直接使用从 **fastNLP** 下载的数据进行处理。该数据集未提供测试集，测试需要通过上传到对应的系统进行评测。

    读取之后训练集 :class:`~fastNLP.core.DataSet` 将具备以下的内容，每个问题的答案只有一个：

    .. csv-table::
       :header: "title", "context", "question", "answers", "answer_starts", "id"

       "范廷颂", "范廷颂枢机（，），圣名保禄·若瑟（）...", "范廷颂是什么时候被任为主教的？", ["1963年"], ["30"], "TRAIN_186_QUERY_0"
       "范廷颂", "范廷颂枢机（，），圣名保禄·若瑟（）...", "1990年，范廷颂担任什么职务？", ["1990年被擢升为天..."], ["41"],"TRAIN_186_QUERY_1"
       "...", "...", "...","...", ".", "..."

    其中 ``title`` 是文本的标题，多条记录可能是相同的 ``title`` ；``id`` 是该问题的 id，具备唯一性。

    验证集 :class:`~fastNLP.core.DataSet` 将具备以下的内容，每个问题的答案可能有三个（有时候只是3个重复的答案）：

    .. csv-table::
       :header: "title", "context", "question", "answers", "answer_starts", "id"

       "战国无双3", "《战国无双3》（）是由光荣和ω-force开发...", "《战国无双3》是由哪两个公司合作开发的？", "['光荣和ω-force', '光荣和ω-force', '光荣和ω-force']", "[30, 30, 30]", "DEV_0_QUERY_0"
       "战国无双3", "《战国无双3》（）是由光荣和ω-force开发...", "男女主角亦有专属声优这一模式是由谁改编的？", "['村雨城', '村雨城', '任天堂游戏谜之村雨城']", "[226, 226, 219]", "DEV_0_QUERY_1"
       "...", "...", "...","...", ".", "..."

    其中 ``answer_starts`` 是从 0 开始的 index。例如 ``"我来自a复旦大学？"`` ，其中 ``"复"`` 的开始 index 为 **4**。另外 ``"Russell评价说"``
    中的 ``"说"`` 的 index 为 **9** ， 因为英文和数字都直接按照 character 计量的。
    """
    def __init__(self):
        super().__init__()

    def _load(self, path: str) -> DataSet:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)['data']
            ds = DataSet()
            for entry in data:
                title = entry['title']
                para = entry['paragraphs'][0]
                context = para['context']
                qas = para['qas']
                for qa in qas:
                    question = qa['question']
                    ans = qa['answers']
                    answers = []
                    answer_starts = []
                    id = qa['id']
                    for an in ans:
                        answers.append(an['text'])
                        answer_starts.append(an['answer_start'])
                    ds.append(Instance(title=title, context=context, question=question, answers=answers,
                                       answer_starts=answer_starts,id=id))
        return ds

    def download(self) -> str:
        r"""
        自动下载数据集。

        :return: 数据集目录地址
        """
        output_dir = self._get_dataset_path('cmrc2018')
        return output_dir

