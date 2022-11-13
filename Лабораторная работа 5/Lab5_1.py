### LAB NUMBER 5 ###

Heroes = [
	["Tank",   100],
	["Support", 20],
	["Ranger",  50],
]

#print(Heroes[0][1]);

def SearchMaxHP():

	max_hp = 0;
	current_hp = 0;

	for i in range(len(Heroes)):
		#print(Heroes[i]);
		for i2 in range(len(Heroes[i])):
			#print(Heroes[i][i2]);
			current_hp = Heroes[i][i2 + 1];
			if current_hp >= max_hp:
				max_hp = current_hp;
			break;
	return max_hp;

print(SearchMaxHP());