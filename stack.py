from linkedlist import Element
from linkedlist import LinkedList

class Stack(object):
    def __init__(self, lastIn=None):
        self.lList = LinkedList(lastIn)

    def push(self, newItem):
        #self.lList.add_item(newItem)
        self.lList.insert_item(newItem, 1)

    def pop(self):
        self.lList.remove_item_from(1)

    def show_all(self):
        return self.lList.show_all()
