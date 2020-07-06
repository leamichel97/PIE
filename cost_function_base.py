# -*- coding: utf-8 -*-
"""
  cost_function_base.py generated by WhatsOpt 1.9.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: https://ether.onera.fr/whatsopt
# analysis_id: 258


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from manufacturing_cost.manufacturing_cost import ManufacturingCost
from carrier_cost.carrier_cost import CarrierCost
from development_cost.development_cost import DevelopmentCost
from direct_operations_cost.direct_operations_cost import DirectOperationsCost
from indirect_operations_costs import IndirectOperationsCosts
from total_cost import TotalCost
from manufacturing_cost.lm import Lm
from manufacturing_cost.cprod import Cprod
from manufacturing_cost.total import Total
from carrier_cost.runway import Runway
from carrier_cost.runway_maintenance import RunwayMaintenance
from carrier_cost.aircraft_flight import AircraftFlight
from carrier_cost.total import Total
from development_cost.tfu import Tfu
from development_cost.fm1 import Fm1
from development_cost.mait import Mait
from development_cost.eng import Eng
from development_cost.mpa import Mpa
from development_cost.po import Po
from development_cost.f0 import F0
from development_cost.total import Total
from development_cost.sum import Sum
from direct_operations_cost.ground_operation import GroundOperation
from direct_operations_cost.propellant_cost import PropellantCost
from direct_operations_cost.flight_mission_operations import FlightMissionOperations
from direct_operations_cost.transportation_cost import TransportationCost
from direct_operations_cost.fees_insurance_cost import FeesInsuranceCost
from direct_operations_cost.total import Total




class CostFunctionBase(Group):
    """ An OpenMDAO base component to encapsulate CostFunction MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(CostFunctionBase, self). __init__(**kwargs)

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
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])

        indeps.add_output('a', np.ones((32,)))
        indeps.add_output('b', np.ones((32,)))
        indeps.add_output('Cf', 1.0)
        indeps.add_output('CostAircraft', 1.0)
        indeps.add_output('CostRunwayMaint', 1.0)
        indeps.add_output('Cox', 1.0)
        indeps.add_output('Cp', 1.0)
        indeps.add_output('Cpres', 1.0)
        indeps.add_output('C_PL', 1.0)
        indeps.add_output('DD', 1.0)
        indeps.add_output('ExtRunway', 1.0)
        indeps.add_output('F', 1.0)
        indeps.add_output('f1', 1.0)
        indeps.add_output('f10', 1.0)
        indeps.add_output('f11', 1.0)
        indeps.add_output('f3', 1.0)
        indeps.add_output('f8', 1.0)
        indeps.add_output('fc', 1.0)
        indeps.add_output('fv', 1.0)
        indeps.add_output('HoursAircraft', 1.0)
        indeps.add_output('HW', np.ones((32,)))
        indeps.add_output('I', 1.0)
        indeps.add_output('L', 1.0)
        indeps.add_output('Ld', np.ones((32,)))
        indeps.add_output('LpA', 1.0)
        indeps.add_output('M0', 1.0)
        indeps.add_output('Mass', [25,0,242.6,257,55,2450,0,326,0,0,15,0,312,53.8,10.9,490,0,120,0,0,30,90,45,0,33,0,0,0,0,0,15,20])
        indeps.add_output('Mp', 1.0)
        indeps.add_output('Mpres', 1.0)
        indeps.add_output('M_PA_percentage', 1.0)
        indeps.add_output('n', 1.0)
        indeps.add_output('Ns', 1.0)
        indeps.add_output('OnekmRunway', 1.0)
        indeps.add_output('p', 1.0)
        indeps.add_output('PayCap', 1.0)
        indeps.add_output('Q_N', 1.0)
        indeps.add_output('r', 1.0)
        indeps.add_output('S', 1.0)
        indeps.add_output('STH', 1.0)
        indeps.add_output('Ts', 1.0)
        indeps.add_output('W', 1.0)
        indeps.add_output('YearsRunway', 1.0)
        self.add_subsystem('DevelopmentCost', self.create_development_cost(), promotes=['a', 'b', 'CdevSum', 'Cp', 'DD', 'f1', 'f10', 'f11', 'f3', 'FM1', 'HW', 'Ld', 'Mass', 'M_PA_percentage', 'Ns', 'STH'])
        self.add_subsystem('ManufacturingCost', self.create_manufacturing_cost(), promotes=['Cp', 'CprodTotal', 'f10', 'f11', 'FM1', 'M_PA_percentage', 'n', 'p'])
        self.add_subsystem('DirectOperationsCost', self.create_direct_operations_cost(), promotes=['Cf', 'Cox', 'Cpres', 'C_DO', 'C_PL', 'F', 'f11', 'f8', 'fc', 'fv', 'I', 'L', 'LpA', 'M0', 'Mp', 'Mpres', 'Ns', 'PayCap', 'Q_N', 'r', 'Ts', 'W'])
        self.add_subsystem('IndirectOperationsCosts', self.create_indirect_operations_costs(), promotes=['C_IO', 'LpA', 'S', 'W'])
        self.add_subsystem('CarrierCost', self.create_carrier_cost(), promotes=['CostAircraft', 'CostRunwayMaint', 'C_carrier', 'ExtRunway', 'HoursAircraft', 'LpA', 'OnekmRunway', 'YearsRunway'])
        self.add_subsystem('TotalCost', self.create_total_cost(), promotes=['CdevSum', 'CprodTotal', 'C_carrier', 'C_DO', 'C_IO', 'C_TOTAL'])

    def create_manufacturing_cost(self):
    	return ManufacturingCost()


    def create_carrier_cost(self):
    	return CarrierCost()


    def create_development_cost(self):
    	return DevelopmentCost()


    def create_direct_operations_cost(self):
    	return DirectOperationsCost()


    def create_indirect_operations_costs(self):
    	return IndirectOperationsCosts()
    def create_total_cost(self):
    	return TotalCost()


# Used by Thrift server to serve disciplines
class CostFunctionFactoryBase(object):
    @staticmethod
    def create_indirect_operations_costs():
    	return IndirectOperationsCosts()
    @staticmethod
    def create_total_cost():
    	return TotalCost()
    @staticmethod
    def create_manufacturing_cost_lm():
    	return Lm()
    @staticmethod
    def create_manufacturing_cost_cprod():
    	return Cprod()
    @staticmethod
    def create_manufacturing_cost_total():
    	return Total()
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
    @staticmethod
    def create_development_cost_tfu():
    	return Tfu()
    @staticmethod
    def create_development_cost_fm1():
    	return Fm1()
    @staticmethod
    def create_development_cost_mait():
    	return Mait()
    @staticmethod
    def create_development_cost_eng():
    	return Eng()
    @staticmethod
    def create_development_cost_mpa():
    	return Mpa()
    @staticmethod
    def create_development_cost_po():
    	return Po()
    @staticmethod
    def create_development_cost_f0():
    	return F0()
    @staticmethod
    def create_development_cost_total():
    	return Total()
    @staticmethod
    def create_development_cost_sum():
    	return Sum()
    @staticmethod
    def create_direct_operations_cost_ground_operation():
    	return GroundOperation()
    @staticmethod
    def create_direct_operations_cost_propellant_cost():
    	return PropellantCost()
    @staticmethod
    def create_direct_operations_cost_flight_mission_operations():
    	return FlightMissionOperations()
    @staticmethod
    def create_direct_operations_cost_transportation_cost():
    	return TransportationCost()
    @staticmethod
    def create_direct_operations_cost_fees_insurance_cost():
    	return FeesInsuranceCost()
    @staticmethod
    def create_direct_operations_cost_total():
    	return Total()
