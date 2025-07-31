#!/usr/bin/env python3
"""
Test script to demonstrate calculator functionality.
"""

from calculator import Calculator
import math


def test_basic_operations():
    """Test basic arithmetic operations."""
    calc = Calculator()
    
    print("=== Basic Operations ===")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2^8 = {calc.power(2, 8)}")
    print()


def test_advanced_functions():
    """Test advanced mathematical functions."""
    calc = Calculator()
    
    print("=== Advanced Functions ===")
    print(f"√16 = {calc.square_root(16)}")
    print(f"5! = {calc.factorial(5)}")
    print(f"sin(π/2) = {calc.sin(math.pi/2)}")
    print(f"cos(0) = {calc.cos(0)}")
    print(f"tan(π/4) = {calc.tan(math.pi/4)}")
    print(f"ln(e) = {calc.log(math.e)}")
    print(f"log₁₀(100) = {calc.log(100, 10)}")
    print(f"25% of 200 = {calc.percentage(200, 25)}")
    print()


def test_expression_evaluation():
    """Test expression evaluation."""
    calc = Calculator()
    
    print("=== Expression Evaluation ===")
    expressions = [
        "2 + 3 * 4",
        "(5 + 3) * 2",
        "sqrt(16) + 2^3",
        "sin(π/2) + cos(0)",
        "log(10) + sqrt(9)",
        "2 * π * 5",  # Circumference formula
        "(1 + sqrt(5)) / 2"  # Golden ratio approximation
    ]
    
    for expr in expressions:
        try:
            result = calc.evaluate_expression(expr)
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"{expr} -> Error: {e}")
    print()


def test_memory_functions():
    """Test memory operations."""
    calc = Calculator()
    
    print("=== Memory Functions ===")
    
    # Store a value
    calc.memory_store(42)
    print(f"Stored 42 in memory")
    
    # Recall value
    recalled = calc.memory_recall()
    print(f"Recalled from memory: {recalled}")
    
    # Add to memory
    calc.memory_add(8)
    print(f"Added 8 to memory")
    
    # Recall again
    recalled = calc.memory_recall()
    print(f"Memory now contains: {recalled}")
    
    # Clear memory
    calc.memory_clear()
    recalled = calc.memory_recall()
    print(f"After clearing, memory contains: {recalled}")
    print()


def test_error_handling():
    """Test error handling."""
    calc = Calculator()
    
    print("=== Error Handling ===")
    
    test_cases = [
        ("Division by zero", lambda: calc.divide(10, 0)),
        ("Square root of negative", lambda: calc.square_root(-4)),
        ("Factorial of negative", lambda: calc.factorial(-5)),
        ("Log of zero", lambda: calc.log(0)),
        ("Invalid expression", lambda: calc.evaluate_expression("2 + + 3"))
    ]
    
    for description, operation in test_cases:
        try:
            result = operation()
            print(f"{description}: {result}")
        except Exception as e:
            print(f"{description}: Error caught - {e}")
    print()


def test_history():
    """Test calculation history."""
    calc = Calculator()
    
    print("=== History Tracking ===")
    
    # Perform some calculations
    calc.add(5, 3)
    calc.multiply(4, 6)
    calc.square_root(25)
    calc.evaluate_expression("2^3 + 1")
    
    # Display history
    history = calc.get_history()
    print("Calculation History:")
    for i, operation in enumerate(history, 1):
        print(f"  {i}. {operation}")
    
    print(f"\nTotal operations: {len(history)}")
    print()


def main():
    """Run all tests."""
    print("Calculator Test Suite")
    print("=" * 50)
    
    test_basic_operations()
    test_advanced_functions()
    test_expression_evaluation()
    test_memory_functions()
    test_error_handling()
    test_history()
    
    print("Tests completed!")
    print("\nTo use the calculator interactively:")
    print("  python calculator.py          # Command-line interface")
    print("  python calculator_gui.py      # Graphical interface")


if __name__ == "__main__":
    main()