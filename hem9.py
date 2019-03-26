class test:
	h=0
	def __init___(self):
		h=6

	def my_func(self,k):
		print("hi,im in class")
		self.h=k
		print(self.h)
o=test()
print(o.h)	
o1=test()
print(o1.h)
o.my_func(2)
print(o.h)
o1.my_func(28)
print(o1.h)		

		