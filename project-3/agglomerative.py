import util
import math


class Node:
    def __init__(self, data, left=None, right=None, distance=0.0):
        self.left = left
        self.right = right
        self.data = data
        self.distance = distance


def min_distance(clust1, clust2, distances):
    d = 12123123123123
    for i in clust1.node_vector:
        for j in clust2.node_vector:
            try:
                distance = distances[(i, j)]
            except:
                try:
                    distance = distances[(j, i)]
                except:
                    distance = euclidean_distance(clust1.vec, clust2.vec)
            if distance < d:
                d = distance
    return d


def agglomerative(data) -> Node:
    tree = Node(None)
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
        v1 = current_data[temp['i']]
        v2 = current_data[temp['j']]
        # update list
        current_data = current_data[:i] + current_data[i + 1:j] + current_data[j + 1:]
        if type(v1) == tuple:
            v1 = Node(v1)
        if type(v2) == tuple:
            v2 = Node(v2)
        parent = Node(util.avg_points_node(1, v2), v1, v2)
        current_data.append(parent)
    return current_data[0]


def agglomerative_clustering(data, distance):
    # cluster the rows of the data matrix
    distances = {}
    currentclustid = -1

    # cluster nodes are initially just the individual rows
    nodes = [cluster_node(np.array(data[i]), id=i) for i in range(len(data))]

    while len(nodes) > k:
        lowestpair = (0, 1)
        closest = euclidean_distance(nodes[0].vec, nodes[1].vec)

        # loop through every pair looking for the smallest distance
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                # distances is the cache of distance calculations
                if (nodes[i].id, nodes[j].id) not in distances:
                    if distance == "min":
                        distances[(nodes[i].id, nodes[j].id)] = min_distance(nodes[i], nodes[j], distances)
                    else:
                        distances[(nodes[i].id, nodes[j].id)] = euclidean_distance(nodes[i].vec, nodes[j].vec)

                d = distances[(nodes[i].id, nodes[j].id)]

                if d < closest:
                    closest = d
                    lowestpair = (i, j)

        # calculate the average of the two nodes
        len0 = len(nodes[lowestpair[0]].node_vector)
        len1 = len(nodes[lowestpair[1]].node_vector)
        mean_vector = [(len0 * nodes[lowestpair[0]].vec[i] + len1 * nodes[lowestpair[1]].vec[i]) / (len0 + len1) \
                       for i in range(len(nodes[0].vec))]

        # create the new cluster node
        new_node = cluster_node(np.array(mean_vector), currentclustid, left=nodes[lowestpair[0]],
                                right=nodes[lowestpair[1]], \
                                distance=closest,
                                node_vector=nodes[lowestpair[0]].node_vector + nodes[lowestpair[1]].node_vector)

        # cluster ids that weren't in the original set are negative
        currentclustid -= 1
        del nodes[lowestpair[1]]
        del nodes[lowestpair[0]]
        nodes.append(new_node)

    return nodes
