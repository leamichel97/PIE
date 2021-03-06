# -*- coding: utf-8 -*-
"""
  indirect_operations_costs.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from indirect_operations_costs_base import IndirectOperationsCostsBase

class IndirectOperationsCosts(IndirectOperationsCostsBase):
    """ An OpenMDAO component to encapsulate IndirectOperationsCosts discipline """
		
    def compute(self, inputs, outputs):
        """ IndirectOperationsCosts computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            LpA = inputs['LpA']
            S = inputs['S']
            W = inputs['W']
        
            C_IO = (40 * S + 24) * LpA**-0.379 * W /1000
        
            outputs['C_IO'] = C_IO
        
        return outputs 

# Reminder: inputs of compute()
#   
#       inputs['LpA'] -> shape: 1, type: Float    
#       inputs['S'] -> shape: 1, type: Float    
#       inputs['W'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(IndirectOperationsCosts, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for IndirectOperationsCosts """
#   
#       	partials['C_IO', 'LpA'] = np.zeros((1, 1))
#       	partials['C_IO', 'S'] = np.zeros((1, 1))
#       	partials['C_IO', 'W'] = np.zeros((1, 1))        
