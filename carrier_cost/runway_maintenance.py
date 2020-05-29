# -*- coding: utf-8 -*-
"""
  runway_maintenance.py generated by WhatsOpt 1.8.2
"""
import numpy as np
from carrier_cost.runway_maintenance_base import RunwayMaintenanceBase

class RunwayMaintenance(RunwayMaintenanceBase):
    """ An OpenMDAO component to encapsulate RunwayMaintenance discipline """
		
    def compute(self, inputs, outputs):
        """ RunwayMaintenance computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            CostRunwayMaint = inputs['CostRunwayMaint']
            Launches = inputs['Launches']

            C_RunwayMaint = CostRunwayMaint / Launches
                    
            outputs['C_RunwayMaint'] = C_RunwayMaint
        return outputs

# Reminder: inputs of compute()
#   
#       inputs['CostRunwayMaint'] -> shape: 1, type: Float    
#       inputs['Launches'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(RunwayMaintenance, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for RunwayMaintenance """
#   
#       	partials['C_RunwayMaint', 'CostRunwayMaint'] = np.zeros((1, 1))
#       	partials['C_RunwayMaint', 'Launches'] = np.zeros((1, 1))        
