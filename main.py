from linkedlist import Element
from linkedlist import LinkedList
from stack import Stack
from queue import Queue

# create instances of Element
element1 = Element(5)
element2 = Element(0)
element3 = Element(2)
element4 = Element(8)
element5 = Element(7)
element6 = Element(9)
element7 = Element(2)
element8 = Element(18)
element9 = Element(19)
element10 = Element(10)
element11 = Element(82)
element12 = Element(21)
element13 = Element(68)
element14 = Element(32)
element15 = Element(55)

# create an instance of LinkedList with head = element1
list1 = LinkedList(element1)

# add a few elements to the LinkedList instance
list1.add_item(element2)
list1.add_item(element3)
list1.add_item(element4)
list1.add_item(element5)

print '* * * * * LINKED LIST STUFF * * * * *'
# print values to confirm that items were added
print 'adding multiple elements to linked list'
print list1.show_all()

# remove a few values from the list and confirm removal
list1.remove_item(2)
list1.remove_item(5)
print 'removing multiple elements from linked list'
print list1.show_all()

# print position of the element at the position = 2
print 'getting position of 2nd element in linked list'
print list1.get_position(2)

# insert items at a given position and confirm addition
list1.insert_item(element6, 1)
print 'inserting new element at 1st position'
print list1.show_all()

# insert items at a given position and confirm addition
list1.insert_item(element7, 4)
print 'inserting new element at 4th position'
print list1.show_all()

# remove item from given position and confirm deletion
list1.remove_item_from(5)
print 'removing 5th item:'
print list1.show_all()

# remove item from given position and confirm deletion
list1.remove_item_from(1)
print 'removing 1st item:'
print list1.show_all()

# delete given value and confirm deletion
list1.delete_item(0)
print 'deleting 0:'
print list1.show_all()

# delete given value and confirm deletion
list1.delete_item(8)
print 'deleting 8:'
print list1.show_all()

print '* * * * * STACK STUFF * * * * *'
# create an instance of LinkedList with head = element1
print 'creating a new stack'
stack = Stack(element8)

# add a few elements to the LinkedList instance
print 'adding multiple items to stack'
print stack.show_all()
stack.push(element9)
print stack.show_all()
stack.push(element10)
print stack.show_all()
stack.push(element11)

#print values to confirm that elements were added to stack
print stack.show_all()

print 'removing multiple items from stack'
stack.pop()
print stack.show_all()
stack.pop()
print stack.show_all()

print '* * * * * QUEUE STUFF * * * * *'
print 'creating queue'
queue = Queue(element12)
print 'adding multiple items to queue'
print queue.show_all()
queue.push(element13)
print queue.show_all()
queue.push(element14)
print queue.show_all()
queue.push(element15)
print queue.show_all()
print 'removing multiple items from queue'
queue.pop()
print queue.show_all()
queue.pop()
print queue.show_all()
queue.pop()
print queue.show_all()
