from collections import defaultdict
import json
from time import time

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
        self.adjacency_list = defaultdict(list)

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

    def get_line(self, source, destination):
        for i in range(len(self.adjacency_list[source])):
            if self.adjacency_list[source][i]['node'] == destination:
                return self.adjacency_list[source][i]['line']

        for i in range(len(self.adjacency_list[destination])):
            if self.adjacency_list[destination][i]['node'] == source:
                return self.adjacency_list[source][i]['line']
        

    def print_graph(self, station):
        print('Printing Graph')
        for i in range(len(self.adjacency_list[station])):
            print(self.adjacency_list[station][i]['line'])
        
    def get_shortest_path(self, source, destination):
        times = {}
        change = []
        backtrace = {}
        foundS, foundD = 0,0
        pq = PriorityQueue()
        times[source] = 0

        for node in self.nodes:
            if node == source:
                foundS = 1
            if node == destination:
                fonudD = 1

            if node != source:
                times[node] = float('inf')

        if foundS == 0 and foundD == 0:
            print("Both Invalid")
            return
        elif foundS == 0:
            print("Source invalid")
            return
        elif foundD == 0:
            print("Desitination invalid")
            return
        

        pq.enqueue([source, 0])

        while not pq.is_empty():
            shortest_step = pq.dequeue()
            current_node = shortest_step[0]

            for neighbour in self.adjacency_list[current_node]:
                total_time = times[current_node] + neighbour['weight']
                if current_node != source:
                    
                    current_to_neighbour = self.get_line(current_node, neighbour['node']) 
                    current_to_back = self.get_line(current_node, backtrace[current_node])
                    
                    if current_to_neighbour != current_to_back:

                        if current_node == "Yamuna Bank" and neighbour['node'] == "Indraprastha" and backtrace[current_node] == "Laxmi Nagar":
                            pass
                        elif current_node == "Yamuna Bank" and neighbour['node'] == "Laxmi Nagar" and backtrace[current_node] == "Indraprastha":
                            pass
                        elif current_node == "Ashok Park Main" and neighbour['node'] == "Punjabi Bagh" and backtrace[current_node] == "Satguru Ram Singh Marg":
                            pass
                        elif current_node == "Ashok Park Main" and neighbour['node'] == "Satguru Ram Singh Marg" and backtrace[current_node] == "Punjabi Bagh":
                            pass
                        elif current_to_neighbour == "1.2km Skywalk" or current_to_back == "1.2km Skywalk":
                            pass
                        elif current_to_neighbour == "300m Walkway/Free e-Rickshaw" or current_to_back == "300m Walkway/Free e-Rickshaw":
                            pass
                        else:
                            total_time += 9
                
                if total_time < total_time[neighbour['node']]:
                    times[neighbour['node']] = total_time
                    backtrace[neighbour['node']] = current_node
                    pq.enqueue([neighbour['node'], total_time])


g = MetroGraph()
g.insert_edge("dhaula kuan", "durgabai deshmukh south campus", 18, "1.2km Skywalk")

g.insert_edge("noida sector 52", "noida sector 51", 12, "300m Walkway/Free e-Rickshaw")


g.insert_single_edge("phase 3", "phase 2", 5.2, "rapid")
g.insert_single_edge("phase 2", "vodafone belvedere towers", 5.2, "rapid")

g.print_graph("phase 3")