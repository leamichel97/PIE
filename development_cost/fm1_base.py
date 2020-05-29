# -*- coding: utf-8 -*-
"""
  fm1_base.py generated by WhatsOpt 1.8.2
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 459


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class Fm1Base(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate Fm1 discipline """

    def __init__(self, **kwargs):
        super(Fm1Base, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("fm1")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('M_PA_percentage', val=0.05, desc='')
        self.add_input('TFU', val=np.ones((32,)), desc='')

        self.add_output('FM1', val=np.ones((32,)), desc='')



        