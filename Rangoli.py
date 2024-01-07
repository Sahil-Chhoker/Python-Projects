def rangoli(size):
    import string

    # Create a list of alphabet characters
    alphabet = string.ascii_lowercase

    # Create the upper half of the rangoli
    upper_half = []
    for i in range(size):
        line = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        upper_half.append((line.center(size*4 - 3, '-')))

    # Invert the upper half
    new_upper_half = []
    for j in reversed(range(0, len(upper_half))):
        new_upper_half.append(upper_half[j])

    # Create the lower half of the rangoli (excluding the center line)
    lower_half = new_upper_half[::-1][1:]

    # Combine upper and lower halves to form the complete rangoli
    full_rangoli = '\n'.join(new_upper_half + lower_half)

    return full_rangoli

# Sample Input
size = int(input().strip())

# Call the function with the sample input
result = rangoli(size)
print(result)
