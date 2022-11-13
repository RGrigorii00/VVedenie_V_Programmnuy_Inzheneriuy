def T5():
	Wheels = {
		4 :  10,
		6 :  25,
		8 :  40,
	}

	Weight_HE = int(input("Выберите количество колёс вашего ТС: "));

	print("Вы выбрали: " + str(Weight_HE) + " колеса. " + "Максимальный перевозимый вес = " + str(Wheels[Weight_HE]) + " тонн.");