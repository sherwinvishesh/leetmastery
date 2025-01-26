# Beginner notes
 This guide is an all-in-one resource for anyone looking to learn Python programming made by me (@sherwinvishesh). It starts with the basics, such as variables, input/output operations, and loops, and progressively covers more advanced topics, including object-oriented programming, data structures, and modules like NumPy, Pandas, and Matplotlib. The notes are enriched with practical examples, hands-on exercises, and easy-to-follow explanations, making it perfect for self-learners and beginners alike. Additionally, it introduces database connectivity, giving readers a glimpse into real-world applications of Python. Whether you're new to coding or enhancing your skills, this guide is a must-have for your Python journey.

## Why python
- Ease of Use: Python's syntax is super clean and easy to understand. When solving problems, this allows you to focus more on the logic than on syntax.

- Rich Libraries: Python comes with built-in libraries and functions (like collections.Counter, heapq, itertools, etc.) that make implementing algorithms much faster. For example, you can easily manage heaps using the heapq module without writing a heap from scratch.

- Dynamic Typing: Python's dynamic typing means you don’t have to declare variable types, which saves time when coding.

- Readable Code: Python code is often more concise and readable compared to languages like Java or C++, which can be verbose. This makes it easier to review and debug solutions.

- Community Support: Python is one of the most popular languages on LeetCode, so you'll find many discussions, hints, and solutions written in Python.

- Quick Prototyping: If you're experimenting with different algorithms to optimize a solution, Python's simplicity helps you quickly iterate through ideas.

- Built-in Data Structures: Lists, dictionaries, sets, and tuples are extremely powerful and allow you to easily implement complex data structures.


## Input and Output

### **Input in Python**
The `input()` function is used to take user input in Python. By default, it returns the input as a string.

#### **Basic Syntax**:
```python
variable = input("Enter something: ")
```

#### **Examples**:
1. **Taking Input**:
   ```python
   name = input("Enter your name: ")
   print(f"Hello, {name}!")
   ```

2. **Casting Input**:
   If you expect a number, you'll need to cast it:
   ```python
   age = int(input("Enter your age: "))  # Converts the input to an integer
   print(f"You are {age} years old.")
   ```

3. **Multiple Inputs**:
   - **Split Method**:
     ```python
     a, b = input("Enter two numbers separated by space: ").split()
     print(f"a: {a}, b: {b}")
     ```

   - **Map Function**:
     ```python
     a, b = map(int, input("Enter two numbers separated by space: ").split())
     print(f"Sum: {a + b}")
     ```

4. **Handling Lists**:
   ```python
   numbers = list(map(int, input("Enter numbers separated by space: ").split()))
   print(f"List of numbers: {numbers}")
   ```

---

### **Output in Python**
The `print()` function is used to display output to the screen.

#### **Basic Syntax**:
```python
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

#### **Examples**:
1. **Simple Print**:
   ```python
   print("Hello, World!")
   ```

2. **Using Variables**:
   ```python
   name = "Alice"
   age = 25
   print(f"{name} is {age} years old.")
   ```

3. **Separator (`sep`)**:
   The `sep` parameter specifies what separates multiple arguments.
   ```python
   print("Python", "is", "fun", sep="-")  # Output: Python-is-fun
   ```

4. **End Parameter (`end`)**:
   The `end` parameter specifies what to print at the end of the statement.
   ```python
   print("Hello", end=", ")
   print("World!")  # Output: Hello, World!
   ```

5. **Formatting Output**:
   - **Using f-strings** (introduced in Python 3.6):
     ```python
     name = "Alice"
     age = 30
     print(f"{name} is {age} years old.")
     ```
   - **Using `.format()` method**:
     ```python
     print("{} is {} years old.".format("Bob", 40))
     ```
   - **Positional Formatting**:
     ```python
     print("{1} is {0} years old.".format(40, "Bob"))  # Output: Bob is 40 years old.
     ```
   - **Using `%` Formatting**:
     ```python
     print("%s is %d years old." % ("Charlie", 50))
     ```

6. **Printing Lists and Dictionaries**:
   ```python
   my_list = [1, 2, 3, 4]
   print("List:", my_list)

   my_dict = {"name": "Alice", "age": 30}
   print("Dictionary:", my_dict)
   ```

7. **Printing to a File**:
   ```python
   with open("output.txt", "w") as file:
       print("Hello, File!", file=file)
   ```

8. **Printing Unicode Characters**:
   ```python
   print("Smile Emoji: \U0001F600")  # Output: 😀
   ```

---

### **Advanced Variations of Input/Output**
1. **Reading Input from a File**:
   ```python
   with open("input.txt", "r") as file:
       data = file.read()
       print(data)
   ```

2. **Printing Numbers with Precision**:
   ```python
   pi = 3.14159265358979
   print(f"Value of pi: {pi:.2f}")  # Output: 3.14
   ```

3. **Zfill for Zero Padding**:
   ```python
   number = 5
   print(str(number).zfill(3))  # Output: 005
   ```

4. **Custom Alignment**:
   ```python
   print(f"{'Left':<10} {'Right':>10} {'Center':^10}")
   # Output:
   # Left                Right    Center
   ```

5. **Escape Sequences**:
   ```python
   print("Line 1\nLine 2")       # Newline
   print("Tab\tSpace")          # Tab
   print("Backslash: \\")       # Backslash
   ```

6. **Printing in a Loop**:
   ```python
   for i in range(5):
       print(f"Iteration {i}", end=" | ")  # Prints in a single line
   ```

7. **Colorful Output** (using external libraries like `colorama` or ANSI codes):
   ```python
   print("\033[1;31mThis is red text\033[0m")  # Output in red
   ```

---

### **Summary Table**
| **Functionality**             | **Code Example**                                     |
|-------------------------------|-----------------------------------------------------|
| Input                         | `name = input("Enter name: ")`                      |
| Input with type conversion    | `age = int(input("Enter age: "))`                   |
| Simple Output                 | `print("Hello")`                                    |
| Multiple Variables            | `print(a, b, c)`                                    |
| Separator                     | `print(a, b, sep="-")`                              |
| Custom End                    | `print(a, end=" ")`                                 |
| F-Strings                     | `print(f"{name} is {age} years old.")`              |
| File Output                   | `print("Hello", file=file)`                         |
| Precision Output              | `print(f"{pi:.2f}")`                                |




## Variables, Functions and classes
### **Variables in Python**
- **Definition**: Variables are used to store data. They are dynamically typed, meaning you don’t need to declare their type explicitly.

#### **Key Points**
1. **Declaring Variables**:
   ```python
   x = 10         # Integer
   name = "John"  # String
   pi = 3.14      # Float
   is_valid = True # Boolean
   ```

2. **Naming Rules**:
   - Must start with a letter or underscore (`_`).
   - Can contain letters, numbers, and underscores.
   - Case-sensitive (`age` and `Age` are different).

3. **Dynamic Typing**:
   ```python
   x = 10
   x = "Now I’m a string"  # No need to specify the type!
   ```

4. **Multiple Assignments**:
   ```python
   a, b, c = 1, 2, 3
   x = y = z = 0  # Assign the same value to multiple variables
   ```

5. **Global and Local Variables**:
   - **Local**: Declared inside a function and accessible only there.
   - **Global**: Declared outside any function, accessible globally.

   ```python
   x = 5  # Global

   def test():
       x = 10  # Local
       print(x)  # Prints 10

   test()
   print(x)  # Prints 5
   ```

---

### **Functions in Python**
- **Definition**: Functions are blocks of reusable code that perform a specific task.

#### **Key Points**
1. **Defining a Function**:
   ```python
   def function_name(parameters):
       # Body of the function
       return result
   ```

2. **Examples**:
   ```python
   def greet(name):
       return f"Hello, {name}!"

   print(greet("Alice"))  # Output: Hello, Alice!
   ```

3. **Default Parameters**:
   ```python
   def add(a, b=10):
       return a + b

   print(add(5))      # Uses default value of b: 15
   print(add(5, 20))  # Overrides default: 25
   ```

4. **Keyword Arguments**:
   ```python
   def describe(person, age):
       return f"{person} is {age} years old."

   print(describe(age=25, person="John"))  # Explicitly pass arguments by name
   ```

5. **Variable-Length Arguments**:
   ```python
   def sum_all(*args):  # Accepts any number of arguments as a tuple
       return sum(args)

   print(sum_all(1, 2, 3, 4))  # Output: 10

   def show_info(**kwargs):  # Accepts keyword arguments as a dictionary
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   show_info(name="Alice", age=30)
   ```

6. **Lambda Functions**:
   - Anonymous, one-line functions.
   ```python
   square = lambda x: x ** 2
   print(square(5))  # Output: 25
   ```

---

### **Classes in Python**
- **Definition**: Classes are blueprints for creating objects. Objects are instances of classes.

#### **Key Points**
1. **Defining a Class**:
   ```python
   class ClassName:
       # Constructor (initializer)
       def __init__(self, parameter1, parameter2):
           self.attribute1 = parameter1
           self.attribute2 = parameter2

       # Method
       def method_name(self):
           return f"{self.attribute1} and {self.attribute2}"
   ```

2. **Example**:
   ```python
   class Dog:
       def __init__(self, name, breed):
           self.name = name
           self.breed = breed

       def bark(self):
           return f"{self.name} says Woof!"

   my_dog = Dog("Buddy", "Golden Retriever")
   print(my_dog.bark())  # Output: Buddy says Woof!
   ```

3. **Attributes**:
   - Instance attributes: Specific to an object (`self.attribute`).
   - Class attributes: Shared across all instances.
   ```python
   class Example:
       class_attr = "shared"

       def __init__(self, instance_attr):
           self.instance_attr = instance_attr
   ```

4. **Inheritance**:
   - A class can inherit attributes and methods from another class.
   ```python
   class Animal:
       def __init__(self, name):
           self.name = name

       def speak(self):
           return "I make a sound"

   class Cat(Animal):  # Cat inherits from Animal
       def speak(self):
           return f"{self.name} says Meow!"

   my_cat = Cat("Whiskers")
   print(my_cat.speak())  # Output: Whiskers says Meow!
   ```

5. **Encapsulation**:
   - Use `_` or `__` to indicate private/protected attributes or methods.
   ```python
   class Person:
       def __init__(self, name):
           self._name = name  # Protected (convention)
           self.__secret = "hidden"  # Private (name mangling)

       def get_secret(self):
           return self.__secret
   ```

6. **Static and Class Methods**:
   ```python
   class Math:
       @staticmethod
       def add(a, b):
           return a + b

       @classmethod
       def describe(cls):
           return f"This is the {cls.__name__} class."

   print(Math.add(5, 3))  # Output: 8
   print(Math.describe())  # Output: This is the Math class.
   ```


## Loops

Loops allow you to execute a block of code repeatedly, either for a fixed number of times or as long as a condition is true. Python supports two main types of loops: `for` loops and `while` loops.

---

### **1. `for` Loop**
- Used to iterate over a sequence (like a list, tuple, dictionary, set, string, or range).

#### **Syntax**:
```python
for variable in sequence:
    # Code block
```

#### **Examples**:
1. **Iterating Over a List**:
   ```python
   fruits = ["apple", "banana", "cherry"]
   for fruit in fruits:
       print(fruit)
   ```

2. **Using `range()`**:
   ```python
   for i in range(5):  # Default range starts from 0
       print(i)  # Output: 0 1 2 3 4
   ```

   - With a start and end:
     ```python
     for i in range(1, 6):
         print(i)  # Output: 1 2 3 4 5
     ```

   - With a step:
     ```python
     for i in range(0, 10, 2):
         print(i)  # Output: 0 2 4 6 8
     ```

3. **Iterating Over a String**:
   ```python
   for char in "hello":
       print(char)
   ```

4. **Iterating Over a Dictionary**:
   ```python
   person = {"name": "Alice", "age": 25}
   for key, value in person.items():
       print(f"{key}: {value}")
   ```

5. **Enumerate**:
   - Used to get both the index and the value during iteration.
   ```python
   items = ["a", "b", "c"]
   for index, item in enumerate(items):
       print(f"Index: {index}, Item: {item}")
   ```

---

### **2. `while` Loop**
- Used when you want to repeat code as long as a condition is true.

#### **Syntax**:
```python
while condition:
    # Code block
```

#### **Examples**:
1. **Basic `while` Loop**:
   ```python
   count = 0
   while count < 5:
       print(count)
       count += 1  # Increment to avoid infinite loop
   ```

2. **Using a Break Condition**:
   ```python
   while True:  # Infinite loop
       answer = input("Type 'exit' to stop: ")
       if answer == "exit":
           break
   ```

3. **Countdown Example**:
   ```python
   n = 5
   while n > 0:
       print(n)
       n -= 1
   print("Liftoff!")
   ```

4. **Simulating Do-While Loop** (Python doesn't have a direct `do-while`):
   ```python
   while True:
       num = int(input("Enter a positive number: "))
       if num > 0:
           break
   print(f"You entered {num}.")
   ```

---

### **3. Control Statements in Loops**
- **`break`**: Exit the loop prematurely.
  ```python
  for i in range(10):
      if i == 5:
          break
      print(i)  # Output: 0 1 2 3 4
  ```

- **`continue`**: Skip the rest of the code and move to the next iteration.
  ```python
  for i in range(5):
      if i == 2:
          continue
      print(i)  # Output: 0 1 3 4
  ```

- **`pass`**: A placeholder that does nothing.
  ```python
  for i in range(3):
      pass  # Does nothing, useful for incomplete code
  ```

- **`else` with Loops**:
  - The `else` block is executed after the loop finishes, unless the loop is exited with `break`.
  ```python
  for i in range(5):
      print(i)
  else:
      print("Loop completed!")  # Output: Loop completed!
  ```

---

### **4. Nested Loops**
- Loops inside loops are called nested loops.

#### **Example**:
```python
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i={i}, j={j}")
```

Output:
```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

---

### **5. Looping Through a 2D List**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")  # Output: 1 2 3 4 5 6 7 8 9
```

---

### **6. Itertools for Advanced Loops**
The `itertools` module provides advanced tools for looping.

#### **Examples**:
1. **Product**:
   ```python
   from itertools import product
   for pair in product([1, 2], ['a', 'b']):
       print(pair)  # Output: (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')
   ```

2. **Permutations**:
   ```python
   from itertools import permutations
   for perm in permutations([1, 2, 3], 2):
       print(perm)  # Output: (1, 2), (1, 3), (2, 1), ...
   ```

3. **Combinations**:
   ```python
   from itertools import combinations
   for comb in combinations([1, 2, 3], 2):
       print(comb)  # Output: (1, 2), (1, 3), (2, 3)
   ```

---

### **7. Infinite Loops**
Be careful with infinite loops! Use `break` to exit when needed.
```python
while True:
    print("This runs forever unless broken.")
    break
```

---

### **8. Summary Table**
| **Type**      | **Usage**                                                                                 |
|---------------|-------------------------------------------------------------------------------------------|
| `for`         | Iterates over a sequence or range.                                                       |
| `while`       | Repeats as long as the condition is `True`.                                              |
| `break`       | Exits the loop early.                                                                    |
| `continue`    | Skips the rest of the current iteration and moves to the next.                           |
| `pass`        | Does nothing (placeholder).                                                              |
| `else`        | Executes after the loop finishes (unless `break` is used).                               |
| `nested`      | Loops inside loops for multi-dimensional data.                                           |
| `itertools`   | Provides advanced tools like permutations, combinations, and Cartesian products.         |


## String
### **Strings in Python**

Strings are one of the most commonly used data types in Python. They are sequences of characters enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`).

---

### **1. Basics of Strings**
1. **Defining Strings**:
   ```python
   single_quote = 'Hello'
   double_quote = "World"
   triple_quote = '''This is a 
   multi-line string.'''
   ```

2. **Empty String**:
   ```python
   empty = ''
   ```

3. **Strings Are Immutable**:
   - Once created, you cannot modify a string directly. You can only create a new string.
   ```python
   text = "hello"
   # text[0] = 'H'  # Error
   text = "Hello"  # New string is created
   ```

---

### **2. String Operations**

#### **Concatenation and Repetition**
1. **Concatenation**:
   ```python
   greeting = "Hello" + " " + "World"
   print(greeting)  # Output: Hello World
   ```

2. **Repetition**:
   ```python
   repeated = "Hi! " * 3
   print(repeated)  # Output: Hi! Hi! Hi!
   ```

---

### **3. String Indexing and Slicing**

#### **Indexing**
- Strings are zero-indexed:
   ```python
   text = "Python"
   print(text[0])  # Output: P
   print(text[-1])  # Output: n (last character)
   ```

#### **Slicing**
- Extract substrings using slicing:
   ```python
   text = "Python"
   print(text[0:3])  # Output: Pyt
   print(text[:3])   # Output: Pyt (same as above)
   print(text[3:])   # Output: hon
   print(text[::2])  # Output: Pto (step of 2)
   print(text[::-1]) # Output: nohtyP (reversed)
   ```

---

### **4. String Methods**

#### **Case Manipulation**
1. **Uppercase and Lowercase**:
   ```python
   print("hello".upper())  # Output: HELLO
   print("HELLO".lower())  # Output: hello
   ```

2. **Capitalize and Title Case**:
   ```python
   print("hello world".capitalize())  # Output: Hello world
   print("hello world".title())       # Output: Hello World
   ```

3. **Swap Case**:
   ```python
   print("Hello World".swapcase())  # Output: hELLO wORLD
   ```

#### **Searching and Finding**
1. **Find and Index**:
   - `find()` returns the index of the first occurrence or `-1` if not found.
   ```python
   print("hello world".find("world"))  # Output: 6
   print("hello world".find("Python"))  # Output: -1
   ```

   - `index()` raises an error if not found.
   ```python
   print("hello world".index("world"))  # Output: 6
   ```

2. **Startswith and Endswith**:
   ```python
   print("hello world".startswith("hello"))  # Output: True
   print("hello world".endswith("world"))    # Output: True
   ```

#### **Modifying Strings**
1. **Replace**:
   ```python
   print("hello world".replace("world", "Python"))  # Output: hello Python
   ```

2. **Strip (Trimming)**:
   - `strip()` removes leading and trailing spaces.
   - `lstrip()` removes leading spaces; `rstrip()` removes trailing spaces.
   ```python
   print("  hello  ".strip())  # Output: hello
   print("  hello  ".lstrip())  # Output: "hello  "
   print("  hello  ".rstrip())  # Output: "  hello"
   ```

3. **Split and Join**:
   - `split()` breaks a string into a list based on a delimiter.
   ```python
   text = "a,b,c"
   print(text.split(","))  # Output: ['a', 'b', 'c']
   ```

   - `join()` combines a list into a string.
   ```python
   words = ["Hello", "World"]
   print(" ".join(words))  # Output: Hello World
   ```

#### **Checking Content**
1. **isalpha, isdigit, isalnum**:
   ```python
   print("abc".isalpha())  # Output: True (only letters)
   print("123".isdigit())  # Output: True (only digits)
   print("abc123".isalnum())  # Output: True (letters and digits)
   ```

2. **isspace**:
   ```python
   print("   ".isspace())  # Output: True
   ```

3. **islower, isupper**:
   ```python
   print("hello".islower())  # Output: True
   print("HELLO".isupper())  # Output: True
   ```

---

### **5. Formatting Strings**

#### **Old-Style Formatting (`%`)**
```python
name = "Alice"
age = 25
print("%s is %d years old." % (name, age))  # Output: Alice is 25 years old.
```

#### **`str.format()` Method**
```python
print("{} is {} years old.".format("Bob", 30))  # Output: Bob is 30 years old
print("{1} is {0} years old.".format(30, "Bob"))  # Positional arguments
```

#### **f-Strings (Recommended, Python 3.6+)**
```python
name = "Alice"
age = 25
print(f"{name} is {age} years old.")  # Output: Alice is 25 years old.
```

---

### **6. String Iteration**
You can iterate through a string using a `for` loop:
```python
for char in "Python":
    print(char)
```

---

### **7. String Escape Sequences**
Escape sequences are special characters preceded by a backslash (`\`):
| Escape Sequence | Description         |
|------------------|---------------------|
| `\'`            | Single quote        |
| `\"`            | Double quote        |
| `\\`            | Backslash           |
| `\n`            | Newline             |
| `\t`            | Tab                 |
| `\r`            | Carriage return     |
| `\u####`        | Unicode character   |

Example:
```python
print("Line 1\nLine 2")  # Output:
# Line 1
# Line 2
```

---

### **8. String Encoding and Decoding**
Strings are Unicode in Python by default. You can encode or decode strings for specific encodings like UTF-8.

1. **Encoding**:
   ```python
   text = "hello"
   encoded = text.encode("utf-8")
   print(encoded)  # Output: b'hello' (byte string)
   ```

2. **Decoding**:
   ```python
   decoded = encoded.decode("utf-8")
   print(decoded)  # Output: hello
   ```

---

### **9. Common String Pitfalls**
1. **Strings Are Immutable**:
   - Operations like `replace()` or `strip()` do not modify the original string but return a new one.
   ```python
   text = "hello"
   new_text = text.replace("h", "H")
   print(new_text)  # Output: Hello
   print(text)      # Output: hello (unchanged)
   ```

2. **Avoid Using `is` for String Comparison**:
   - Use `==` instead of `is` for value comparison.
   ```python
   print("abc" == "abc")  # True (correct way)
   print("abc" is "abc")  # May be True, but not guaranteed
   ```

---

### **10. Summary Table**
| **Operation**            | **Method/Code**                        |
|---------------------------|----------------------------------------|
| Concatenation             | `"Hello" + "World"`                   |
| Repetition                | `"Hi!" * 3`                          |
| Slicing                   | `"Python"[0:3]`                      |
| Length                    | `len("Hello")`                       |
| Replace                   | `"Hello".replace("H", "J")`          |
| Uppercase/Lowercase       | `"hello".upper()`                    |
| Split into List           | `"a,b,c".split(",")`                 |
| Join List into String     | `" ".join(["Hello", "World"])`        |
| Check Substring           | `"world" in "hello world"`           |
| Reverse String            | `"Python"[::-1]`                    |

## Intro to Data Structures in Python

### **Introduction to Data Structures in Python**

Data structures are a way of organizing and storing data so that it can be accessed and modified efficiently. Python provides several **built-in data structures**, each designed to handle specific types of operations efficiently.

---

### **1. Types of Data Structures in Python**

| **Data Structure** | **Mutable/Immutable** | **Description**                                        |
|---------------------|-----------------------|--------------------------------------------------------|
| **List**           | Mutable              | Ordered collection of elements. Allows duplicates.     |
| **Tuple**          | Immutable            | Ordered collection, similar to lists, but immutable.   |
| **Set**            | Mutable              | Unordered collection of unique elements.               |
| **Dictionary**     | Mutable              | Unordered collection of key-value pairs.               |
| **String**         | Immutable            | Sequence of characters (special case of a data type).  |

---

### **2. Overview of Built-in Data Structures**

#### **A. Lists**
- **Definition**: Ordered, mutable collections that can contain elements of different data types.
- **Usage**: Ideal for dynamic arrays where elements need to be added or removed frequently.
- **Example**:
   ```python
   my_list = [1, 2, 3, "Python"]
   ```

#### **B. Tuples**
- **Definition**: Ordered, immutable collections. Similar to lists, but their size and content cannot be changed after creation.
- **Usage**: Useful for read-only data or as keys in dictionaries.
- **Example**:
   ```python
   my_tuple = (1, 2, 3, "Python")
   ```

#### **C. Sets**
- **Definition**: Unordered collections of unique elements.
- **Usage**: Ideal for operations involving unique values, such as removing duplicates or performing mathematical set operations (union, intersection).
- **Example**:
   ```python
   my_set = {1, 2, 3, 4}
   ```

#### **D. Dictionaries**
- **Definition**: Unordered collections of key-value pairs.
- **Usage**: Useful for fast lookups or storing data with meaningful keys.
- **Example**:
   ```python
   my_dict = {"name": "Alice", "age": 25}
   ```

#### **E. Strings**
- **Definition**: Immutable sequences of characters.
- **Usage**: Used to store and manipulate text.
- **Example**:
   ```python
   my_string = "Hello, Python!"
   ```

---

### **3. Mutability of Data Structures**

| **Data Structure** | **Can Modify?** | **Can Add/Remove Elements?** |
|---------------------|-----------------|-------------------------------|
| List               | Yes             | Yes                           |
| Tuple              | No              | No                            |
| Set                | Yes             | Yes                           |
| Dictionary         | Yes             | Yes                           |
| String             | No              | No                            |

---

### **4. Choosing the Right Data Structure**

| **Use Case**                                             | **Recommended Data Structure** |
|----------------------------------------------------------|---------------------------------|
| Need a dynamic collection of elements                   | **List**                       |
| Data must remain constant (read-only)                   | **Tuple**                      |
| Need unique values or want to perform set operations    | **Set**                        |
| Need fast lookups using keys                            | **Dictionary**                 |
| Need to store text or a sequence of characters          | **String**                     |

---

### **5. Operations on Data Structures**

| **Operation**            | **Supported Data Structures**         | **Example**                                      |
|--------------------------|----------------------------------------|------------------------------------------------|
| Add an element           | List, Set, Dictionary                 | `my_list.append(4)`, `my_set.add(5)`          |
| Remove an element        | List, Set, Dictionary                 | `my_list.remove(2)`, `my_set.discard(5)`      |
| Check membership         | List, Set, Dictionary, String         | `3 in my_list`, `'key' in my_dict`            |
| Iterate                  | All                                   | `for item in my_list:`                        |
| Access by index          | List, Tuple, String                   | `my_list[0]`, `my_string[1]`                  |
| Access by key            | Dictionary                           | `my_dict['key']`                              |
| Slicing                  | List, Tuple, String                   | `my_list[1:3]`, `my_string[:5]`               |

---

### **6. Advanced Data Structures in Python**

In addition to the built-in ones, Python provides modules for more complex data structures:

1. **Deque (Double-Ended Queue)**:
   - Found in the `collections` module.
   - Example:
     ```python
     from collections import deque
     dq = deque([1, 2, 3])
     dq.append(4)  # Add to the right
     dq.appendleft(0)  # Add to the left
     ```

2. **DefaultDict**:
   - A dictionary that provides default values for missing keys.
   - Example:
     ```python
     from collections import defaultdict
     dd = defaultdict(int)
     dd['a'] += 1
     ```

3. **OrderedDict**:
   - A dictionary that remembers the insertion order of keys.
   - Example:
     ```python
     from collections import OrderedDict
     od = OrderedDict()
     od['a'] = 1
     od['b'] = 2
     ```

4. **Heap (Min-Heap)**:
   - Found in the `heapq` module.
   - Example:
     ```python
     import heapq
     heap = [3, 1, 4]
     heapq.heapify(heap)  # Converts the list into a heap
     heapq.heappush(heap, 2)  # Push an element
     ```

---

### **Summary**

Python provides versatile data structures to handle various types of data. Here’s a quick comparison:

| **Data Structure** | **Key Features**                    | **Ideal For**                                     |
|---------------------|-------------------------------------|-------------------------------------------------|
| List               | Ordered, mutable                   | Dynamic arrays, maintaining order               |
| Tuple              | Ordered, immutable                 | Read-only data                                  |
| Set                | Unordered, unique elements         | Removing duplicates, set operations             |
| Dictionary         | Unordered, key-value pairs         | Fast lookups, associating keys with values      |
| String             | Immutable, sequence of characters  | Text manipulation, storage of characters        |

 

## Lists
Lists are one of the most versatile and commonly used data structures in Python. They are ordered, mutable (modifiable), and can hold elements of any data type, including other lists.

---

### **1. Creating a List**
1. **Basic Syntax**:
   ```python
   my_list = [1, 2, 3, 4, 5]  # List of integers
   mixed_list = [1, "Hello", 3.14, True]  # List with mixed data types
   empty_list = []  # Empty list
   ```

2. **Using `list()` Constructor**:
   ```python
   my_list = list((1, 2, 3))  # Creating a list from a tuple
   print(my_list)  # Output: [1, 2, 3]
   ```

---

### **2. Accessing Elements**
1. **Indexing**:
   - Lists are zero-indexed.
   ```python
   my_list = [10, 20, 30, 40]
   print(my_list[0])  # Output: 10 (first element)
   print(my_list[-1])  # Output: 40 (last element)
   ```

2. **Slicing**:
   - Extract a portion of the list.
   ```python
   print(my_list[1:3])  # Output: [20, 30] (from index 1 to 2)
   print(my_list[:2])   # Output: [10, 20] (first two elements)
   print(my_list[2:])   # Output: [30, 40] (from index 2 to the end)
   print(my_list[::-1]) # Output: [40, 30, 20, 10] (reversed list)
   ```

---

### **3. Modifying Lists**
1. **Updating Elements**:
   ```python
   my_list[1] = 25
   print(my_list)  # Output: [10, 25, 30, 40]
   ```

2. **Adding Elements**:
   - **Using `append()`**:
     Adds an element to the end of the list.
     ```python
     my_list.append(50)
     print(my_list)  # Output: [10, 20, 30, 40, 50]
     ```

   - **Using `insert()`**:
     Inserts an element at a specific index.
     ```python
     my_list.insert(2, 15)
     print(my_list)  # Output: [10, 20, 15, 30, 40]
     ```

   - **Using `extend()`**:
     Adds multiple elements to the end of the list.
     ```python
     my_list.extend([50, 60])
     print(my_list)  # Output: [10, 20, 30, 40, 50, 60]
     ```

3. **Removing Elements**:
   - **Using `remove()`**:
     Removes the first occurrence of a specific value.
     ```python
     my_list.remove(20)
     print(my_list)  # Output: [10, 30, 40]
     ```

   - **Using `pop()`**:
     Removes and returns an element at a specific index (default is the last element).
     ```python
     my_list.pop()  # Removes the last element
     my_list.pop(1)  # Removes the element at index 1
     ```

   - **Using `clear()`**:
     Empties the list.
     ```python
     my_list.clear()
     print(my_list)  # Output: []
     ```

4. **Deleting Elements**:
   - **Using `del`**:
     Removes an element or a slice from the list.
     ```python
     del my_list[1]  # Removes the element at index 1
     del my_list[:]  # Deletes all elements (same as clear)
     ```

---

### **4. List Operations**
1. **Concatenation**:
   ```python
   list1 = [1, 2, 3]
   list2 = [4, 5]
   combined = list1 + list2
   print(combined)  # Output: [1, 2, 3, 4, 5]
   ```

2. **Repetition**:
   ```python
   repeated = [1, 2] * 3
   print(repeated)  # Output: [1, 2, 1, 2, 1, 2]
   ```

3. **Membership Testing**:
   ```python
   print(3 in [1, 2, 3])  # Output: True
   print(4 not in [1, 2, 3])  # Output: True
   ```

---

### **5. Looping Through a List**
1. **Using `for` Loop**:
   ```python
   for item in [10, 20, 30]:
       print(item)
   ```

2. **Using `enumerate()`**:
   - Get both index and value.
   ```python
   for index, value in enumerate([10, 20, 30]):
       print(f"Index: {index}, Value: {value}")
   ```

3. **List Comprehension**:
   - Create a new list using an expression.
   ```python
   squares = [x ** 2 for x in range(5)]
   print(squares)  # Output: [0, 1, 4, 9, 16]
   ```

---

### **6. Common List Methods**
| **Method**       | **Description**                                       |
|-------------------|-------------------------------------------------------|
| `append(x)`       | Adds an element `x` to the end of the list.           |
| `extend(iterable)`| Adds elements from an iterable to the end of the list.|
| `insert(i, x)`    | Inserts `x` at position `i`.                          |
| `remove(x)`       | Removes the first occurrence of `x`.                  |
| `pop([i])`        | Removes and returns the element at index `i` (last by default).|
| `clear()`         | Removes all elements from the list.                   |
| `index(x)`        | Returns the index of the first occurrence of `x`.     |
| `count(x)`        | Counts the occurrences of `x` in the list.            |
| `sort()`          | Sorts the list in ascending order (in-place).         |
| `reverse()`       | Reverses the list in-place.                           |
| `copy()`          | Returns a shallow copy of the list.                   |

---

### **7. Sorting and Reversing Lists**
1. **Sorting**:
   - **In-place Sorting**:
     ```python
     my_list = [3, 1, 4, 1, 5]
     my_list.sort()
     print(my_list)  # Output: [1, 1, 3, 4, 5]
     ```

   - **Using `sorted()`**:
     Returns a new sorted list without modifying the original.
     ```python
     new_list = sorted(my_list, reverse=True)
     print(new_list)  # Output: [5, 4, 3, 1, 1]
     ```

2. **Reversing**:
   - **In-place Reversal**:
     ```python
     my_list.reverse()
     print(my_list)
     ```

   - **Using Slicing**:
     ```python
     reversed_list = my_list[::-1]
     print(reversed_list)
     ```

---

### **8. Nested Lists**
1. **Creating a Nested List**:
   ```python
   nested = [[1, 2], [3, 4], [5, 6]]
   ```

2. **Accessing Elements**:
   ```python
   print(nested[1][0])  # Output: 3
   ```

3. **Using Loops**:
   ```python
   for sublist in nested:
       for item in sublist:
           print(item)
   ```

---

### **9. Copying Lists**
1. **Shallow Copy**:
   ```python
   list1 = [1, 2, 3]
   list2 = list1.copy()
   ```

2. **Deep Copy (for nested lists)**:
   ```python
   import copy
   nested_list = [[1, 2], [3, 4]]
   deep_copied = copy.deepcopy(nested_list)
   ```

---

### **10. Common Pitfalls**
1. **Modifying While Iterating**:
   - Avoid modifying a list while iterating over it. Instead, create a copy.
   ```python
   for x in my_list[:]:  # Use a slice to iterate over a copy
       if x < 0:
           my_list.remove(x)
   ```

2. **Shared References**:
   - Directly assigning one list to another creates a reference, not a copy.
   ```python
   list1 = [1, 2, 3]
   list2 = list1
   list2.append(4)
   print(list1)  # Output: [1, 2, 3, 4] (both lists are modified)
   ```

---

### **Summary**

| **Operation**                  | **Example**                              | **Output**                        |
|--------------------------------|------------------------------------------|-----------------------------------|
| Access Element by Index        | `my_list[0]`                            | First element                    |
| Add Element to End             | `my_list.append(10)`                    | Adds `10` to the list            |
| Insert Element at Index        | `my_list.insert(1, 20)`                 | Adds `20` at index 1             |
| Remove Element by Value        | `my_list.remove(30)`                    | Removes the first occurrence     |
| Remove Element by Index        | `my_list.pop(2)`                        | Removes element at index 2       |
| Sort List                      | `my_list.sort()`                        | Sorts the list                   |
| Reverse List                   | `my_list.reverse()`                     | Reverses the list                |
| Nested List Access             | `nested[1][0]`                         | Accesses sub-element             |

## Dictionary

A dictionary in Python is an **unordered collection of key-value pairs**. It is one of the most powerful and versatile data structures, allowing for fast lookups, insertion, and deletion operations.

---

### **1. Creating a Dictionary**

#### **Basic Syntax**:
```python
my_dict = {key1: value1, key2: value2, ...}
```

#### **Examples**:
1. **Empty Dictionary**:
   ```python
   empty_dict = {}
   ```

2. **Dictionary with Data**:
   ```python
   my_dict = {"name": "Alice", "age": 25, "city": "New York"}
   ```

3. **Using `dict()` Constructor**:
   ```python
   my_dict = dict(name="Alice", age=25, city="New York")
   ```

4. **From a List of Tuples**:
   ```python
   my_dict = dict([("name", "Alice"), ("age", 25)])
   ```

5. **From Keys with Default Values**:
   ```python
   keys = ["name", "age", "city"]
   my_dict = dict.fromkeys(keys, "unknown")
   print(my_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
   ```

---

### **2. Accessing Dictionary Elements**

1. **Access by Key**:
   ```python
   my_dict = {"name": "Alice", "age": 25}
   print(my_dict["name"])  # Output: Alice
   ```

2. **Using `get()`**:
   - Safer method as it doesn’t throw an error if the key doesn’t exist.
   ```python
   print(my_dict.get("name"))  # Output: Alice
   print(my_dict.get("gender", "Not Specified"))  # Output: Not Specified
   ```

---

### **3. Adding and Updating Elements**

1. **Adding a Key-Value Pair**:
   ```python
   my_dict["gender"] = "Female"
   print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'gender': 'Female'}
   ```

2. **Updating a Value**:
   ```python
   my_dict["age"] = 26
   ```

3. **Using `update()`**:
   - Add or update multiple key-value pairs.
   ```python
   my_dict.update({"city": "London", "age": 27})
   ```

---

### **4. Removing Elements**

1. **Using `del`**:
   ```python
   del my_dict["age"]
   print(my_dict)  # Removes the 'age' key
   ```

2. **Using `pop()`**:
   - Removes and returns the value of a key.
   ```python
   age = my_dict.pop("age", "Not Found")
   print(age)  # Output: 25
   ```

3. **Using `popitem()`**:
   - Removes and returns the last inserted key-value pair (Python 3.7+).
   ```python
   item = my_dict.popitem()
   print(item)  # Output: ('city', 'London')
   ```

4. **Using `clear()`**:
   - Empties the dictionary.
   ```python
   my_dict.clear()
   print(my_dict)  # Output: {}
   ```

---

### **5. Dictionary Methods**

| **Method**        | **Description**                                               |
|--------------------|---------------------------------------------------------------|
| `keys()`          | Returns a view object with all keys.                          |
| `values()`        | Returns a view object with all values.                        |
| `items()`         | Returns a view object with all key-value pairs.               |
| `get(key)`        | Returns the value for the given key (or a default if not found).|
| `update(dict2)`   | Updates the dictionary with key-value pairs from another dictionary. |
| `pop(key)`        | Removes a key and returns its value.                          |
| `popitem()`       | Removes and returns the last inserted key-value pair.         |
| `setdefault()`    | Returns the value for a key, or sets a default if the key doesn’t exist. |
| `copy()`          | Returns a shallow copy of the dictionary.                     |
| `fromkeys(keys)`  | Creates a dictionary from a list of keys with a default value. |

---

### **6. Looping Through a Dictionary**

1. **Loop Through Keys**:
   ```python
   for key in my_dict:
       print(key)
   ```

2. **Loop Through Values**:
   ```python
   for value in my_dict.values():
       print(value)
   ```

3. **Loop Through Key-Value Pairs**:
   ```python
   for key, value in my_dict.items():
       print(f"{key}: {value}")
   ```

---

### **7. Dictionary Comprehensions**
Similar to list comprehensions, you can create dictionaries in one line.

1. **Basic Example**:
   ```python
   squares = {x: x**2 for x in range(5)}
   print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
   ```

2. **With Condition**:
   ```python
   even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
   print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
   ```

---

### **8. Nested Dictionaries**
Dictionaries can hold other dictionaries as values, creating nested structures.

1. **Creating a Nested Dictionary**:
   ```python
   nested_dict = {
       "person1": {"name": "Alice", "age": 25},
       "person2": {"name": "Bob", "age": 30}
   }
   ```

2. **Accessing Nested Values**:
   ```python
   print(nested_dict["person1"]["name"])  # Output: Alice
   ```

---

### **9. Copying Dictionaries**

1. **Shallow Copy**:
   ```python
   shallow_copy = my_dict.copy()
   ```

2. **Deep Copy**:
   For nested dictionaries, use `copy.deepcopy()` to ensure changes in one dictionary don’t affect the other.
   ```python
   import copy
   deep_copy = copy.deepcopy(nested_dict)
   ```

---

### **10. Common Use Cases for Dictionaries**

1. **Counting Occurrences**:
   ```python
   from collections import Counter
   data = ["apple", "banana", "apple", "orange"]
   counts = Counter(data)
   print(counts)  # Output: {'apple': 2, 'banana': 1, 'orange': 1}
   ```

2. **Grouping Data**:
   ```python
   from collections import defaultdict
   groups = defaultdict(list)
   items = [("fruit", "apple"), ("fruit", "banana"), ("veggie", "carrot")]

   for category, item in items:
       groups[category].append(item)

   print(groups)  # Output: {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}
   ```

3. **Lookups**:
   - Fast key-based lookups make dictionaries ideal for tasks like storing configuration settings or caching.

---

### **11. Common Pitfalls**

1. **KeyError**:
   - Trying to access a key that doesn’t exist.
   ```python
   print(my_dict["unknown"])  # Raises KeyError
   ```

2. **Mutable Keys**:
   - Only immutable types (like strings, numbers, or tuples) can be used as dictionary keys.
   ```python
   # This will raise a TypeError:
   my_dict = {[1, 2]: "value"}
   ```

3. **Order of Keys**:
   - In Python 3.7+, dictionaries maintain insertion order by default. In earlier versions, this is not guaranteed.

---

### **12. Summary Table**

| **Operation**               | **Example**                                  | **Description**                              |
|-----------------------------|----------------------------------------------|----------------------------------------------|
| Access Value by Key         | `my_dict["key"]`                            | Get value for a specific key.                |
| Add/Update Key-Value Pair   | `my_dict["key"] = value`                    | Add a new key-value pair or update existing. |
| Remove Key                  | `del my_dict["key"]` or `my_dict.pop("key")`| Remove a key from the dictionary.            |
| Get All Keys                | `my_dict.keys()`                            | Returns all keys as a view object.           |
| Get All Values              | `my_dict.values()`                          | Returns all values as a view object.         |
| Get All Key-Value Pairs     | `my_dict.items()`                           | Returns all key-value pairs as a view object.|
| Clear Dictionary            | `my_dict.clear()`                           | Empties the dictionary.                      |
| Check Key Existence         | `"key" in my_dict`                          | Returns `True` if key exists.                |

## Sets

A **set** in Python is an **unordered collection of unique elements**. Sets are highly useful for operations that involve uniqueness, such as removing duplicates, and for performing mathematical set operations like union, intersection, and difference.

---

### **1. Creating a Set**

#### **Basic Syntax**:
```python
my_set = {element1, element2, element3, ...}
```

#### **Examples**:
1. **Empty Set**:
   - Use `set()` to create an empty set (not `{}` because that creates an empty dictionary).
   ```python
   empty_set = set()
   print(type(empty_set))  # Output: <class 'set'>
   ```

2. **Set with Elements**:
   ```python
   my_set = {1, 2, 3, 4}
   ```

3. **Using `set()` Constructor**:
   - You can create a set from any iterable (e.g., list, tuple, string).
   ```python
   my_set = set([1, 2, 3, 4])
   string_set = set("hello")  # Output: {'h', 'e', 'l', 'o'} (unique characters)
   ```

4. **Set with Mixed Data Types**:
   ```python
   mixed_set = {1, "Python", 3.14}
   ```

---

### **2. Properties of Sets**

1. **Unordered**:
   - The order of elements is not preserved.
   ```python
   my_set = {3, 1, 4, 2}
   print(my_set)  # Output: {1, 2, 3, 4} (order may vary)
   ```

2. **Unique Elements**:
   - Duplicate elements are automatically removed.
   ```python
   my_set = {1, 2, 2, 3}
   print(my_set)  # Output: {1, 2, 3}
   ```

3. **Immutable Elements**:
   - Elements in a set must be immutable (e.g., numbers, strings, tuples). Lists or other sets cannot be elements.
   ```python
   # This will raise a TypeError:
   my_set = {1, [2, 3]}
   ```

---

### **3. Accessing Set Elements**

- Sets do not support indexing or slicing because they are unordered.
- You can loop through a set or check for membership:
   ```python
   my_set = {1, 2, 3}
   for element in my_set:
       print(element)
   
   print(2 in my_set)  # Output: True
   print(4 not in my_set)  # Output: True
   ```

---

### **4. Modifying Sets**

1. **Adding Elements**:
   - Use `add()` to add a single element.
   ```python
   my_set = {1, 2, 3}
   my_set.add(4)
   print(my_set)  # Output: {1, 2, 3, 4}
   ```

2. **Updating with Multiple Elements**:
   - Use `update()` to add multiple elements from an iterable.
   ```python
   my_set.update([4, 5, 6])
   print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
   ```

3. **Removing Elements**:
   - **`remove()`**: Removes a specific element. Raises a `KeyError` if the element does not exist.
     ```python
     my_set.remove(2)
     ```

   - **`discard()`**: Removes a specific element but does not raise an error if the element does not exist.
     ```python
     my_set.discard(10)  # No error
     ```

   - **`pop()`**: Removes and returns a random element. Raises a `KeyError` if the set is empty.
     ```python
     element = my_set.pop()
     print(element)
     ```

4. **Clearing All Elements**:
   - Use `clear()` to empty the set.
   ```python
   my_set.clear()
   print(my_set)  # Output: set()
   ```

---

### **5. Set Operations**

Python sets support a wide variety of mathematical operations.

1. **Union** (`|` or `union()`):
   - Combines elements from both sets (removes duplicates).
   ```python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}
   print(set1 | set2)  # Output: {1, 2, 3, 4, 5}
   print(set1.union(set2))  # Same as above
   ```

2. **Intersection** (`&` or `intersection()`):
   - Returns elements common to both sets.
   ```python
   print(set1 & set2)  # Output: {3}
   print(set1.intersection(set2))  # Same as above
   ```

3. **Difference** (`-` or `difference()`):
   - Returns elements in the first set but not in the second.
   ```python
   print(set1 - set2)  # Output: {1, 2}
   print(set1.difference(set2))  # Same as above
   ```

4. **Symmetric Difference** (`^` or `symmetric_difference()`):
   - Returns elements in either set, but not in both.
   ```python
   print(set1 ^ set2)  # Output: {1, 2, 4, 5}
   print(set1.symmetric_difference(set2))  # Same as above
   ```

---

### **6. Subset and Superset Checks**

1. **Subset**:
   - Check if one set is a subset of another.
   ```python
   set1 = {1, 2}
   set2 = {1, 2, 3, 4}
   print(set1.issubset(set2))  # Output: True
   ```

2. **Superset**:
   - Check if one set is a superset of another.
   ```python
   print(set2.issuperset(set1))  # Output: True
   ```

3. **Disjoint Sets**:
   - Check if two sets have no elements in common.
   ```python
   set3 = {5, 6}
   print(set1.isdisjoint(set3))  # Output: True
   ```

---

### **7. Frozen Sets**

A **frozenset** is an immutable version of a set. Once created, its elements cannot be changed.

1. **Creating a Frozen Set**:
   ```python
   frozen = frozenset([1, 2, 3])
   print(frozen)  # Output: frozenset({1, 2, 3})
   ```

2. **Why Use Frozen Sets?**:
   - Useful as keys in dictionaries or elements in other sets since they are immutable.

---

### **8. Common Use Cases for Sets**

1. **Removing Duplicates from a List**:
   ```python
   my_list = [1, 2, 2, 3, 4, 4]
   unique_list = list(set(my_list))
   print(unique_list)  # Output: [1, 2, 3, 4]
   ```

2. **Finding Common Elements Between Lists**:
   ```python
   list1 = [1, 2, 3]
   list2 = [2, 3, 4]
   common = set(list1) & set(list2)
   print(common)  # Output: {2, 3}
   ```

3. **Checking Membership**:
   - Sets provide fast membership checks compared to lists.
   ```python
   my_set = {1, 2, 3, 4}
   print(3 in my_set)  # Output: True
   ```

---

### **9. Performance of Sets**

| **Operation**          | **Time Complexity** |
|-------------------------|---------------------|
| Add Element (`add()`)   | O(1)                |
| Remove Element (`remove()`) | O(1)          |
| Membership Test (`in`)  | O(1)                |
| Union (`|`)             | O(len(set1) + len(set2)) |
| Intersection (`&`)      | O(min(len(set1), len(set2))) |

---

### **10. Summary Table**

| **Operation**                  | **Code Example**                             | **Description**                                 |
|--------------------------------|-----------------------------------------------|------------------------------------------------|
| Add Element                   | `my_set.add(10)`                             | Adds an element to the set.                    |
| Remove Element                | `my_set.remove(10)`                          | Removes an element (raises error if not found).|
| Discard Element               | `my_set.discard(10)`                         | Removes an element (no error if not found).    |
| Union                         | `set1 | set2`                                | Combines elements from both sets.              |
| Intersection                  | `set1 & set2`                                | Finds common elements in both sets.            |
| Difference                    | `set1 - set2`                                | Finds elements in set1 not in set2.            |
| Symmetric Difference          | `set1 ^ set2`                                | Finds elements in either set but not in both.  |
| Check Subset                  | `set1.issubset(set2)`                        | Checks if set1 is a subset of set2.            |
| Check Superset                | `set1.issuperset(set2)`                      | Checks if set1 is a superset of set2.          |


## Tuples 

A **tuple** in Python is an **ordered, immutable collection** of elements. Tuples are similar to lists but have the key distinction that their contents cannot be modified once created. They are often used for data that should not change throughout the program's lifecycle.

---

### **1. Creating a Tuple**

#### **Basic Syntax**:
```python
my_tuple = (element1, element2, ...)
```

#### **Examples**:
1. **Empty Tuple**:
   ```python
   empty_tuple = ()
   ```

2. **Single-Element Tuple**:
   - You must include a comma after the element to make it a tuple.
   ```python
   single_element_tuple = (5,)
   print(type(single_element_tuple))  # Output: <class 'tuple'>
   ```

3. **Tuple with Multiple Elements**:
   ```python
   my_tuple = (1, 2, 3)
   ```

4. **Using `tuple()` Constructor**:
   - Converts an iterable into a tuple.
   ```python
   my_tuple = tuple([1, 2, 3])  # List to tuple
   string_tuple = tuple("hello")  # String to tuple
   print(string_tuple)  # Output: ('h', 'e', 'l', 'l', 'o')
   ```

---

### **2. Properties of Tuples**

1. **Ordered**:
   - The order of elements in a tuple is fixed.
   ```python
   my_tuple = (10, 20, 30)
   print(my_tuple[0])  # Output: 10
   ```

2. **Immutable**:
   - Tuples cannot be changed after creation. Any operation that tries to modify them will result in an error.
   ```python
   my_tuple = (1, 2, 3)
   # my_tuple[1] = 5  # Raises TypeError
   ```

3. **Allows Duplicates**:
   - Tuples can have duplicate elements.
   ```python
   my_tuple = (1, 1, 2, 3)
   ```

---

### **3. Accessing Tuple Elements**

1. **Indexing**:
   - Access elements using their index.
   ```python
   my_tuple = (10, 20, 30, 40)
   print(my_tuple[1])  # Output: 20
   print(my_tuple[-1])  # Output: 40 (last element)
   ```

2. **Slicing**:
   - Extract portions of the tuple.
   ```python
   print(my_tuple[1:3])  # Output: (20, 30)
   print(my_tuple[:2])   # Output: (10, 20)
   print(my_tuple[::2])  # Output: (10, 30)
   print(my_tuple[::-1]) # Output: (40, 30, 20, 10)
   ```

---

### **4. Tuple Operations**

1. **Concatenation**:
   ```python
   tuple1 = (1, 2, 3)
   tuple2 = (4, 5)
   combined = tuple1 + tuple2
   print(combined)  # Output: (1, 2, 3, 4, 5)
   ```

2. **Repetition**:
   ```python
   repeated = (1, 2) * 3
   print(repeated)  # Output: (1, 2, 1, 2, 1, 2)
   ```

3. **Membership Testing**:
   ```python
   print(3 in (1, 2, 3))  # Output: True
   print(4 not in (1, 2, 3))  # Output: True
   ```

4. **Length**:
   ```python
   my_tuple = (1, 2, 3, 4)
   print(len(my_tuple))  # Output: 4
   ```

5. **Tuple Unpacking**:
   - Assign tuple elements to variables.
   ```python
   my_tuple = (10, 20, 30)
   a, b, c = my_tuple
   print(a, b, c)  # Output: 10 20 30
   ```

6. **Nested Tuples**:
   - Tuples can contain other tuples.
   ```python
   nested = (1, (2, 3), (4, 5))
   print(nested[1][1])  # Output: 3
   ```

---

### **5. Tuple Methods**

| **Method**       | **Description**                                              |
|-------------------|--------------------------------------------------------------|
| `count(value)`    | Returns the number of occurrences of `value` in the tuple.   |
| `index(value)`    | Returns the index of the first occurrence of `value`.        |

#### **Examples**:
1. **Using `count()`**:
   ```python
   my_tuple = (1, 2, 2, 3, 2)
   print(my_tuple.count(2))  # Output: 3
   ```

2. **Using `index()`**:
   ```python
   print(my_tuple.index(2))  # Output: 1 (first occurrence)
   ```

---

### **6. Immutability of Tuples**

Although tuples themselves are immutable, they can contain mutable elements like lists. This means you can modify the mutable elements within a tuple:
```python
my_tuple = (1, [2, 3], 4)
my_tuple[1][0] = 99  # Modifies the list inside the tuple
print(my_tuple)  # Output: (1, [99, 3], 4)
```

---

### **7. Tuple vs List**

| **Feature**          | **Tuple**                              | **List**                              |
|-----------------------|----------------------------------------|---------------------------------------|
| **Mutability**        | Immutable                             | Mutable                              |
| **Syntax**            | `(1, 2, 3)`                           | `[1, 2, 3]`                          |
| **Performance**       | Faster (less overhead)                | Slower (more overhead)               |
| **Usage**             | Fixed data, read-only purposes         | Dynamic data, frequent modifications |
| **Allows Mutability?**| Can contain mutable elements           | All elements mutable                 |

---

### **8. Use Cases of Tuples**

1. **Fixed Data**:
   - Use tuples to represent data that should not change (e.g., coordinates, RGB values).
   ```python
   coordinates = (10.5, 20.3)
   ```

2. **Keys in Dictionaries**:
   - Tuples can be used as keys in dictionaries because they are immutable.
   ```python
   my_dict = {("x", "y"): "Point A", ("a", "b"): "Point B"}
   print(my_dict[("x", "y")])  # Output: Point A
   ```

3. **Return Multiple Values from Functions**:
   ```python
   def get_stats():
       return (100, 200, 300)

   min_val, max_val, avg_val = get_stats()
   print(min_val, max_val, avg_val)
   ```

4. **Efficient Data Storage**:
   - Tuples use less memory compared to lists, making them ideal for large datasets that won’t change.

---

### **9. Performance of Tuples**

| **Operation**            | **Time Complexity** |
|---------------------------|---------------------|
| Access Element by Index   | O(1)                |
| Length (`len()`)          | O(1)                |
| Concatenation (`+`)       | O(n)                |
| Membership Test (`in`)    | O(n)                |

---

### **10. Summary Table**

| **Operation**                  | **Example**                                  | **Output/Description**                       |
|--------------------------------|----------------------------------------------|---------------------------------------------|
| Access Element                | `my_tuple[0]`                               | First element of the tuple                  |
| Slicing                       | `my_tuple[1:3]`                             | Subset of the tuple                         |
| Count Element Occurrences     | `my_tuple.count(2)`                         | Number of times `2` appears in the tuple    |
| Find Element Index            | `my_tuple.index(3)`                         | Index of the first occurrence of `3`        |
| Concatenate Tuples            | `(1, 2) + (3, 4)`                           | `(1, 2, 3, 4)`                              |
| Repeat Tuple                  | `(1, 2) * 3`                                | `(1, 2, 1, 2, 1, 2)`                        |
| Unpack Elements               | `a, b = (1, 2)`                             | `a = 1, b = 2`                              |
| Nested Tuple                  | `nested[1][0]`                              | Access elements inside nested tuples        |

## Date and Time 

Python provides powerful libraries like `datetime`, `time`, and `calendar` for working with dates and times. These exercises will help you practice working with various aspects of date and time manipulation.

---

### **1. Importing Necessary Libraries**
Make sure to import the required modules:
```python
from datetime import datetime, date, time, timedelta
import time
import calendar
```

---

### **2. Exercises**

#### **Exercise 1: Get the Current Date and Time**
- **Task**: Print the current date and time.
- **Hint**: Use `datetime.now()`.
```python
now = datetime.now()
print("Current date and time:", now)
```

---

#### **Exercise 2: Extract Specific Components from a Date**
- **Task**: Print the year, month, day, hour, minute, and second from the current datetime.
- **Hint**: Use `datetime.now()` and access attributes like `.year`, `.month`, etc.
```python
now = datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
```

---

#### **Exercise 3: Format a Date**
- **Task**: Format the current date as `DD-MM-YYYY` and `YYYY/MM/DD HH:MM:SS`.
- **Hint**: Use `strftime()`.
```python
now = datetime.now()
formatted_date = now.strftime("%d-%m-%Y")
formatted_datetime = now.strftime("%Y/%m/%d %H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Datetime:", formatted_datetime)
```

---

#### **Exercise 4: Parse a String into a Date**
- **Task**: Convert the string `"2025-01-25 14:30:00"` into a `datetime` object.
- **Hint**: Use `strptime()`.
```python
date_str = "2025-01-25 14:30:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed Date:", parsed_date)
```

---

#### **Exercise 5: Calculate Days Until a Specific Date**
- **Task**: Calculate how many days are left until New Year (January 1st).
- **Hint**: Use `timedelta` and subtraction.
```python
today = date.today()
new_year = date(today.year + 1, 1, 1)
days_until_new_year = (new_year - today).days
print("Days until New Year:", days_until_new_year)
```

---

#### **Exercise 6: Add or Subtract Time**
- **Task**: Add 7 days to the current date, then subtract 3 hours from the current time.
- **Hint**: Use `timedelta`.
```python
now = datetime.now()

# Add 7 days
future_date = now + timedelta(days=7)
print("Date after 7 days:", future_date)

# Subtract 3 hours
past_time = now - timedelta(hours=3)
print("Time 3 hours ago:", past_time)
```

---

#### **Exercise 7: Get the Day of the Week**
- **Task**: Print the day of the week for the current date and a specific date (e.g., `2025-01-25`).
- **Hint**: Use `strftime()` or `.weekday()`.
```python
# Current date
now = datetime.now()
print("Day of the week (today):", now.strftime("%A"))

# Specific date
specific_date = datetime(2025, 1, 25)
print("Day of the week (2025-01-25):", specific_date.strftime("%A"))
```

---

#### **Exercise 8: Check if a Year is a Leap Year**
- **Task**: Write a function that checks whether a given year is a leap year.
- **Hint**: Use the `calendar` module.
```python
def is_leap_year(year):
    return calendar.isleap(year)

print("Is 2024 a leap year?", is_leap_year(2024))  # True
print("Is 2025 a leap year?", is_leap_year(2025))  # False
```

---

#### **Exercise 9: Calculate Age**
- **Task**: Write a function that calculates a person's age based on their date of birth.
- **Hint**: Use `datetime` subtraction.
```python
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

dob = date(1990, 5, 15)
print("Age:", calculate_age(dob))
```

---

#### **Exercise 10: Convert a Timestamp to a Date**
- **Task**: Convert the Unix timestamp `1672444800` to a human-readable date.
- **Hint**: Use `datetime.fromtimestamp()`.
```python
timestamp = 1672444800
readable_date = datetime.fromtimestamp(timestamp)
print("Readable Date:", readable_date)
```

---

#### **Exercise 11: Measure Execution Time**
- **Task**: Measure the time taken to execute a block of code.
- **Hint**: Use `time.time()` or `time.perf_counter()`.
```python
start_time = time.time()

# Code block
for i in range(1000000):
    pass

end_time = time.time()
execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")
```

---

#### **Exercise 12: Generate a Calendar**
- **Task**: Print the calendar for a specific month and year (e.g., January 2025).
- **Hint**: Use `calendar.month()`.
```python
year = 2025
month = 1
print(calendar.month(year, month))
```

---

#### **Exercise 13: Get ISO Week Number**
- **Task**: Find the ISO week number of a given date.
- **Hint**: Use `isocalendar()`.
```python
specific_date = date(2025, 1, 25)
iso_week = specific_date.isocalendar()
print("ISO Year, Week Number, Weekday:", iso_week)
```

---

#### **Exercise 14: Find the Difference Between Two Dates**
- **Task**: Calculate the number of days, hours, and minutes between two dates.
- **Hint**: Use `datetime` subtraction.
```python
date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 25, 18, 30, 0)

difference = date2 - date1
days = difference.days
seconds = difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60

print(f"Difference: {days} days, {hours} hours, {minutes} minutes")
```

---

#### **Exercise 15: Display Time in Different Time Zones**
- **Task**: Print the current time in UTC and a different time zone (e.g., US/Pacific).
- **Hint**: Use `pytz` (install with `pip install pytz`).
```python
import pytz

utc_now = datetime.now(pytz.utc)
pacific_now = utc_now.astimezone(pytz.timezone("US/Pacific"))

print("UTC Time:", utc_now)
print("US/Pacific Time:", pacific_now)
```

##  Object-Oriented Programming (OOP) in Python 

Object-Oriented Programming (OOP) is a programming paradigm that organizes data and behavior into **objects**, which are instances of **classes**. Python is a multi-paradigm language, and OOP is one of its key strengths.

---

### **1. Core Concepts of OOP**
OOP revolves around the following four key principles:

| **Principle**    | **Description**                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| **Encapsulation** | Bundling of data (attributes) and methods (functions) into a single unit (class).                         |
| **Abstraction**   | Hiding implementation details and showing only the essential features of an object.                       |
| **Inheritance**   | The mechanism by which one class can inherit attributes and methods from another.                         |
| **Polymorphism**  | The ability to redefine or overload methods to perform different tasks based on the object or input type.  |

---

### **2. Defining Classes and Creating Objects**

#### **Defining a Class**
A **class** is a blueprint for creating objects. It defines attributes (data) and methods (behavior).

```python
class MyClass:
    # Class attributes
    class_attribute = "I am a class attribute"

    # Constructor (__init__)
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    # Instance method
    def greet(self):
        return f"Hello, {self.instance_attribute}!"
```

#### **Creating Objects**
An **object** is an instance of a class.
```python
# Creating an object
my_object = MyClass("Alice")

# Accessing attributes and methods
print(my_object.instance_attribute)  # Output: Alice
print(my_object.greet())             # Output: Hello, Alice!
```

---

### **3. Components of a Class**

1. **Attributes**:
   - Variables that belong to a class or object.

   **Example**:
   ```python
   class Person:
       species = "Homo sapiens"  # Class attribute

       def __init__(self, name, age):
           self.name = name       # Instance attribute
           self.age = age
   ```

2. **Methods**:
   - Functions defined within a class to describe the behavior of objects.

   **Types**:
   | **Method Type**      | **Description**                                              |
   |----------------------|--------------------------------------------------------------|
   | Instance Methods     | Operate on instance attributes; require `self`.             |
   | Class Methods        | Operate on class attributes; require `@classmethod` and `cls`. |
   | Static Methods       | Do not require `self` or `cls`; defined with `@staticmethod`. |

   **Examples**:
   ```python
   class Example:
       # Instance method
       def instance_method(self):
           print("I am an instance method.")

       # Class method
       @classmethod
       def class_method(cls):
           print("I am a class method.")

       # Static method
       @staticmethod
       def static_method():
           print("I am a static method.")
   ```

3. **The `__init__` Method (Constructor)**:
   - A special method that initializes object attributes when an object is created.
   ```python
   class Dog:
       def __init__(self, name, breed):
           self.name = name
           self.breed = breed
   ```

4. **The `self` Keyword**:
   - Refers to the instance of the class. Used to access instance attributes and methods.

---

### **4. Inheritance**

Inheritance allows a class to reuse the attributes and methods of another class.

1. **Basic Inheritance**:
   ```python
   class Animal:
       def speak(self):
           return "I make a sound."

   class Dog(Animal):  # Dog inherits from Animal
       def speak(self):
           return "Woof!"
   ```

2. **Using `super()`**:
   - Call methods of the parent class.
   ```python
   class Animal:
       def __init__(self, species):
           self.species = species

   class Dog(Animal):
       def __init__(self, name, species="Canine"):
           super().__init__(species)  # Call parent constructor
           self.name = name
   ```

3. **Multiple Inheritance**:
   - A class can inherit from multiple parent classes.
   ```python
   class A:
       def method_a(self):
           print("Method from class A")

   class B:
       def method_b(self):
           print("Method from class B")

   class C(A, B):  # Inherits from both A and B
       pass
   ```

---

### **5. Polymorphism**

Polymorphism allows methods in different classes to have the same name but behave differently.

1. **Method Overriding**:
   ```python
   class Parent:
       def greet(self):
           return "Hello from Parent!"

   class Child(Parent):
       def greet(self):
           return "Hello from Child!"
   ```

2. **Duck Typing**:
   - Python supports polymorphism through duck typing: "If it looks like a duck and quacks like a duck, it’s a duck."
   ```python
   class Cat:
       def speak(self):
           return "Meow!"

   class Dog:
       def speak(self):
           return "Woof!"

   def animal_sound(animal):
       print(animal.speak())

   animal_sound(Cat())  # Output: Meow!
   animal_sound(Dog())  # Output: Woof!
   ```

---

### **6. Encapsulation**

Encapsulation involves restricting direct access to some of an object’s attributes and methods.

1. **Public Attributes**:
   - Accessible from outside the class.
   ```python
   self.name = "Alice"
   ```

2. **Protected Attributes**:
   - Indicated with a single underscore (`_`); intended for internal use.
   ```python
   self._age = 30
   ```

3. **Private Attributes**:
   - Indicated with double underscores (`__`); not directly accessible outside the class.
   ```python
   self.__salary = 50000
   ```

   **Access Private Attributes with Getter/Setter**:
   ```python
   class Employee:
       def __init__(self, name, salary):
           self.name = name
           self.__salary = salary

       def get_salary(self):  # Getter
           return self.__salary

       def set_salary(self, salary):  # Setter
           self.__salary = salary
   ```

---

### **7. Special Methods (Dunder Methods)**

Special methods (also known as magic methods) allow customization of class behavior.

1. **Common Special Methods**:
   | **Method**    | **Purpose**                                      |
   |---------------|--------------------------------------------------|
   | `__init__`    | Initializes a new object.                       |
   | `__str__`     | Returns a string representation of the object.  |
   | `__repr__`    | Returns an official string representation.      |
   | `__len__`     | Defines behavior for `len()` function.          |
   | `__add__`     | Defines behavior for the `+` operator.          |

2. **Example**:
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __str__(self):
           return f"Point({self.x}, {self.y})"

       def __add__(self, other):
           return Point(self.x + other.x, self.y + other.y)

   p1 = Point(1, 2)
   p2 = Point(3, 4)
   print(p1 + p2)  # Output: Point(4, 6)
   ```

---

### **8. Advanced OOP Concepts**

1. **Abstract Classes**:
   - Classes that cannot be instantiated and serve as blueprints for other classes.
   - Use the `abc` module.

   ```python
   from abc import ABC, abstractmethod

   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius ** 2
   ```

2. **Interfaces**:
   - Abstract classes can act as interfaces to define required methods for subclasses.

3. **Class Decorators**:
   - Use decorators like `@property` to define getter, setter, and deleter methods.

   ```python
   class Person:
       def __init__(self, name):
           self._name = name

       @property
       def name(self):
           return self._name

       @name.setter
       def name(self, value):
           self._name = value
   ```

---

### **9. Summary Table**

| **Concept**       | **Description**                                            | **Example**                                  |
|--------------------|------------------------------------------------------------|---------------------------------------------|
| Class             | Blueprint for creating objects.                           | `class MyClass: ...`                        |
| Object            | Instance of a class.                                      | `obj = MyClass()`                           |
| Encapsulation     | Restricting access to internal details.                   | `_protected`, `__private`                   |
| Inheritance       | Reuse behavior from parent classes.                       | `class Child(Parent): ...`                  |
| Polymorphism      | Same interface, different implementations.                | `def speak(): return "Meow"`               |
| Special Methods   | Define custom behavior for operators and built-in methods.| `__add__`, `__str__`                        |

---

### **10. Practical Example**
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"Driving a {self.brand} {self.model}."

class Car(Vehicle):
    def drive(self):
        return f"Driving a car: {self.brand} {self.model}."

class Bike(Vehicle):
    def drive(self):
        return f"Riding a bike: {self.brand} {self.model}."

vehicles = [Car("Toyota", "Corolla"), Bike("Yamaha", "MT-07")]
for v in vehicles:
    print(v.drive())
```

### JSON Exercises

The **JSON (JavaScript Object Notation)** format is widely used for data exchange between a client and server. Python provides the `json` module to parse and manipulate JSON data. Below are some exercises to help you practice working with JSON in Python.

---

### **1. Importing the `json` Module**
```python
import json
```

---

### **2. Exercises**

#### **Exercise 1: Parse a JSON String**
- **Task**: Parse the JSON string `{"name": "Alice", "age": 25, "city": "New York"}` and access its values.
- **Hint**: Use `json.loads()`.

```python
import json

data = '{"name": "Alice", "age": 25, "city": "New York"}'
parsed_data = json.loads(data)

print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])
```

---

#### **Exercise 2: Convert a Dictionary to JSON**
- **Task**: Convert a Python dictionary to a JSON string.
- **Hint**: Use `json.dumps()`.

```python
python_dict = {"name": "Alice", "age": 25, "city": "New York"}
json_string = json.dumps(python_dict)

print("JSON String:", json_string)
```

---

#### **Exercise 3: Write JSON to a File**
- **Task**: Write the following dictionary to a JSON file: `{"name": "Alice", "age": 25, "city": "New York"}`.
- **Hint**: Use `json.dump()`.

```python
data = {"name": "Alice", "age": 25, "city": "New York"}

with open("data.json", "w") as file:
    json.dump(data, file)

print("Data written to data.json")
```

---

#### **Exercise 4: Read JSON from a File**
- **Task**: Read the JSON file you created in the previous exercise and print its contents.
- **Hint**: Use `json.load()`.

```python
with open("data.json", "r") as file:
    data = json.load(file)

print("Data from file:", data)
```

---

#### **Exercise 5: Pretty Print JSON**
- **Task**: Pretty print the JSON string `{"name": "Alice", "age": 25, "city": "New York"}` with an indentation of 4.
- **Hint**: Use `json.dumps()` with the `indent` parameter.

```python
python_dict = {"name": "Alice", "age": 25, "city": "New York"}
pretty_json = json.dumps(python_dict, indent=4)

print(pretty_json)
```

---

#### **Exercise 6: Nested JSON Parsing**
- **Task**: Parse the following JSON string and print the name and first friend:
  ```json
  {
      "name": "Alice",
      "friends": [
          {"name": "Bob", "age": 27},
          {"name": "Charlie", "age": 25}
      ]
  }
  ```
- **Hint**: Access nested elements using keys and indices.

```python
json_data = '''
{
    "name": "Alice",
    "friends": [
        {"name": "Bob", "age": 27},
        {"name": "Charlie", "age": 25}
    ]
}
'''

data = json.loads(json_data)
print("Name:", data["name"])
print("First Friend's Name:", data["friends"][0]["name"])
```

---

#### **Exercise 7: Validate JSON**
- **Task**: Write a function to check if a string is valid JSON.
- **Hint**: Use `try` and `except` with `json.loads()`.

```python
def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False

valid_string = '{"name": "Alice", "age": 25}'
invalid_string = '{name: Alice, age: 25}'  # Invalid JSON

print("Valid JSON:", is_valid_json(valid_string))  # Output: True
print("Invalid JSON:", is_valid_json(invalid_string))  # Output: False
```

---

#### **Exercise 8: Convert JSON to a Python Object**
- **Task**: Parse the JSON string `{"name": "Alice", "age": 25}` into a Python dictionary and access its elements.
- **Hint**: Use `json.loads()`.

```python
json_string = '{"name": "Alice", "age": 25}'
python_object = json.loads(json_string)

print("Name:", python_object["name"])
print("Age:", python_object["age"])
```

---

#### **Exercise 9: Update JSON Data**
- **Task**: Add a new key `"gender": "female"` to the dictionary parsed from the JSON string.
- **Hint**: Update the dictionary and convert it back to JSON.

```python
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)

# Update the dictionary
data["gender"] = "female"

# Convert back to JSON
updated_json = json.dumps(data, indent=4)
print(updated_json)
```

---

#### **Exercise 10: Convert JSON Array to Python List**
- **Task**: Parse the JSON array `["red", "green", "blue"]` into a Python list and iterate through it.
- **Hint**: Use `json.loads()`.

```python
json_array = '["red", "green", "blue"]'
python_list = json.loads(json_array)

for color in python_list:
    print(color)
```

---

#### **Exercise 11: Handle Missing Keys Gracefully**
- **Task**: Write a function to safely retrieve a key from JSON data, returning `None` if the key does not exist.
- **Hint**: Use the `get()` method.

```python
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)

def safe_get(json_obj, key):
    return json_obj.get(key, None)

print("Name:", safe_get(data, "name"))
print("City:", safe_get(data, "city"))  # Output: None
```

---

#### **Exercise 12: Merge Two JSON Objects**
- **Task**: Merge the following JSON objects into one:
  - `{"name": "Alice", "age": 25}`
  - `{"city": "New York", "country": "USA"}`
- **Hint**: Use dictionary unpacking.

```python
json1 = '{"name": "Alice", "age": 25}'
json2 = '{"city": "New York", "country": "USA"}'

data1 = json.loads(json1)
data2 = json.loads(json2)

# Merge dictionaries
merged_data = {**data1, **data2}
print(json.dumps(merged_data, indent=4))
```

---

#### **Exercise 13: Filter JSON Data**
- **Task**: Extract all people above the age of 25 from the following JSON:
  ```json
  {
      "people": [
          {"name": "Alice", "age": 25},
          {"name": "Bob", "age": 30},
          {"name": "Charlie", "age": 28}
      ]
  }
  ```
- **Hint**: Use list comprehension.

```python
json_data = '''
{
    "people": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 28}
    ]
}
'''

data = json.loads(json_data)
filtered_people = [person for person in data["people"] if person["age"] > 25]
print(json.dumps(filtered_people, indent=4))
```

---

#### **Exercise 14: Flatten Nested JSON**
- **Task**: Flatten the following JSON:
  ```json
  {
      "name": "Alice",
      "address": {
          "city": "New York",
          "zip": "10001"
      }
  }
  ```
  **Output**:
  ```json
  {
      "name": "Alice",
      "address_city": "New York",
      "address_zip": "10001"
  }
  ```

```python
def flatten_json(nested_json, parent_key='', separator='_'):
    flat_dict = {}
    for key, value in nested_json.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            flat_dict.update(flatten_json(value, new_key, separator))
        else:
            flat_dict[new_key] = value
    return flat_dict

nested = {
    "name": "Alice",
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

flat = flatten_json(nested)
print(json.dumps(flat, indent=4))
```

### **Random Data Generation in Python**

Python provides the `random` module to generate random numbers, shuffle sequences, and simulate random behavior. Additionally, the `numpy` and `faker` libraries are powerful tools for generating random data for more advanced use cases.

---

### **1. Importing Necessary Modules**
```python
import random
import string
import numpy as np
from faker import Faker
```

---

### **2. Generating Random Numbers**

1. **Generate a Random Integer**:
   ```python
   random_int = random.randint(1, 100)  # Random integer between 1 and 100
   print(random_int)
   ```

2. **Generate a Random Float**:
   ```python
   random_float = random.uniform(0.1, 1.0)  # Random float between 0.1 and 1.0
   print(random_float)
   ```

3. **Generate a Random Number in a Range**:
   ```python
   random_range = random.randrange(0, 101, 5)  # Random multiple of 5 between 0 and 100
   print(random_range)
   ```

4. **Generate Random Numbers Using `numpy`**:
   ```python
   random_array = np.random.randint(1, 101, size=10)  # Array of 10 random integers
   print(random_array)
   ```

---

### **3. Randomly Select Elements**

1. **Random Choice from a List**:
   ```python
   items = ['apple', 'banana', 'cherry', 'date']
   choice = random.choice(items)
   print(choice)
   ```

2. **Randomly Select Multiple Elements**:
   ```python
   sample = random.sample(items, 2)  # Select 2 unique items
   print(sample)
   ```

3. **Randomly Shuffle a List**:
   ```python
   random.shuffle(items)
   print(items)
   ```

---

### **4. Generate Random Strings**

1. **Random Letters**:
   ```python
   random_letters = ''.join(random.choices(string.ascii_letters, k=10))  # Random string of 10 letters
   print(random_letters)
   ```

2. **Random Alphanumeric Strings**:
   ```python
   random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
   print(random_string)
   ```

3. **Random Password**:
   ```python
   password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%", k=16))
   print(password)
   ```

---

### **5. Simulate Random Distributions**

1. **Random Gaussian Distribution**:
   ```python
   gauss = random.gauss(mu=0, sigma=1)  # Mean = 0, Standard Deviation = 1
   print(gauss)
   ```

2. **Using `numpy` for Normal Distribution**:
   ```python
   normal_data = np.random.normal(loc=0, scale=1, size=10)  # 10 samples, mean=0, std=1
   print(normal_data)
   ```

3. **Other Distributions with `numpy`**:
   - Uniform Distribution:
     ```python
     uniform_data = np.random.uniform(0, 10, size=10)  # Uniform data between 0 and 10
     print(uniform_data)
     ```

   - Binomial Distribution:
     ```python
     binomial_data = np.random.binomial(n=10, p=0.5, size=10)  # 10 samples, 10 trials, p=0.5
     print(binomial_data)
     ```

---

### **6. Generate Random Data with `Faker`**

The `Faker` library is perfect for generating fake names, addresses, emails, and more.

1. **Basic Usage**:
   ```python
   fake = Faker()
   print("Name:", fake.name())
   print("Address:", fake.address())
   print("Email:", fake.email())
   ```

2. **Generate a List of Fake Data**:
   ```python
   fake_data = [{"name": fake.name(), "email": fake.email(), "city": fake.city()} for _ in range(5)]
   print(fake_data)
   ```

3. **Custom Locale**:
   ```python
   fake = Faker("fr_FR")  # Generate data in French
   print("French Name:", fake.name())
   ```

4. **Generate Random Dates**:
   ```python
   print("Random Date:", fake.date())
   print("Random DateTime:", fake.date_time())
   ```

---

### **7. Random Binary and Boolean Data**

1. **Random Boolean**:
   ```python
   random_bool = random.choice([True, False])
   print(random_bool)
   ```

2. **Random Binary String**:
   ```python
   binary_string = ''.join(random.choices(['0', '1'], k=8))  # 8-bit binary string
   print(binary_string)
   ```

---

### **8. Generate Random DataFrames with `pandas`**

1. **Create a Random DataFrame**:
   ```python
   import pandas as pd

   data = {
       "Name": [fake.name() for _ in range(5)],
       "Age": [random.randint(18, 60) for _ in range(5)],
       "Email": [fake.email() for _ in range(5)]
   }
   df = pd.DataFrame(data)
   print(df)
   ```

2. **Add Random Dates to a DataFrame**:
   ```python
   data["Joining Date"] = [fake.date_this_decade() for _ in range(5)]
   print(pd.DataFrame(data))
   ```

---

### **9. Generate Random JSON Data**

1. **Random JSON Object**:
   ```python
   random_json = {
       "id": random.randint(1, 1000),
       "name": fake.name(),
       "email": fake.email(),
       "address": fake.address(),
       "is_active": random.choice([True, False])
   }
   print(random_json)
   ```

2. **Random JSON Array**:
   ```python
   random_json_array = [
       {"id": i, "name": fake.name(), "email": fake.email()} for i in range(5)
   ]
   print(random_json_array)
   ```

---

### **10. Simulating Random Events**

1. **Flip a Coin**:
   ```python
   coin = random.choice(["Heads", "Tails"])
   print("Coin Flip:", coin)
   ```

2. **Roll a Dice**:
   ```python
   dice = random.randint(1, 6)
   print("Dice Roll:", dice)
   ```

3. **Simulate Lottery Numbers**:
   ```python
   lottery_numbers = random.sample(range(1, 50), 6)  # Select 6 unique numbers from 1 to 49
   print("Lottery Numbers:", lottery_numbers)
   ```

---

### **11. Password Generator**
```python
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choices(characters, k=length))

print("Generated Password:", generate_password(16))
```

---

### **12. Random Color Generator**
```python
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

print("Random Color:", random_color())
```

---

### **13. Random Weighted Choices**
- Generate random outcomes based on specified probabilities.

```python
outcomes = ["Win", "Lose", "Draw"]
weights = [0.5, 0.4, 0.1]  # Probabilities for each outcome
result = random.choices(outcomes, weights=weights, k=10)
print(result)
```

---

### **14. Random Data for Machine Learning**

1. **Generate Random Features**:
   ```python
   X = np.random.rand(100, 5)  # 100 samples, 5 features
   print(X)
   ```

2. **Generate Random Labels**:
   ```python
   y = np.random.choice([0, 1], size=100)  # Binary labels
   print(y)
   ```

##  NumPy 

**NumPy** (short for Numerical Python) is a Python library used for working with arrays, performing mathematical and logical operations, and enabling advanced data manipulation and computation.

---

### **1. Installing NumPy**

If NumPy is not already installed, you can install it using pip:
```bash
pip install numpy
```

---

### **2. Importing NumPy**

```python
import numpy as np
```

---

### **3. NumPy Arrays**

#### **Creating Arrays**

1. **1D Array**:
   ```python
   arr = np.array([1, 2, 3, 4, 5])
   print(arr)
   ```

2. **2D Array (Matrix)**:
   ```python
   arr = np.array([[1, 2, 3], [4, 5, 6]])
   print(arr)
   ```

3. **3D Array**:
   ```python
   arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
   print(arr)
   ```

---

#### **Array Attributes**

1. **Shape**:
   - Returns the dimensions of the array.
   ```python
   arr = np.array([[1, 2, 3], [4, 5, 6]])
   print(arr.shape)  # Output: (2, 3)
   ```

2. **Size**:
   - Returns the total number of elements in the array.
   ```python
   print(arr.size)  # Output: 6
   ```

3. **Data Type**:
   - Returns the type of the array elements.
   ```python
   print(arr.dtype)  # Output: int32 (or int64 depending on your system)
   ```

4. **Number of Dimensions (`ndim`)**:
   - Returns the number of dimensions in the array.
   ```python
   print(arr.ndim)  # Output: 2
   ```

---

#### **Array Initialization**

1. **Zeros**:
   ```python
   zeros = np.zeros((3, 3))
   print(zeros)
   ```

2. **Ones**:
   ```python
   ones = np.ones((2, 4))
   print(ones)
   ```

3. **Identity Matrix**:
   ```python
   identity = np.eye(3)
   print(identity)
   ```

4. **Arange**:
   ```python
   arr = np.arange(0, 10, 2)  # Start, Stop, Step
   print(arr)
   ```

5. **Linspace**:
   - Creates evenly spaced numbers over a specified range.
   ```python
   arr = np.linspace(0, 1, 5)  # 5 equally spaced points between 0 and 1
   print(arr)
   ```

6. **Random Arrays**:
   ```python
   random_arr = np.random.rand(3, 3)  # Uniform distribution
   random_ints = np.random.randint(0, 10, (2, 3))  # Random integers
   ```

---

### **4. Indexing and Slicing**

#### **1D Array**:
```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])     # First element
print(arr[-1])    # Last element
print(arr[1:4])   # Elements from index 1 to 3
```

#### **2D Array**:
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1, 2])       # Access element at row 1, column 2
print(arr[0:2, 1:3])   # Slicing rows 0-1 and columns 1-2
```

---

### **5. Reshaping and Flattening**

1. **Reshape**:
   - Change the shape of the array.
   ```python
   arr = np.array([1, 2, 3, 4, 5, 6])
   reshaped = arr.reshape((2, 3))
   print(reshaped)
   ```

2. **Flatten**:
   - Convert a multi-dimensional array into a 1D array.
   ```python
   flattened = reshaped.flatten()
   print(flattened)
   ```

---

### **6. Basic Operations**

#### **Arithmetic Operations**
- Element-wise operations are supported.
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # Output: [5 7 9]
print(arr1 - arr2)  # Output: [-3 -3 -3]
print(arr1 * arr2)  # Output: [4 10 18]
print(arr1 / arr2)  # Output: [0.25 0.4 0.5]
```

#### **Broadcasting**
- Operations between arrays of different shapes.
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2
print(arr + scalar)  # Adds 2 to each element
```

---

### **7. Statistical Functions**

1. **Sum**:
   ```python
   print(np.sum(arr))            # Sum of all elements
   print(np.sum(arr, axis=0))    # Column-wise sum
   print(np.sum(arr, axis=1))    # Row-wise sum
   ```

2. **Mean, Median, Std**:
   ```python
   print(np.mean(arr))           # Mean of elements
   print(np.median(arr))         # Median
   print(np.std(arr))            # Standard deviation
   ```

3. **Min and Max**:
   ```python
   print(np.min(arr))            # Minimum value
   print(np.max(arr, axis=0))    # Maximum values column-wise
   ```

---

### **8. Matrix Operations**

1. **Dot Product**:
   ```python
   A = np.array([[1, 2], [3, 4]])
   B = np.array([[5, 6], [7, 8]])
   print(np.dot(A, B))  # Matrix multiplication
   ```

2. **Transpose**:
   ```python
   print(A.T)  # Transpose of A
   ```

3. **Inverse**:
   ```python
   from numpy.linalg import inv
   print(inv(A))  # Inverse of A
   ```

4. **Determinant**:
   ```python
   from numpy.linalg import det
   print(det(A))  # Determinant of A
   ```

---

### **9. Logical Operations**

1. **Element-wise Comparison**:
   ```python
   arr = np.array([1, 2, 3, 4])
   print(arr > 2)  # Output: [False False  True  True]
   ```

2. **Logical Operations**:
   ```python
   print(np.logical_and(arr > 1, arr < 4))
   print(np.logical_or(arr == 2, arr == 4))
   ```

3. **Filtering Elements**:
   ```python
   filtered = arr[arr > 2]
   print(filtered)  # Output: [3 4]
   ```

---

### **10. Advanced Features**

1. **Stacking Arrays**:
   ```python
   arr1 = np.array([1, 2, 3])
   arr2 = np.array([4, 5, 6])

   vertical_stack = np.vstack((arr1, arr2))
   horizontal_stack = np.hstack((arr1, arr2))
   ```

2. **Splitting Arrays**:
   ```python
   arr = np.array([1, 2, 3, 4, 5, 6])
   split = np.split(arr, 3)  # Split into 3 equal parts
   print(split)
   ```

3. **Unique Values**:
   ```python
   arr = np.array([1, 2, 2, 3, 4, 4, 4])
   print(np.unique(arr))  # Output: [1 2 3 4]
   ```

4. **Sorting**:
   ```python
   arr = np.array([3, 1, 2, 5, 4])
   print(np.sort(arr))  # Output: [1 2 3 4 5]
   ```

---

### **11. Random Numbers with `numpy.random`**

1. **Generate Random Numbers**:
   ```python
   random_array = np.random.rand(3, 3)  # Uniform distribution
   random_ints = np.random.randint(0, 10, (3, 3))  # Random integers
   ```

2. **Random Seed**:
   ```python
   np.random.seed(42)  # Fixes the random numbers for reproducibility
   print(np.random.rand(3))
   ```

---

### **12. Summary Table**

| **Functionality**         | **Function/Method**                     | **Example**                                      |
|---------------------------|-----------------------------------------|------------------------------------------------|
| Create Array              | `np.array()`                           | `np.array([1, 2, 3])`                          |
| Array Shape               | `.shape`                               | `arr.shape`                                    |
| Initialize Zeros          | `np.zeros()`                           | `np.zeros((2, 3))`                             |
| Initialize Random Numbers | `np.random.rand()`                     | `np.random.rand(2, 3)`                         |
| Reshape Array             | `.reshape()`                           | `arr.reshape(3, 2)`                            |
| Sum of Elements           | `np.sum()`                             | `np.sum(arr, axis=0)`                          |
| Mean                      | `np.mean()`                            | `np.mean(arr)`                                 |
| Transpose                 | `.T`                                   | `arr.T`                                        |
| Dot Product               | `np.dot()`                             | `np.dot(A, B)`                                 |
| Filter Elements           | Array Comparison                       | `arr[arr > 5]`                                 |


## Pandas

**Pandas** is a powerful library in Python used for data manipulation and analysis. It provides two primary data structures: **Series** and **DataFrame**, making it easy to work with structured data like spreadsheets and databases.

---

### **1. Installing Pandas**
If Pandas is not installed, use pip to install it:
```bash
pip install pandas
```

---

### **2. Importing Pandas**
```python
import pandas as pd
```

---

### **3. Pandas Data Structures**

#### **A. Series**
- A **Series** is a one-dimensional array with labels (like a column in a spreadsheet).

**Creating a Series**:
```python
import pandas as pd

# From a list
s = pd.Series([10, 20, 30, 40])
print(s)

# From a dictionary
s = pd.Series({'a': 10, 'b': 20, 'c': 30})
print(s)

# Accessing elements
print(s['a'])  # Output: 10
print(s[1])    # Output: 20
```

---

#### **B. DataFrame**
- A **DataFrame** is a two-dimensional, tabular data structure (like an Excel spreadsheet or SQL table).

**Creating a DataFrame**:
1. **From a Dictionary of Lists**:
   ```python
   data = {
       'Name': ['Alice', 'Bob', 'Charlie'],
       'Age': [25, 30, 35],
       'City': ['New York', 'San Francisco', 'Los Angeles']
   }
   df = pd.DataFrame(data)
   print(df)
   ```

2. **From a List of Dictionaries**:
   ```python
   data = [
       {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
       {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'}
   ]
   df = pd.DataFrame(data)
   ```

3. **From a NumPy Array**:
   ```python
   import numpy as np
   arr = np.array([[1, 2], [3, 4], [5, 6]])
   df = pd.DataFrame(arr, columns=['Col1', 'Col2'])
   print(df)
   ```

4. **From a CSV File**:
   ```python
   df = pd.read_csv('data.csv')
   ```

---

### **4. DataFrame Attributes**

| **Attribute**        | **Description**                          |
|-----------------------|------------------------------------------|
| `df.shape`           | Returns the number of rows and columns. |
| `df.columns`         | Returns column names.                   |
| `df.dtypes`          | Returns data types of columns.          |
| `df.head(n)`         | Returns the first `n` rows (default 5). |
| `df.tail(n)`         | Returns the last `n` rows (default 5).  |
| `df.info()`          | Prints summary of the DataFrame.        |
| `df.describe()`      | Provides statistical summary.           |

---

### **5. Selecting Data**

#### **A. Selecting Columns**
```python
# Single column (returns a Series)
print(df['Name'])

# Multiple columns (returns a DataFrame)
print(df[['Name', 'Age']])
```

#### **B. Selecting Rows**
1. **By Index** (`iloc` for position-based indexing):
   ```python
   print(df.iloc[0])  # First row
   print(df.iloc[1:3])  # Rows 1 and 2
   ```

2. **By Label** (`loc` for label-based indexing):
   ```python
   print(df.loc[0])  # Row with label 0
   print(df.loc[df['Age'] > 25])  # Filter rows where Age > 25
   ```

#### **C. Conditional Selection**
```python
print(df[df['Age'] > 30])  # Rows where Age > 30
```

---

### **6. Adding, Updating, and Deleting Data**

#### **A. Adding Columns**
```python
df['Country'] = ['USA', 'USA', 'USA']  # Adds a new column
```

#### **B. Updating Columns**
```python
df['Age'] = df['Age'] + 1  # Increment all ages by 1
```

#### **C. Deleting Columns**
```python
df.drop('Country', axis=1, inplace=True)  # Deletes 'Country' column
```

#### **D. Adding Rows**
```python
new_row = {'Name': 'David', 'Age': 40, 'City': 'Chicago'}
df = df.append(new_row, ignore_index=True)
```

#### **E. Deleting Rows**
```python
df.drop(0, axis=0, inplace=True)  # Deletes the first row
```

---

### **7. Handling Missing Data**

#### **A. Checking for Missing Values**
```python
print(df.isnull())  # True for missing values
print(df.isnull().sum())  # Count missing values per column
```

#### **B. Dropping Missing Values**
```python
df.dropna(inplace=True)  # Drops rows with any missing values
```

#### **C. Filling Missing Values**
```python
df.fillna(0, inplace=True)  # Replaces missing values with 0
```

---

### **8. Sorting and Filtering**

1. **Sorting by Columns**:
   ```python
   df.sort_values(by='Age', ascending=False, inplace=True)
   ```

2. **Filtering Rows**:
   ```python
   filtered_df = df[df['City'] == 'New York']
   ```

---

### **9. Grouping and Aggregation**

1. **Grouping**:
   ```python
   grouped = df.groupby('City')
   print(grouped['Age'].mean())  # Average age per city
   ```

2. **Aggregation**:
   ```python
   print(df.groupby('City').agg({'Age': ['mean', 'max'], 'Name': 'count'}))
   ```

---

### **10. Merging, Joining, and Concatenating**

#### **A. Merging DataFrames**:
```python
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Age': [25, 30]})

merged_df = pd.merge(df1, df2, on='ID')  # Merges on 'ID'
```

#### **B. Concatenating DataFrames**:
```python
df1 = pd.DataFrame({'Name': ['Alice'], 'Age': [25]})
df2 = pd.DataFrame({'Name': ['Bob'], 'Age': [30]})

concat_df = pd.concat([df1, df2])
```

---

### **11. Reading and Writing Files**

1. **CSV Files**:
   - **Read**:
     ```python
     df = pd.read_csv('data.csv')
     ```
   - **Write**:
     ```python
     df.to_csv('output.csv', index=False)
     ```

2. **Excel Files**:
   - **Read**:
     ```python
     df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
     ```
   - **Write**:
     ```python
     df.to_excel('output.xlsx', index=False)
     ```

3. **JSON Files**:
   - **Read**:
     ```python
     df = pd.read_json('data.json')
     ```
   - **Write**:
     ```python
     df.to_json('output.json', orient='records')
     ```

---

### **12. Plotting with Pandas**
Pandas integrates with Matplotlib for basic plotting.

```python
df['Age'].plot(kind='bar')  # Bar chart
df.plot(x='Name', y='Age', kind='line')  # Line plot
```

---

### **13. Common Pandas Functions**

| **Function**            | **Description**                                   |
|-------------------------|---------------------------------------------------|
| `pd.read_csv()`         | Reads a CSV file into a DataFrame.                |
| `df.head()`             | Displays the first few rows of the DataFrame.     |
| `df.tail()`             | Displays the last few rows of the DataFrame.      |
| `df.info()`             | Provides an overview of the DataFrame.            |
| `df.describe()`         | Generates summary statistics.                     |
| `df.sort_values()`      | Sorts the DataFrame by column(s).                 |
| `df.groupby()`          | Groups data and performs aggregation.             |
| `df.drop()`             | Deletes rows or columns.                          |
| `df.fillna()`           | Fills missing values.                             |
| `df.isnull()`           | Checks for missing values.                        |
| `pd.merge()`            | Merges two DataFrames.                            |

---

### **14. Example Workflow**
```python
import pandas as pd

# Step 1: Load Data
df = pd.read_csv('data.csv')

# Step 2: Inspect Data
print(df.head())
print(df.info())

# Step 3: Clean Data
df.dropna(inplace=True)  # Drop rows with missing values
df['Age'] = df['Age'].astype(int)  # Convert Age to integer

# Step 4: Analyze Data
average_age = df['Age'].mean()
print("Average Age:", average_age)

# Step 5: Visualize Data
df['Age'].plot(kind='hist')
```

## Matplotlib 

**Matplotlib** is a powerful Python library for creating static, interactive, and animated visualizations. It provides a variety of tools to make line plots, bar charts, scatter plots, histograms, and more.

---

### **1. Installing Matplotlib**

If you don’t already have Matplotlib installed, you can install it with:
```bash
pip install matplotlib
```

---

### **2. Importing Matplotlib**

The most commonly used module in Matplotlib is `pyplot`, which provides an interface similar to MATLAB.

```python
import matplotlib.pyplot as plt
```

---

### **3. Basic Plotting**

#### **A. Basic Line Plot**
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
```

#### **B. Plotting Multiple Lines**
```python
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]

plt.plot(x, y1, label="y = x^2", color="blue", linestyle="--")
plt.plot(x, y2, label="y = x^3", color="green")
plt.legend()
plt.title("Multiple Lines")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

---

### **4. Scatter Plots**

Scatter plots are used to show relationships between two variables.

```python
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x, y, color="red", marker="o", s=100)  # 's' controls marker size
plt.title("Scatter Plot Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
```

---

### **5. Bar Charts**

#### **A. Vertical Bar Chart**
```python
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]

plt.bar(categories, values, color="purple")
plt.title("Vertical Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
```

#### **B. Horizontal Bar Chart**
```python
plt.barh(categories, values, color="orange")
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()
```

---

### **6. Histograms**

Histograms are used to represent the frequency distribution of a dataset.

```python
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

plt.hist(data, bins=5, color="green", edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()
```

---

### **7. Pie Charts**

Pie charts represent data as a proportion of a whole.

```python
sizes = [40, 30, 20, 10]
labels = ["A", "B", "C", "D"]
colors = ["gold", "lightblue", "lightgreen", "pink"]
explode = (0.1, 0, 0, 0)  # Explodes the first slice

plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%")
plt.title("Pie Chart Example")
plt.show()
```

---

### **8. Customization**

#### **A. Titles, Labels, and Legends**
- Add title, axis labels, and a legend.
```python
plt.plot([1, 2, 3], [4, 5, 6], label="Line 1")
plt.title("Customized Plot")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.legend()
plt.show()
```

#### **B. Line Styles and Colors**
```python
plt.plot([1, 2, 3], [4, 5, 6], color="red", linestyle="--", linewidth=2, marker="o")
plt.show()
```

| **Style**        | **Code**        |
|-------------------|-----------------|
| Line Style        | `"-"`, `"--"`, `"-."`, `":"` |
| Marker            | `"o"`, `"s"`, `"D"`, `"^"` |
| Colors            | `"red"`, `"blue"`, `"green"`, or HEX codes (`"#FF5733"`) |

---

### **9. Subplots**

#### **A. Create Multiple Subplots**
```python
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(2, 1, 1)  # 2 rows, 1 column, plot 1
plt.plot(x, y1, color="blue")
plt.title("Subplot 1")

plt.subplot(2, 1, 2)  # 2 rows, 1 column, plot 2
plt.plot(x, y2, color="green")
plt.title("Subplot 2")

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
```

#### **B. Using `plt.subplots()`**
```python
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

axes[0, 0].plot([1, 2, 3], [4, 5, 6], color="red")
axes[0, 0].set_title("Plot 1")

axes[0, 1].plot([1, 2, 3], [1, 4, 9], color="blue")
axes[0, 1].set_title("Plot 2")

axes[1, 0].bar(["A", "B", "C"], [5, 7, 3], color="purple")
axes[1, 0].set_title("Bar Chart")

axes[1, 1].hist([10, 20, 20, 30], bins=3, color="green")
axes[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()
```

---

### **10. Annotations**

Add annotations to highlight specific points.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker="o")
plt.title("Annotation Example")

# Add annotation
plt.annotate("This is the peak", xy=(5, 10), xytext=(3, 8),
             arrowprops=dict(facecolor="black", shrink=0.05))
plt.show()
```

---

### **11. Working with Dates**

```python
import matplotlib.dates as mdates
import datetime

dates = [datetime.date(2023, 1, i) for i in range(1, 6)]
values = [10, 20, 15, 25, 30]

plt.plot(dates, values)
plt.gcf().autofmt_xdate()  # Auto-format date labels
plt.title("Date Plot")
plt.show()
```

---

### **12. Saving Figures**

Save the plot as an image file:
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("plot.png", dpi=300, bbox_inches="tight")  # High-resolution PNG
plt.show()
```

---

### **13. Common Functions in Matplotlib**

| **Function**            | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `plt.plot()`            | Plot a line graph.                                   |
| `plt.scatter()`         | Plot a scatter plot.                                 |
| `plt.bar()`             | Create a vertical bar chart.                         |
| `plt.barh()`            | Create a horizontal bar chart.                       |
| `plt.hist()`            | Plot a histogram.                                    |
| `plt.pie()`             | Create a pie chart.                                  |
| `plt.title()`           | Set the title of the plot.                           |
| `plt.xlabel()`          | Label the X-axis.                                    |
| `plt.ylabel()`          | Label the Y-axis.                                    |
| `plt.legend()`          | Add a legend to the plot.                            |
| `plt.savefig()`         | Save the plot to a file.                             |
| `plt.show()`            | Display the plot.                                    |

---

### **14. Example: Full Workflow**
```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Line 1", color="blue", marker="o")
plt.title("Example Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True)

# Save and show the plot
plt.savefig("example_plot.png", dpi=300)
plt.show()
```

### **Working with Databases in Python**

Python provides powerful libraries for working with relational and non-relational databases. The most common database operations involve connecting to a database, querying data, and performing CRUD (Create, Read, Update, Delete) operations.

---

### **1. Database Libraries in Python**

| **Library**      | **Database**                  | **Installation**          |
|-------------------|-------------------------------|---------------------------|
| `sqlite3`        | SQLite (built-in)             | Comes with Python         |
| `mysql-connector`| MySQL                         | `pip install mysql-connector-python` |
| `psycopg2`       | PostgreSQL                    | `pip install psycopg2`    |
| `SQLAlchemy`     | Multiple databases (ORM)      | `pip install sqlalchemy`  |
| `pymongo`        | MongoDB (NoSQL)               | `pip install pymongo`     |

---

### **2. SQLite with `sqlite3`**

SQLite is a lightweight, built-in database for Python. It is perfect for local or small-scale applications.

#### **A. Connecting to a SQLite Database**
```python
import sqlite3

# Connect to (or create) a database file
conn = sqlite3.connect("example.db")

# Create a cursor to execute SQL queries
cursor = conn.cursor()
```

#### **B. Creating a Table**
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()  # Commit the changes
```

#### **C. Inserting Data**
```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()
```

#### **D. Fetching Data**
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # Retrieve all rows
for row in rows:
    print(row)
```

#### **E. Updating Data**
```python
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (30, "Alice"))
conn.commit()
```

#### **F. Deleting Data**
```python
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
conn.commit()
```

#### **G. Closing the Connection**
```python
cursor.close()
conn.close()
```

---

### **3. MySQL with `mysql-connector-python`**

#### **A. Connecting to a MySQL Database**
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
)
cursor = conn.cursor()
```

#### **B. Creating a Table**
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department VARCHAR(255),
    salary FLOAT
)
""")
```

#### **C. Inserting Data**
```python
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", ("John Doe", "HR", 50000))
conn.commit()
```

#### **D. Fetching Data**
```python
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)
```

#### **E. Closing the Connection**
```python
cursor.close()
conn.close()
```

---

### **4. PostgreSQL with `psycopg2`**

#### **A. Connecting to a PostgreSQL Database**
```python
import psycopg2

conn = psycopg2.connect(
    dbname="test_db",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
```

#### **B. Creating a Table**
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC
)
""")
conn.commit()
```

#### **C. Inserting Data**
```python
cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Laptop", 999.99))
conn.commit()
```

#### **D. Fetching Data**
```python
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)
```

#### **E. Closing the Connection**
```python
cursor.close()
conn.close()
```

---

### **5. MongoDB with `pymongo`**

#### **A. Connecting to MongoDB**
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]  # Access the database
collection = db["users"]  # Access the collection
```

#### **B. Inserting Documents**
```python
user = {"name": "Alice", "age": 25}
collection.insert_one(user)
```

#### **C. Fetching Documents**
```python
for user in collection.find():
    print(user)
```

#### **D. Updating Documents**
```python
collection.update_one({"name": "Alice"}, {"$set": {"age": 30}})
```

#### **E. Deleting Documents**
```python
collection.delete_one({"name": "Alice"})
```

#### **F. Closing the Connection**
```python
client.close()
```

---

### **6. Using SQLAlchemy (Object-Relational Mapping - ORM)**

SQLAlchemy is a popular library for interacting with relational databases using Python objects.

#### **A. Setting Up SQLAlchemy**
```bash
pip install sqlalchemy
```

#### **B. Connecting to a Database**
```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db")
```

#### **C. Defining a Model**
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
```

#### **D. Creating the Table**
```python
Base.metadata.create_all(engine)
```

#### **E. Adding Data**
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Alice", age=25)
session.add(new_user)
session.commit()
```

#### **F. Querying Data**
```python
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
```

#### **G. Closing the Session**
```python
session.close()
```

---

### **7. Best Practices**

1. **Use Parameterized Queries**:
   - Avoid SQL injection by using parameterized queries:
   ```python
   cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
   ```

2. **Close Connections**:
   - Always close the database connection after your operations are done to free up resources.

3. **Use ORM for Large Projects**:
   - Libraries like SQLAlchemy simplify working with databases and improve code readability.

4. **Handle Errors Gracefully**:
   - Use `try-except` blocks to handle database errors:
   ```python
   try:
       conn = sqlite3.connect("example.db")
       cursor = conn.cursor()
   except sqlite3.Error as e:
       print("Error:", e)
   ```

---

### **8. Example Workflow for SQLite**
```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL
)
""")

# Insert data
cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", ("John Doe", "Manager", 75000))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

# Close the connection
cursor.close()
conn.close()
```
