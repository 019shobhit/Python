import pgmpy.models
import pgmpy.factors.discrete
import pgmpy.inference
import networkx as nx
import matplotlib.pyplot as plt

# Define the Bayesian Network structure
model = pgmpy.models.BayesianNetwork([('Burglary', 'Alarm'), 
                                      ('Earthquake', 'Alarm'),
                                      ('Alarm', 'JohnCalls'), 
                                      ('Alarm', 'MaryCalls')])

# Define CPDs
cpd_burglary = pgmpy.factors.discrete.TabularCPD("Burglary", 2, [[0.001], [0.999]])
cpd_earthquake = pgmpy.factors.discrete.TabularCPD("Earthquake", 2, [[0.002], [0.998]])
cpd_alarm = pgmpy.factors.discrete.TabularCPD('Alarm', 2, [[0.95, 0.94, 0.29, 0.001], 
                                                           [0.05, 0.06, 0.71, 0.999]], 
                                              evidence=['Burglary', 'Earthquake'], 
                                              evidence_card=[2, 2])
cpd_john = pgmpy.factors.discrete.TabularCPD('JohnCalls', 2, [[0.90, 0.05], 
                                                              [0.10, 0.95]], 
                                              evidence=['Alarm'], 
                                              evidence_card=[2])
cpd_mary = pgmpy.factors.discrete.TabularCPD('MaryCalls', 2, [[0.70, 0.01], 
                                                              [0.30, 0.99]], 
                                              evidence=['Alarm'], 
                                              evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)

# Validate the model
if model.check_model():
    print("Model is valid!")
else:
    print("Model is invalid. Check the CPDs or structure.")

# Convert Bayesian Network to a NetworkX graph for visualization
nx_graph = nx.DiGraph(model.edges())

# Generate positions for nodes
pos = nx.spring_layout(nx_graph)

# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(nx_graph, pos, with_labels=True, 
        node_color="lightblue", 
        node_size=3000, 
        font_size=10, 
        font_weight='bold', 
        edge_color="gray")

# Add title and show plot
plt.title("Bayesian Network")
plt.show()

# Perform inference
infer = pgmpy.inference.VariableElimination(model)

# Query 1: Probability of Burglary if John and Mary call
result_1 = infer.query(['Burglary'], evidence={'JohnCalls': 0, 'MaryCalls': 0})
print("P(Burglary | JohnCalls=True, MaryCalls=True):")
print(result_1)

# Query 2: Probability of Alarm if there is a Burglary and Earthquake
result_2 = infer.query(['Alarm'], evidence={'Burglary': 0, 'Earthquake': 0})
print("P(Alarm | Burglary=True, Earthquake=True):")
print(result_2) 