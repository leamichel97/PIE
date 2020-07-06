# -*- coding: utf-8 -*-
"""
  total_base.py generated by WhatsOpt 1.9.4
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

class TotalBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate Total discipline """

    def __init__(self, **kwargs):
        super(TotalBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("total")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('Cmission', val=1.0, desc='')
        self.add_input('Cprop', val=1.0, desc='')
        self.add_input('Ctransp', val=1.0, desc='')
        self.add_input('C_FeesInsurance', val=1.0, desc='')
        self.add_input('C_GO', val=1.0, desc='')

        self.add_output('C_DO', val=1.0, desc='')



        