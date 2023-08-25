class Node:
    def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node


class LinkedList:
      def __init__(self):
            self.head = None
            self.last_node = None

      def to_list(self):
            l = []
            if self.head is None:
                 return l
            

            node = self.head
            while node:
                  l.append(node.data)
                  node = node.next_node
            return l      


      def print_ll(self):
            ll_string = ""
            node = self.head
            if node is None:
                  print (None)
            while node:
                 ll_string += f" {str(node.data)} ->"  
                 if node.next_node is None:
                       ll_string += " None"
                       node = node.next_node
            print(ll_string)        


      def insert_beginning(self, data):
             if self.head is None:
                  new_node = Node(data, None)
                  new_node = self.head
             else:
                   new_node = Node(data, self.head)
                   self.head = new_node     
            


      def insert_end(self, data):
            if self.head  is None:
                  self.insert_beginning(data)
                  return
            # if self.last_node is None:
            #       node = self.head
            #       while node.next_node:
            #             node = node.next_node

            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node
       
      def  get_user_by_id(self, user_id):      
             node = self.head
             while node:
                   if node.data["id"] is int(user_id):
                         return node.data
                   node = node.next_node

















ll = LinkedList()
node4 = Node("data", None)
node3 = Node("data", node4)
node2 = Node("data", node3)
node1 = Node("data", node2)

ll.head = node1




            