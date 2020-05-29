# -*- coding: utf-8 -*-
"""
  eng.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from development_cost.eng_base import EngBase

class Eng(EngBase):
    """ An OpenMDAO component to encapsulate Eng discipline """
		
    def compute(self, inputs, outputs):
        """ Eng computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            DD = inputs['DD']
            FM1 = inputs['FM1']

            ENG = DD * FM1

            outputs['ENG'] = ENG
        return outputs  

# Reminder: inputs of compute()
#   
#       inputs['DD'] -> shape: 1, type: Float    
#       inputs['FM1'] -> shape: (32,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Eng, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Eng """
#   
#       	partials['ENG', 'DD'] = np.zeros((32, 1))
#       	partials['ENG', 'FM1'] = np.zeros((32, 32))        
