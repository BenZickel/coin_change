#
# Solution given by ChatGPT based on the conversation at https://chat.openai.com/share/1f3302ef-9ad6-4b75-b995-4cda7c5dfa86
#

def get_combination(coins_counts, target_amount):
    # Sort coins in descending order
    sorted_coins = sorted(coins_counts.keys(), reverse=True)

    # Initialize the result dictionary
    result = {}

    # Recursive function to find a valid combination
    def find_combination(current_coin_index, remaining_amount):
        if remaining_amount == 0:
            return True
        if current_coin_index == len(sorted_coins):
            return False

        current_coin = sorted_coins[current_coin_index]
        coin_count = coins_counts[current_coin]

        # Try different counts of the current coin
        for count in range(min(remaining_amount // current_coin, coin_count) + 1):
            result[current_coin] = count
            if find_combination(current_coin_index + 1, remaining_amount - count * current_coin):
                return True

        # If no valid combination found with the current coin, backtrack
        del result[current_coin]
        return False

    if find_combination(0, target_amount):
        return result
    else:
        return None

# Example usage:
coins_counts_input = {5: 1, 2: 5}
target_amount_input = 8

result_combination = get_combination(coins_counts_input, target_amount_input)

if result_combination is not None:
    print("Valid combination found:")
    print(result_combination)
else:
    print("No valid combination found.")
