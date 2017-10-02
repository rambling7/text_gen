from histograms import Dictogram
from markov_model import make_markov_model, make_higher_order_markov_model
import random
from collections import deque
import re

def generate_random_start(model):
#	return random.choice(list(model.keys()))	# случайное начальное слово

	if 'END' in model:
		seed_word = 'END'
		while seed_word == 'END':
			seed_word = model['END'].return_weighted_random_word()
		return seed_word
	return random.choice(list(model.keys()))
	
def generate_random_sentence(length, markov_model):
	current_word = generate_random_start(markov_model)
	sentence = [current_word]
	for i in range(0, length):
		current_dictogram = markov_model[current_word]
		random_weighted_word = current_dictogram.return_weighted_random_word()
		current_word = random_weighted_word
		sentence.append(current_word)
	sentence[0] = sentence[0].capitalize()
	return ' '.join(sentence)+ '.'
	return sentence

if __name__ == '__main__':	
	fish_text = 'Прежде всего, надо понять, что получить эту бесценную человеческую жизнь с восемнадцатью драгоценными привилегиями не очень просто. Мы можем подумать: „На Земле столько людей! Разве получить человеческую жизнь так тяжело?” Чтобы осознать ценность драгоценного человеческого рождения, мы должны сравнить количество живых существ всех шести сфер, и только тогда мы увидим настоящую картину. Люди являются лишь незначительной частицей всех живых существ шести сфер. Если быть точным, то просто стать человеком, иметь человеческое тело, не так уж и тяжело — для этого достаточно лишь посмотреть на статую будды и ощутить большую преданность. Если эта преданность сохраняется и не уменьшается, то создается причина для человеческого перерождения.'.split()
	fish_model = make_markov_model(fish_text)
#	print(fish_model)
	random_start_word = generate_random_start(fish_model)
#	print(random_start_word)
	random_sentence = generate_random_sentence(10, fish_model)
	print(random_sentence)
