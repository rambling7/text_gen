import random 

class Dictogram(dict):
	def __init__(self, iterable=None):
		super(Dictogram, self).__init__()
		self.types = 0			# уникальные ключи
		self.tokens = 0			# общее количество слов
		if iterable: 
			self.update(iterable)
			
	def update(self, iterable):	# обновляем распределение элементами итерируемого набора данных
		for item in iterable:
			if item in self:
				self[item] += 1
				self.tokens += 1
			else: 
				self[item] = 1
				self.types += 1
				self.tokens += 1
		
	def count(self, item):
		if item in self:		# возвращаем счетчик, иначе 0
			return self[item]
		return 0
		
	def return_random_word(self):
		random_key = random.sample(self.keys(), 1)
		return random_key[0]
		
	def return_weighted_random_word(self):
		random_int = random.randint(0, self.tokens-1)
		index = 0
		list_of_keys = list(self.keys())
		for i in range(0, self.types):
			index += self[list_of_keys[i]]
			if (index > random_int):
				return list_of_keys[i] 
				
if __name__ == '__main__':
	fish_text = 'one fish two fish blue fish red fish'.split()
	fish_dgram = Dictogram(fish_text)
	print(fish_dgram)
	test1 = fish_dgram.return_weighted_random_word()
	print(test1)
	test2 = fish_dgram.return_random_word()
	print(test2)
