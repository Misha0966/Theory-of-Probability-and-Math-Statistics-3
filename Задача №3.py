# В университет на факультеты A и B поступило равное количество студентов,
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7,
# а для студента факультета C - 0.9.
# Студент сдал первую сессию.
# Какова вероятность,
# что он учится: a). на факультете A б). на факультете B в). на факультете C?

pA = 0.8
pB = 0.7
pC = 0.9

x1 = 1/4  # вероятность того, что студент окажется  с факультета А или В
x2 = 0.5  # вероятность того, что студент окажется с факультета С.

p = 1/4*0.8+1/4*0.7+1/2*0.9
# 0.825

A = 1/4*0.8/p
# Ответ: 0.24242424242424246 или ~ 24.24%

B = 1/4*0.7/p
# Ответ: 0.21212121212121213 или ~ 21.21%

C = 1/2*0.9/p
# Ответ: 0.5454545454545455 или ~ 54.54%