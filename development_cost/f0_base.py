# -*- coding: utf-8 -*-
"""
  f0_base.py generated by WhatsOpt 1.9.0
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

class F0Base(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate F0 discipline """

    def __init__(self, **kwargs):
        super(F0Base, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("f0")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('Ns', val=3.5, desc='')

        self.add_output('f0', val=1.0, desc='')



        