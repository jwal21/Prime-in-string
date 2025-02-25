# Cache of numbers that have already been checked for primality
# Dictionary (Hash Table)
import time
from math import isqrt


cached_primes: dict[int, bool] = {}

def is_prime(n: int) -> bool:
    
    if n in cached_primes:
        return cached_primes[n]
    if n < 2:
        cached_primes[n] = False
        return False
    if n in (2, 3):
        cached_primes[n] = True
        return True
    if n % 2 == 0 or n % 3 == 0:
        cached_primes[n] = False
        return False
    
    # Check divisibility using 6k ± 1 optimization
    max_prime = isqrt(n)
    mod = 5
    while mod <= max_prime:
        if n % mod == 0 or n % (mod + 2) == 0:
            cached_primes[n] = False
            return False
        mod += 6
    
    cached_primes[n] = True
    return True


def binary_to_decimal(string: str, max_num: int) -> str:
    
    if not all(s in '01' for s in string):
        return "Invalid binary string"

    seen_primes: set[int] = set()
    processed_numbers: set[int] = set()

    # Optimized substring generation
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            decimal_value = int(string[i:j], 2)
            
            if decimal_value in processed_numbers or decimal_value > max_num:
                continue
            
            processed_numbers.add(decimal_value)
            
            if is_prime(decimal_value):
                seen_primes.add(decimal_value)

    sorted_primes = sorted(seen_primes)
    count = len(sorted_primes)

    if count < 6:
        return f"\nThe binary string '{string}': \nContains {count} prime numbers: {sorted_primes}"
    else:
        return f"\nFor the binary string '{string}', the 3 smallest prime numbers are {sorted_primes[:3]} and the 3 largest prime numbers are {sorted_primes[-3:]}"
    

# Main function that runs the functions
if __name__ == '__main__':
    test_strings = [
        '0100001101001111', '01000011010011110100110101010000', '1111111111111111111111111111111111111111', 
        '010000110100111101001101010100000011000100111000', '01000011010011110100110101010000001100010011100000110001', 
        '0100001101001111010011010101000000110001001110000011000100111001', 
        '010000110100111101001101010100000011000100111000001100010011100100100001', 
        '01000011010011110100110101010000001100010011100000110001001110010010000101000001', 
        '0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100', 
        '010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011'
    ]
    
    max_nums = [
        999999, 999999, 999999, 999999999, 123456789012, 123456789012345, 
        123456789012345678, 1234567890123456789, 1234567890123456789, 12345678901234567890
    ]
    
    start = time.time()
    for string, max_num in zip(test_strings, max_nums):
        print(binary_to_decimal(string, max_num))
    end = time.time()

    print(f"\nTime taken: {end - start:} seconds")
