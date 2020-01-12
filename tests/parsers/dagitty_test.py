from downstream.parsers.dagitty import DagittyParser


def test_dagitty_parser():
    input_str = """
    dag {
        x -> y
        x <- z -> y
    }
    """
    expected_edges = [
        [('x', 'y')],
        [('z', 'x'), ('z', 'y')]
    ]
    parser = DagittyParser()
    edges = parser(input_str)
    assert(edges == expected_edges) 