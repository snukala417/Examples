class Node():
    def __init__(self, data, next_node=None):
        self.data=data
        self.next_node=next_node

    def set_next(self, node):
        self.next_node=node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node



class LinkedList():
      def __init__(self,head=None):
          self.head=head

      def insert(self, data):
          new_node = Node(data)
          new_node.set_next(self.head)
          self.head=new_node

      def size(self):
          i = 0
          current = self.head
          while current:
            i += 1
            current = current.get_next()

          return i

       def delete(self,data):
           current = self.head
           previous = None
           found = False
           while current and found is False:
               if current.get_data==data:
                   found=True
               else:
                   previous=current
                   current = current.get_next()
           if current == None:
               return False
           if previous



