class Node: 
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.mid = data//2


class BinarySearchTree:
        def __init__(self):
            self.root = None
        if(data):
         if(self.mid == target):
            return mid
         if(mid < target):
            return self.left    
         else: 
            return self.right


        def _insert_recursive(self, value, node):
           if value < node.data:
              if node.left is None:
                  node.left = Node(value)
              else: 
                  self._insert_recursive(value, self.left)
           elif value > node.data:
               if node.right is None:
                   node.right = Node(value)
               else: 
                   self._insert_recursive(value, node.right)
           else:
               return



        def insert(self, value):
            if self.root is None:
                self.root = Node(value)
            else:
                self._insert_recursive(value, self.root)      
         
        

        def _search_recursive(self, blog_post_id, node):
            if node.left == None and node.right == None:
                 return False
            
            if blog_post_id == node.data["id"]:
                return node.data
            
            if blog_post_id < node.data["id"]:
               if blog_post_id == node.left.data["id"]:
                return node.left.data
               return self._search_recursive(blog_post_id, node.left)


            if blog_post_id > node.data["id"]:
               if blog_post_id == node.right.data["id"]:
                    return node.right.data
               return self._search_recursive(blog_post_id, node.right)   


def search(self, blog_post_id):
      blog_post_id = int(blog_post_id)
      if self.root is None:
           return False

      return self._search_recursive(blog_post_id, self.root)
         






































