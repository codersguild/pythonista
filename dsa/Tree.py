# -*- coding: utf-8 -*-
from graphviz import Source, Graph, Digraph
import uuid


def format_stmts(node):
    return "\n".join([str(elems) for elems in node.data])


class TreeNode(dict):
    def __init__(self, nodeId=""):
        self.left = None
        self.right = None
        self.type = None
        self.parent = None
        self.added = False
        self.id = None
        self.data = []
        self.edges = []
        dict.__init__(self, nodeId=nodeId, uid=str(uuid.uuid4()))
        self.data.append(nodeId)


class TreeEdge:
    def __init__(self, parent, child, label="execution", color="black"):
        self.parent = parent
        self.child = child
        child.parent = parent
        self.label = label
        self.data = label
        self.color = color
        self.graph = Digraph(comment="Execution Edge", format="png")

    def view_edge(self):
        """
        Just show the edge i.e Parent --> Child
        """
        self.graph.edge(
            format_stmts(self.parent),
            format_stmts(self.child),
            color=self.color,
            label=self.label,
        )
        self.graph.render()


class Tree:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.counter = 0
        self.leaves = []
        self.edgeSet = []
        self.root = None

    def save_cfg(self, name="Tree", filename="sample", directory="."):
        graph = Digraph(name=name,
                        filename=filename,
                        directory=directory,
                        format="png")
        for node in self.nodes:
            for edge in node.edges:
                graph.edge(
                    format_stmts(edge.parent),
                    format_stmts(edge.child),
                    color=edge.color,
                    label=edge.label,
                )
        graph.render()

    def add_node(self, node):
        if not node.added:
            node.id = uuid.uuid4()
            self.counter += 1
            node.added = True
            node.uid = self.counter
            self.nodes.append(node)
