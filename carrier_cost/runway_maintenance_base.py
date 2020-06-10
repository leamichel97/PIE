# -*- coding: utf-8 -*-
"""
  runway_maintenance_base.py generated by WhatsOpt 1.9.0
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 458


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class RunwayMaintenanceBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate RunwayMaintenance discipline """

    def __init__(self, **kwargs):
        super(RunwayMaintenanceBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("runway_maintenance")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('CostRunwayMaint', val=25, desc='')
        self.add_input('LpA', val=1.0, desc='')

        self.add_output('C_RunwayMaint', val=1.0, desc='')



        