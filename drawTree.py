"""
CSCI0302: Algorithms
Group Implementation Project
AVL Tree 

Members: Hamilton Evans, Harrison Govan, Brendan Murphy, Rose Gold
Referenced CLRS Textbook
"""

from turtle import * 
from math import acos

nodeSize = 25 # Size of each node
levelGap = 75 # Height distance between each level

def init ():
    # Innitializes turtle screen
    
    hideturtle ()
    setup (700,700)
    speed (0)
    bgcolor ('White')
    title ()

def drawTree (depth, rootLoc, rootNode, inserted):
    # Draws entire tree given the root node and the depth
    
    speed (0)
    hideturtle ()
    title ()
    penup ()
    setposition(rootLoc) # Setting location of root
    pencolor('Black')
    
    drawNode (rootNode.key, rootLoc, inserted, rootNode.height) 
    # Draws node with value given by rootNode.key
    
    if (depth == 0):  # If previous node is a leaf
        resetTurtle()
        return 
    
    distance = ((levelGap**2 + (2*depth * nodeSize / 2)**2)**0.5) 
    # Line distance connecting nodes
    angle = (acos(levelGap/distance)/0.0174533) 
    # Angle between nodes, switching from rad to degs
    
    if (rootNode.right != None): # If there is a right node
        rightSub = drawRight(rootLoc, distance, angle, 'Black', rootNode.right.key, inserted)
        drawTree ((depth-1), rightSub, rootNode.right, inserted)
        
    if (rootNode.left != None): # If there is a left node 
        leftSub = drawLeft(rootLoc, distance, angle, 'Black', rootNode.left.key, inserted)
        drawTree ((depth-1), leftSub, rootNode.left, inserted)
    
def drawNode (value,rootLoc, inserted, height):
    # Draws node
    
    if (inserted == value): # Colors newly inserted value 
        pencolor('Red')
    dot (nodeSize)
    pencolor('White')
    write(value, align='center')
    # Prints value in node
    pencolor('Black')    
    write ('                     ' + str(height), align='center') 
    # Prints height next to node

def drawRight (rootLoc, distance, angle, pcolor, value, inserted):
    # Draws a line connecting nodes to the right
    
    setposition (rootLoc)
    setheading (270)
    pendown()
    pencolor(pcolor)
    
    if (value == inserted): # Colors newly inserted values
        pencolor ('Red')
        
    left(angle)
    # Sets angle to the left for the right line since turtle is facing down
    forward(distance)
    penup()
    return position ()
    
def drawLeft(rootLoc,distance, angle, pcolor, value, inserted):
    # Draws a line connecting nodes to the left
    setposition (rootLoc)
    setheading (270)
    pendown()
    pencolor(pcolor)
    
    if (value == inserted): # Colors newly inserted values
        pencolor ('Red')
        
    right(angle) 
    # Sets angle to the right for the left line since turtle is facing down
    forward(distance)
    penup()
    return position ()
    
def animateTraversal (rootLoc, root, searchVal, depth, addNode, isInTree):
    # Animates tree traversal and highlights node if found
    
    speed(2)
    distance = ((levelGap**2 + (2*depth * nodeSize / 2)**2)**0.5)
    angle = (acos(levelGap/distance)/0.0174533) 
    penup ()
    setposition (rootLoc)
    pendown()
    pencolor ('Red')
    
    if (searchVal == root.key): 
        # If we found what were looking for, stop traversing
        drawNode (searchVal, rootLoc, None, root.height)
        resetTurtle()
        return True
    
    if (searchVal > root.key):
        # Node not found, traversing right subbtree
        if (root.right is None):
            # No right subtree
            return False
        newLoc = drawRight (rootLoc, distance, angle, 'Red', None, None)
        return animateTraversal (newLoc, root.right, searchVal, depth-1, addNode, isInTree)
    
    if (searchVal < root.key):
        # Node not found, traversing left subtree
        if (root.left is None):
            # No left subtree
            return False
        newLoc = drawLeft (rootLoc, distance, angle, 'Red', None, None)
        return animateTraversal (newLoc, root.left, searchVal, depth-1, addNode, isInTree)
    
def resetTurtle ():
    # Resets turtle to middle of screen
    
    penup ()
    setposition (0,0)
    
def title ():
    # Prints title on top of screen
    
    penup ()
    setposition (0, 200)
    pencolor ('Black')
    pendown ()
    FONT = ("Arial", 50, "bold")
    write ('AVL Tree', font=FONT, align='CENTER')
    penup ()
    setposition (0,0)
    
def erasableWrite(tortoise, name, reuse=None):
    # Allows writing at bottom of page to be erased 
    
    FONT = ("Arial", 20, "bold")
    eraser = Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(0,-300)
    eraser.write(name, font=FONT, align='CENTER')
    return eraser    



