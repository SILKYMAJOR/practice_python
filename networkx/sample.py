import matplotlib.pyplot as plt
import networkx as nx


def draw_cycle_graph():
    g = nx.cycle_graph(24)
    pos = nx.spring_layout(G, iterations=200)
    nx.draw(g, pos, node_color=range(24), node_size=800, cmap=plt.cm.Blues)
    plt.show()


def main():
    draw_cycle_graph()


if __name__ == '__main__':
    main()
