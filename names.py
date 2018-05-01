

class Name(object):
	def __init__(self, text_init=""):
		self.text = text_init

class Firstname(Name):
	def __init__(self, text_init=""):
		super(Firstname, self).__init__(text_init)
