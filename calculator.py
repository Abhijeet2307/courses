import math
import re
from typing import Union, Any

class Calculator:
    """A comprehensive calculator class with basic and advanced operations."""
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract second number from first."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide first number by second."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result
    
    def power(self, a: float, b: float) -> float:
        """Raise first number to the power of second."""
        result = a ** b
        self._add_to_history(f"{a} ^ {b} = {result}")
        return result
    
    def square_root(self, a: float) -> float:
        """Calculate square root."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(a)
        self._add_to_history(f"√{a} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of a number."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers")
        result = math.factorial(n)
        self._add_to_history(f"{n}! = {result}")
        return result
    
    def sin(self, x: float, degrees: bool = False) -> float:
        """Calculate sine of angle."""
        if degrees:
            x = math.radians(x)
        result = math.sin(x)
        unit = "°" if degrees else "rad"
        self._add_to_history(f"sin({x}{unit}) = {result}")
        return result
    
    def cos(self, x: float, degrees: bool = False) -> float:
        """Calculate cosine of angle."""
        if degrees:
            x = math.radians(x)
        result = math.cos(x)
        unit = "°" if degrees else "rad"
        self._add_to_history(f"cos({x}{unit}) = {result}")
        return result
    
    def tan(self, x: float, degrees: bool = False) -> float:
        """Calculate tangent of angle."""
        if degrees:
            x = math.radians(x)
        result = math.tan(x)
        unit = "°" if degrees else "rad"
        self._add_to_history(f"tan({x}{unit}) = {result}")
        return result
    
    def log(self, x: float, base: float = math.e) -> float:
        """Calculate logarithm."""
        if x <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base")
        
        if base == math.e:
            result = math.log(x)
            self._add_to_history(f"ln({x}) = {result}")
        else:
            result = math.log(x, base)
            self._add_to_history(f"log{base}({x}) = {result}")
        return result
    
    def percentage(self, value: float, percent: float) -> float:
        """Calculate percentage of a value."""
        result = (percent / 100) * value
        self._add_to_history(f"{percent}% of {value} = {result}")
        return result
    
    def evaluate_expression(self, expression: str) -> float:
        """Evaluate a mathematical expression safely."""
        # Remove whitespace
        expression = expression.replace(" ", "")
        
        # Replace common mathematical symbols
        expression = expression.replace("^", "**")
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))
        
        # Add support for common functions
        expression = re.sub(r'sin\(([^)]+)\)', r'math.sin(\1)', expression)
        expression = re.sub(r'cos\(([^)]+)\)', r'math.cos(\1)', expression)
        expression = re.sub(r'tan\(([^)]+)\)', r'math.tan(\1)', expression)
        expression = re.sub(r'sqrt\(([^)]+)\)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'log\(([^)]+)\)', r'math.log(\1)', expression)
        
        try:
            # Use eval with restricted globals for safety
            allowed_names = {
                "__builtins__": {},
                "math": math,
                "abs": abs,
                "round": round,
                "min": min,
                "max": max,
            }
            result = eval(expression, allowed_names)
            self._add_to_history(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
    
    def memory_store(self, value: float) -> None:
        """Store value in memory."""
        self.memory = value
        self._add_to_history(f"Stored {value} in memory")
    
    def memory_recall(self) -> float:
        """Recall value from memory."""
        self._add_to_history(f"Recalled {self.memory} from memory")
        return self.memory
    
    def memory_clear(self) -> None:
        """Clear memory."""
        self.memory = 0
        self._add_to_history("Memory cleared")
    
    def memory_add(self, value: float) -> None:
        """Add value to memory."""
        self.memory += value
        self._add_to_history(f"Added {value} to memory (now {self.memory})")
    
    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
    
    def _add_to_history(self, operation: str) -> None:
        """Add operation to history."""
        self.history.append(operation)
        if len(self.history) > 100:  # Keep only last 100 operations
            self.history.pop(0)


def main():
    """Command-line interface for the calculator."""
    calc = Calculator()
    
    print("=" * 50)
    print("           Python Calculator")
    print("=" * 50)
    print("\nAvailable operations:")
    print("• Basic: +, -, *, /, ** (or ^)")
    print("• Functions: sin, cos, tan, sqrt, log")
    print("• Constants: π (pi), e")
    print("• Memory: ms (store), mr (recall), mc (clear), m+ (add)")
    print("• Special: history, clear, quit")
    print("\nExamples:")
    print("  2 + 3 * 4")
    print("  sin(π/2)")
    print("  sqrt(16)")
    print("  log(10)")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nEnter calculation: ").strip()
            
            if not user_input:
                continue
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            elif user_input.lower() == 'history':
                history = calc.get_history()
                if history:
                    print("\nCalculation History:")
                    for i, operation in enumerate(history[-10:], 1):  # Show last 10
                        print(f"{i:2d}. {operation}")
                else:
                    print("No history available.")
                continue
            elif user_input.lower() == 'clear':
                calc.clear_history()
                print("History cleared.")
                continue
            elif user_input.lower() == 'mc':
                calc.memory_clear()
                print("Memory cleared.")
                continue
            elif user_input.lower() == 'mr':
                result = calc.memory_recall()
                print(f"Memory: {result}")
                continue
            elif user_input.lower().startswith('ms '):
                try:
                    value = float(user_input[3:])
                    calc.memory_store(value)
                    print(f"Stored {value} in memory.")
                except ValueError:
                    print("Invalid value for memory store.")
                continue
            elif user_input.lower().startswith('m+ '):
                try:
                    value = float(user_input[3:])
                    calc.memory_add(value)
                    print(f"Added {value} to memory (now {calc.memory}).")
                except ValueError:
                    print("Invalid value for memory add.")
                continue
            
            # Evaluate mathematical expression
            result = calc.evaluate_expression(user_input)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()