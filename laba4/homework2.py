"""
Задание полнейший бред
Оно сделана не столько по условию,
Сколько для дальнейшей модификации в случае если условие изменится
"""

n = int(input("Сколько гостей сидит за столом? "))
pie_sceme = [0]  # отображает кол-во кусков. Число - количество итераций //2 куска
cuts_count = 0  # кол-во разрезов
q = int(input("Какое условие применить (1-3)? "))  # номер условия

if q == 1:
    # Условие 1
    while len(pie_sceme) < n:
        cut_piece = min(pie_sceme)
        pie_sceme.remove(cut_piece)
        pie_sceme += [cut_piece + 1, cut_piece + 1]
        cuts_count += 1
elif q == 2:
    # Условие 2
    while len(pie_sceme) < n + (n // 2 + n % 2):
        cut_piece = min(pie_sceme)
        pie_sceme.remove(cut_piece)
        pie_sceme += [cut_piece + 1, cut_piece + 1]
        cuts_count += 1
elif q == 3:
    # Условие 3
    while len(pie_sceme) < n + 10:
        cut_piece = min(pie_sceme)
        pie_sceme.remove(cut_piece)
        pie_sceme += [cut_piece + 1, cut_piece + 1]
        cuts_count += 1

print("Потребуется " + str(cuts_count) + " разрез(ов).")
