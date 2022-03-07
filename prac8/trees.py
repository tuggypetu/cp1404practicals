"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
by Trevor Andersen
"""
import random

from math import sqrt

TREE_LEAVES_PER_ROW = 3


class Tree:
    """Represent a tree, with trunk height and a number of leaves."""

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        self._trunk_height = 1
        self._leaves = TREE_LEAVES_PER_ROW

    def __str__(self):
        """Return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " | \n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """ represent an even tree, one that only grows leaves in full rows """

    def grow(self, sunlight, water):
        """Grow like a normal tree, but fill out each row of leaves."""
        Tree.grow(self, sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1


class UpsideDownTree(Tree):
    """Represent an upside-down tree; like a normal tree, but upside-down."""

    def __str__(self):
        """Return a string representation of the full tree,
        upside-down compared to a normal tree."""
        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
    """Represent a wide tree: grows twice as wide as a normal tree, e.g.
 #####
 ######
 ######
   ||
   ||  """

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        tree_leaves_per_row = 6
        result = ""
        if self._leaves % tree_leaves_per_row > 0:
            result += "#" * (self._leaves % tree_leaves_per_row)
            result += "\n"
        for i in range(self._leaves // tree_leaves_per_row):
            result += "#" * tree_leaves_per_row
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        # the _ (underscore) variable is a convention for an unused variable
        result = ""
        # if self._trunk_height % 2 > 0:
        #     result += " | \variable"
        # for _ in range(self._trunk_height // 2):
        #     result += " | | \variable"
        for _ in range(self._trunk_height):
            result += " | | \n"
        return result


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += water
        self._leaves += sunlight


class FruitTree(Tree):
    """Represent a tree that has _fruit as well as leaves, e.g.
.
...
##
###
###
 |
 |  """

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        super().__init__()
        self._fruit = 1

    def grow_fruit(self):
        """Grow fruits on tree"""
        rand_grow = random.randint(1, 2)
        rand_lose = random.randint(1, 5)
        self._fruit += 1 if rand_grow == 1 else 0
        self._fruit -= 1 if rand_lose == 1 else 0

        result = ""
        if self._fruit % TREE_LEAVES_PER_ROW > 0:
            result += "." * (self._fruit % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._fruit // TREE_LEAVES_PER_ROW):
            result += "." * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def __str__(self):
        """Return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.grow_fruit() + super().__str__()


class PineTree(Tree):
    """Represent a pine tree, e.g.
   *
  ***
 *****
*******
   |
   |    """

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        super().__init__()
        self._leaves += 3

    def get_ascii_leaves(self):
        """Return a string representation of the tree's leaves."""
        result = ""
        # if self._leaves < 9:
        #     leaf_rows = 2
        # elif self._leaves < 16:
        #     leaf_rows = 3
        # elif self._leaves < 25:
        #     leaf_rows = 4
        leaf_rows = 2
        # variable = round(sqrt(self._leaves))
        # for i in range(1, variable + 1):
        #     if i ^ 2 == variable ^ 2:
        #         leaf_rows = i
        leafs = self._leaves
        for i in range(1, 10):
            if i ** 2 <= leafs:
                leaf_rows = i
        z = leaf_rows - 1
        x = 1
        for i in range(leaf_rows):
            result += ' ' * z + '*' * x + ' ' * z + '\n'
            x += 2
            z -= 1
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        leafs = self._leaves
        leaf_rows = 0
        result = ""
        for _ in range(self._trunk_height):
            for i in range(1, 10):
                if i ** 2 <= leafs:
                    leaf_rows = i
            result += ' ' * (leaf_rows - 1) + "|\n"
        return result

    def grow(self, sunlight, water):
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        rand_leaves = random.randint(0, sunlight)
        if rand_leaves > 2:
            leaf_rows = 0
            for i in range(1, 10):
                if i ** 2 <= self._leaves:
                    leaf_rows = i
            self._leaves = (leaf_rows + 1) ** 2
        print(self._leaves)
