def fastPower(a, n):
    """Compute a^n using fast exponentiation (recursive).

    Args:
        a (float): The base.
        n (int): The exponent (non-negative integer).
    Returns:
        float: The result of a raised to the power of n
    """
    if n == 0:
        return 1
    
    subProblem = fastPower(a, n // 2)
    subProblemSquared = subProblem * subProblem
    if n % 2 == 0:
        return subProblemSquared
    else:
        return a * subProblemSquared
    
# Example usage:
if __name__ == "__main__":
    base = 2
    exponent = 10
    result = fastPower(base, exponent)
    print(f"{base} to the power of {exponent} is {result}")