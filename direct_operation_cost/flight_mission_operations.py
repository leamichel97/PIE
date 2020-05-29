# -*- coding: utf-8 -*-
"""
  flight_mission_operations.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from direct_operation_cost.flight_mission_operations_base import FlightMissionOperationsBase

class FlightMissionOperations(FlightMissionOperationsBase):
    """ An OpenMDAO component to encapsulate FlightMissionOperations discipline """
		
    def compute(self, inputs, outputs):
        """ FlightMissionOperations computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
                    
            outputs['Cmission'] = 1.0   

# Reminder: inputs of compute()
#   
#       inputs['f8'] -> shape: 1, type: Float    
#       inputs['L'] -> shape: 1, type: Float    
#       inputs['LpA'] -> shape: 1, type: Float    
#       inputs['Q_N'] -> shape: 1, type: Float    
#       inputs['W'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(FlightMissionOperations, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for FlightMissionOperations """
#   
#       	partials['Cmission', 'f8'] = np.zeros((1, 1))
#       	partials['Cmission', 'L'] = np.zeros((1, 1))
#       	partials['Cmission', 'LpA'] = np.zeros((1, 1))
#       	partials['Cmission', 'Q_N'] = np.zeros((1, 1))
#       	partials['Cmission', 'W'] = np.zeros((1, 1))        
