def FizzBuzz(start, finish):
    result = []
    # We use finish + 1 because range() is exclusive of the stop value
    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
