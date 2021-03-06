# -*- coding: utf-8 -*-
"""
  runway.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from carrier_cost.runway_base import RunwayBase

class Runway(RunwayBase):
    """ An OpenMDAO component to encapsulate Runway discipline """
		
    def compute(self, inputs, outputs):
        """ Runway computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            ExtRunway = inputs['ExtRunway']
            LpA = inputs['LpA']
            OnekmRunway = inputs['OnekmRunway']
            YearsRunway = inputs['YearsRunway']

            C_runway = ((OnekmRunway * ExtRunway) / YearsRunway) / LpA
                    
            outputs['C_runway'] = C_runway
        return outputs   
# Reminder: inputs of compute()
#   
#       inputs['ExtRunway'] -> shape: 1, type: Float    
#       inputs['LpA'] -> shape: 1, type: Float    
#       inputs['OnekmRunway'] -> shape: 1, type: Float    
#       inputs['YearsRunway'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Runway, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Runway """
#   
#       	partials['C_runway', 'ExtRunway'] = np.zeros((1, 1))
#       	partials['C_runway', 'LpA'] = np.zeros((1, 1))
#       	partials['C_runway', 'OnekmRunway'] = np.zeros((1, 1))
#       	partials['C_runway', 'YearsRunway'] = np.zeros((1, 1))        
