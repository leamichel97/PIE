# -*- coding: utf-8 -*-
"""
  ground_operation_base.py generated by WhatsOpt 1.8.2
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 322


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class GroundOperationBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate GroundOperation discipline """

    def __init__(self, **kwargs):
        super(GroundOperationBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("ground_operation")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('f11', val=0.50, desc='')
        self.add_input('f8', val=0.86, desc='')
        self.add_input('fc', val=0.60, desc='')
        self.add_input('fv', val=0.50, desc='')
        self.add_input('L', val=0.56, desc='')
        self.add_input('LpA', val=30, desc='')
        self.add_input('M0', val=26.60, desc='')
        self.add_input('N', val=3.50, desc='')
        self.add_input('W', val=320000, desc='')

        self.add_output('C_GO', val=1.0, desc='')



        