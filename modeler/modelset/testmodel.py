# -*- coding: utf-8 -*-
import random

__author__ = 'stsouko'
from modelset import register_model


class Model():
    def __init__(self):
        print("started")

    def getdesc(self):
        desc = 'this model nothing do, but return something'
        return desc

    def getname(self):
        name = 'tesmodelname'
        return name

    def is_reation(self):
        return 1

    def gethashes(self):
        hashlist = ['1006099,1017020,4007079', '1006099,1007079,1017020']
        return hashlist

    def getresult(self, chemical):
        """do some operations on chemical"""

        result = [dict(type='text', attrib='fictparam', value=random.randrange(0, 100)),
                  dict(type='link', attrib='fictlink', value='download/1427724576.zip'),
                  dict(type='structure', attrib='fictstruct', value='<?xml version="1.0" encoding="UTF-8"?><cml xmlns="http://www.chemaxon.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.chemaxon.com/marvin/help/formats/schema/mrvSchema_14_7_14.xsd" version="ChemAxon file format v14.7.14, generated by v14.7.28.0"><MDocument>  <MChemicalStruct>    <molecule molID="m1">      <atomArray atomID="a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 a16 a17 a18" elementType="C C C C C C C C C C C C C C C C C C" x2="-1.278749942779541 -2.612389942779541 -3.946183942779541 -3.946183942779541 -2.612389942779541 -1.278749942779541 0.05489005722045892 1.388684057220459 1.388684057220459 0.05489005722045892 2.722324057220459 1.388684057220459 0.05489005722045892 2.722324057220459 4.055964057220459 5.389758057220459 5.389758057220459 4.055964057220459" y2="0.8937500011920929 1.663750001192093 0.8937500011920929 -0.6462499988079071 -1.4162499988079071 -0.6462499988079071 -1.4162499988079071 -0.6462499988079071 0.8937500011920929 1.663750001192093 3.203750001192093 3.973750001192093 3.203750001192093 1.663750001192093 0.8937500011920929 1.663750001192093 3.203750001192093 3.973750001192093"/>      <bondArray>        <bond id="b1" atomRefs2="a1 a2" order="2"/>        <bond id="b2" atomRefs2="a1 a6" order="1"/>        <bond id="b3" atomRefs2="a1 a10" order="1"/>        <bond id="b4" atomRefs2="a2 a3" order="1"/>        <bond id="b5" atomRefs2="a3 a4" order="2"/>        <bond id="b6" atomRefs2="a4 a5" order="1"/>        <bond id="b7" atomRefs2="a5 a6" order="2"/>        <bond id="b8" atomRefs2="a6 a7" order="1"/>        <bond id="b9" atomRefs2="a7 a8" order="2"/>        <bond id="b10" atomRefs2="a8 a9" order="1"/>        <bond id="b11" atomRefs2="a9 a10" order="2"/>        <bond id="b12" atomRefs2="a11 a12" order="1"/>        <bond id="b13" atomRefs2="a12 a13" order="2"/>        <bond id="b14" atomRefs2="a15 a16" order="1"/>        <bond id="b15" atomRefs2="a16 a17" order="2"/>        <bond id="b16" atomRefs2="a17 a18" order="1"/>        <bond id="b17" atomRefs2="a11 a14" order="1"/>        <bond id="b18" atomRefs2="a11 a18" order="2"/>        <bond id="b19" atomRefs2="a14 a15" order="2"/>        <bond id="b20" atomRefs2="a9 a14" order="1"/>        <bond id="b21" atomRefs2="a13 a10" order="1"/>      </bondArray>    </molecule>  </MChemicalStruct></MDocument></cml>')]
        return result


model = Model()
register_model(model.getname(), model)