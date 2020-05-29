# -*- coding: utf-8 -*-
"""
  po.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from development_cost.po_base import PoBase

class Po(PoBase):
    """ An OpenMDAO component to encapsulate Po discipline """
		
    def compute(self, inputs, outputs):
        """ Po computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            ENG = inputs['ENG']      
            MPA = inputs['MPA']

            PO = ENG * MPA

            outputs['PO'] = PO
        return outputs

# Reminder: inputs of compute()
#   
#       inputs['ENG'] -> shape: (32,), type: Float    
#       inputs['MPA'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Po, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Po """
#   
#       	partials['PO', 'ENG'] = np.zeros((32, 32))
#       	partials['PO', 'MPA'] = np.zeros((32, 1))        
