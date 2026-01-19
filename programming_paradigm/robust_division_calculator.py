# Implement a robust division calculator that robustly handles errors like zero division and non-numeric inputs. This will contain the divion logic while command line arguments will be handled in a separate file. 
def safe_divide(numerator, denominator):
	"""A function that performs divsion , handling zero-divion errors and non-numeric input."""
	try:
		num = float(numerator)
		den = float(denominator)
		result = num / den
	except ZeroDivisionError:
		return "Error: Cannot divide by zero."
	except ValueError:
		return "Error: Please enter numeric values only."
	else:
		return f"The result of the division is {result}"