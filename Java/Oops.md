
# Java OOPs Questions and Answers

### 1. What are objects and classes in Java?
**Answer:**
- **Class**: A blueprint or template for creating objects. It defines properties (fields) and behaviors (methods).
- **Object**: An instance of a class. It represents a real-world entity with a state (attributes) and behavior (methods).

```java
class Car {
    String brand;
    int speed;

    void accelerate() {
        speed += 10;
    }
}

Car car = new Car(); // Object of class Car
```

---

### 2. How does method overloading work in Java? Give an example.
**Answer:**
- Method overloading allows multiple methods with the same name but different parameter lists (type, number, or order).
- It provides compile-time polymorphism.

```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}
```

---

### 3. What is method overriding, and how is it different from overloading?
**Answer:**
- **Method Overriding**: Redefining a method in a subclass that exists in the parent class. It provides runtime polymorphism.
- **Difference**:
  - Overloading happens within the same class, overriding occurs across a superclass and subclass.
  - Overloading is resolved at compile time, overriding at runtime.

```java
class Parent {
    void display() {
        System.out.println("Parent method");
    }
}

class Child extends Parent {
    @Override
    void display() {
        System.out.println("Child method");
    }
}
```

---

### 4. Explain the difference between an abstract class and an interface.
**Answer:**
| Feature             | Abstract Class                      | Interface                              |
|---------------------|-------------------------------------|---------------------------------------|
| Inheritance         | Single inheritance                 | Multiple inheritance                  |
| Method Types        | Can have abstract and concrete     | Only abstract methods (until Java 7), default and static methods (Java 8+) |
| Fields              | Can have instance variables        | Only constants                        |
| Keywords            | `abstract`                         | `interface`                           |

```java
abstract class Animal {
    abstract void makeSound();
}

interface Vehicle {
    void start();
}
```

---

### 5. What is multiple inheritance, and how is it implemented in Java?
**Answer:**
- Multiple inheritance refers to a class inheriting from more than one class or interface.
- Java does not support multiple inheritance with classes to avoid the Diamond Problem.
- It is achieved using interfaces.

```java
interface A {
    void methodA();
}

interface B {
    void methodB();
}

class C implements A, B {
    public void methodA() {
        System.out.println("Method A");
    }

    public void methodB() {
        System.out.println("Method B");
    }
}
```

---

### 6. What is the role of constructors in Java? Can we have a private constructor?
**Answer:**
- **Role**: Constructors initialize an object when it is created.
- Yes, we can have a private constructor. It is used in Singleton design patterns.

```java
class Singleton {
    private static Singleton instance;
    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

---

### 7. How does the super keyword work with inheritance?
**Answer:**
- **`super`** is used to access methods or constructors of the parent class.
- It is used to:
  - Call the superclass constructor.
  - Access superclass methods and fields.

```java
class Parent {
    Parent(String name) {
        System.out.println("Parent: " + name);
    }
}

class Child extends Parent {
    Child(String name) {
        super(name);
    }
}
```

---

### 8. What are static and dynamic binding in Java?
**Answer:**
- **Static Binding**: Method calls resolved at compile-time (e.g., private, final, or static methods).
- **Dynamic Binding**: Method calls resolved at runtime (e.g., overridden methods).

```java
class Parent {
    void display() {
        System.out.println("Parent method");
    }
}

class Child extends Parent {
    @Override
    void display() {
        System.out.println("Child method");
    }
}
```

---

### 9. What is an inner class? Differentiate between a static inner class and a non-static inner class.
**Answer:**
- **Inner Class**: A class defined within another class.
- **Static Inner Class**:
  - Can be accessed without creating an instance of the outer class.
  - Does not have access to instance members of the outer class.
- **Non-Static Inner Class**:
  - Requires an instance of the outer class.
  - Can access all members of the outer class.

```java
class Outer {
    class NonStaticInner {}
    static class StaticInner {}
}
```

---

### 10. How are objects compared in Java? What is the role of the compareTo() method?
**Answer:**
- Objects are compared using:
  - `==` for reference comparison.
  - `.equals()` for value comparison.
- **`compareTo()`**:
  - Used for natural ordering (e.g., sorting).
  - Returns:
    - Negative: Current object < argument.
    - Zero: Current object == argument.
    - Positive: Current object > argument.

```java
class Person implements Comparable<Person> {
    String name;

    public int compareTo(Person other) {
        return this.name.compareTo(other.name);
    }
}
```



