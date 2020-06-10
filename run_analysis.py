# -*- coding: utf-8 -*-
"""
  run_analysis.py generated by WhatsOpt 1.9.0
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 258

from openmdao.api import Problem
from run_parameters_init import initialize
from cost_function import CostFunction 

pb = Problem(CostFunction())
pb.setup()  

initialize(pb)

pb.run_model()   
pb.model.list_inputs(print_arrays=False)
pb.model.list_outputs(print_arrays=False)

