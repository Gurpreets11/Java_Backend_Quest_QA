
# Java Keywords Explained with Examples

## 1. What is the purpose of the `volatile` keyword in Java?
The `volatile` keyword in Java is used to indicate that a variable's value may be changed by multiple threads. It ensures visibility and ordering of changes to the variable across threads, preventing cached copies of the variable in CPU registers or local caches.

### Example:
```java
class SharedResource {
    private volatile boolean flag = false;

    public void setFlagTrue() {
        flag = true;
    }

    public void printFlag() {
        while (!flag) {
            // Waiting for the flag to change
        }
        System.out.println("Flag is now true");
    }
}
```

## 2. Explain the `strictfp` keyword.
The `strictfp` keyword ensures that floating-point calculations (like addition, multiplication, division, etc.) follow the IEEE 754 standard for portability and consistency across platforms.

### Example:
```java
strictfp class Calculator {
    public double add(double a, double b) {
        return a + b;
    }
}
```

## 3. How does the `native` keyword work in Java?
The `native` keyword is used to declare a method that is implemented in platform-dependent code, typically written in languages like C or C++. Native methods enable interaction with low-level operating system functions.

### Example:
```java
class NativeExample {
    public native void displayMessage();

    static {
        System.loadLibrary("nativeLib"); // Load native library
    }
}
```

## 4. What is the purpose of the `assert` keyword?
The `assert` keyword is used to create assertions in Java, which are conditions that must be true during the program's execution. Assertions are primarily used for debugging.

### Example:
```java
public class AssertExample {
    public static void main(String[] args) {
        int number = 10;
        assert number > 0 : "Number must be positive";
        System.out.println("Number is: " + number);
    }
}
```

## 5. How does the `instanceof` operator work in Java?
The `instanceof` operator checks whether an object is an instance of a specific class or subclass. It is often used in type checking.

### Example:
```java
class Animal {}
class Dog extends Animal {}

public class InstanceofExample {
    public static void main(String[] args) {
        Animal animal = new Dog();
        System.out.println(animal instanceof Dog); // true
        System.out.println(animal instanceof Animal); // true
    }
}
```

## 6. What is the use of the `synchronized` keyword?
The `synchronized` keyword is used to control access to critical sections or shared resources in multithreading environments. It prevents race conditions by allowing only one thread at a time to execute a synchronized block or method.

### Example:
```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}
```

## 7. Explain the `transient` keyword with an example.
The `transient` keyword prevents a variable from being serialized. It is useful for variables that do not need to be saved as part of an object's state.

### Example:
```java
import java.io.*;

class TransientExample implements Serializable {
    private String name;
    private transient int age;

    public TransientExample(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Age: " + age;
    }
}
```

## 8. What is the purpose of the `enum` keyword?
The `enum` keyword is used to define a set of named constants. Enums are type-safe and can include fields, methods, and constructors.

### Example:
```java
enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;
}

public class EnumExample {
    public static void main(String[] args) {
        Day today = Day.FRIDAY;
        System.out.println("Today is: " + today);
    }
}
```

## 9. What is the difference between `abstract` and `final` keywords in Java?
- **`abstract`**: Used to declare a class or method that must be implemented by subclasses. An abstract class cannot be instantiated.
- **`final`**: Used to declare constants, prevent method overriding, or inheritance.

### Example:
```java
abstract class Shape {
    abstract void draw();
}

final class Constants {
    public static final double PI = 3.14159;
}
```

## 10. What are access modifiers in Java, and how do they work?
Access modifiers define the visibility of classes, methods, and variables. They are:
- **`public`**: Accessible from everywhere.
- **`protected`**: Accessible within the same package and subclasses.
- **`default`**: Accessible within the same package.
- **`private`**: Accessible only within the defining class.

### Example:
```java
public class AccessModifiers {
    public int publicVar;
    protected int protectedVar;
    int defaultVar;
    private int privateVar;

    public void accessExample() {
        privateVar = 10; // Allowed
    }
}
