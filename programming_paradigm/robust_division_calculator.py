def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
    except ValueError:
        return "Error: Both numerator and denominator must be numbers."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result of {num} divided by {denom} is {result}."