#Is it a lucky ticket? Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера
#билета. Написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если
#суммы различны.На вход программе подаётся строка из шести цифр.Выводить слово "Счастливый" или "Обычный", с большой буквы.
t = int(input('Enter the number: '))
if ((t % 1000) % 10) + (((t % 1000) % 100) // 10) + ((t % 1000) // 100) != ((t // 1000) % 10) + (((t // 1000) % 100) // 10) + ((t // 1000) // 100):
    print('Unlucky :(')
else:
    print('Congrats! :)')
