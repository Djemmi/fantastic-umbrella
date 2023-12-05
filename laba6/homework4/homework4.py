"""
Условие подразумевает хранение не более 1 значения
из файлов ./matrix1.txt && ./matrix2.txt за раз

Тоесть мы будем писать все поверх одной и той же переменной
Вообще в задаче сказано что можно хранить ПО ОДНОМУ элементу
КАЖДОЙ матрицы, но мы же экстрималы-энтузиасты, верно?
"""

# cahce - переменная для хранения едиественная

result_matrix = [[], []]

current_line = 0
current_row = 0

"""
00*00 + 01*10 | 00*01 + 01*11
10*00 + 11*10 | 10*01 + 11*11
"""
'123'.strip()

with open('./matrix1.txt') as matrix1:
    with open('./matrix2.txt') as matrix2:
        for line in matrix1.readlines(): # массив где элемент - строка матрицы как строка
            for element in line.replace("\n", "").split(" "):
                result_matrix[]
                print(int(element))
            print('-----')
        """
        
        0 0\n -> ["0 0","0 0"] 
        0 0\n
        """