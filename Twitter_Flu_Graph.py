"""
CptS 483
Twitter Flu graph 
------------------
Generate a directed multigraph over the twitter data in the file
flu-vac_string.edgelist.

The lines are formatted as:
        [source] [target] [tweet_count]

Two tweets are connected by an edge between the source and target
users. 
"""
__author__ = """\n""".join(['Griffin Fujioka (fujiokag@hotmail.com)'])


import networkx as nx
import shlex            # for parsing lines of text
import matplotlib.pyplot as plt
import sys

print 'Welcome to the Griffin Fujioka Twitter Data Mining Program!'
print ''

g=nx.DiGraph()        # Create an empty graph

# Open the data file for reading 
file=open('flu-vac_string.edgelist', 'r')
i = 0
counter = 0
temp = 0
while 1:
    line = file.readline()
    if not line:
        break       # We've read in all lines from the file 
    else:
        nodes_array = g.nodes()   # Get all nodes currently in the graph
        tweet = shlex.split(line)
        source = tweet[0]
        target = tweet[1]
        tweetCountAsString = tweet[2]
        #print 'tweetCountAsString = ' + tweetCountAsString
        tweetCount = int(tweet[2])  # Get integer value of tweetCount
        

        if source in nodes_array:
            if target in nodes_array:

                # Check to see if an edge already exists. If so, get its weight
                g.add_edge(source, target, weight=tweetCount)
                #print 'Edge added from ' + source + ' to ' + target
            else:
                g.add_node(target)      # We must add the target node first
                g.add_edge(source, target, weight=tweetCount)
                #print 'Added node ' + target + '. Edge added from ' + source + ' to ' + target
        else:
            g.add_node(source)
            if target in nodes_array:
                g.add_edge(source, target, weight=tweetCount)
                #print 'Edge added from ' + source + ' to ' + target
            else:
                g.add_node(target)      # We must add the target node first
                g.add_edge(source, target, weight=tweetCount)
                #print 'Added node ' + target + '. Edge added from ' + source + ' to ' + target


print 'Graph contains ' + str(g.number_of_nodes()) + ' nodes.'
print 'Graph contains ' + str(g.number_of_edges()) + ' edges.'
print 'Graph contains ' + str(nx.number_strongly_connected_components(g)) + ' strongly connected components.'


# Determine which node has the greatest out degree
out_degree_dictionary = g.out_degree(g.nodes())     #Put all of the nodes in with the key=node name and value=out degree
max_id_node_name = out_degree_dictionary.keys()[0] 
max_out_degree = out_degree_dictionary.values()[0]
for key, value in out_degree_dictionary.iteritems():
    #print key + " " +  str(value)
    if value > max_out_degree:
        max_od_node_name = key
        max_out_degree = value
   
print 'Node with highest out degree: ' + max_od_node_name + ' (' + str(max_out_degree) + ')'

# Determine which node has the highest in degree
in_degree_dictionary = g.in_degree(g.nodes())
max_id_node_name = in_degree_dictionary.keys()[0]
max_in_degree = in_degree_dictionary.values()[0]
for key, value in in_degree_dictionary.iteritems():
    #print key + " " + str(value)
    if value > max_in_degree:
        max_id_node_name = key
        max_in_degree = value

print 'Node with highest in degree: ' + max_id_node_name + ' (' + str(max_in_degree) + ')'



# Determine the longest path
#h = nx.DiGraph(g);          # Create a copy of the graph
#for u,v in h.edges_iter():
#    h[u][v]['weight'] *= -1    # Negate the weights of all of the edges 

# Run Bellman-Ford algorithm
#print nx.bellman_ford(h, "jonkeel")  #  two dictionaries keyed by node to predecessor in the path and to the distance from the source respectively
#print nx.bellman_ford(h, "official_pax")

print 'Diameter: ' + str(nx.diameter(g))

print 'Drawing graph...'
nx.draw(g)
plt.savefig("graph.png")
print 'Graph saved as graph.png'

