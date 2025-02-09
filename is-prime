def is_prime(n) -> bool:
    
    # Checks if less than 2 as negative numbers, 0 and 1 are not prime
    if n < 2:
        return False
    
    # Checks if the number is 2 or 3 as these have no other factors
    if n in (2, 3):
        return True
    
    # Checks if even or divisible by 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for divisibility by 6k +/- 1 as all primes (besides 2 and 3) are either one less or one more than a multiple of 6
    mod = 5
    while mod ** 2 <= n:
        # Checks divisibility one less and one more than a multiple of 6
        if n % mod  == 0 or n % (mod + 2) == 0:
            return False
        mod += 6
    return True

# Run the function
if __name__ == '__main__':
    # Takes a binary string from the user
    string = (input("Enter a binary string: "))

    # Checks if the string is a valid binary string
    if not all(s in '01' for s in string):
            print("Invalid binary string")
            exit()
    
    # Set to store all the substrings of the binary string
    substrings = set()
    # Loop that will slice the string into all possible substrings and add them to the set
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.add(string[i:j])
    
    # Set to store the prime numbers we have identified, but not including duplicates
    seen_prime = set()

    # Converting each binary substring from the substrings set into decimal
    for substring in substrings: 
        decimal_value = int(substring, 2)

        # Checks if the decimal value is prime AND if it has not already been added to the seen_prime set, then prints the decimal value
        if is_prime(decimal_value) and decimal_value not in seen_prime:
           seen_prime.add(decimal_value)
           
    print(f"The binary string '{string}' \nContains {len(seen_prime)} prime numbers: {sorted(seen_prime)}")
