import tkinter as tk
from tkinter import ttk, messagebox
import math
from calculator import Calculator


class CalculatorGUI:
    """A modern GUI calculator using tkinter."""
    
    def __init__(self):
        self.calc = Calculator()
        self.root = tk.Tk()
        self.setup_window()
        self.create_variables()
        self.create_widgets()
        self.setup_layout()
        self.bind_keyboard()
    
    def setup_window(self):
        """Configure the main window."""
        self.root.title("Python Calculator")
        self.root.geometry("400x600")
        self.root.resizable(True, True)
        self.root.configure(bg='#2b2b2b')
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Display.TEntry', 
                       fieldbackground='#1e1e1e', 
                       foreground='white',
                       borderwidth=2,
                       font=('Arial', 16))
        
        style.configure('Calc.TButton',
                       font=('Arial', 12, 'bold'),
                       padding=10)
        
        style.configure('Number.TButton',
                       background='#404040',
                       foreground='white')
        
        style.configure('Operator.TButton',
                       background='#ff9500',
                       foreground='white')
        
        style.configure('Function.TButton',
                       background='#505050',
                       foreground='white')
    
    def create_variables(self):
        """Create tkinter variables."""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.memory_var = tk.StringVar()
        self.memory_var.set("Memory: 0")
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Memory display
        memory_frame = ttk.Frame(main_frame)
        memory_frame.pack(fill=tk.X, pady=(0, 5))
        
        self.memory_label = ttk.Label(memory_frame, textvariable=self.memory_var,
                                     font=('Arial', 10), foreground='#888888')
        self.memory_label.pack(anchor=tk.E)
        
        # Display
        self.display = ttk.Entry(main_frame, textvariable=self.display_var,
                                style='Display.TEntry', justify=tk.RIGHT,
                                state='readonly', font=('Arial', 20))
        self.display.pack(fill=tk.X, pady=(0, 10), ipady=10)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid weights
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        
        # Button layout
        buttons = [
            # Row 0: Function buttons
            [('MC', self.memory_clear, 'Function.TButton'), 
             ('MR', self.memory_recall, 'Function.TButton'),
             ('MS', self.memory_store, 'Function.TButton'), 
             ('M+', self.memory_add, 'Function.TButton')],
            
            # Row 1: Clear and functions
            [('C', self.clear, 'Function.TButton'), 
             ('±', self.plus_minus, 'Function.TButton'),
             ('√', lambda: self.function_button('sqrt'), 'Function.TButton'), 
             ('÷', lambda: self.operator_button('/'), 'Operator.TButton')],
            
            # Row 2: Numbers and operators
            [('7', lambda: self.number_button('7'), 'Number.TButton'), 
             ('8', lambda: self.number_button('8'), 'Number.TButton'),
             ('9', lambda: self.number_button('9'), 'Number.TButton'), 
             ('×', lambda: self.operator_button('*'), 'Operator.TButton')],
            
            # Row 3
            [('4', lambda: self.number_button('4'), 'Number.TButton'), 
             ('5', lambda: self.number_button('5'), 'Number.TButton'),
             ('6', lambda: self.number_button('6'), 'Number.TButton'), 
             ('-', lambda: self.operator_button('-'), 'Operator.TButton')],
            
            # Row 4
            [('1', lambda: self.number_button('1'), 'Number.TButton'), 
             ('2', lambda: self.number_button('2'), 'Number.TButton'),
             ('3', lambda: self.number_button('3'), 'Number.TButton'), 
             ('+', lambda: self.operator_button('+'), 'Operator.TButton')],
            
            # Row 5
            [('0', lambda: self.number_button('0'), 'Number.TButton'), 
             ('.', lambda: self.number_button('.'), 'Number.TButton'),
             ('=', self.equals_button, 'Operator.TButton'), 
             ('^', lambda: self.operator_button('**'), 'Operator.TButton')]
        ]
        
        # Create buttons
        for row, button_row in enumerate(buttons):
            for col, (text, command, style) in enumerate(button_row):
                btn = ttk.Button(button_frame, text=text, command=command,
                               style=style)
                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        
        # Function buttons frame
        func_frame = ttk.Frame(main_frame)
        func_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Additional function buttons
        functions = [
            ('sin', lambda: self.function_button('sin')),
            ('cos', lambda: self.function_button('cos')),
            ('tan', lambda: self.function_button('tan')),
            ('log', lambda: self.function_button('log')),
            ('π', lambda: self.number_button(str(math.pi))),
            ('e', lambda: self.number_button(str(math.e)))
        ]
        
        for i, (text, command) in enumerate(functions):
            btn = ttk.Button(func_frame, text=text, command=command,
                           style='Function.TButton', width=6)
            btn.grid(row=0, column=i, sticky='ew', padx=1)
            func_frame.grid_columnconfigure(i, weight=1)
        
        # History frame
        history_frame = ttk.LabelFrame(main_frame, text="History", padding=5)
        history_frame.pack(fill=tk.X, pady=(10, 0))
        
        # History listbox with scrollbar
        history_container = ttk.Frame(history_frame)
        history_container.pack(fill=tk.BOTH, expand=True)
        
        self.history_listbox = tk.Listbox(history_container, height=4,
                                         bg='#1e1e1e', fg='white',
                                         selectbackground='#404040',
                                         font=('Arial', 9))
        scrollbar = ttk.Scrollbar(history_container, orient=tk.VERTICAL,
                                command=self.history_listbox.yview)
        self.history_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # History buttons
        hist_btn_frame = ttk.Frame(history_frame)
        hist_btn_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Button(hist_btn_frame, text="Clear History",
                  command=self.clear_history).pack(side=tk.LEFT)
        ttk.Button(hist_btn_frame, text="Use Result",
                  command=self.use_history_result).pack(side=tk.RIGHT)
        
        self.current_input = ""
        self.operator = None
        self.operand = None
    
    def setup_layout(self):
        """Setup the layout and styling."""
        pass
    
    def bind_keyboard(self):
        """Bind keyboard events."""
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
    
    def on_key_press(self, event):
        """Handle keyboard input."""
        key = event.char
        
        if key.isdigit() or key == '.':
            self.number_button(key)
        elif key in '+-*/':
            self.operator_button(key)
        elif key == '=' or key == '\r':
            self.equals_button()
        elif key == '\x08':  # Backspace
            self.backspace()
        elif key.lower() == 'c':
            self.clear()
        elif key == '\x1b':  # Escape
            self.clear()
    
    def number_button(self, num):
        """Handle number button press."""
        current = self.display_var.get()
        if current == "0" or current == "Error":
            self.display_var.set(num)
        else:
            self.display_var.set(current + num)
    
    def operator_button(self, op):
        """Handle operator button press."""
        current = self.display_var.get()
        if current != "Error":
            self.current_input = current + op
            self.display_var.set("0")
    
    def function_button(self, func):
        """Handle function button press."""
        current = self.display_var.get()
        if current != "Error":
            self.current_input = f"{func}({current})"
            self.equals_button()
    
    def equals_button(self):
        """Handle equals button press."""
        try:
            current = self.display_var.get()
            if self.current_input:
                expression = self.current_input + current
            else:
                expression = current
            
            result = self.calc.evaluate_expression(expression)
            self.display_var.set(str(result))
            self.update_history()
            self.current_input = ""
            
        except Exception as e:
            self.display_var.set("Error")
            messagebox.showerror("Calculation Error", str(e))
    
    def clear(self):
        """Clear the display and reset."""
        self.display_var.set("0")
        self.current_input = ""
        self.operator = None
        self.operand = None
    
    def backspace(self):
        """Remove last character."""
        current = self.display_var.get()
        if len(current) > 1:
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")
    
    def plus_minus(self):
        """Toggle sign of current number."""
        current = self.display_var.get()
        try:
            value = float(current)
            self.display_var.set(str(-value))
        except ValueError:
            pass
    
    def memory_store(self):
        """Store current value in memory."""
        try:
            value = float(self.display_var.get())
            self.calc.memory_store(value)
            self.memory_var.set(f"Memory: {value}")
            self.update_history()
        except ValueError:
            messagebox.showerror("Error", "Invalid value for memory")
    
    def memory_recall(self):
        """Recall value from memory."""
        value = self.calc.memory_recall()
        self.display_var.set(str(value))
        self.update_history()
    
    def memory_clear(self):
        """Clear memory."""
        self.calc.memory_clear()
        self.memory_var.set("Memory: 0")
        self.update_history()
    
    def memory_add(self):
        """Add current value to memory."""
        try:
            value = float(self.display_var.get())
            self.calc.memory_add(value)
            self.memory_var.set(f"Memory: {self.calc.memory}")
            self.update_history()
        except ValueError:
            messagebox.showerror("Error", "Invalid value for memory")
    
    def update_history(self):
        """Update the history display."""
        history = self.calc.get_history()
        self.history_listbox.delete(0, tk.END)
        for operation in history[-10:]:  # Show last 10 operations
            self.history_listbox.insert(tk.END, operation)
        self.history_listbox.see(tk.END)
    
    def clear_history(self):
        """Clear calculation history."""
        self.calc.clear_history()
        self.history_listbox.delete(0, tk.END)
    
    def use_history_result(self):
        """Use selected history result."""
        selection = self.history_listbox.curselection()
        if selection:
            operation = self.history_listbox.get(selection[0])
            # Extract result from operation string
            if "=" in operation:
                result = operation.split("=")[-1].strip()
                self.display_var.set(result)
    
    def run(self):
        """Start the GUI application."""
        self.root.mainloop()


def main():
    """Launch the GUI calculator."""
    app = CalculatorGUI()
    app.run()


if __name__ == "__main__":
    main()