from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np

bayesNet = BayesianNetwork()

# nodes
nodes = ['L', 'I', 'S', 'N', 'R']
for node in nodes:
    bayesNet.add_node(node)

# edges
bayesNet.add_edge('L', 'N')
bayesNet.add_edge('I', 'N')
bayesNet.add_edge('S', 'N')
bayesNet.add_edge('S', 'R')
bayesNet.add_edge('N', 'R')

# cpd
cpd_L = TabularCPD('L', 2, [[0.08], [0.92]], state_names={'L': ['T', 'F']})
cpd_I = TabularCPD('I', 2, [[0.21], [0.79]], state_names={'I': ['T', 'F']})
cpd_S = TabularCPD('S', 2, [[0.12], [0.88]], state_names={'S': ['T', 'F']})

cpd_N = TabularCPD('N', 2, 
    [[0.92, 0.88, 0.79, 0.73, 0.22, 0.08, 0.17, 0.03],
     [0.08, 0.12, 0.21, 0.27, 0.78, 0.92, 0.83, 0.97]],
    evidence=['L', 'S', 'I'],
    evidence_card=[2, 2, 2],
    state_names={'N': ['T', 'F'], 'L': ['T', 'F'], 'S': ['T', 'F'], 'I': ['T', 'F']})

cpd_R = TabularCPD('R', 2,
    [[0.38, 0.08, 0.08, 0.05],
     [0.62, 0.92, 0.92, 0.95]],
    evidence=['N', 'S'],
    evidence_card=[2, 2],
    state_names={'R': ['T', 'F'], 'N': ['T', 'F'], 'S': ['T', 'F']})

# cpd to bayes
bayesNet.add_cpds(cpd_L, cpd_I, cpd_S, cpd_N, cpd_R)


# question 1.3
print("Model check:", bayesNet.check_model())

# question 1.4
solver = VariableElimination(bayesNet)

# question 2.1 
result = solver.query(variables=['N'])
print(f"P(N=T) = {result.values[0]:.4f}")

# question 2.2
result = solver.query(variables=['N'], evidence={'L': 'T'})
print(f"P(N=T|L=T) = {result.values[0]:.4f}")

# question 3
independencies = bayesNet.get_independencies()
print("Independence Relations:", independencies)

