import os

# Test 1
path = "C:/Users/Admin/Desktop/black-book"


def black_book(page: int) -> bool:
    status_code = os.system(f"./{path} -n {page}")
    return status_code == 0


print(black_book(10000000))


# Предположил что, если страниц не более 10 000 000, то за основу взял это количество, что бы
# посчитать сумму номеров страниц
print(sum(i for i in range(1, 10000000 + 1)))

# Через цикл while находим номер последней страницы.
s, n = 50000005000000, 0
while s >= n:
    n += 1
    s -= n
print(f'Страниц:', n)