def power(a, N):
    """Compute a to the power of N using recursion.

    Args:
        a (float): The base number.
        N (int): The exponent (non-negative integer).

    Returns:
        float: The result of a raised to the power of N.
    """
    if N == 0:
        return 1
    else:
        return a * power(a, N - 1)
    
# Example usage:
if __name__ == "__main__":
    base = 2
    exponent = 5
    result = power(base, exponent)
    print(f"{base} to the power of {exponent} is {result}") 