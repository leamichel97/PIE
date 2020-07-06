# -*- coding: utf-8 -*-
"""
  f0.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from development_cost.f0_base import F0Base

class F0(F0Base):
    """ An OpenMDAO component to encapsulate F0 discipline """
		
    def compute(self, inputs, outputs):
        """ F0 computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Ns = inputs['Ns']  

            f0 = 1.05 ** Ns

            outputs['f0'] = f0
        return outputs   

# Reminder: inputs of compute()
#   
#       inputs['Ns'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(F0, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for F0 """
#   
#       	partials['f0', 'Ns'] = np.zeros((1, 1))        
