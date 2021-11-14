import util


class Node:
    def __init__(self, data, left=None, right=None, original=False, distance=0.0):
        self.left = left
        self.right = right
        self.data = data
        self.original = original
        self.distance = distance

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.original:
            print(self.data),
        else:
            print(""),
        if self.right:
            self.right.print_tree()


def agglomerative(data) -> Node:
    current_data = list(data)
    if len(current_data) == 1:
        return Node(current_data[0], original=True)
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
        dist = temp['distance']
        v1 = current_data[i]
        v2 = current_data[j]
        # update list
        current_data = current_data[:i] + current_data[i + 1:j] + current_data[j + 1:]
        if type(v1) == tuple:
            v1 = Node(v1, original=True)
        if type(v2) == tuple:
            v2 = Node(v2, original=True)
        parent = Node(util.avg_points_node(v1, v2), v1, v2, distance=dist)
        current_data.append(parent)
    return current_data[0]
