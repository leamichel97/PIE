# -*- coding: utf-8 -*-
"""
  carrier_cost_base.py generated by WhatsOpt 1.9.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 458


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from carrier_cost.runway import Runway
from carrier_cost.runway_maintenance import RunwayMaintenance
from carrier_cost.aircraft_flight import AircraftFlight
from carrier_cost.total import Total






class CarrierCostBase(Group):
    """ An OpenMDAO base component to encapsulate CarrierCost MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(CarrierCostBase, self). __init__(**kwargs)

        self.nonlinear_solver = NonlinearBlockGS() 
        self.nonlinear_solver.options['atol'] = 1.0e-10
        self.nonlinear_solver.options['rtol'] = 1.0e-10
        self.nonlinear_solver.options['err_on_non_converge'] = True
        self.nonlinear_solver.options['reraise_child_analysiserror'] = False

        self.linear_solver = ScipyKrylov()       
        self.linear_solver.options['atol'] = 1.0e-10
        self.linear_solver.options['rtol'] = 1.0e-10
        self.linear_solver.options['err_on_non_converge'] = True
        self.linear_solver.options['iprint'] = 1

    def setup(self): 

        self.add_subsystem('Runway', self.create_runway(), promotes=['C_runway', 'ExtRunway', 'LpA', 'OnekmRunway', 'YearsRunway'])
        self.add_subsystem('RunwayMaintenance', self.create_runway_maintenance(), promotes=['CostRunwayMaint', 'C_RunwayMaint', 'LpA'])
        self.add_subsystem('AircraftFlight', self.create_aircraft_flight(), promotes=['CostAircraft', 'C_aircraft', 'HoursAircraft'])
        self.add_subsystem('Total', self.create_total(), promotes=['C_aircraft', 'C_carrier', 'C_runway', 'C_RunwayMaint'])

    def create_runway(self):
    	return Runway()
    def create_runway_maintenance(self):
    	return RunwayMaintenance()
    def create_aircraft_flight(self):
    	return AircraftFlight()
    def create_total(self):
    	return Total()


# Used by Thrift server to serve disciplines
class CarrierCostFactoryBase(object):
    @staticmethod
    def create_carrier_cost_runway():
    	return Runway()
    @staticmethod
    def create_carrier_cost_runway_maintenance():
    	return RunwayMaintenance()
    @staticmethod
    def create_carrier_cost_aircraft_flight():
    	return AircraftFlight()
    @staticmethod
    def create_carrier_cost_total():
    	return Total()
