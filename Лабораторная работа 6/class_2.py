### LAB NUMBER 6 ###

Name_HE = input();
Height_HE = int(input());

class Students:
	def __init__(self, idn, name, height):

		self.idn = idn;
		St_idn = self.idn;
		self.name = name;
		St_names = self.name;
		self.height = height;
		St_heights = self.height;

		if ((St_names == Name_HE) and (St_heights - 5 < Height_HE < St_heights + 5)):
			person = (St_idn, St_names, height);
			print(person);

###               ID --- Name --- Height
Natasha = Students(0, "Natasha", 160);
Natasha = Students(1, "Natasha", 160);
Oleg    = Students(2, "Oleg", 180);
Oleg    = Students(3, "Oleg", 183);
Olga    = Students(4, "Olga", 158);
Olga    = Students(5, "Olga", 170);

#Name_HE = input(); # HE - Human Enter
#Height_HE = int(input());

#print(Oleg.__dict__)
