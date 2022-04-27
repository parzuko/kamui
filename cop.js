while (!pq.isEmpty()) {
  let shortestStep = pq.dequeue();
  let currentNode = shortestStep[0];
  this.adjacencyList[currentNode].forEach((neighbor) => {
    let time = times[currentNode] + neighbor.weight;
    if (currentNode != startNode) {
      if (
        this.getline(currentNode, neighbor.node) !=
        this.getline(currentNode, backtrace[currentNode])
      ) {
        //Yamuna Bank Handler
        if (
          currentNode == "Yamuna Bank" &&
          neighbor.node == "Indraprastha" &&
          backtrace[currentNode] == "Laxmi Nagar"
        ) {
          time = time + 0;
        } else if (
          currentNode == "Yamuna Bank" &&
          neighbor.node == "Laxmi Nagar" &&
          backtrace[currentNode] == "Indraprastha"
        ) {
          time = time + 0;
        }
        //Dhaula Kuan - Durgabai Deshmukh South Campus Handler
        else if (
          this.getline(currentNode, neighbor.node) == "1.2km Skywalk" ||
          this.getline(currentNode, backtrace[currentNode]) == "1.2km Skywalk"
        )
          time = time + 0;
        //Noida Sector 51 - Noida Sector 52 Handler
        else if (
          this.getline(currentNode, neighbor.node) ==
            "300m Walkway/Free e-Rickshaw" ||
          this.getline(currentNode, backtrace[currentNode]) ==
            "300m Walkway/Free e-Rickshaw"
        )
          time = time + 0;
        //Ashok Park Main handler
        else if (
          currentNode == "Ashok Park Main" &&
          neighbor.node == "Punjabi Bagh" &&
          backtrace[currentNode] == "Satguru Ram Singh Marg"
        ) {
          time = time + 0;
        } else if (
          currentNode == "Ashok Park Main" &&
          neighbor.node == "Satguru Ram Singh Marg" &&
          backtrace[currentNode] == "Punjabi Bagh"
        ) {
          time = time + 0;
        }
        //Interchange Time Penalty
        else time = time + 9;
      }
    }

    if (time < times[neighbor.node]) {
      times[neighbor.node] = time;
      backtrace[neighbor.node] = currentNode;
      pq.enqueue([neighbor.node, time]);
    }
  });
}
