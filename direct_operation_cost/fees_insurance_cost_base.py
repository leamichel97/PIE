# -*- coding: utf-8 -*-
"""
  fees_insurance_cost_base.py generated by WhatsOpt 1.8.2
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

class FeesInsuranceCostBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate FeesInsuranceCost discipline """

    def __init__(self, **kwargs):
        super(FeesInsuranceCostBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("fees_insurance_cost")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('C_PL', val=5.51, desc='')
        self.add_input('F', val=1220, desc='')
        self.add_input('I', val=100, desc='')
        self.add_input('P', val=150, desc='')

        self.add_output('C_FeesInsurance', val=1.0, desc='')



        