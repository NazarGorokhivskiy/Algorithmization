input1 = "NNN NNN NNN"
input2 = "NYY YNY YYN"
input3 = "NYNNN YNYNN NYNYN NNYNY NNNYN"


class Graph:
    def __init__(self, size):
        self.vertexes = {}
        for i in range(size):
            self.vertexes[i] = []

    def add_vertex(self, v1, v2):
        self.vertexes[v1].append(v2)

    def count_friends(self, head):
        count = -1  # should be -1 because head element does not count as "friend"
        visited = []

        for neighbor in self.vertexes[head]:
            if neighbor not in visited:
                count += 1
                visited.append(neighbor)
            for sub_neighbor in self.vertexes[neighbor]:
                if sub_neighbor not in visited:
                    count += 1
                    visited.append(sub_neighbor)

        return count

    def print(self):
        print(self.vertexes)


def parse_string(str):
    rows = str.split(" ")
    matrix = []
    for i in range(rows.__len__()):
        matrix.append(list(rows[i]))
    return matrix


def find_max_friends(matrix):
    graph = Graph(matrix.__len__())

    # filling the graph according to matrix content
    for i in range(matrix.__len__()):
        for j in range(i + 1, matrix.__len__()):
            if matrix[i][j] is 'Y':
                graph.add_vertex(i, j)
                graph.add_vertex(j, i)

    # finding maximum friends count in graph
    max_friend_count = 0
    for i in range(matrix.__len__()):
        friends = graph.count_friends(i)
        if max_friend_count < friends:
            max_friend_count = friends

    return max_friend_count


# main function
students = parse_string(input3)
print(find_max_friends(students))
