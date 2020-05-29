# -*- coding: utf-8 -*-
"""
  total_cost.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from total_cost_base import TotalCostBase

class TotalCost(TotalCostBase):
    """ An OpenMDAO component to encapsulate TotalCost discipline """
		
    def compute(self, inputs, outputs):
        """ TotalCost computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
                    
            outputs['C_TOTAL'] = 1.0   

# Reminder: inputs of compute()
#   
#       inputs['CprodTotal'] -> shape: 1, type: Float    
#       inputs['C_carrier'] -> shape: 1, type: Float    
#       inputs['C_DO'] -> shape: 1, type: Float    
#       inputs['C_IO'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(TotalCost, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for TotalCost """
#   
#       	partials['C_TOTAL', 'CprodTotal'] = np.zeros((1, 1))
#       	partials['C_TOTAL', 'C_carrier'] = np.zeros((1, 1))
#       	partials['C_TOTAL', 'C_DO'] = np.zeros((1, 1))
#       	partials['C_TOTAL', 'C_IO'] = np.zeros((1, 1))        
