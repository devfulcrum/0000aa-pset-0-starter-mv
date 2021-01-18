#!/usr/bin/env python3
"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """

    """Ensure rows is type casted as int for subsequent program use
    """
    rows = int(rows)

    """Work through for loop for the range = rows
    - The variable x determines the overall places to be filled
      to the left and right of each pyramid layer
    - The variable y determines the length of the pyramid layer 
      from the top to the bottom
    - Finally print the combination for each row of the pyramid
    """
    for i in range(rows):
        if i == 0:
            x = '-' * (rows - 1)
            y = '='
        else:
            x = '-' * (rows - (i + 1))
            y = '=' * ((i * 2) + 1)
        print(x + y + x)
    "Commented the exception as the method is now implemented above"
    # raise NotImplementedError("Called with rows={}".format(rows))


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
