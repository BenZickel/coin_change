def coin_change(coins, amount):
    '''
    Return amount change from given coins.
    '''
    if len(coins) == 0:
        return {} if amount == 0 else None
    max_coin = max(coins)
    max_count = min(coins[max_coin], int(amount / max_coin))
    if max_count * max_coin == amount: return {max_coin: max_count}
    for count in range(max_count, -1, -1):
        solution = coin_change({coin:coins[coin] for coin in coins if coin != max_coin}, amount - count * max_coin)
        if solution is not None:
            solution[max_coin] = count
            return solution
    return None

# Example
coins = {5: 1,
         2: 4}

for amount in [7, 8, 9, 10, 11]:
    solution = coin_change(coins, amount)
    print('For amount {} the solution is {}'.format(amount, solution))
