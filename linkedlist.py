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

	# gets position of the element at the given number
	# gets 2nd element's position for position=2
	def get_position(self, position):
		if self.head:
			counter = 1
			current = self.head
			if position >= 1:
				while current and counter <= position:
					if counter == position:
						return current
					current = current.next
					counter += 1
		return None

	# inserts new item at a given position instead of at end of list
	def insert_item(self, new_element, position):
		if self.head:
			previous = None
			current = self.head
			current_position = 1
			if position > 1:
				while current_position <= position and current:
					if current_position == position:
						previous.next = new_element
						new_element.next = current
					previous = current
					current = current.next
					current_position += 1
			elif position == 1:
				new_element.next = self.head
				self.head = new_element

	# removes item from a given location
	def remove_item_from(self, position):
		if self.head:
			previous = None
			current = self.head
			current_position = 1
			if position > 1:
				while current_position <= position and current:
					if current_position == position:
						previous.next = current.next
					previous = current
					current = current.next
					current_position += 1
			elif position == 1:
				self.head = current.next

	# deletes first item with a given value from the linked list
	def delete_item(self, value):
		if self.head.value == value:
			self.head = self.head.next
		else:
			previous = None
			current = self.head
			while current.value != value and current.next:
				previous = current
				current = current.next
			if current.value == value:
				previous.next = current.next
