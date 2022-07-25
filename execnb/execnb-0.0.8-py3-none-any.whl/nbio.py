# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_nbio.ipynb.

# %% auto 0
__all__ = ['NbCell', 'dict2nb', 'read_nb', 'nb2dict', 'nb2str', 'write_nb']

# %% ../nbs/01_nbio.ipynb 2
from fastcore.imports import *
from fastcore.foundation import *
from fastcore.basics import *
from fastcore.xtras import *

import ast,functools
from pprint import pformat,pprint

# %% ../nbs/01_nbio.ipynb 12
class NbCell(AttrDict):
    def __init__(self, idx, cell):
        super().__init__(cell)
        self.idx_ = idx
        if 'source' in self: self.set_source(self.source)

    def set_source(self, source):
        self.source = ''.join(source)
        if '_parsed_' in self: del(self['_parsed_'])

    def parsed_(self):
        if self.cell_type!='code' or self.source.strip()[:1] in ['%', '!']: return
        if '_parsed_' not in self: 
            try: self._parsed_ = ast.parse(self.source).body
            except SyntaxError: return # you can assign the result of ! to a variable in a notebook cell, which will result in a syntax error if parsed with the ast module.
        return self._parsed_

    def __hash__(self): return hash(self.source) + hash(self.cell_type)
    def __eq__(self,o): return self.source==o.source and self.cell_type==o.cell_type

# %% ../nbs/01_nbio.ipynb 14
def dict2nb(js):
    "Convert dict `js` to an `AttrDict`, "
    nb = dict2obj(js)
    nb.cells = nb.cells.enumerate().starmap(NbCell)
    return nb

# %% ../nbs/01_nbio.ipynb 19
def read_nb(path):
    "Return notebook at `path`"
    res = dict2nb(Path(path).read_json(encoding='utf-8'))
    res['path_'] = str(path)
    return res

# %% ../nbs/01_nbio.ipynb 25
def nb2dict(d, k=None):
    "Convert parsed notebook to `dict`"
    if k in ('source',): return d.splitlines(keepends=True)
    if isinstance(d, (L,list)): return list(L(d).map(nb2dict))
    if not isinstance(d, dict): return d
    return dict(**{k:nb2dict(v,k) for k,v in d.items() if k[-1] != '_'})

# %% ../nbs/01_nbio.ipynb 28
def nb2str(nb):
    "Convert `nb` to a `str`"
    if isinstance(nb, (AttrDict,L)): nb = nb2dict(nb)
    return dumps(nb, sort_keys=True, indent=1, ensure_ascii=False) + "\n"

# %% ../nbs/01_nbio.ipynb 31
def write_nb(nb, path):
    "Write `nb` to `path`"
    with maybe_open(path, 'w', encoding='utf-8') as f: f.write(nb2str(nb))
