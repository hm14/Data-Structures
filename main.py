from linkedlist import Element
from linkedlist import LinkedList

# create a instances of Element
element1 = Element(5)
element2 = Element(0)
element3 = Element(2)
element4 = Element(8)
element5 = Element(7)
element6 = Element(9)
element7 = Element(2)
element8 = Element(18)
element9 = Element(19)

# create an instance of LinkedList with head = element1
list1 = LinkedList(element1)

# add a few elements to the LinkedList instance
list1.add_item(element2)
list1.add_item(element3)
list1.add_item(element4)
list1.add_item(element5)

# print values to confirm that items were added
print list1.show_all()

# remove a few values from the list and confirm removal
list1.remove_item(2)
list1.remove_item(5)
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

# insert items at a given position and confirm addition
list1.insert_item(element8, 2)
print 'inserting new element at 2nd position'
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
list1.delete_item(18)
print 'deleting 18:'
print list1.show_all()

# delete given value and confirm deletion
list1.delete_item(7)
print 'deleting 7:'
print list1.show_all()
