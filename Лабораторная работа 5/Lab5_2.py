### LAB NUMBER 5 ###

Heroes = {
	1 : 100,
	2 :  20,
	3 :  50,
}


def SearchMaxHp():

	max_hp = 0;
	current_hp = 0;

	for i in Heroes:
		current_hp = Heroes[i];
		if current_hp >= max_hp:
			max_hp = current_hp;
		#break;
	return max_hp;
print(SearchMaxHp());

	#print("Самый живучий герой имеет: " + str(max_hp) + " очков здоровья");