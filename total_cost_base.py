# -*- coding: utf-8 -*-
"""
  total_cost_base.py generated by WhatsOpt 1.8.2
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: https://ether.onera.fr/whatsopt
# analysis_id: 258


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class TotalCostBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate TotalCost discipline """

    def __init__(self, **kwargs):
        super(TotalCostBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("total_cost")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('CdevSum', val=1.0, desc='')
        self.add_input('CprodTotal', val=1.0, desc='')
        self.add_input('C_carrier', val=1.0, desc='')
        self.add_input('C_DO', val=1.0, desc='')
        self.add_input('C_IO', val=1.0, desc='')

        self.add_output('C_TOTAL', val=1.0, desc='')



        