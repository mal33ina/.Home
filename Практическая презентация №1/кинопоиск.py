a=str(input("Введите запрос: "))
if a=="лучший фильм" or a=="фильм":
	b=int(input("Введите дату: "))
	if b<2017 or b>2020:
		print("Повторите попытку")
	if b==2017:
		c=str(input("введите жанр: "))
		if c=="боевик":
			print("Gans")
	elif b==2018:
		c=str(input("введите жанр: "))
		if c=="боевик":
			print("Шлейф подласти")
	elif b==2019:
		c=str(input("введите жанр: "))
		if c=="боевик":
			print("Зло на месте")
	elif b==2020:
		c=str(input("введите жанр: "))
		if c=="боевик":
			print("Закрег")	
	if b==2017:
		if c=="комедия":
			print("Один в лифте")
	elif b==2018:
		if c=="комедия":
			print("Ни за одной")
	elif b==2019:
		if c=="комедия":
			print("За городом")
	elif b==2020:
		if c=="комедия":
			print("Скрепучий малый")	
	if b==2017:
		if c=="мелодрама":
			print("Поцелуй в губы")
	elif b==2018:
		if c=="мелодрама":
			print("Не за чем так")
	elif b==2019:
		if c=="мелодрама":
			print("Не упусти свой шанс")
	elif b==2020:
		if c=="мелодрама":
			print("Поцелуй в низ")