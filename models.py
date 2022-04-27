from collections import defaultdict
import json


class PriorityQueue:
    def __init__(self):
        self.collection = []

    def is_empty(self):
        return len(self.collection) == 0

    def dequeue(self):
        return self.collection.pop(0)

    def enqueue(self, element):
        if self.is_empty():
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
            print(self.adjacency_list[station][i])

    def get_shortest_path(self, source, destination):
        times = {}
        change = []
        backtrace = {}
        foundS, foundD = 0, 0
        pq = PriorityQueue()
        times[source] = 0

        for node in self.nodes:
            if node == source:
                foundS = 1
            if node == destination:
                foundD = 1

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

                    current_to_neighbour = self.get_line(
                        current_node, neighbour['node'])
                    current_to_back = self.get_line(
                        current_node, backtrace[current_node])

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

                if total_time < times[neighbour['node']]:
                    times[neighbour['node']] = total_time
                    backtrace[neighbour['node']] = current_node
                    pq.enqueue([neighbour['node'], total_time])

        path = [destination]
        last_step = destination

        while last_step != source:
            # last_to_back = self.get_line(last_step, backtrace[last_step])
            # back_last_to_last = self.get_line(
            #     backtrace[last_step], backtrace[backtrace[last_step]])

            # if last_to_back != back_last_to_last:
            #     # if backtrace[last_step] == source:
            #     #     pass
            #     # elif backtrace[last_step] == "Yamuna Bank" and last_step == "Indraprastha" and backtrace[backtrace[last_step]] == "Laxmi Nagar":
            #     #     pass
            #     # elif backtrace[last_step] == 'Yamuna Bank' and last_step == 'Laxmi Nagar' and backtrace[backtrace[last_step]] == 'Indraprastha':
            #     #     pass
            #     # elif backtrace[last_step] == 'Ashok Park Main' and last_step == 'Punjabi Bagh' and backtrace[backtrace[last_step]] == 'Satguru Ram Singh Marg':
            #     #     pass
            #     # elif backtrace[last_step] == 'Ashok Park Main' and last_step == 'Satguru Ram Singh Marg' and backtrace[backtrace[last_step]] == 'Punjabi Bagh':
            #     #     pass
            #     # else:
            #     #     line1Send =
            #     pass
            # x[0:0] = y
            # prepend array to start of another
            path[0:0] =[backtrace[last_step]]
            last_step = backtrace[last_step]

        return [path, total_time]




# def populate_graph():
#     # Blue line
#     blueFile = open("routes/blue.json")
#     blueline = json.load(blueFile)
#     for station in blueline:
#         g.insert_node(station)
#     for i in range(len(blueline) - 1):
#         g.insert_edge(blueline[i], blueline[i + 1], 2.02, "blue")


#     # Yellow line
#     yellowFile = open("routes/yellow.json")
#     yellow_line = json.load(yellowFile)
#     for station in yellow_line:
#         if station == "hauz khas" or station == "rajiv chowk":
#             continue
#         g.insert_node(station)

#     for i in range(len(yellow_line) - 1):
#         g.insert_edge(yellow_line[i], yellow_line[i + 1], 2.22, "yellow")


g = MetroGraph()
blueFile = open("routes/blue.json")
blueline = json.load(blueFile)
for station in blueline:
    g.insert_node(station)
for i in range(len(blueline) - 1):
    g.insert_edge(blueline[i], blueline[i + 1], 2.02, "blue")


# Yellow line
yellowFile = open("routes/yellow.json")
yellow_line = json.load(yellowFile)
for station in yellow_line:
    if station == "rajiv chowk":
        continue
    g.insert_node(station)

for i in range(len(yellow_line) - 1):
    g.insert_edge(yellow_line[i], yellow_line[i + 1], 2.22, "yellow")

print(g.get_shortest_path("jahangirpuri", "noida city centre"))
# g.print_graph("rajiv chowk")