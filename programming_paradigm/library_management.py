class Book:
	"""A class to list book details in a library. """
	def __init__(self, title, author):
		"""Instatiate the class attributes"""
		self.title = title
		self.author = author
		self._is_checked_out = is_checked_out = False
    

	def check_out(self):
		self._is_checked_out = True

	def return_book(self):
		self._is_checked_out = False 
	
	def is_available(self):
		return not self._is_checked_out
	
	def __str__(self):
		return f"{self.title} by {self.author}"
                     

class Library:
	"""Perform normal functions of a library with regard to book handling"""
	def __init__(self):
		self._books = []

	def add_book(self, book):
		"""Add books to the library"""
		if isinstance(book, Book):
			self._books.append(book)

	def check_out_book(self, title):
		for book in self._books:
			if book.title == title and book.is_available():
				book.check_out()
				return True
		return False
	
	def return_book(self, title):
		for book in self._books:
			if book.title == title and not book.is_available():
				book.return_book()
				return True
		return False
	
	def list_available_books(self):
		for book in self._books:
			if book.is_available():
				print(book)
				


