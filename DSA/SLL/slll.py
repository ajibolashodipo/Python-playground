#  class Node:
#      def __init__(self, data):
#          self.data= data
#          self.nextNode= None
#
#
#
# class LinkedList:
#     def __init__(self):
#         self.head= None
#         self.tail= None
#         self.numOfNodes= 0
#
#     def insert_start(self, data):
#         self.numOfNodes += 1
#         new_node= Node(data)
#         # check if head exists
#         if not self.head:
#             self.head= new_node
#             self.tail= self.head
#
#         else:
#             old_head= self.head
#             new_node.nextNode= old_head
#             self.head= new_node

class Node:
    def __init__(self, value=None):
        self.value= value
        self.next= None

class SLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None