from histograms import Dictogram

def make_markov_model(data):
	markov_model = dict()
	
	for i in range(0, len(data)-1):
		if data[i] in markov_model:
			markov_model[data[i]].update([data[i+1]])
		else: 
			markov_model[data[i]] = Dictogram([data[i+1]])
	return markov_model
	
def make_higher_order_markov_model(order, data):
	markov_model = dict()
	
	for i in range(0, len(data)-order):
		window = tuple(data[i: i+order])
		
		if window in markov_model:
			markov_model[window].update([data[i+order]])
		else:
			markov_model[window] = Dictogram([data[i+order]])
	return markov_model


if __name__ == '__main__':	
	fish_text = 'one fish two fish blue fish red fish'.split()
	test1 = make_markov_model(fish_text)
	print(test1)
	test2 = make_higher_order_markov_model(2, fish_text)
	print(test2)
