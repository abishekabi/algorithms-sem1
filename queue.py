"""
Implement Queue
"""

class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		#super(Queue, self).__init__()
		#for _ in range(10):
		self.queue_array = [None] * 10
		self.f = 0
		self.r = 0
		self.N = 10

	def size(self):
		#self.N = len(self.queue_array)
		return (self.N - self.f + self.r ) % self.N

	def enqueue(self, item):
		if self.queue_array[self.r] == None:
			self.queue_array[self.r] = item
			# self.N += 1
			self.r = (self.r + 1) % self.N
			return self.queue_array
		else:
			print "enqueue Error"

	def dequeue(self, item):
		if self.queue_array[self.f] != None:
			self.queue_array[self.f] = None
			# self.N -= 1
			self.f = (self.f + 1) % self.N
			return self.queue_array
		else:
			print "Dequeue Error"


Q1 = Queue()

#print(Q1.size())
for i in range(10):
	print(Q1.enqueue(2))
	print(Q1.size())
print(Q1.dequeue(2))