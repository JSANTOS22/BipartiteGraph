from matplotlib.offsetbox import OffsetImage

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from galeShapley import animateAlgo

# NOTE: CHANGE INTERVAL (LINE 8) TO CHANGE THE SPEED OF ANIMATION - THE HIGHER THE INTERVAL THE SLOWER - THE LOWER THE FASTER
Interval = 1000

# this is the animation function that does the actual animation
# it gets each iteration output of the algorithm to then display it as each frame for the animation
def animate(graph, count, preference, men_positions, men, women_positions, women):

    n = len(preference[0])

    # initialize lists
    freeM = [-1] * n
    prefW = [-1] * n

    # this keeps track of all the existing edges
    old_edges = []

    # this function updates the algorithm for each frame
    def update(frame, freeM, prefW, old_edges):

        plt.gcf()
        plt.clf() # clears the previous drawing

        if frame == 0:
            old_edges.clear()  # clear old_edges for the initial frame
        else:
    
            # this gets the prefW after one iteration of the algorithm
            freeM, prefW, newMatch, s = animateAlgo(freeM, prefW, preference)

            # Create a new graph object
            new_graph = nx.Graph()

            # Add nodes to the new graph
            new_graph.add_nodes_from(men, bipartite=0)
            new_graph.add_nodes_from(women, bipartite=1)
            new_graph.add_nodes_from(men_positions.keys(), bipartite=0)
            new_graph.add_nodes_from(women_positions.keys(), bipartite=1)

            # loop that adds all the previous edges and new edge from the algorithm
            for i in range(len(prefW)):
                if prefW[i] == -1:
                    # skip the iteration if prefW[i] == -1 since that means there's no matching for it yet
                    continue
                
                # create the key of each M and W that are matched to make a pair
                Mkey = "M" + str(prefW[i])
                Wkey = "W" + str(i)
                
                if i == newMatch:
                    # add a blue edge since it's the newest edge being updated
                    new_graph.add_edge(Mkey, Wkey, color='blue')
                else:
                    # add a black edge since it's an already existing edge
                    new_graph.add_edge(Mkey, Wkey, color='black')

            # add colors to the nodes based off of their edge colors, if no edge exists it'll be gray
            node_colors = ['gray' if new_graph.degree(node) == 0 else new_graph[node][list(new_graph.adj[node])[0]]['color'] for node in new_graph.nodes()]

            # Draw nodes and edges
            pos = {**men_positions, **women_positions}

            # set the text at the top of the graph to say whoever is being engaged
            if s != '':
                plt.text(0.5, 1.05, s, horizontalalignment='center', fontsize=12, transform=plt.gca().transAxes)
            else:
                plt.text(0.5, 1.05, 'Gale Shapley Algorithm is finished!', horizontalalignment='center', fontsize=12, transform=plt.gca().transAxes)
                
            nx.draw(new_graph, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=6, edge_color=[new_graph[u][v]['color'] for u,v in new_graph.edges()],font_weight='bold',font_color='white')

            time.sleep(1.5)

    ani = FuncAnimation(plt.gcf(), update, frames=count+2, fargs=(freeM, prefW, old_edges),interval=Interval, repeat=False)
    plt.show()

# this initializes the base graph to which I will be animating
def initialize_Animation(count, preference_list):

    n = len(preference_list[0])

    # create graph
    G = nx.Graph()

    # create men and women list
    men = []
    women = []
    for i in range(n):
        men.append("M"+str(i))
        women.append("W"+str(i))

    men_image = 'https://icon2.cleanpng.com/20180420/weq/kisspng-suit-clip-art-5ada5223efc3a0.6956283315242573159821.jpg'
    men_with_images = [(node, {'image': men_image}) for node in men]

    # now add the nodes on the graph
    G.add_nodes_from(men_with_images, bipartite=0)
    G.add_nodes_from(women, bipartite=1)

    # define the positions of the nodes
    men_positions = {}
    women_positions = {}

    for i in range(n):
        men_pair = (0, (n-i)*n)
        women_pair = (1, (n-i)*n)
        men_positions[men[i]] = men_pair
        women_positions[women[i]] = women_pair

    # Add nodes to the graph with positions
    G.add_nodes_from(men_positions.keys(), bipartite=0)
    G.add_nodes_from(women_positions.keys(), bipartite=1)

    # calls the animation function
    animate(G, count, preference_list, men_positions, men_with_images, women_positions, women)