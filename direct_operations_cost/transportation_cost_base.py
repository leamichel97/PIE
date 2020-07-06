# -*- coding: utf-8 -*-
"""
  transportation_cost_base.py generated by WhatsOpt 1.9.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 800


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class TransportationCostBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate TransportationCost discipline """

    def __init__(self, **kwargs):
        super(TransportationCostBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("transportation_cost")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('M0', val=26.60, desc='')
        self.add_input('Ts', val=5.37, desc='')

        self.add_output('Ctransp', val=1.0, desc='')



        