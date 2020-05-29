# -*- coding: utf-8 -*-
"""
  development_cost.py generated by WhatsOpt 1.8.2
"""
from optparse import OptionParser
from openmdao.api import Problem
from openmdao.api import NonlinearBlockGS, ScipyKrylov
# from openmdao_extensions.reckless_nonlinear_block_gs import RecklessNonlinearBlockGS
from development_cost.development_cost_base import DevelopmentCostBase, DevelopmentCostFactoryBase

class DevelopmentCost(DevelopmentCostBase):
    """ An OpenMDAO component to encapsulate DevelopmentCost analysis """
    def __init__(self, **kwargs):
        super(DevelopmentCost, self).__init__(**kwargs)

        # Example of manual solver adjusments (imports should be adjusted accordingly)
        # self.nonlinear_solver = NewtonSolver() 
        # self.nonlinear_solver.options['maxiter'] = 20
        # self.linear_solver = DirectSolver()

    def setup(self):
        super(DevelopmentCost, self).setup()


class DevelopmentCostFactory(DevelopmentCostFactoryBase):
    """ A factory to create disciplines of DevelopmentCost analysis """
    pass

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--no-n2", action="store_false", dest='n2_view', default=True, 
                      help="display N2 openmdao viewer")
    (options, args) = parser.parse_args()

    problem = Problem()
    problem.model = DevelopmentCost()

    problem.setup()
    problem.final_setup()
    
    if options.n2_view:
        from packaging import version
        if version.parse(OPENMDAO_VERSION) < version.parse("2.10.0"):
            from openmdao.api import view_model as n2
        else:
            from openmdao.visualization.n2_viewer.n2_viewer import n2
            n2(problem)
