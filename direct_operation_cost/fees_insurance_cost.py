# -*- coding: utf-8 -*-
"""
  fees_insurance_cost.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from direct_operation_cost.fees_insurance_cost_base import FeesInsuranceCostBase

class FeesInsuranceCost(FeesInsuranceCostBase):
    """ An OpenMDAO component to encapsulate FeesInsuranceCost discipline """
		
    def compute(self, inputs, outputs):
        """ FeesInsuranceCost computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            C_PL = inputs['C_PL']
            F = inputs['F']
            I = inputs['I']
            P = inputs['P']

            C_FeesInsurance = I + F + C_PL*P / 1000
                    
            outputs['C_FeesInsurance'] = C_FeesInsurance
        return outputs

# Reminder: inputs of compute()
#   
#       inputs['C_PL'] -> shape: 1, type: Float    
#       inputs['F'] -> shape: 1, type: Float    
#       inputs['I'] -> shape: 1, type: Float    
#       inputs['P'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(FeesInsuranceCost, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for FeesInsuranceCost """
#   
#       	partials['C_FeesInsurance', 'C_PL'] = np.zeros((1, 1))
#       	partials['C_FeesInsurance', 'F'] = np.zeros((1, 1))
#       	partials['C_FeesInsurance', 'I'] = np.zeros((1, 1))
#       	partials['C_FeesInsurance', 'P'] = np.zeros((1, 1))        
