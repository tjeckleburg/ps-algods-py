
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.N = 0

    def printpaths(self):
        """Given a binary tree, print out all of its root-to-leaf
        paths, one per line."""
        def printpathsBT(node):
            path = [None] * 1000
            printpathsrecur(node, path, 0)

        def printpathsrecur(node, path, pathlen):
            if node is None:
                return

            path[pathlen] = node.data
            pathlen = pathlen + 1

            # if its a leaf then print the path which led to here
            if (node.left is None) and (node.right is None):
                printList(path, pathlen)
            else:
                printpathsrecur(node.left, path, pathlen)
                printpathsrecur(node.right, path, pathlen)

        def printList(path, pathlen):
            for p in range(pathlen):
                print (path[p], sep=" ", end= " ")
            print ()
        printpathsBT(self.root)


    def haspathsum(self, targetsum):
        """ Given a tree and a sum, return true if there is a path from the root
        down to a leaf, such that adding up all the values along the path
        equals the given sum."""
        def haspathsumBT(node, targetsum):
            if node is None:
                return targetsum == 0
            # lets check both subtress
            return haspathsumBT(node.left, targetsum - node.data) or \
                haspathsumBT(node.right, targetsum - node.data)
        return haspathsumBT(self.root, targetsum)

    def insert(self, data):
        def insertBST(node, data):
            if node is None:
                return Node(data)
            if data <= node.data:
                node.left = insertBST(node.left, data)
            else:
                node.right = insertBST(node.right, data)
            return node

        self.root = insertBST(self.root, data)

    def minvalue(self):
        def minvalbst(node):
            if node is None:
                return None
            while node.left is not None:
                node = node.left
            return node.data
        return minvalbst(self.root)

    def maxvalue(self):
        def maxvalbst(node):
            if node is None:
                return None
            while node.right is not None:
                node = node.right
            return node.data
        return maxvalbst(self.root)

    def maxdepth(self):
        def maxdepthBT(node):
            if node is None:
                return 0
            left = maxdepthBT(node.left)
            right = maxdepthBT(node.right)
            if left > right:
                return left + 1
            else:
                return right + 1
        return maxdepthBT(self.root)

    def size(self):
        def sizebt(node):
            if node is None:
                return 0
            return (sizebt(node.left) + 1 + sizebt(node.right))
        return sizebt(self.root)

    def preorder(self):
        def preorderBT(node):
            if node is None:
                return
            print (node.data, sep=" ", end=" ")
            preorderBT(node.left)
            preorderBT(node.right)
        preorderBT(self.root)
        print ()

    def postorder(self):
        def postorderBT(node):
            if node is None:
                return
            postorderBT(node.left)
            postorderBT(node.right)
            print (node.data, sep=" ", end=" ")
        postorderBT(self.root)
        print ()

    def inorder(self):
        def inorderBST(node):
            if node is None:
                return
            inorderBST(node.left)
            print (node.data, sep=" ", end=" ")
            inorderBST(node.right)

        inorderBST(self.root)
        print ()

    def isempty(self):
        return self.N == 0