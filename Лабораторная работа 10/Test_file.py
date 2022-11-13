### COPY FOR TEST ###

### Human input
name_he = input()
height_he = int(input())

### Var's
#compare_return = 0

class Students:


	def __init__(self, idn, name, height):
			self.idn = idn
			st_idn = self.idn
			self.name = name
			St_names = self.name
			self.height = height
			St_heights = self.height

			### Algoritm Compare
			count = 0
			len_0 = len(name_he)
			len_1 = len(St_names)
			elem_0 = str(name_he)
			elem_1 = St_names
			compare_return = 0

			### Search maximum length
			if len_0 > len_1:
				max_len = len_0
			else:
				max_len = len_1

			### Iterating over segments of word
			for i in range(max_len):
				try:
					if elem_0[i] == elem_1[i]:
						count += 1
				except:
					pass

			compare_return = count / len_1 
			'''
			 len_1 потомучто если ввести символов многобольше чем 
			 длина имени, то не работает как нужно
			'''

			### Search condition
			if ((St_heights - 5 < height_he < St_heights + 5) and (compare_return >= 0.4)):
				person = (st_idn, St_names, height)
				print(person)

###               ID --- Name --- Height
Natasha = Students(0, "Natasha", 160)
Natasha = Students(1, "Natasha", 160)
Oleg    = Students(2, "Oleg", 180)
Oleg    = Students(3, "Oleg", 183)
Olga    = Students(4, "Olga", 158)
Olga    = Students(5, "Olga", 170)