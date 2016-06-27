# -*- coding: utf-8 -*-
#
# Copyright 2016 Ramil Nugmanov <stsouko@live.ru>
# This file is part of PREDICTOR.
#
# PREDICTOR is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
import pandas as pd
from CGRtools.SDFread import SDFread
from CGRtools.RDFread import RDFread


class Descriptorchain(object):
    def __init__(self, *args):
        self.__gens = args

    def get(self, structure, **kwargs):

        return dict(X=pd.concat(tX, axis=1), Y=tY, AD=reduce(operator.mul, tD), )


class Descriptorsdict(object):
    def __init__(self, data, isreaction=False):
        self.__isreaction = isreaction
        self.__extention = data
        self.__extheader = self.__prepareextheader(data)

    def __prepareextheader(self, data):
        tmp = []
        for i, j in data.items():
            if j:
                tmp.extend(j['value'].columns)
            else:
                tmp.append(i)
        return tmp

    def __parsefile(self, structures):
        extblock = []
        reader = RDFread(structures) if self.__isreaction else SDFread(structures)
        for i in reader.readdata():
            meta = i['meta'] if self.__isreaction else i.graph['meta']
            tmp = []
            for key, value in meta.items():
                if key in self.__extention:
                    data = self.__extention[key]['value'].loc[self.__extention[key]['key'] == value] if \
                        self.__extention[key] else pd.DataFrame([{key: float(value)}])
                    data.index = [0]
                    tmp.append(data)
            extblock.append(pd.concat(tmp, axis=1) if tmp else pd.DataFrame([{}]))
        res = pd.DataFrame(pd.concat(extblock), columns=self.__extheader)
        res.index = range(len(res.index))
        return res

    def __parseadditions0(self, **kwargs):  # buggy???
        extblock = []
        for i, j in kwargs.items():
            if i in self.__extention:
                for n, k in enumerate(j) if isinstance(j, list) else j.items():
                    data = self.__extention[i]['value'].loc[self.__extention[i]['key'] == k] if \
                        self.__extention[i] else pd.DataFrame([{i: k}])
                    data.index = [0]
                    if len(extblock) > n:
                        extblock[n].append(data)
                    else:
                        extblock.extend([[] for _ in range(n - len(extblock))] + [[data]])
        res = pd.DataFrame(pd.concat([pd.concat(x, axis=1) if x else pd.DataFrame([{}]) for x in extblock]),
                           columns=self.__extheader)
        res.index = range(len(res.index))
        return res

    def __parseadditions1(self, **kwargs):
        tmp = []
        for i, j in kwargs.items():
            if i in self.__extention:
                data = self.__extention[i]['value'].loc[self.__extention[i]['key'] == j] if \
                       self.__extention[i] else pd.DataFrame([{i: j}])
                data.index = [0]
                tmp.append(data)
        return pd.DataFrame(pd.concat(tmp, axis=1) if tmp else pd.DataFrame([{}]), columns=self.__extheader)

    def get(self, structure=None, **kwargs):
        if kwargs.get('parsesdf'):
            extblock = self.__parsefile(structure)

        elif all(isinstance(x, list) or isinstance(x, dict) for y, x in kwargs.items() if y in self.__extention):
            extblock = self.__parseadditions0(**kwargs)

        elif not any(isinstance(x, list) or isinstance(x, dict) for y, x in kwargs.items() if
                     y in self.__extention):
            extblock = self.__parseadditions1(**kwargs)

        else:
            print('WHAT DO YOU WANT? use correct extentions params')
            return False

        return dict(X=extblock, AD=-extblock.isnull().any(axis=1))