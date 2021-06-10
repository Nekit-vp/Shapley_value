function = {
    '1': 20,
    '2': 30,
    '3': 0,
    '12': 80,
    '13': 50,
    '23': 65,
    '123': 100
}

N_COUNT = 3


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


def player_profit(coalition, player):
    with_player = function.get(coalition)
    without_player = function.get(coalition.replace(str(player), ''), 0)
    return with_player - without_player


def number_of_inclusions(n, coalition):
    fact_nk = fac(N_COUNT - len(coalition))
    fact_k1 = fac(len(coalition) - 1)
    fact_n = fac(N_COUNT)
    return (fact_nk * fact_k1) / fact_n


vector = []

for i in range(N_COUNT):
    value = 0
    player = i + 1

    for key in function.keys():
        if str(player) in key:
            value += number_of_inclusions(N_COUNT, key) * player_profit(key, player)
    vector.append(value)

print("Вектор Шепли: " + str(vector))
