from linkedlist import Element
from linkedlist import LinkedList

class Queue(object):
    def __init__(self, firstIn=None):
        self.lList = LinkedList(firstIn)

    def push(self, newItem):
        #self.lList.add_item(newItem)
        self.lList.add_item(newItem)

    def pop(self):
        self.lList.remove_item_from(1)

    def show_all(self):
        return self.lList.show_all()
