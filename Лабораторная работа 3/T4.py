def T4():
	print("Программа найдёт минимальное значение параметра hp у героя. \nВведите слово hp для того чтобы начать поиск подходящего героя.")
	human_input = str(input());

	Heroes = [
		["Tank",   100],
		["Support", 20],
		["Ranger",  50],
	]
	#print(Heroes[1])

	min_hp = 50;
	current_hp = 0;

	for i in range(len(Heroes)):
		#print(Heroes[i]);
		for i2 in range(len(Heroes[i])):
			#print(Heroes[i][i2]);
			current_hp = Heroes[i][i2 + 1];
			if current_hp <= min_hp and human_input == "hp":
				min_hp = current_hp;
				print("Самое минимальное кол-во hp имеет: " + str(Heroes[i][i2]) + ".   Значение параметра hp = " + str(Heroes[i][i2 + 1]));
			break;
	#print("Самое минимальное кол-во hp имеет: " + str(Heroes[i][i2]) + ".   Значение параметра hp = " + str(Heroes[i][i2 + 1]));

	