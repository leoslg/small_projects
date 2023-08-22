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


def inorder(root):
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
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


if __name__ == "__main__":

    root = None

    root = insert(root, 100)

    insert(root, 50)
    insert(root, 20)
    insert(root, 30)
    insert(root, 10)
    insert(root, 40)
    insert(root, 60)
    insert(root, 80)
    insert(root, 70)
    insert(root, 90)

    print("Indorder traversal BTS:", end=" ")
    inorder(root)
