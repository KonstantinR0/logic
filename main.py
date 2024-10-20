age = int(input("Введите свой возраст: "))
citizen = input("Являетесь ли вы гражданином РФ?  ").casefold()
pirson = input("Есть ли у вас уголовыная стать?  ").casefold()

if (age >= 18 ) and (citizen == "Да".casefold()) and (pirson == "Нет".casefold()):
    print("Вы можете проголосовать!")
else:
    print("К сожалению вы не можете прогоосовать")