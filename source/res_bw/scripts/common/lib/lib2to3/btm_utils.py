# Python 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/Lib/lib2to3/btm_utils.py
"""Utility functions used by the btm_matcher module"""
from . import pytree
from .pgen2 import grammar, token
from .pygram import pattern_symbols, python_symbols
syms = pattern_symbols
pysyms = python_symbols
tokens = grammar.opmap
token_labels = token
TYPE_ANY = -1
TYPE_ALTERNATIVES = -2
TYPE_GROUP = -3

class MinNode(object):
    """This class serves as an intermediate representation of the
    pattern tree during the conversion to sets of leaf-to-root
    subpatterns"""

    def __init__(self, type = None, name = None):
        self.type = type
        self.name = name
        self.children = []
        self.leaf = False
        self.parent = None
        self.alternatives = []
        self.group = []
        return

    def __repr__(self):
        return str(self.type) + ' ' + str(self.name)

    def leaf_to_root(self):
        """Internal method. Returns a characteristic path of the
        pattern tree. This method must be run for all leaves until the
        linear subpatterns are merged into a single"""
        node = self
        subp = []
        while node:
            if node.type == TYPE_ALTERNATIVES:
                node.alternatives.append(subp)
                if len(node.alternatives) == len(node.children):
                    subp = [tuple(node.alternatives)]
                    node.alternatives = []
                    node = node.parent
                    continue
                else:
                    node = node.parent
                    subp = None
                    break
            if node.type == TYPE_GROUP:
                node.group.append(subp)
                if len(node.group) == len(node.children):
                    subp = get_characteristic_subpattern(node.group)
                    node.group = []
                    node = node.parent
                    continue
                else:
                    node = node.parent
                    subp = None
                    break
            if node.type == token_labels.NAME and node.name:
                subp.append(node.name)
            else:
                subp.append(node.type)
            node = node.parent

        return subp

    def get_linear_subpattern(self):
        """Drives the leaf_to_root method. The reason that
        leaf_to_root must be run multiple times is because we need to
        reject 'group' matches; for example the alternative form
        (a | b c) creates a group [b c] that needs to be matched. Since
        matching multiple linear patterns overcomes the automaton's
        capabilities, leaf_to_root merges each group into a single
        choice based on 'characteristic'ity,
        
        i.e. (a|b c) -> (a|b) if b more characteristic than c
        
        Returns: The most 'characteristic'(as defined by
          get_characteristic_subpattern) path for the compiled pattern
          tree.
        """
        for l in self.leaves():
            subp = l.leaf_to_root()
            if subp:
                return subp

    def leaves(self):
        """Generator that returns the leaves of the tree"""
        for child in self.children:
            for x in child.leaves():
                yield x

        if not self.children:
            yield self


def reduce_tree(node, parent = None):
    """
    Internal function. Reduces a compiled pattern tree to an
    intermediate representation suitable for feeding the
    automaton. This also trims off any optional pattern elements(like
    [a], a*).
    """
    new_node = None
    if node.type == syms.Matcher:
        node = node.children[0]
    if node.type == syms.Alternatives:
        if len(node.children) <= 2:
            new_node = reduce_tree(node.children[0], parent)
        else:
            new_node = MinNode(type=TYPE_ALTERNATIVES)
            for child in node.children:
                if node.children.index(child) % 2:
                    continue
                reduced = reduce_tree(child, new_node)
                if reduced is not None:
                    new_node.children.append(reduced)

    elif node.type == syms.Alternative:
        if len(node.children) > 1:
            new_node = MinNode(type=TYPE_GROUP)
            for child in node.children:
                reduced = reduce_tree(child, new_node)
                if reduced:
                    new_node.children.append(reduced)

            if not new_node.children:
                new_node = None
        else:
            new_node = reduce_tree(node.children[0], parent)
    elif node.type == syms.Unit:
        if isinstance(node.children[0], pytree.Leaf) and node.children[0].value == '(':
            return reduce_tree(node.children[1], parent)
        if isinstance(node.children[0], pytree.Leaf) and node.children[0].value == '[' or len(node.children) > 1 and hasattr(node.children[1], 'value') and node.children[1].value == '[':
            return
        leaf = True
        details_node = None
        alternatives_node = None
        has_repeater = False
        repeater_node = None
        has_variable_name = False
        for child in node.children:
            if child.type == syms.Details:
                leaf = False
                details_node = child
            elif child.type == syms.Repeater:
                has_repeater = True
                repeater_node = child
            elif child.type == syms.Alternatives:
                alternatives_node = child
            if hasattr(child, 'value') and child.value == '=':
                has_variable_name = True

        if has_variable_name:
            name_leaf = node.children[2]
            if hasattr(name_leaf, 'value') and name_leaf.value == '(':
                name_leaf = node.children[3]
        else:
            name_leaf = node.children[0]
        if name_leaf.type == token_labels.NAME:
            if name_leaf.value == 'any':
                new_node = MinNode(type=TYPE_ANY)
            elif hasattr(token_labels, name_leaf.value):
                new_node = MinNode(type=getattr(token_labels, name_leaf.value))
            else:
                new_node = MinNode(type=getattr(pysyms, name_leaf.value))
        elif name_leaf.type == token_labels.STRING:
            name = name_leaf.value.strip("'")
            if name in tokens:
                new_node = MinNode(type=tokens[name])
            else:
                new_node = MinNode(type=token_labels.NAME, name=name)
        elif name_leaf.type == syms.Alternatives:
            new_node = reduce_tree(alternatives_node, parent)
        if has_repeater:
            if repeater_node.children[0].value == '*':
                new_node = None
            elif repeater_node.children[0].value == '+':
                pass
            else:
                raise NotImplementedError
        if details_node and new_node is not None:
            for child in details_node.children[1:-1]:
                reduced = reduce_tree(child, new_node)
                if reduced is not None:
                    new_node.children.append(reduced)

    if new_node:
        new_node.parent = parent
    return new_node


def get_characteristic_subpattern(subpatterns):
    """Picks the most characteristic from a list of linear patterns
    Current order used is:
    names > common_names > common_chars
    """
    if not isinstance(subpatterns, list):
        return subpatterns
    if len(subpatterns) == 1:
        return subpatterns[0]
    subpatterns_with_names = []
    subpatterns_with_common_names = []
    common_names = ['in',
     'for',
     'if',
     'not',
     'None']
    subpatterns_with_common_chars = []
    common_chars = '[]().,:'
    for subpattern in subpatterns:
        if any(rec_test(subpattern, lambda x: type(x) is str)):
            if any(rec_test(subpattern, lambda x: isinstance(x, str) and x in common_chars)):
                subpatterns_with_common_chars.append(subpattern)
            elif any(rec_test(subpattern, lambda x: isinstance(x, str) and x in common_names)):
                subpatterns_with_common_names.append(subpattern)
            else:
                subpatterns_with_names.append(subpattern)

    if subpatterns_with_names:
        subpatterns = subpatterns_with_names
    elif subpatterns_with_common_names:
        subpatterns = subpatterns_with_common_names
    elif subpatterns_with_common_chars:
        subpatterns = subpatterns_with_common_chars
    return max(subpatterns, key=len)


def rec_test(sequence, test_func):
    """Tests test_func on all items of sequence and items of included
    sub-iterables"""
    for x in sequence:
        if isinstance(x, (list, tuple)):
            for y in rec_test(x, test_func):
                yield y

        else:
            yield test_func(x)
