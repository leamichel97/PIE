# -*- coding: utf-8 -*-
"""
  total.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from direct_operations_cost.total_base import TotalBase

class Total(TotalBase):
    """ An OpenMDAO component to encapsulate Total discipline """
		
    def compute(self, inputs, outputs):
        """ Total computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Cmission = inputs['Cmission']
            Cprop = inputs['Cprop']
            Ctransp = inputs['Ctransp']
            C_FeesInsurance = inputs['C_FeesInsurance']
            C_GO = inputs['C_GO']

            C_DO = Cmission + Cprop + Ctransp + C_FeesInsurance + C_GO
                    
            outputs['C_DO'] = C_DO
        return outputs    

# Reminder: inputs of compute()
#   
#       inputs['Cmission'] -> shape: 1, type: Float    
#       inputs['Cprop'] -> shape: 1, type: Float    
#       inputs['Ctransp'] -> shape: 1, type: Float    
#       inputs['C_FeesInsurance'] -> shape: 1, type: Float    
#       inputs['C_GO'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Total, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Total """
#   
#       	partials['C_DO', 'Cmission'] = np.zeros((1, 1))
#       	partials['C_DO', 'Cprop'] = np.zeros((1, 1))
#       	partials['C_DO', 'Ctransp'] = np.zeros((1, 1))
#       	partials['C_DO', 'C_FeesInsurance'] = np.zeros((1, 1))
#       	partials['C_DO', 'C_GO'] = np.zeros((1, 1))        
