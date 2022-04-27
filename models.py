import json

class PriorityQueue:
    def __init__(self):
        self.collection = []

    def is_empty(self):
        return len(self.collection) == 0

    def dequeue(self):
        return self.collection.pop(0)

    def enqueue(self, element):
        if self.is_empty(self.collection):
            self.collection.append(element)
            return

        for i in range(1, len(self.collection) + 1):
            if element[1] < self.collection[i - 1][1]:
                self.collection.insert(i - 1, element)
                return

        self.collection.append(element)
        return


class MetroGraph:
    def __init__(self):
        self.nodes = []
        self.adjacency_list = []

    def insert_node(self, node):
        self.nodes.append(node)
        self.adjacency_list[node] = []

    def insert_edge(self, source, destination, weight, color):
        self.adjacency_list[source].append(
            {'node': destination, 'weight': weight, 'line': color})
        self.adjacency_list[destination].append(
            {'node': source, 'weight': weight, 'line': color})
    
    def insert_single_edge(self, source, destination, weight, color):
        self.adjacency_list[source].append(
            {'node': destination, 'weight': weight, 'line': color})

    def print_graph(self, station):
        print('Printing Graph')
        for i in range(len(self.adjacency_list[station])):
            print(self.adjacency_list[station][i].line)
        

    # def get_shortest_path(self, source, destination):
    #     times = {}
    #     change = []
    #     backtrace = {}
    #     foundS, foundD = 0,0
    #     pq = PriorityQueue()
    #     times[source] = 0

    #     for node in self.nodes:
    #         if node == source:
    #             foundS = 1
    #         if node == destination:
    #             fonudD = 1

    #         if node != source:
    #             times[node] = float('inf')