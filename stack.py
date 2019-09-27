"""
Implement stack 

"""



class Stack(object):
	"""stack class"""
	def __init__(self, arg):
		super(Stack, self).__init__()
		self.arg = arg
	def size(self):
		self.ob