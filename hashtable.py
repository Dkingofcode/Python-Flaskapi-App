class Node:
    def __init__(self, data):
         self.data = data
         self.next_node = next_node

class Data:
     def __init__(self, key, value):
          self.key = key
          self.value = value 

class HashTable:
     def __init__(self, table_size):
          self.table_size = table_size
          self.hash_table = [None]  + table_size

     def custom_hash(self, key):
          hash_value = 0
          for i in key:
               hash_value += ord(i)
               













