# -*- coding: utf-8 -*-
"""
  run_doe.py generated by WhatsOpt 1.9.0
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 258

import sys
import numpy as np
import matplotlib.pyplot as plt
from packaging import version

from openmdao import __version__ as OPENMDAO_VERSION
from openmdao.api import Problem, SqliteRecorder, CaseReader
from openmdao_extensions.smt_doe_driver import SmtDOEDriver
from cost_function import CostFunction 

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
parser.add_option("-n", "--ncases", type="int",
                  dest="n_cases", default=50,
                  help="number of samples")
parser.add_option("-p", "--parallel", 
                  action="store_true", default=False,
                  help="run doe in parallel")
(options, args) = parser.parse_args()

pb = Problem(CostFunction())
pb.driver = SmtDOEDriver(sampling_method_name='LHS', n_cases=options.n_cases, sampling_method_options={'criterion': 'ese'})
pb.driver.options['run_parallel'] = options.parallel

case_recorder_filename = 'cost_function_doe.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)
if version.parse(OPENMDAO_VERSION) > version.parse("2.8.0"):
    pb.model.nonlinear_solver.options['err_on_non_converge'] = True
else:
    pb.model.nonlinear_solver.options['err_on_maxiter'] = True


pb.model.add_design_var('LpA', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('Ns', lower=-sys.float_info.max, upper=sys.float_info.max)


pb.model.add_objective('C_TOTAL')

pb.setup()  
pb.run_driver()        


if options.batch or options.parallel:
    exit(0)
reader = CaseReader(case_recorder_filename)
cases = reader.list_cases('driver')
n = len(cases)
data = {'inputs': {}, 'outputs': {} }

data['inputs']['LpA'] = np.zeros((n,)+(1,))
data['inputs']['Ns'] = np.zeros((n,)+(1,))

data['outputs']['C_TOTAL'] = np.zeros((n,)+(1,))

for i in range(len(cases)):
    case = reader.get_case(cases[i])
    data['inputs']['LpA'][i,:] = case.outputs['LpA']
    data['inputs']['Ns'][i,:] = case.outputs['Ns']
    data['outputs']['C_TOTAL'][i,:] = case.outputs['C_TOTAL']
      

output = data['outputs']['C_TOTAL'].reshape(-1)

input = data['inputs']['LpA'].reshape(-1)
plt.subplot(1, 2, 1)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('C_TOTAL')
plt.xlabel('LpA')

input = data['inputs']['Ns'].reshape(-1)
plt.subplot(1, 2, 2)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('Ns')

plt.show()
