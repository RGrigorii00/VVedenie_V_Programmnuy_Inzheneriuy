### LAB NUMBER 6 ###

Name_HE = input();
Name_HE = Name_HE.lower()
Height_HE = int(input());
#Compare_return = 0;

class Students:
	def __init__(self, idn, name, height):

		self.idn = idn;
		St_idn = self.idn;
		self.name = name;
		St_names = self.name;
		St_names = St_names.lower()
		#print(St_names)
		self.height = height;
		St_heights = self.height;

### Algoritm Compare
		count = 0;
		len_0 = len(Name_HE);
		len_1 = len(St_names);
		elem_0 = str(Name_HE);
		elem_1 = St_names;
		Compare_return = 0;
		#print(elem_1)

		if len_0 > len_1:
			max_len = len_0;
		else:
			max_len = len_1;

		#print('Max: ' + str(max_len));

		for i in range(max_len):
			try:
				if elem_0[i] == elem_1[i]:
					count += 1;
			except:
				pass;
				#print(count)
		#print(max_len)
		Compare_return = count / len_1; 


		if ((St_heights - 5 < Height_HE < St_heights + 5) and (Compare_return >= 0.4)):
			person = (St_idn, St_names, height);
			print(person);

###               ID --- Name --- Height
Natasha = Students(0, "Natasha", 160);
Natasha = Students(1, "Natasha", 160);
Oleg    = Students(2, "Oleg", 180);
Oleg    = Students(3, "Oleg", 183);
Olga    = Students(4, "Olga", 158);
Olga    = Students(5, "Olga", 170);
