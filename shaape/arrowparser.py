from node import Node
from rightarrow import RightArrow
from leftarrow import LeftArrow
from uparrow import UpArrow
from downarrow import DownArrow
from parser import Parser
from drawable import *
from graphalgorithms import angle
import networkx

class ArrowParser(Parser):
    def __init__(self):
        super(ArrowParser, self).__init__()
        self._arrows = {}
        self._arrows['>'] = RightArrow
        self._arrows['<'] = LeftArrow
        self._arrows['^'] = UpArrow
        self._arrows['v'] = DownArrow
        return

    def run(self, raw_data, drawable_objects):
        arrows = []
        for y in range(0, len(raw_data)):
            for x in range(0, len(raw_data[0])): 
                if raw_data[y][x] in self._arrows.keys():
                    arrow = self._arrows[raw_data[y][x]]((x + 0.5, y + 0.5))
                    arrows.append(arrow)

        graph = None
        try:
            graph = next(obj for obj in drawable_objects if type(obj) == nx.Graph)
        except StopIteration:
            pass
        if graph != None:
            for arrow in arrows:
                connector = Node(*(arrow.tip()))
                nodes_in_front = [node for node in graph.nodes() if angle(arrow.direction(), node - connector) < 90]
                if nodes_in_front:
                    nearest_node = min(nodes_in_front, key=lambda node: (node - connector.position()).length())
                    diff = nearest_node - connector
                    if diff.length() <= 0.5:
                        arrow.translate(diff)

        self._drawable_objects = drawable_objects + arrows
        drawable_objects += arrows
        self._parsed_data = raw_data
        return
