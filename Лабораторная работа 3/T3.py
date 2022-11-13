def T3():
	print("Программа найдёт максимальное значение параметра hp у героя. \nВведите слово hp для того чтобы начать поиск подходящего героя.")
	human_input = str(input());	

	Heroes = [
		["Tank",   100],
		["Support", 200],
		["Ranger",  50],
	]
	#print(Heroes[1])

	max_hp = 0;
	current_hp = 0;

	for i in range(len(Heroes)):
		#print(Heroes[i]);
		for i2 in range(len(Heroes[i])):
			#print(Heroes[i][i2]);
			current_hp = Heroes[i][i2 + 1];
			if (current_hp >= max_hp) and (human_input == "hp"):
				max_hp = current_hp;
				print("Самое максимальное кол-во hp имеет: " + str(Heroes[i][i2]) + ".   Значение параметра hp = " + str(Heroes[i][i2 + 1]));
			break;

	#print("Самое максимальное кол-во hp имеет: " + str(Heroes[i][i2]) + ".   Значение параметра hp = " + str(Heroes[i][i2 + 1]));
		#print("Самое максимальное кол-во hp имеет: " + str(Heroes[i][i2]) + ".   Значение параметра hp = " + str(Heroes[i][i2 + 1]));

	#print("Самое минимальное кол-во hp имеет: " +  + "Значение параметра hp = " + );
			





#print("Программа найдёт максимальное значение параметра hp у героя. \nВведите слово hp для того чтобы начать поиск подходящего героя.")
#human_input = str(input());
#human_input_hp = input("Введите количество hp которое вам нужно, верну название класса героя.")