# Type: Optimised Solution 1
import time
from math import isqrt

# Dictionary to store previously checked numbers
cached_nums: dict[int, bool] = {}

# Function that checks primality using the 6k ± 1 method
def is_prime(n: int) -> bool:
    # Check if the number is already in the cache
    if n in cached_nums:
        return cached_nums[n]
    
    # Perform other checks if number not in cache
    if n < 2:
        cached_nums[n] = False
        return False
    if n in (2, 3):
        cached_nums[n] = True
        return True
    if n % 2 == 0 or n % 3 == 0:
        cached_nums[n] = False
        return False
    
    # Check primality using 6k ± 1 
    # isqrt will return the square root of n rounded down to the nearest integer
    max_prime = isqrt(n)       
    mod = 5
    while mod <= max_prime:
        if n % mod == 0 or n % (mod + 2) == 0:
            cached_nums[n] = False
            return False
        mod += 6
    
    cached_nums[n] = True
    return True


# Function that gets all substrings of a binary string and converts into decimal and finally checks if the number 'is_prime'.
def binary_to_decimal(string: str, max_num: int) -> str:
    # Checks if the string is a valid binary string
    if not all(s in '01' for s in string):
        return "Invalid binary string"

    # Set to store the prime numbers
    seen_primes: set[int] = set()
    # Set to store the non-prime numbers
    processed_numbers: set[int] = set()

    # Optimized substring generation, performs substring extraction and prime check consecutively
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            decimal_value = int(string[i:j], 2)
            
            # Check if the number is already processed or greater than the max number
            if decimal_value in processed_numbers or decimal_value > max_num:
                continue
            
            processed_numbers.add(decimal_value)
            
            if is_prime(decimal_value):
                seen_primes.add(decimal_value)

    # Sort the prime numbers into a list
    sorted_primes = sorted(seen_primes)
    count = len(sorted_primes)

    if count < 6:
        return f"\nThe binary string: '{string}': \nContains {count} prime numbers: {sorted_primes}"
    else:
        return f"\nThe binary string: '{string}': \nContains {count} prime numbers. The smallest 3 prime numbers are {sorted_primes[:3]} and the 3 largest prime numbers are {sorted_primes[-3:]}"
    


# Main function that runs the functions in 10 test cases
if __name__ == "__main__":
    test_cases = {
        'Test1:': ('0100001101001111', 999999),
        'Test2:': ('01000011010011110100110101010000', 999999),
        'Test3:': ('1111111111111111111111111111111111111111', 999999),
        'Test4:': ('010000110100111101001101010100000011000100111000', 999999999),
        'Test5:': ('01000011010011110100110101010000001100010011100000110001', 123456789012),
        'Test6:': ('0100001101001111010011010101000000110001001110000011000100111001', 123456789012345),
        'Test7:': ('010000110100111101001101010100000011000100111000001100010011100100100001', 123456789012345678),
        'Test8:': ('01000011010011110100110101010000001100010011100000110001001110010010000101000001', 1234567890123456789),
        'Test9:': ('0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100', 1234567890123456789),
        'Test10:': ('010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011', 12345678901234567890),
    }
    
    start_total = time.time()
    for test_name, (string, max_num) in test_cases.items():
        start = time.time()
        print(test_name)
        print(binary_to_decimal(string, max_num))
        end = time.time()
        print(f"Time taken: {end - start:} seconds\n")
    
    end_total = time.time()
    print(f"Total time taken: {end_total - start_total:} seconds")