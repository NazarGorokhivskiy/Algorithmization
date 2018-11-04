class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []


class Graph:
    def __init__(self):
        self.vertexes = []

    def add_pair(self, vertex1, vertex2):
        iter = 0
        for v in self.vertexes:
            if vertex1.value == v.value:
                vertex1 = self.vertexes[iter]
                self.vertexes.pop(iter)
                break
            iter += 1

        iter = 0
        for v in self.vertexes:
            if vertex2.value == v.value:
                vertex2 = self.vertexes[iter]
                self.vertexes.pop(iter)
                break
            iter += 1

        vertex1.neighbours.append(vertex2)
        vertex2.neighbours.append(vertex1)
        self.vertexes.append(vertex1)
        self.vertexes.append(vertex2)

    def dfs_find_elem(self, head, searched_v):
        stack = [head]
        is_visited = {v.value: False for v in self.vertexes}

        while stack:
            vertex = stack.pop()

            if searched_v.value == vertex.value:
                return True

            if is_visited[vertex.value]:
                continue
            is_visited[vertex.value] = True
            for neighbor in vertex.neighbours:
                stack.append(neighbor)

        return False


def fill_graph_from_file(graph, filename):
    with open(filename) as file:
        lines = file.readlines()

    for elem in lines[1:]:
        line = tuple(map(int, elem.split()))
        graph.add_pair(Vertex(line[0]), Vertex(line[1]))


graph = Graph()
fill_graph_from_file(graph, "in2")

wedding_count = 0

for i in range(graph.vertexes.__len__()):
    for j in range(i + 1, graph.vertexes.__len__()):
        if not graph.dfs_find_elem(graph.vertexes[i], graph.vertexes[j]):
            if (graph.vertexes[i].value % 2 == 0 and graph.vertexes[j].value % 2 != 0) or (
                    graph.vertexes[i].value % 2 != 0 and graph.vertexes[j].value % 2 == 0):
                wedding_count += 1
                print("%d / %d" % (graph.vertexes[i].value, graph.vertexes[j].value))

print("All pairs count: %d" % wedding_count)
