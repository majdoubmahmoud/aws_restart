list1 = []  # List for prime numbers
list2 = []  # List for non-prime numbers

for i in range(2, 255):
    for j in range(2, i):
        if i % j == 0:
            list2.append(i)  # Add to non-prime list if a divisor is found
            break
    else:  # Executed only if the inner loop completes without breaks
        list1.append(i)  # Add to prime list if no divisors found

print("Prime numbers list:", list1)  # Print the prime numbers list