
* **What is Java, and why is it platform-independent?**

	**Answer:**
 
	Java is a high-level, object-oriented programming language that was developed by James Gosling at Sun Microsystems (later acquired by Oracle Corporation) and released in 1995. Java is widely used for building various types of applications, including desktop, web, mobile, and enterprise solutions.
	Key Features of Java

	- **Object-Oriented:** Follows OOP principles like encapsulation, inheritance, and polymorphism.
	- **Simple:** Designed to be easy to learn and use, especially for those familiar with C++.
	- **Secure:** Offers built-in security features like bytecode verification, a secure runtime environment, and APIs for cryptography.
	- **Portable:** Java applications can run on any platform without modification.
	- **Robust:** Provides strong memory management, exception handling, and automatic garbage collection.
	- **High Performance:** Though not as fast as C++, Java uses Just-In-Time (JIT) compilation to achieve near-native performance.
	- **Multithreaded:** Supports concurrent execution of multiple threads for better performance.
	- **Distributed:** Includes APIs like RMI (Remote Method Invocation) for building distributed systems.

	**Why is Java Platform-Independent?**

	Java is platform-independent because of its "Write Once, Run Anywhere" (WORA) philosophy, which is achieved through the use of the Java Virtual Machine (JVM) and bytecode. Here's how:

	- **Source Code Compilation:**
    When you write Java code, it is compiled by the Java Compiler (javac) into an intermediate form called bytecode.
    Bytecode is a platform-neutral representation of the code.

	- **Java Virtual Machine (JVM):**
    The JVM is responsible for executing the bytecode. It acts as an abstraction layer between the compiled Java program and the underlying hardware or operating system.
    Different platforms have their own JVM implementations, but all JVMs can execute the same bytecode.

	- **Platform Independence:**
    Since the bytecode is the same regardless of the underlying hardware or operating system, Java programs can run on any platform with a compatible JVM.
    For example, you can compile a Java program on Windows and run it on Linux, macOS, or any other OS without recompilation.
		

* **Explain the structure of a Java program.**		

	**Answer:**
	A Java program follows a specific structure to ensure clarity and functionality. Below is an overview of the main components and their roles in a typical Java program.



	**Basic Structure of a Java Program**

	```java
	// 1. Package Declaration (Optional)
	package com.example;

	// 2. Import Statements (Optional)
	import java.util.Scanner;

	// 3. Class Declaration
	public class MyClass {

		// 4. Main Method (Entry Point)
		public static void main(String[] args) {

			// 5. Statements and Code
			System.out.println("Hello, World!");
		}

		// 6. Other Methods (Optional)
		public void myMethod() {
			System.out.println("This is a custom method.");
		}
	}
	```


* **What are identifiers and literals in Java?**

	**Answer:**

	**Identifiers in Java**

	Identifiers are the names used to represent variables, methods, classes, or other elements in a Java program. They must start with a letter, underscore (_), or dollar sign ($), followed by letters, digits, or underscores. Identifiers cannot be Java keywords and are case-sensitive. For example, age, calculateSum, and _temp are valid identifiers.

	**Literals in Java**

	Literals are fixed values directly assigned to variables in the code. They represent constant data types like numbers, characters, or strings. Examples include:

		Integer: 10
		Floating-point: 3.14
		Character: 'A'
		String: "Hello"
		Boolean: true, false.

	These values cannot be modified.


* **Describe the differences between primitive and non-primitive data types.**

	**Answer:**  

	Java provides two categories of data types: **Primitive** and **Non-Primitive**. Below is a comparison highlighting their key differences:

| **Aspect**              | **Primitive Data Types**                                   | **Non-Primitive Data Types**                                  |
|--------------------------|----------------------------------------------------------|-------------------------------------------------------------|
| **Definition**           | Basic built-in data types provided by Java.              | Custom or complex types defined by users or Java.           |
| **Examples**             | `int`, `float`, `char`, `boolean`, `double`, `byte`.     | `String`, `Array`, `Class`, `Interface`, `Object`.          |
| **Memory Usage**         | Stores actual values directly in memory.                 | Stores references (memory addresses) to the actual objects. |
| **Size**                 | Fixed for each type (e.g., `int` is 4 bytes).            | Depends on the object and its structure.                    |
| **Null Values**          | Cannot be `null`.                                         | Can be `null`.                                              |
| **Methods**              | Do not have methods.                                      | Have built-in methods (e.g., `String.length()`).            |
| **Performance**          | Faster and more efficient.                               | Slower due to additional overhead of object manipulation.   |
| **Usage**                | Used for simple values (e.g., numbers, characters).      | Used for complex structures (e.g., strings, collections).   |



	**Examples**

	**Primitive Data Type Example**
	```java
	int age = 25;
	char grade = 'A';
	boolean isPassed = true;
	```

	**Non-Primitive Data Type Example**

	```
	String name = "John";
	int[] numbers = {1, 2, 3, 4, 5};
	Object obj = new Object();
	```

	**Key Takeaways**

	- Primitive Types are simpler and more performance-efficient but lack advanced features.
	- Non-Primitive Types are more versatile, supporting methods and structures but with additional overhead.
	
	

* **What are reserved keywords in Java? List some examples.**

	**Answer:**  
	Reserved keywords in Java are predefined words that have special meanings and purposes in the language. These keywords are part of the Java syntax and cannot be used as identifiers (e.g., variable names, class names, or method names).


	**Characteristics of Reserved Keywords**

	- **Case-Sensitive**: All keywords must be written in lowercase.
	- **Fixed Purpose**: Each keyword has a specific function and cannot be repurposed.
	- **Integral to Syntax**: They form the foundation of Java programming.


	**Examples of Reserved Keywords**

	Java has **53 reserved keywords**, which include control flow statements, data types, modifiers, and others. Below are some examples:

	**Control Statements**
	- `if`, `else`, `switch`, `case`, `default`
	- `for`, `while`, `do`, `break`, `continue`

	**Data Types**
	- `int`, `float`, `double`, `boolean`, `char`, `byte`, `short`, `long`

	**Access Modifiers**
	- `public`, `private`, `protected`

	**Class and Object Keywords**
	- `class`, `interface`, `extends`, `implements`, `this`, `super`

	**Exception Handling**
	- `try`, `catch`, `finally`, `throw`, `throws`

	**Others**
	- `return`, `void`, `static`, `final`, `abstract`, `synchronized`, `volatile`, `transient`



	**Notes**

	1. **Reserved Literals**: Java also includes reserved literals like `true`, `false`, and `null` which are technically not keywords but are reserved for specific uses.
	2. **Future Reserved Words**: Some words like `const` and `goto` are reserved but not currently in use.


	### Example Program Using Reserved Keywords
	```java
	public class KeywordExample {
		public static void main(String[] args) {
			int number = 10;
			if (number > 5) {
				System.out.println("Number is greater than 5");
			} else {
				System.out.println("Number is 5 or less");
			}
		}
	}
	```


	### Key Takeaways

	- Reserved keywords form the building blocks of Java programming.
	- They cannot be redefined or used as custom identifiers.
	- Familiarity with these keywords is essential for writing syntactically correct Java programs.



* **Explain the concept of type promotion in expressions.**

	**Answer:**
	Type promotion in Java refers to the automatic conversion of smaller data types (e.g., `byte`, `short`, `char`) to larger data types (e.g., `int`, `long`, `float`, `double`) when evaluating expressions. This ensures precision and consistency during calculations.



### Rules of Type Promotion

1. **Small Data Types to `int`**:
   - In expressions, `byte`, `short`, and `char` are automatically promoted to `int` if they are involved in any operation.
   - Example:
     ```java
     byte b1 = 10, b2 = 20;
     int sum = b1 + b2; // Promotes `b1` and `b2` to `int`
     ```

2. **Wider Data Type Determines Result**:
   - If different data types are involved in an expression, the smaller type is promoted to the larger type.
   - Example:
     ```java
     int a = 10;
     double b = 5.5;
     double result = a + b; // `a` is promoted to `double`
     ```

3. **Promotion Hierarchy**:
   - `byte` → `short` → `int` → `long` → `float` → `double`

4. **Character Promotion**:
   - Characters are promoted to their Unicode `int` value during operations.
   - Example:
     ```java
     char ch = 'A'; // Unicode value of 'A' is 65
     int result = ch + 1; // Promoted to `int`, result is 66
     ```

---

### Example of Type Promotion
```java
public class TypePromotionExample {
    public static void main(String[] args) {
        byte b = 10;
        short s = 20;
        int i = 30;
        float f = 5.5f;
        double d = 15.5;

        // Expression with multiple types
        double result = b + s + i + f + d; // All promoted to `double`
        System.out.println("Result: " + result);
    }
}

```


### Key Points to Remember

  - Type promotion ensures precision during calculations by converting smaller types to larger types automatically.
  - Operations involving byte, short, and char always result in an int.
  - Mixed-type expressions follow the promotion hierarchy, ensuring no loss of information.
	
	
### Use Cases

  - Mathematical operations involving multiple data types.
  - Avoiding explicit type casting in simple arithmetic expressions.	
	


* **What is the purpose of the main() method in Java?**

**Answer:**

The `main()` method in Java is the **entry point** of any standalone Java application. When a program is executed, the Java Virtual Machine (JVM) begins execution by calling the `main()` method.

---

### Syntax of `main()` Method

```java
public static void main(String[] args) {
    // Program logic goes here
}
```


### Explanation of Keywords:

  - public: Makes the method accessible from anywhere, ensuring the JVM can call it.
  - static: Allows the method to be invoked without creating an instance of the class.
  - void: Indicates the method does not return any value.
  - String[] args: Accepts command-line arguments as an array of String.


### Purpose of the main() Method

  - Entry Point: The JVM starts program execution from the main() method.
  - Command-Line Arguments: Enables passing data to the program at runtime.
  - Execution Control: Serves as the central control point for invoking other methods or classes.



### Example of a main() Method


```
public class MainExample {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        // Accessing command-line arguments
        if (args.length > 0) {
            System.out.println("First argument: " + args[0]);
        }
    }
}

```

### Execution:

  - Compile: javac MainExample.java
  - Run: java MainExample Hello
    Output:
	```
	Hello, World!
	First argument: Hello

	```
Key Points

  - The main() method must always follow the correct syntax for the JVM to recognize it.
  - It is possible to overload the main() method, but only the standard version is called by the JVM.
  - In GUI or web applications, the main() method is typically used to initialize the program or start the application server.



* **What is the difference between ++i and i++?**

**Answer**

In Java, both `++i` and `i++` are increment operators used to increase the value of a variable by 1. However, they behave differently depending on their usage in expressions.

---

### Key Differences

| **Aspect**              | **`++i` (Pre-Increment)**                          | **`i++` (Post-Increment)**                       |
|--------------------------|---------------------------------------------------|-------------------------------------------------|
| **Operation Order**      | Increments the value of `i` first, then uses it.  | Uses the current value of `i`, then increments. |
| **Execution**            | The increment happens **before** the value is used. | The increment happens **after** the value is used. |
| **Usage in Expressions** | Updated value is returned immediately.            | Original value is returned, then updated.       |

---

### Example and Behavior

### Pre-Increment (`++i`)
```java
int i = 5;
int result = ++i; // i is incremented first, then assigned to result.
System.out.println("i: " + i);        // Output: 6
System.out.println("result: " + result); // Output: 6
```

### Post-Increment (i++)
```
int i = 5;
int result = i++; // i is assigned to result first, then incremented.
System.out.println("i: " + i);        // Output: 6
System.out.println("result: " + result); // Output: 5

```

## Key Points

1. **Standalone Usage**:
   - When used alone (e.g., `i++` or `++i`), both perform the same operation, incrementing the value of `i` by 1.
   - Example:
   ```java
     int i = 5;
     i++;
     System.out.println(i); // Output: 6
   ```

2. **Usage in Expressions**:
   - The difference becomes evident when used in expressions, as the order of increment affects the result.

---

### Visual Summary

 - **`++i` (Pre-Increment)**:
  - Increments first → Uses updated value.
 - **`i++` (Post-Increment)**:
  - Uses current value → Increments after usage.
  
  
  

* **What are wrapper classes in Java? Why are they used?** 

**Answer**

Wrapper classes in Java are objects that wrap around primitive data types and allow them to be treated as objects. They are part of the `java.lang` package and provide a way to work with primitive types as objects. Each primitive type has a corresponding wrapper class:

| **Primitive Type** | **Wrapper Class**   |
|---------------------|---------------------|
| `byte`              | `Byte`              |
| `short`             | `Short`             |
| `int`               | `Integer`           |
| `long`              | `Long`              |
| `float`             | `Float`             |
| `double`            | `Double`            |
| `char`              | `Character`         |
| `boolean`           | `Boolean`           |

---

## Why are Wrapper Classes Used?

1. **Object Manipulation**:
   - Wrapper classes allow primitive types to be used as objects, which is essential when working with Java collections like `ArrayList`, which do not support primitive types.

2. **Utility Methods**:
   - Wrapper classes provide methods for converting between strings and their respective primitive types (e.g., `Integer.parseInt()` for converting a `String` to an `int`).

3. **Autoboxing and Unboxing**:
   - Java supports **autoboxing** (automatic conversion of primitives to their wrapper classes) and **unboxing** (automatic conversion of wrapper objects to primitives), making it easier to work with collections and primitive types.
   ```java
   int num = 5;
   Integer wrapper = num; // Autoboxing
   int newNum = wrapper;  // Unboxing
	```

4. **Null Handling:**

    Wrapper classes can be assigned null, making them useful in scenarios where a value might be absent (e.g., handling database queries).

5. **Constants and Immutable Nature:**

    Wrapper classes provide constants like Integer.MAX_VALUE and Double.MIN_VALUE for specific type ranges.
    They are immutable, ensuring that the value cannot be changed once created, which helps in maintaining data integrity.


### Example of Wrapper Classes

### Autoboxing and Unboxing

```
// Autoboxing: primitive to wrapper class
int num = 10;
Integer wrapperNum = num; // int to Integer

// Unboxing: wrapper class to primitive
Integer wrapper = 20;
int primitiveNum = wrapper; // Integer to int

```


### Using Wrapper Class Methods

```
String str = "123";
int parsedInt = Integer.parseInt(str); // Converts String to int

double value = 15.75;
String strValue = Double.toString(value); // Converts double to String

```

### Key Takeaways

   - Wrapper classes are used to treat primitive types as objects.
   - They enable the use of primitive types in collections and provide utility methods for conversions.
   - Autoboxing and unboxing make conversions between primitives and wrapper classes seamless.
   - Wrapper classes help manage null values and provide useful constants.



* **What is the difference between == and equals() in Java?**

**Answer**

In Java, both `==` and `equals()` are used for comparison, but they serve different purposes. Understanding the difference is essential for accurate comparisons between objects and primitives.

---

### `==` Operator

 - **Purpose**: Compares **references** (memory addresses) of objects or **values** of primitive data types.
 - **Usage**: Checks if two variables point to the same memory location or if their primitive values are the same.
 - **Example**:
  ```java
   int a = 10;
   int b = 10;
   System.out.println(a == b); // Output: true (compares primitive values)

   String str1 = new String("Hello");
   String str2 = new String("Hello");
   System.out.println(str1 == str2); // Output: false (compares memory references)
  ```

### equals() Method

  Purpose: Compares the contents of objects for equality.
  Usage: Checks if two objects have the same state or values. This method is overridden in most classes, such as String, to compare the actual contents.
  Example:

```
String str1 = new String("Hello");
String str2 = new String("Hello");
System.out.println(str1.equals(str2)); // Output: true (compares contents)

```

### Key Differences

| **Aspect**              | **`==` Operator**                            | **`equals()` Method**                           |
|-------------------------|-----------------------------------------------|-------------------------------------------------|
| **Type of Comparison**  | Compares references (objects) or primitive values. | Compares contents or values of objects.       |
| **Default Behavior**    | For objects, `==` checks if references are the same. | By default, `equals()` behaves like `==`.    |
| **Common Use Case**     | Used for comparing primitive types and reference checks. | Used for content comparison in objects.     |



### Example Scenarios

### Primitive Types

```
int x = 5;
int y = 5;
System.out.println(x == y); // true (compares primitive values)

```

### Object References

```
String a = new String("Hello");
String b = new String("Hello");
System.out.println(a == b); // false (different memory locations)
System.out.println(a.equals(b)); // true (same content)

```


### Custom equals() Method

To ensure proper content comparison, classes should override the equals() method:

 ```
 public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return age == person.age && name.equals(person.name);
    }
 }

 ```

## Key Takeaways

  - Use == for comparing primitive types and checking reference equality for objects.
  - Use equals() for checking the logical equality of object contents.
  - Always override equals() when comparing custom objects for equality.
	
	
