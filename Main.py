# task 1
print('Пользователь вводит с клавиатурыдва числа. Нужнопосчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.')
try:
    a = int(input('Enter number value start range: '))
    b = int(input('Enter number value end range: '))
    even_number = 0
    odd_number = 0
    multiple_9 = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            even_number += i
        else:
            odd_number += i
        if i % 9 == 0:
            multiple_9 += i
    avg_number = ( even_number + odd_number + multiple_9 ) / 3
    print('summa_even =',even_number)
    print('summa_odd_number =',odd_number)
    print('summa_multiple_9 =',multiple_9)
    print('avg_number =',avg_number)
    print('\n')
except ValueError:
    print('Enter number error')

# task 2
print('Пользователь вводит с клавиатуры длину линии и символ для заполнения линии.\n Нужно отобразить на экране вертикальную линию из введенного символа указанной длины.')
try:
    count_simvol = int(input('Enter count simvol: '))
    simvol = input('Enter simvol: ')
    for i in range(count_simvol):
        print(simvol)
    print('\n')
except ValueError:
    print('Enter number error')

# task 3
print('Пользователь вводит с клавиатурычисла.\n Если число больше нуля нужно вывести надпись «Number is positive»,\nесли меньше нуля «Number is negative»,\n если равно нулю «Number is equal to zero».')
a = bool(1)
while a:
    try:
        input_value = int(input('Enter number value: '))
        if input_value == 7:
            a = bool(0)
            break
        elif input_value > 0:
            print('Number is positive')
        elif input_value < 0:
            print('Number is negative')
        elif input_value == 0:
            print('Number is equal to zero')
    except ValueError:
        print('Input value error')         
print('Good bye!')
print('\n')

# task 4
print('task 4')
a = bool(1)
min_value = 0
max_value = 0
summa_value = 0
counter_value = 0
while a:
    try:
        input_value = int(input('Enter number value: '))
        if input_value == 7:
            a = bool(0)
            break
        else:
            summa_value += input_value
            if counter_value == 0:
                min_value = input_value
                max_value = input_value
            else:
                if input_value < min_value :
                    min_value = input_value
                if input_value > max_value :
                    max_value = input_value
        counter_value += 1
    except ValueError:
        print('Input value error')
print('Max =',max_value)
print('Min =',min_value)
print('Summa =',summa_value)
print('Good bye!')
    
