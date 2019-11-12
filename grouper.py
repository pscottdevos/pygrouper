from itertools import zip_longest


def group(string, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks. adapted from the
    Python itertool docs at: https://docs.python.org/2/library/itertools.html
    """
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(string)] * n
    return ["".join(t) for t in zip_longest(fillvalue=fillvalue, *args)]
