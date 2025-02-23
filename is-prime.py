# Cache of numbers that have already been checked for primality
# Dictionary (Hash Table)
cached_nums: dict[int, bool] = {}

# Function that checks if a number is prime
def is_prime(n: int) -> bool:
    
    # Checks if less than 2 as negative numbers, 0 and 1 are not prime
    if n < 2:
        cached_nums[n] = False
        return False
    
    # Checks if the number is 2 or 3 as these have no other factors
    if n in (2, 3):
        cached_nums[n] = True
        return True
    
    # Checks if even or divisible by 3
    if n % 2 == 0 or n % 3 == 0:
        cached_nums[n] = False
        return False
    
    # Check for divisibility by 6k +/- 1 as all primes
    # (besides 2 and 3) are either one less or one more than a multiple of 6
    
    mod: int = 5
    while mod ** 2 <= n:
        # Checks divisibility one less and one more than a multiple of 6
        if n % mod  == 0 or n % (mod + 2) == 0:
            cached_nums[n] = False
            return False
        mod += 6
    
    cached_nums[n] = True
    return True


# Function that gets all substrings of a binary string and converts into decimal and finally checks if the number 'is_prime'.
def binary_to__decimal(string: str, max_num: int) -> str:
    # Checks if the string is a valid binary string
    if not all(s in '01' for s in string):
        return "Invalid binary string"
    
    # Set to store all the substrings of the binary string
    substrings: set[str] = set()
    # Loop that will slice the string into all possible substrings and add them to the set
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.add(string[i:j])
    
    # Set to store the prime numbers we have identified, but not including duplicates
    seen_prime: set[int] = set()

    # Converting each binary substring from the substrings set into decimal
    for substring in substrings: 
        decimal_value = int(substring, 2)

        # Checks if the decimal value is prime AND if it has not already been added to the seen_prime set, then prints the decimal value
        if is_prime(decimal_value) and decimal_value not in seen_prime:
            if decimal_value > max_num:
                break
            seen_prime.add(decimal_value)

    if len(seen_prime) < 6:
        return f"\nThe binary string '{string}': \nContains {len(seen_prime)} prime numbers: {sorted(seen_prime)}"
    else:
        return f"\nFor the binary string '{string}', the 3 smallest prime numbers are {sorted(seen_prime)[:3]} and the 3 largest prime numbers are {sorted(seen_prime)[-3:]}"

# Main function that runs the functions
if __name__ == '__main__':
    
    # Takes a binary string from the user
    #test_strings = ['0100001101001111', '01000011010011110100110101010000', '1111111111111111111111111111111111111111', '010000110100111101001101010100000011000100111000', 
    #'01000011010011110100110101010000001100010011100000110001', '0100001101001111010011010101000000110001001110000011000100111001', '010000110100111101001101010100000011000100111000001100010011100100100001', 
    #'01000011010011110100110101010000001100010011100000110001001110010010000101000001', '0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100', 
    #'010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011', ]
    
    #max_nums = [999999, 999999, 999999, 999999999, 123456789012, 123456789012345, 123456789012345678, 1234567890123456789, 1234567890123456789, 12345678901234567890]
    
    #for string, max_num in zip(test_strings, max_nums):
   
    string = input("Enter a binary string: ")
    # Takes the maximum cut off value for the prime numbers
    max_num = int( input ("Enter the maximum value prime number: "))
    print(binary_to__decimal(string, max_num))
