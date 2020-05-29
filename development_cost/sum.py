# -*- coding: utf-8 -*-
"""
  sum.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from development_cost.sum_base import SumBase

class Sum(SumBase):
    """ An OpenMDAO component to encapsulate Sum discipline """
		
    def compute(self, inputs, outputs):
        """ Sum computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Cdev = inputs['Cdev']   

            CdevSum = sum(Cdev)

            outputs['CdevSum'] = CdevSum
        return outputs   

# Reminder: inputs of compute()
#   
#       inputs['Cdev'] -> shape: (32,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Sum, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Sum """
#   
#       	partials['CdevSum', 'Cdev'] = np.zeros((1, 32))        
