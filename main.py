from linkedlist import Element
from linkedlist import LinkedList

element1 = Element(2)
element2 = Element(2)
element3 = Element(2)
element4 = Element(2)
element5 = Element(7)
element6 = Element(9)
element7 = Element(2)

list1 = LinkedList(element1)
list1.add_item(element2)
list1.add_item(element3)
list1.add_item(element4)
list1.add_item(element5)
print list1.show_all()
list1.remove_item(2)
print list1.show_all()
list1.add_item(element6)
#list1.add_item(element7)
print list1.show_all()
list1.remove_item(2)
print list1.show_all()