#создаем функции для вычисления площади кругна и длины окружности
def S(a):
    return a * a * 3.14
def C(a):
    return 2 * a * 3.14
R=float(input('введите радиус: ')) #вводим радиус круга с клавиатуры
res1 = S(R) #вызываем функцию 
print("Площадь круга равна:", res1) #выводим результат
res2 = C(R) #вызываем функцию 
print("Длина окружности равна:", res2) #выводим результат
