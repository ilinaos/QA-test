'''
Если я правильно поняла вводные, то имеется последовательность чисел от 0 до 9,
количество которых от 1 до 100. И необходимо посчитать количество чисел в этой последовательности,
которые больше двух своих соседей.
Не очень понятно, как поступить с первым и последним числом в этой последовательности.
А именно, считать ли их соседями или нет. Во втором случае каждое из них достаточно сравнить
лишь с одним своим соседом.
'''

#решение первое - первое и последнее число считаются соседями
try:
    numbers = [int(input('число: ')) for _ in range(int(input('сколько будет чисел? ')))]
except ValueError:
    print('ошибка ввода - нужны только целые числа')
except:
    print('unknown error')
else:
    bug_count = 0
    for index in range(len(numbers)):
        # если число не последнее в списке
        if index<len(numbers)-1:
            if numbers[index]>numbers[index+1] and numbers[index]>numbers[index-1]:
                bug_count+=1
        # и для последнего числа
        else:
            if numbers[index]>numbers[0] and numbers[index]>numbers[index-1]:
                bug_count+=1
    print(f'Багов будет исправлено: {bug_count}')

#вариант второй - первое и последнее число не считаются соседями
try:
    numbers = [int(input('число: ')) for _ in range(int(input('сколько будет чисел? ')))]
except ValueError:
    print('ошибка ввода - нужны только целые числа')
except:
    print('unknown error')
else:
    bug_count = 0
    #просматриваем числа, кроме первого и последнего
    for index in range(1, len(numbers)-1):
        if numbers[index]>numbers[index+1] and numbers[index]>numbers[index-1]:
            bug_count+=1
    #и оставшиеся два числа
    bug_count = bug_count+1 if numbers[0]>numbers[1] else bug_count
    bug_count = bug_count + 1 if numbers[-1] > numbers[-2] else bug_count

    print(f'Багов будет исправлено: {bug_count}')

