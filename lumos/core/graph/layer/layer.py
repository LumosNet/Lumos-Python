from turtle import width


class Layer(object):

    def __init__(self, init_weights_type="random"):
        self._graph = None
        self.height = 0
        self.width = 0
        self.channel = 0
        self.init_weights_type = init_weights_type

    def _to_graph(self):
        pass

    def calculate(self):
        pass
