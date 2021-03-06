# -*- coding: utf-8 -*-
"""
  direct_operations_cost_base.py generated by WhatsOpt 1.9.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 800


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from direct_operations_cost.ground_operation import GroundOperation
from direct_operations_cost.propellant_cost import PropellantCost
from direct_operations_cost.flight_mission_operations import FlightMissionOperations
from direct_operations_cost.transportation_cost import TransportationCost
from direct_operations_cost.fees_insurance_cost import FeesInsuranceCost
from direct_operations_cost.total import Total








class DirectOperationsCostBase(Group):
    """ An OpenMDAO base component to encapsulate DirectOperationsCost MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(DirectOperationsCostBase, self). __init__(**kwargs)

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

        self.add_subsystem('GroundOperation', self.create_ground_operation(), promotes=['C_GO', 'f11', 'f8', 'fc', 'fv', 'L', 'LpA', 'M0', 'Ns', 'W'])
        self.add_subsystem('PropellantCost', self.create_propellant_cost(), promotes=['Cf', 'Cox', 'Cpres', 'Cprop', 'Mp', 'Mpres', 'r'])
        self.add_subsystem('FlightMissionOperations', self.create_flight_mission_operations(), promotes=['Cmission', 'f8', 'L', 'LpA', 'Q_N', 'W'])
        self.add_subsystem('TransportationCost', self.create_transportation_cost(), promotes=['Ctransp', 'M0', 'Ts'])
        self.add_subsystem('FeesInsuranceCost', self.create_fees_insurance_cost(), promotes=['C_FeesInsurance', 'C_PL', 'F', 'I', 'PayCap'])
        self.add_subsystem('Total', self.create_total(), promotes=['Cmission', 'Cprop', 'Ctransp', 'C_DO', 'C_FeesInsurance', 'C_GO'])

    def create_ground_operation(self):
    	return GroundOperation()
    def create_propellant_cost(self):
    	return PropellantCost()
    def create_flight_mission_operations(self):
    	return FlightMissionOperations()
    def create_transportation_cost(self):
    	return TransportationCost()
    def create_fees_insurance_cost(self):
    	return FeesInsuranceCost()
    def create_total(self):
    	return Total()


# Used by Thrift server to serve disciplines
class DirectOperationsCostFactoryBase(object):
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
