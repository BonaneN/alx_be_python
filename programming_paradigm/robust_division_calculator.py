def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
    except ValueError:
        return "Error: Both numerator and denominator must be numbers."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result of {num} divided by {denom} is {result}."