# -*- coding: utf-8 -*-
"""
  ground_operation.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from direct_operation_cost.ground_operation_base import GroundOperationBase

class GroundOperation(GroundOperationBase):
    """ An OpenMDAO component to encapsulate GroundOperation discipline """
		
    def compute(self, inputs, outputs):
        """ GroundOperation computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            f11 = inputs['f11'] 
            f8 = inputs['f8'] 
            fc = inputs['fc'] 
            fv = inputs['fv']  
            L = inputs['L'] 
            LpA = inputs['LpA']
            M0 = inputs['M0']
            N = inputs['N']
            W = inputs['W']

            C_GO = W * 8 * (M0 ** 0.67) * (LpA ** -0.9) * (N ** 0.7) * fc * fv * L * f8 * f11 / 1000

            outputs['C_GO'] = C_GO
        return outputs

# Reminder: inputs of compute()
#   
#       inputs['f11'] -> shape: 1, type: Float    
#       inputs['f8'] -> shape: 1, type: Float    
#       inputs['fc'] -> shape: 1, type: Float    
#       inputs['fv'] -> shape: 1, type: Float    
#       inputs['L'] -> shape: 1, type: Float    
#       inputs['LpA'] -> shape: 1, type: Float    
#       inputs['M0'] -> shape: 1, type: Float    
#       inputs['N'] -> shape: 1, type: Float    
#       inputs['W'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(GroundOperation, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for GroundOperation """
#   
#       	partials['C_GO', 'f11'] = np.zeros((1, 1))
#       	partials['C_GO', 'f8'] = np.zeros((1, 1))
#       	partials['C_GO', 'fc'] = np.zeros((1, 1))
#       	partials['C_GO', 'fv'] = np.zeros((1, 1))
#       	partials['C_GO', 'L'] = np.zeros((1, 1))
#       	partials['C_GO', 'LpA'] = np.zeros((1, 1))
#       	partials['C_GO', 'M0'] = np.zeros((1, 1))
#       	partials['C_GO', 'N'] = np.zeros((1, 1))
#       	partials['C_GO', 'W'] = np.zeros((1, 1))        
