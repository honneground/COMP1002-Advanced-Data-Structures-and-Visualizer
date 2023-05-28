def CFDD(n, x, k):
    """
    Calculates a value based on the input parameters n, x, and k.

    Args:
        n (int): A non-negative integer representing a value for computation.
        x (int): An integer representing the dividend.
        k (int): An integer representing the divisor.

    Returns:
        float: The result of the computation, which is obtained by dividing the factorial of n by the difference between x and k.

    Notes:
        - If n or x is less than k, the function returns -1 to indicate an invalid input.
        - If the difference between x and k is equal to 0, the function returns None.
        - If invalid input values for n, x, and k pass to the function (eg. string or char inputs), the function returns None.
        - The function uses a recursive wapper function to calculate the factorial of n.
    """

    def factorial(num): # Nested recursive wrapper function that calculates the factorial of a given number num
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    try:  
        if n < 0 or x < k:
            return -1  # Invalid input
        if x - k < 0:
            return 0 # The code here will never be executed as the two if statement above is equivalent.
    
        somevalue = factorial(n)
        result = somevalue / (x - k)
    
    except TypeError: # Exception handling for invalid input data types
        result = None
    except ZeroDivisionError: # Exception handling for dedivide by zero
        result = None
    except Exception as e: # Exception handling for any other unknown errors
        print(e)
        result = None

    return result

def main():
    # Test cases
    print("Test Case 1: Valid inputs")
    result = CFDD(5, 8, 2)
    print("Expected Result: 20.0")
    print("Actual Result: ", result, "\n")

    print("Test Case 2: Invalid inputs value (n < 0)")
    result = CFDD(-2, 8, 2)
    print("Expected Result: -1")
    print("Actual Result: ", result, "\n")

    print("Test Case 3: Invalid inputs value (x < k) aka. (x - k < 0)")
    result = CFDD(5, 2, 8)
    print("Expected Result: -1")
    print("Actual Result: ", result, "\n")

    print("Test Case 4: n = 0")
    result = CFDD(0, 2, 1)
    print("Expected Result: 1.0")
    print("Actual Result: ", result, "\n")

    print("Test Case 5: n = 1")
    result = CFDD(1, 2, 1)
    print("Expected Result: 1.0")
    print("Actual Result: ", result, "\n")

    print("Test Case 6: Zero division (x = k) aka. (x - k = 0)")
    result = CFDD(5, 10, 10)
    print("Expected Result: None")
    print("Actual Result: ", result, "\n")

    print("Test Case 7: Invalid inputs data type")
    result = CFDD("five", "two", "A")
    print("Expected Result: None")
    print("Actual Result: ", result, "\n")

if __name__ == '__main__':
    main()
