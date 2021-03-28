class Cube:

    def __init__(self):
        node = []
        for node in range(2**4):
            self.nodes[node] = str(bin(node)).zfill(4)
            print(self.nodes[node])

   # def print_coord
