# -*- coding: utf-8 -*-
"""
  transportation_cost.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from direct_operations_cost.transportation_cost_base import TransportationCostBase

class TransportationCost(TransportationCostBase):
    """ An OpenMDAO component to encapsulate TransportationCost discipline """
		
    def compute(self, inputs, outputs):
        """ TransportationCost computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
                    
            outputs['Ctransp'] = 1.0   

# Reminder: inputs of compute()
#   
#       inputs['M0'] -> shape: 1, type: Float    
#       inputs['Ts'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(TransportationCost, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for TransportationCost """
#   
#       	partials['Ctransp', 'M0'] = np.zeros((1, 1))
#       	partials['Ctransp', 'Ts'] = np.zeros((1, 1))        
