from itertools import permutations
from functools import reduce as fold
from time import time

start = time()

def get_all_permutations(string: str) -> list:
    # itertools coming in clutch
    all_permutations = [
        "".join(i) for i in list(permutations(string, len(string)))
    ]
    return all_permutations


def product_of_string(string: str) -> int:
    def _times(num1, num2):
        return num1 * num2
    digits = [int(string[i]) for i in range(len(string))]
    return fold(_times, digits)


perms = get_all_permutations("12345678")

counter = 0
for string in perms:
    left = string[:5]
    right = string[5:]
    if product_of_string(left) < product_of_string(right):
        counter += 1
end = time()
print(f"Time taken: {end - start}s")
print(f"Result: {counter / len(perms)}")