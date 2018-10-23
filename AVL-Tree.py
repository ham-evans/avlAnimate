"""
CSCI0302: Algorithms
Group Implementation Project
AVL Tree

Members: Hamilton Evans, Harrison Govan, Brendan Murphy, and Rose Gold
Referenced CLRS Textbook
"""

from turtle import *
import sys
from drawTree import init, drawTree, animateTraversal, erasableWrite
from turtle import reset, write
import time


class Node():

    def __init__(self, key):
        """
        Initializes instance variables.
        """
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class Tree():


    def get_height(self, root):
        """
        Obtains height of input root.
        """
        if not root:
            return 0
        else:
            return root.height


    def get_balance(self, root):
        """
        Obtains balance factor of input root.
        """
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)


    def rotateL(self, root):
        """
        Tri-node restructuring of root. Left rotation version.
        """
        # following alg from CLRS
        newroot = root.right
        newright = newroot.left

        newroot.left = root
        root.right = newright

        # update heights
        root.height = max(self.get_height(root.left),
                          self.get_height(root.right)) + 1
        newroot.height = max(self.get_height(newroot.left),
                             self.get_height(newroot.right)) + 1
        print("Left Rotation: ")
        print('New Root: ' + str(newroot.key))
        print('New Left Child: ' + str(newroot.left.key))
        print('New Right Child: ' + str(newroot.right.key))
        return newroot


    def rotateR(self, root):
        """
        Tri-node restructuring of root. Right rotation version.
        """
        # following alg from CLRS
        newroot = root.left
        newleft = newroot.right

        newroot.right = root
        root.left = newleft

        # update heights
        root.height = max(self.get_height(root.left),
                          self.get_height(root.right)) + 1
        newroot.height = max(self.get_height(newroot.left),
                             self.get_height(newroot.right)) + 1
        print("Right Rotation: ")
        print('New Root: ' + str(newroot.key))
        print('New Left Child: ' + str(newroot.left.key))
        print('New Right Child: ' + str(newroot.right.key))
        return newroot


    def search(self, root, key):
        """
        Search function for key given input root. Returns root if key in tree
        and returns None otherwise.
        """
        if not root:
            return None
        elif root.key == key:
            return root

        if (key < root.key):
            return self.search(root.left, key)
        if (key > root.key):
            return self.search(root.right, key)

        


    def insertHelp(self, root, key):
        """
        Insert function takes input key and root, calls rotateL or rotateR
        according to balance factor of insertion.
        """
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insertHelp(root.left, key)
        else: # key > root.key
            root.right = self.insertHelp(root.right, key)

        # Adjust height.
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        bal = self.get_balance(root)
        # Go through each case
        if bal < -1:
            if key > root.right.key:
                # Single left rotation.
                return self.rotateL(root)
            elif key < root.right.key:
                # Double left rotation.
                root.right = self.rotateR(root.right)
                return self.rotateL(root)

        if bal > 1:
            if key < root.left.key:
                # Single right rotation.
                return self.rotateR(root)
            elif key > root.left.key:
                # Double right rotation.
                root.left = self.rotateL(root.left)
                return self.rotateR(root)
        return root


    def delete(self, root, key):
        """
        Delete function takes input key and root. Removes the
        """
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)

        # If no right or left children...
        else:
            if not root.left:
                new = root.right
                root = None
                return new
            elif not root.right:
                new = root.left
                root = None
                return new

            # Get smallest node in right subtree
            minR = root.right
            while(minR.left):
                minR = minR.left

            # Replace minR with desired node to delete.
            root.key = minR.key
            root.right = self.delete(root.right, minR.key)

        if not root:
            return root

        #Now need to balance
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        bal = self.get_balance(root)

        if bal < -1:
            if self.get_balance(root.right) <= 0:
                # Single left rotation.
                return self.rotateL(root)
            elif self.get_balance(root.right) > 0:
                # Double left rotation.
                root.right = self.rotateR(root.right)
                return self.rotateL(root)
        if bal > 1:
            if self.get_balance(root.left) >= 0:
                # Single right rotation.
                return self.rotateR(root)
            elif self.get_balance(root.left) < 0:
                # Double right rotation.
                root.left = self.rotateL(root.left)
                return self.rotateR(root)

        return root


def main():
    """
    Main executable code.
    """
    tree = Tree()
    root = None
    val = [""]
    init ()
    t = Turtle ()
    t.hideturtle()

    while val[0] != "end":
        isInTree = False
        val = input("add/search/delete [int]: ").split()

        if val[0] != "end":
            if val[0] == "add":
                root = tree.insertHelp(root, int(val[1]))
                reset ()
                drawTree(int(root.height-1), (0,150), root, int(val[1]))
                erasable=erasableWrite (t, val[1]  + ' has been inserted.')
                time.sleep(1)
                drawTree(int(root.height-1), (0,150), root, None)
                erasable.clear()


            elif val[0] == "search":
                drawTree(int(root.height-1), (0,150), root, None)
                tree.search(root, int(val[1]))
                isInTree = animateTraversal((0,150), root, int(val[1]),
                                             int(root.height-1), True, isInTree)

                if (isInTree == True):
                    erasable = erasableWrite(t, val[1]  + ' is in the tree.')
                    time.sleep (2)
                    erasable.clear ()
                else:
                    erasable = erasableWrite(t, val[1]  + ' is NOT in the tree.')
                    time.sleep (2)
                    erasable.clear ()



            elif val[0] == "delete":
                x = tree.search(root, int(val[1]))
                if (x != None):
                    root = tree.delete(root, int(val[1]))
                    reset ()
                    drawTree(int(root.height-1), (0,150), root, int(val[1]))
                    erasable=erasableWrite (t, val[1]  + ' has been deleted.')
                    time.sleep (1)
                    drawTree(int(root.height-1), (0,150), root, None)
                    erasable.clear()
                else:
                    print("Value not in tree. Try again.")
            
            else:
                print("ERROR: must type 'add/search/delete [int]' or 'end'")


if __name__ == "__main__":
    # When program is run.
    main()
