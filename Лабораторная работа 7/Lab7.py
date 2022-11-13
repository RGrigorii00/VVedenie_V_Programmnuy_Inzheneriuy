### LAB NUMBER 7 ###
# Import
from itertools import product
from pprint import pprint


class Person:


	def __init__(self, name, age, adress):
		self.name = name
		self.age = age
		self.adress = adress
		self.key = (name, adress)


	def __repr__(self):
		return "Person('%s', '%s', '%s')"


	def fuzzy_compare(query):
		q = set(query.split())
		score = 0
		for m, a in zip([ADDRES_WORDS, ], [by_adress, by_name, by_age]):
			if m & q:
				score += f(q)
			return score > 0.49


	for query, person in product(quaries, people.values()):
		if person == query:
			pprint((query, person))


	def __eq__(self, obj):	
		if type(obj) == Person:
			return
		elif type(obj) == str:
			return fuzzy_compare(obj)
		else:
			return

	def by_adress(Q):
		Q = Q - ADRESS_WORDS
		W = set(self.adress.split())
		rez = []
		for a, b in product(Q, W):
			rez += [(compare(a, b), a, b)]
		return max(rez)[0]

	# Age
	def by_age(Q):
		q_age = max([int_val(q) for q in Q])
		if 'elder' in Q:
			return q_age < self.age
		return q_age + 5 >= self.age >= q_age - 5


	lena = Person("Lena", 19, "Pushkina")
	oleg = Person("Oleg", 34, "Lenskogo")
	olga = Person("Olga", 28, "Onegina")
	natasha = Person("Natasha", 17, "Rostova")
		
	queries = [
		'name Olga',
		'age 30',
		'elder 20',
		'younger 20',
		'live on st.Pushkina',
		'house 10',
		'second name Rostova',
		'name Natasha',
	]
	people = {
		lena.key : lena,
		oleg.key : oleg,
		olga.key : olga,
		natasha.key : natasha,
	}

	ADRESS_WORDS = {'house', 'street', 'live'}


# Test
if __name__ == '__main__':
	for a, b in [
			('algoritm', 'algoritmi'),
			('stol', 'stolik'),
			('stol', 'styl'),
			]:
			print(a, b, compare(a, b))
	print([int_val(s) for s in ['c', '1']])


#for query, person in product(quaries, people.values()):
#	if person == query:
#		pprint((query, person))

