# Python Calculator

A comprehensive calculator application with both command-line and graphical user interfaces, featuring basic arithmetic operations, advanced mathematical functions, memory operations, and calculation history.

## Features

### Basic Operations
- **Addition (+)**: Add two numbers
- **Subtraction (-)**: Subtract one number from another
- **Multiplication (*)**: Multiply two numbers
- **Division (/)**: Divide one number by another (with zero-division protection)
- **Exponentiation (^, **)**: Raise a number to a power

### Advanced Functions
- **Square Root (√, sqrt)**: Calculate square root of a number
- **Factorial (!)**: Calculate factorial of integers
- **Trigonometric Functions**: sin, cos, tan (supports both radians and degrees)
- **Logarithms**: Natural log (ln) and logarithm with custom base
- **Percentage**: Calculate percentage of a value
- **Constants**: π (pi) and e (Euler's number)

### Memory Operations
- **Memory Store (MS)**: Store a value in memory
- **Memory Recall (MR)**: Retrieve stored value from memory
- **Memory Clear (MC)**: Clear the memory
- **Memory Add (M+)**: Add a value to the current memory value

### Additional Features
- **Expression Evaluation**: Evaluate complex mathematical expressions
- **Calculation History**: Track and review previous calculations
- **Error Handling**: Comprehensive error checking and user-friendly error messages
- **Keyboard Support**: Full keyboard input support in GUI mode

## Files

- `calculator.py` - Core calculator class and command-line interface
- `calculator_gui.py` - Graphical user interface using tkinter
- `test_calculator.py` - Test suite demonstrating all features
- `README.md` - This documentation file

## Usage

### Command-Line Interface

Run the calculator in interactive mode:

```bash
python calculator.py
```

#### Examples:
```
Enter calculation: 2 + 3 * 4
Result: 14

Enter calculation: sqrt(16) + 2^3
Result: 12.0

Enter calculation: sin(π/2)
Result: 1.0

Enter calculation: history
Calculation History:
  1. 2+3*4 = 14
  2. sqrt(16)+2**3 = 12.0
  3. sin(π/2) = 1.0
```

#### Special Commands:
- `history` - Show calculation history
- `clear` - Clear history
- `ms <value>` - Store value in memory
- `mr` - Recall memory value
- `mc` - Clear memory
- `m+ <value>` - Add value to memory
- `quit` or `q` - Exit calculator

### Graphical User Interface

Launch the GUI calculator:

```bash
python calculator_gui.py
```

The GUI features:
- Large, easy-to-read display
- Memory indicator
- Standard calculator button layout
- Additional function buttons (sin, cos, tan, log, π, e)
- Calculation history panel
- Keyboard support for all operations
- Modern dark theme

#### Keyboard Shortcuts:
- **Numbers (0-9)**: Input numbers
- **Operators (+, -, *, /)**: Mathematical operations
- **Enter or =**: Calculate result
- **C**: Clear display
- **Backspace**: Delete last character
- **Escape**: Clear display

### Running Tests

Execute the test suite to see all features in action:

```bash
python test_calculator.py
```

## Examples

### Basic Calculations
```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)          # 8
result = calc.multiply(4, 6)     # 24
result = calc.divide(15, 3)      # 5.0

# Advanced functions
result = calc.square_root(16)    # 4.0
result = calc.factorial(5)       # 120
result = calc.sin(math.pi/2)     # 1.0
```

### Expression Evaluation
```python
calc = Calculator()

# Complex expressions
result = calc.evaluate_expression("2 + 3 * 4")        # 14
result = calc.evaluate_expression("sqrt(16) + 2^3")   # 12.0
result = calc.evaluate_expression("sin(π/2) + cos(0)") # 2.0
```

### Memory Operations
```python
calc = Calculator()

calc.memory_store(42)    # Store 42 in memory
value = calc.memory_recall()  # Retrieve 42
calc.memory_add(8)       # Memory now contains 50
calc.memory_clear()      # Memory reset to 0
```

## Error Handling

The calculator includes comprehensive error handling:

- **Division by zero**: Prevents division by zero with clear error message
- **Invalid inputs**: Validates all inputs and provides helpful error messages
- **Mathematical errors**: Handles cases like square root of negative numbers
- **Expression parsing**: Safely evaluates expressions with error reporting

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- math module (built-in)
- re module (built-in)

## Installation

1. Clone or download the calculator files
2. Ensure Python 3.6+ is installed
3. Run any of the calculator files directly:

```bash
python calculator.py        # Command-line version
python calculator_gui.py    # GUI version
python test_calculator.py   # Run tests
```

## License

This project is open source and available under the MIT License. 

