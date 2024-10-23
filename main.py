import timeit


# Жадібний алгоритм
def find_coins_greedy(amount, coins):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin

    return result


# Алгоритм динамічного програмування
def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


# Функція для вимірювання часу виконання
def measure_time(func, amount, coins):
    start_time = timeit.default_timer()
    result = func(amount, coins)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


# Тестування
if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amounts = [15, 40, 113, 175, 450, 1113]
    results = []

    for amount in amounts:
        print(f"\nAmount: {amount}")

        # Жадібний алгоритм
        greedy_result, greedy_time = measure_time(find_coins_greedy, amount, coins)
        print(f"Greedy algorithm result: {greedy_result}")
        print(f"Greedy algorithm execution time: {greedy_time} seconds")

        # Динамічне програмування
        dp_result, dp_time = measure_time(find_min_coins, amount, coins)
        print(f"Dynamic programming result: {dp_result}")
        print(f"Dynamic programming execution time: {dp_time} seconds")
