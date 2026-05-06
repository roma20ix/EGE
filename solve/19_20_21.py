"""
Задания 19-21 - Теория игр

В этом задании дана одна или две кучи камней и два игрока, которые могут увеличивать или уменьшать количество камней в куче.
Необходимо ответить на 3 вопроса, связанных со стратегией игроков.

Рассмотрим обычное и более быстрое решение для одной и двух куч
"""

# Задача на одну кучу
# Код на kompege - 28940

def f(s, m):
    if s >= 124: return m % 2 == 0
    if m == 0: return 0
    nx = (f(x, m-1) for x in (s+1, s+5, s*3))
    return any(nx) if m % 2 else all(nx)

print([s for s in range(1, 124) if f(s, 2)])
print([s for s in range(1, 124) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 124) if not f(s, 2) and f(s, 4)])
print()

# Далее выбираем необходимые s для каждого пункта или делаем это сразу в коде


# Задача на одну кучу с неудачным ходом
# Код на kompege - 18958

def f(s, m, p=0):  # p - флаг для №19
    if s >= 666: return m % 2 == 0
    if m == 0: return 0
    nx = (f(x, m-1) for x in (s+3, s*3, s+s*s))
    return any(nx) if p or m % 2 else all(nx)

print([s for s in range(1, 666) if f(s, 2, 1)][0])
ss = [s for s in range(1, 666) if not f(s, 1) and f(s, 3)]
print(ss[0], ss[-1])
print([s for s in range(1, 666) if not f(s, 2) and f(s, 4)][-1])
print()


# Задача на две кучи
# Код на kompege - 20907

def moves(s1, s2):
    return [(s1+1, s2), (s1, s2+1), (s1*2, s2), (s1, s2*2)]

def f(s1, s2, m, p=0):
    if s1+s2 >= 81: return m % 2 == 0
    if m == 0: return 0
    nx = (f(x, y, m-1) for x, y in moves(s1, s2))
    return any(nx) if p or m % 2 else all(nx)

print([s for s in range(1, 74) if f(7, s, 2, 1)][0])
print(*[s for s in range(1, 74) if not f(7, s, 1) and f(7, s, 3)][:2])
print([s for s in range(1, 74) if not f(7, s, 2) and f(7, s, 4)][0])
print()


# Так с помощью одного параметра можно решать оба варианта задачи 19
# В задачах, где количество куч больше чем одна, удобно вывести отдельную функцию для определения всех возможных ходов

# Теперь рассмотрим одну интересную оптимизацию
# Её не стоит делать на ЕГЭ, так как таких задач на ЕГЭ не бывает

# Предположим, что в игре слишком маленькие шаги, большие числа или много ходов
# Значит рекурсия будет работать ОЧЕНЬ долго из-за большого количества вызовов функции
# Заметим, что для ответа нам обычно найти нужно минимальное или максимальное значение s
# Давайте воспользуемся генератором для 'ленивого' подсчёта

def f(s, m, p=0):  # p - флаг для №19
    if s >= 666: return m % 2 == 0
    if m == 0: return 0
    nx = (f(x, m-1) for x in (s+3, s*3, s+s*s))
    return any(nx) if p or m % 2 else all(nx)
    
print(next( s for s in range(1, 666) if f(s, 2, 1) ))

# Если нам нужно посчитать минимальное и максимальное значение s, то нужно сделать генератор с двух сторон
F = next( s for s in range(1, 666) if not f(s, 1) and f(s, 3) )
L = next( s for s in range(665, 0, -1) if not f(s, 1) and f(s, 3) )
print(F, L)

print(next( s for s in range(665, 0, -1) if not f(s, 2) and f(s, 4) ))

# Результат получился тот же, но сработало быстрее
# Если хотите потренироваться на сложной задаче, где эта оптимизация необходима, то вот интересная задача:
    # https://acmp.ru/asp/do/index.asp?main=topic&id_course=6&id_section=45&id_topic=437
