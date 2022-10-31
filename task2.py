dct = {}#создаем пустой словарь
for i in range(int(input())):#цикл от (0) до введённого значения(N)
    country,* towns = input().split()
    #вводим нашу строку,методом split()разбиваем на части(разделитель -пробел-)
    #первое слово идёт в список (coutry),остальные в список (towns)
    for town in towns:#ищем (town) в списке (towns)
        dct[town] = country#присваиваем ключу(town) значение country
print(*(dct[input()] for i in range(int(input()))),sep='\n')
