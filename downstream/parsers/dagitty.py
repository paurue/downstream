from lark import Lark, Transformer


DAGITTY_SYNTAX = r"""
    dag: "dag" "{"  block+ "}"
    node: WORD
    block: node ( ( LEFT_ARROW | RIGHT_ARROW | DOUBLE_ARROW ) node )+
    LEFT_ARROW: "->"
    RIGHT_ARROW: "<-"
    DOUBLE_ARROW: "<->"
    %import common.WORD 
    %import common.WS 
    %ignore WS
    """

DAGITTY_PARSER = Lark(DAGITTY_SYNTAX, start="dag")


class DagittyTransformer(Transformer):
    def dag(self, s):
        return s

    def block(self, items):
        edges = []
        for i in range(0, len(items) - 2, 2):
            node_1, arrow, node_2 = items[i : i + 3]
            arrow = str(arrow)
            if arrow == "->":
                edges.append((node_1, node_2))
            elif arrow == "<-":
                edges.append((node_2, node_1))
            elif arrow == "<->":
                edges.append((node_1, node_2))
                edges.append((node_2, node_1))
        return edges

    def node(self, s):
        (s,) = s
        return str(s)


class DagittyParser:
    def __call__(self, input_str: str):
        parsed_tree = DAGITTY_PARSER.parse(input_str)
        edge_sets = DagittyTransformer().transform(parsed_tree)
        edges = [edge for edge_set in edge_sets for edge in edge_set]
        return edges
