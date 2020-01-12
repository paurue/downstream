from networkx import DiGraph
import pydot
from downstream.parsers.dagitty import DagittyParser


class CausalModel:
    def __init__(self, model: str = None):
        assert isinstance(model, str)
        edges = self._parse_dagitty_str(model)
        self._dag = DiGraph()
        self._dag.add_edges_from(edges)

    def __repr__(self):
        edges = self._dag.edges
        edges_format = ", ".join([f"{e[0]} → {e[1]}" for e in edges])
        return f"CausalModel({edges_format})"

    @property
    def variables(self):
        return list(self._dag.nodes)

    @property
    def edges(self):
        return self._dag.edges

    @property
    def nodes(self):
        return self._dag.nodes

    @staticmethod
    def _parse_dagitty_str(input_str):
        parser = DagittyParser()
        edges = parser(input_str)
        return edges

    def plot(self):
        g = pydot.Dot()

        g.set_node_defaults(
            tooltip=str,
            shape="box",
            style="rounded, filled",
            fillcolor="#3DAF77",
            fontcolor="white",
            penwidth="0",
            fontname="helvetica",
            fontsize="10",
        )

        for n in self._dag.nodes:
            g.add_node(pydot.Node(name=n))
        for e in self._dag.edges:
            g.add_edge(pydot.Edge(e[0], e[1]))
        return g


# TODO: move elsewhere
def _repr_svg_(self: pydot.Dot):
    return self.create_svg().decode("utf-8")


pydot.Dot._repr_svg_ = _repr_svg_
