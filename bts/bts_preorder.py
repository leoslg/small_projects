#!/usr/bin/env python

"""Module BTS tree."""


class Node:
    """
    Construct a BTS tree node.

    Args:
        key (int): The key value of the node.
        left (Optional['Node'], optional): The left child node. Defaults to None.
        right (Optional['Node'], optional): The right child node. Defaults to None.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    """
    Insert a new node with the given key into a binary search tree.

    Parameters:
        node (Optional['Node']): The root node of the binary search tree
        key (int): The key value to be inserted

    Returns:
        'Node': The root node of the modified binary search tree with the new node inserted
    """
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node


def preorder(root):
    """
    Perform an in-order traversal of a binary tree.

    Parameters:
    - root: The root node of the binary tree.python

    Returns:
    None
    Let us create following BST
          50
       /     \
      30      70
     /  \    /  \
    20  40  60   80
    """

    if root is not None:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


if __name__ == "__main__":

    root = None

    keys = [50, 30, 20, 40, 10, 70, 90, 60, 80]

    for key in keys:
        root = insert(root, key)

    print("Preorder traversal BTS:", end=" ")
    preorder(root)
