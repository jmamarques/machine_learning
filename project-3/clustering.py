import random
import util


class Cluster:
    cluster: list
    without_cluster: list
    distance: float

    def __init__(self, distance) -> None:
        self.distance = distance
        self.cluster = []
        self.without_cluster = []

    def fit(self, data):
        cluster = []
        current_data = list(data)
        random.shuffle(current_data)
        while len(current_data) != 0:
            centroid = current_data.pop()
            if len(current_data) == 0:
                # new cluster with 1 element
                cluster.append([centroid])
                break
            data_validated = []
            data_not_validated = [centroid]

            while len(data_not_validated) != 0:
                new_data = []
                centroid = data_not_validated.pop()
                distances = [util.distance(centroid, elem) for elem in current_data]
                for i in range(len(distances)):
                    if distances[i] <= self.distance:
                        data_not_validated.append(current_data[i])
                    else:
                        new_data.append(current_data[i])
                data_validated.append(centroid)
                current_data = list(new_data)
            cluster.append(data_validated)
        new_cluster = []
        for elems in cluster:
            if len(elems) == 1:
                self.without_cluster.append(elems.pop())
            else:
                new_cluster.append(elems)
        self.cluster = new_cluster
