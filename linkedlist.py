# class for elements of the linkedlist
class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

# class for linkedlist
class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	# prints values of all elements in a linkedlist
	def show_all(self):
		if self.head:
			current = self.head
			values = [current.value]
			while current.next:
				current = current.next
				values.append(current.value)
			return values
		else:
			return None

	# adds an element to the end of the linkedlist
	def add_item(self, element):
		if self.head:
			current = self.head
			while current.next:
				current = current.next
			current.next = element

	# removes first element with a given value from the linkedlist
	def remove_item(self, value):
		if self.head:
			current = self.head
			previous = None
			while current.value != value and current.next:
				previous = current
				current = current.next
			if current.value == value:
				if previous:
					previous.next = current.next
				else:
					self.head = current.next


