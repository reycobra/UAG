#!/usr/bin/env python3

from collections import defaultdict, deque
from tensorflow.python.ops.gen_dataset_ops import iterator
from lego import lego_tank
import socket

HOST = "127.0.0.1"                                                              # Computer IP address
PORT = 65432                                                                    # Port to listen on (non-privileged ports are > 1023)
movements = []                                                                  # List with all the require movemens to reach the desire node

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return  list(full_path) #visited[destination]

def selecPoint(elemento):
    if(elemento=='A'):
        return [0,0]
    if(elemento=='B'):
        return [1,0]
    if(elemento=='C'):
        return [2,0]
    if(elemento=='D'):
        return [3,0]
    if(elemento=='E'):
        return [0,1]
    if(elemento=='F'):
        return [1,1]
    if(elemento=='G'):
        return [2,1]
    if(elemento=='H'):
        return [3,1]
    if(elemento=='I'):
        return [0,2]
    if(elemento=='J'):
        return [1,2]
    if(elemento=='K'):
        return [2,2]
    if(elemento=='L'):
        return [3,2]
    if(elemento=='M'):
        return [0,3]
    if(elemento=='N'):
        return [1,3]
    if(elemento=='O'):
        return [2,3]
    if(elemento=='P'):
        return [3,3]

def desplazamiento(punto1, punto2): #Agregar codigo de lego aqui
    if(punto1[0]==punto2[0] and punto1[1]<punto2[1]):
        movements.append(b"forward")
    if(punto1[0]==punto2[0] and punto1[1]>punto2[1]):
        movements.append(b"backward")
    if(punto1[0]<punto2[0] and punto1[1]==punto2[1]):
        movements.append(b"right")
    if(punto1[0]>punto2[0] and punto1[1]==punto2[1]):
        movements.append(b"left")

if __name__ == '__main__':

    graph = Graph()

    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']:
        graph.add_node(node)

    # laberinto
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'E', 1)
    graph.add_edge('B', 'A', 1)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('C', 'B', 1)
    graph.add_edge('D', 'H', 1)
    graph.add_edge('E', 'A', 1)
    graph.add_edge('E', 'F', 1)
    graph.add_edge('F', 'E', 1)
    graph.add_edge('F', 'J', 1)
    graph.add_edge('F', 'G', 1)
    graph.add_edge('G', 'F', 1)
    graph.add_edge('G', 'K', 1)
    graph.add_edge('G', 'H', 1)
    graph.add_edge('H', 'G', 1)
    graph.add_edge('H', 'L', 1)
    graph.add_edge('I', 'M', 1)
    graph.add_edge('I', 'J', 1)
    graph.add_edge('J', 'I', 1)
    graph.add_edge('J', 'F', 1)
    graph.add_edge('J', 'K', 1)
    graph.add_edge('K', 'J', 1)
    graph.add_edge('K', 'G', 1)
    graph.add_edge('K', 'O', 1)
    graph.add_edge('L', 'H', 1)
    graph.add_edge('L', 'P', 1)
    graph.add_edge('M', 'I', 1)
    graph.add_edge('N', 'O', 1)
    graph.add_edge('O', 'N', 1)
    graph.add_edge('O', 'K', 1)
    graph.add_edge('O', 'P', 1)
    graph.add_edge('P', 'O', 1)
    graph.add_edge('P', 'L', 1)
    # ...



    solucion=shortest_path(graph, 'A', 'P');
    auxList=solucion.copy()
    auxList.pop(0)
    print(solucion) # output: (25, ['A', 'B', 'D'])


    for index, item in enumerate(solucion):
        for index2, item2 in enumerate(auxList):
            point1=selecPoint(item)
            point2=selecPoint(item2)
            print(point1, point2)
            auxList.pop(index2)
            desplazamiento(point1, point2)
            break

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for movement in movements:
            print(movement)
            s.sendall(movement)
            data = s.recv(1024)
            print(data)
