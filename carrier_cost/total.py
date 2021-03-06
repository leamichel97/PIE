# -*- coding: utf-8 -*-
"""
  total.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from carrier_cost.total_base import TotalBase

class Total(TotalBase):
    """ An OpenMDAO component to encapsulate Total discipline """
		
    def compute(self, inputs, outputs):
        """ Total computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            C_aircraft = inputs['C_aircraft']
            C_runway = inputs['C_runway']
            C_RunwayMaint = inputs['C_RunwayMaint']

            C_carrier = C_aircraft + C_runway + C_RunwayMaint
                    
            outputs['C_carrier'] = C_carrier
        return outputs 

# Reminder: inputs of compute()
#   
#       inputs['C_aircraft'] -> shape: 1, type: Float    
#       inputs['C_runway'] -> shape: 1, type: Float    
#       inputs['C_RunwayMaint'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Total, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Total """
#   
#       	partials['C_carrier', 'C_aircraft'] = np.zeros((1, 1))
#       	partials['C_carrier', 'C_runway'] = np.zeros((1, 1))
#       	partials['C_carrier', 'C_RunwayMaint'] = np.zeros((1, 1))        
