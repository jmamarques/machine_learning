import util


class Node:
    def __init__(self, data, left=None, right=None, distance=0.0):
        self.left = left
        self.right = right
        self.data = data
        self.distance = distance


def agglomerative(data) -> Node:
    current_data = list(data)
    if len(current_data) == 1:
        return Node(current_data[0])
    while len(current_data) > 1:
        # calculate distances
        distances = []
        for i in range(len(current_data)):
            for j in range(i + 1, len(current_data)):
                distances.append({"i": i, "j": j, "distance": util.distance_node(current_data[i], current_data[j])})
        # lower value
        lower = float('inf')
        temp = None
        for elem in distances:
            if lower > elem['distance']:
                temp = elem
                lower = elem['distance']
        i = temp['i']
        j = temp['j']
        v1 = current_data[i]
        v2 = current_data[j]
        # update list
        current_data = current_data[:i] + current_data[i + 1:j] + current_data[j + 1:]
        if type(v1) == tuple:
            v1 = Node(v1)
        if type(v2) == tuple:
            v2 = Node(v2)
        parent = Node(util.avg_points_node(v1, v2), v1, v2)
        current_data.append(parent)
    return current_data[0]
