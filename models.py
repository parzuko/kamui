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

        self.BLUE_TIME = 2.02
        self.BLUE_BRANCH_TIME = 1.875
        self.MAGENTA_TIME = 2.36
        self.YELLOW_TIME = 2.22
        self.RED_TIME = 2.03
        self.GREEN_TIME = 2.49
        self.GREEN_BRANCH_TIME = 1.33
        self.VIOLET_TIME = 2.24
        self.PINK_TIME = 2.69
        self.PINK_BRANCH_TIME = 2.43
        self.ORANGE_TIME = 5.2
        self.AQUA_TIME = 2.86
        self.GREY_TIME = 2.10
        self.RAPID_TIME = 5.2

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
        if source not in self.adjacency_list or destination not in self.adjacency_list:
            return -1

        for i in range(len(self.adjacency_list[source])):
            if self.adjacency_list[source][i]['node'] == destination:
                return self.adjacency_list[source][i]['line']

        for i in range(len(self.adjacency_list[destination])):
            if self.adjacency_list[destination][i]['node'] == source:
                return self.adjacency_list[destination][i]['line']
    
    def get_station_line(self, current_station):
        return self.adjacency_list[current_station][0]['line']

    def populate_graph(self):
        # Add Blue Line
        with open("routes/blue.json") as file:
            blue_line = json.load(file)
        for station in blue_line:
            self.insert_node(station)
        for i in range(len(blue_line) - 1):
            self.insert_edge(
                blue_line[i], blue_line[i + 1], self.BLUE_TIME, "blue")

        # Add Blue Branch
        with open("routes/bluebranch.json") as file:
            blue_branch = json.load(file)
        for station in blue_branch:
            if station == "yamuna bank":
                continue
            self.insert_node(station)
        for i in range(len(blue_branch) - 1):
            self.insert_edge(
                blue_branch[i], blue_branch[i + 1], self.BLUE_BRANCH_TIME, "blue_branch")

        # Add Magenta Line
        with open("routes/magenta.json") as file:
            magenta_line = json.load(file)
        for station in magenta_line:
            if station == "janakpuri west" or station == "botanical garden":
                continue
            self.insert_node(station)
        for i in range(len(magenta_line) - 1):
            self.insert_edge(
                magenta_line[i], magenta_line[i + 1], self.MAGENTA_TIME, "magenta")

        # Add Yellow Line
        with open("routes/yellow.json") as file:
            yellow_line = json.load(file)
        for station in yellow_line:
            if station == "rajiv chowk" or station == "hauz khas":
                continue
            self.insert_node(station)
        for i in range(len(yellow_line) - 1):
            self.insert_edge(
                yellow_line[i], yellow_line[i + 1], self.YELLOW_TIME, "yellow")

        # Add Violet Line
        with open("routes/violet.json") as file:
            violet_line = json.load(file)
        for station in violet_line:
            if station == "kashmere gate" or station == "mandi house" or station == "central secretariat" or station == "kalkaji mandir":
                continue
            self.insert_node(station)
        for i in range(len(violet_line) - 1):
            self.insert_edge(
                violet_line[i], violet_line[i + 1], self.VIOLET_TIME, "violet")

        # Add Red Line
        with open("routes/red.json") as file:
            red_line = json.load(file)
        for station in red_line:
            if station == "kashmere gate":
                continue
            self.insert_node(station)
        for i in range(len(red_line) - 1):
            self.insert_edge(
                red_line[i], red_line[i + 1], self.RED_TIME, "red")

        # Add Green Line
        with open("routes/green.json") as file:
            green_line = json.load(file)
        for station in green_line:
            if station == "inderlok":
                continue
            self.insert_node(station)
        for i in range(len(green_line) - 1):
            self.insert_edge(green_line[i], green_line[i + 1], self.GREEN_TIME, "green")

        # Add Green Branch
        with open("routes/greenbranch.json") as file:
            green_branch = json.load(file)
        for station in green_branch:
            if station == "kirti nagar" or station == "ashok park main":
                continue
            self.insert_node(station)
        for i in range(len(green_branch) - 1):
            self.insert_edge(green_branch[i], green_branch[i + 1], self.GREEN_BRANCH_TIME, "green_branch")

        # Add Pink Line
        with open("routes/pink.json") as file:
            pink_line = json.load(file)
        for station in pink_line:
            if station == "azadpur" or station == "netaji subhash place" or station == "rajouri garden" or station == "ina" or station == "lajpat nagar" or station == "mayur vihar - i":
                continue
            self.insert_node(station)
        for i in range(len(pink_line) - 1):
            self.insert_edge(pink_line[i], pink_line[i + 1], self.PINK_TIME, "pink")

        # Add Pink Branch
        with open("routes/pinkbranch.json") as file:
            pink_branch = json.load(file)
        for station in pink_branch:
            if station == "welcome" or station == "karkarduma" or station == "anand vihar":
                continue
            self.insert_node(station)
        for i in range(len(pink_branch) - 1):
            self.insert_edge(pink_branch[i], pink_branch[i + 1], self.PINK_BRANCH_TIME, "pink_branch")

        # Add Orange Line
        with open("routes/orange.json") as file:
            orange_line = json.load(file)
        for station in orange_line:
            if station == "new delhi" or station == "dwarka sector 21":
                continue
            self.insert_node(station)
        for i in range(len(orange_line) - 1):
            self.insert_edge(orange_line[i], orange_line[i + 1], self.ORANGE_TIME, "orange")

        # Add Aqua Line
        with open("routes/aqua.json") as file:
            aqua_line = json.load(file)
        for station in aqua_line:
            self.insert_node(station)
        for i in range(len(aqua_line) - 1):
            self.insert_edge(aqua_line[i], aqua_line[i + 1], self.AQUA_TIME, "aqua")

        # Add Grey Line
        with open("routes/grey.json") as file:
            grey_line = json.load(file)
        for station in grey_line:
            if station == "dwarka":
                continue
            self.insert_node(station)
        for i in range(len(grey_line) - 1):
            self.insert_edge(grey_line[i], grey_line[i + 1], self.GREY_TIME, "grey")

        # Add Rapid Line
        with open("routes/rapid.json") as file:
            rapid_line = json.load(file)
        for station in rapid_line:
            if station == "sikandarpur":
                continue
            self.insert_node(station)
        for i in range(len(rapid_line) - 1):
            self.insert_edge(rapid_line[i], rapid_line[i + 1], self.RAPID_TIME, "rapid")

        # Add Rapid Loop
        with open("routes/rapidloop.json") as file:
            rapid_loop = json.load(file)
        for station in rapid_loop:
            self.insert_node(station)
        for i in range(len(rapid_loop) - 1):
            self.insert_edge(rapid_loop[i], rapid_loop[i + 1], self.RAPID_TIME, "rapidloop")

        #Dhaula Kuan - South Campus Connection
        self.insert_edge("dhaula kuan", "durgabai deshmukh south campus", 18, "1.2km Skywalk");

        # Noida Sec 52 - Noida Sec 51
        self.insert_edge("noida sector 52", "noida sector 51", 12, "300m Walkway/Free e-Rickshaw");

        # Aqua Line Looper
        self.insert_single_edge("phase 3", "phase 2", 5.2, "rapid");
        self.insert_single_edge("phase 2", "vodafone belvedere towers", 5.2, "rapid");
        return

    def get_shortest_path(self, source, destination):
        if source not in self.nodes and destination not in self.nodes:
            print("Both Invalid")
            return
        elif source not in self.nodes:
            print("Source invalid")
            return
        elif destination not in self.nodes:
            print("Desitination invalid")
            return
        
        pq = PriorityQueue()
        time_weight_hashmap = {}
        bracktrack_stored_nodes = {}
        
        pq.enqueue([source, 0])
        time_weight_hashmap[source] = 0

        while not pq.is_empty():
            shortest_step = pq.dequeue()
            current_node = shortest_step[0]

            for neighbour in self.adjacency_list[current_node]:
                total_time = time_weight_hashmap[current_node] + neighbour['weight']
                if current_node != source:

                    current_to_neighbour = self.get_line(
                        current_node, neighbour['node'])
                    current_to_back = self.get_line(
                        current_node, bracktrack_stored_nodes[current_node])

                    if current_to_neighbour != current_to_back:

                        if current_node == "Yamuna Bank" and neighbour['node'] == "Indraprastha" and bracktrack_stored_nodes[current_node] == "Laxmi Nagar":
                            pass
                        elif current_node == "Yamuna Bank" and neighbour['node'] == "Laxmi Nagar" and bracktrack_stored_nodes[current_node] == "Indraprastha":
                            pass
                        elif current_node == "Ashok Park Main" and neighbour['node'] == "Punjabi Bagh" and bracktrack_stored_nodes[current_node] == "Satguru Ram Singh Marg":
                            pass
                        elif current_node == "Ashok Park Main" and neighbour['node'] == "Satguru Ram Singh Marg" and bracktrack_stored_nodes[current_node] == "Punjabi Bagh":
                            pass
                        elif current_to_neighbour == "1.2km Skywalk" or current_to_back == "1.2km Skywalk":
                            pass
                        elif current_to_neighbour == "300m Walkway/Free e-Rickshaw" or current_to_back == "300m Walkway/Free e-Rickshaw":
                            pass
                        else:
                            total_time += 9

                if total_time < time_weight_hashmap[neighbour['node']]:
                    time_weight_hashmap[neighbour['node']] = total_time
                    bracktrack_stored_nodes[neighbour['node']] = current_node
                    pq.enqueue([neighbour['node'], total_time])

        path = [destination]
        last_step = destination

        while last_step != source:
            current_station = bracktrack_stored_nodes[last_step]

            last_step = current_station
            current_line = self.get_station_line(current_station)
            # Add to the start of the list
            path[0:0] = [current_station]

        return [path, time_weight_hashmap[destination]]


# https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
