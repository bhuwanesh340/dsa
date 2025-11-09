def spell(number):
    """Convert a non-negative integer to its English words representation using recursion.

    Args:
        number (int): A non-negative integer to convert.
    Returns:
        str: The English words representation of the number.
    """

    spell_arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    if number == 0:
        return
    last_digit = number % 10
    spell(number // 10)
    print(spell_arr[last_digit], end=' ')

# Example usage:
if __name__ == "__main__":
    num = 123045
    print(f"The number {num} in words is: ", end='')
    spell(num)
    print()  # for newline after the output
