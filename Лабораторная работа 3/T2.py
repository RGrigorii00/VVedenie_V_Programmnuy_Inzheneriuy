def T2():
	Heroes = {
		1 : 100, # Tank
		2 :  20, # Support
		3 :  50, # Ranger
	}

	max_hp = 0;
	current_hp = 0;
	
	for i in Heroes:
		current_hp = Heroes[i];
		if current_hp >= max_hp:
			max_hp = current_hp;
	#print(max_hp);

	print("Самый живучий герой имеет: " + str(max_hp) + " очков здоровья");