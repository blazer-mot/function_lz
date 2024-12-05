#создаем функции для подсчета суммы цифр числа
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
n=int(input('введите число: ')) #вводим число с клавиатуры
print(sum_of_digits(n)) #выводи ответ