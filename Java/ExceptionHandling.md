# Java Exception Handling Questions and Answers

### 1. What are the advantages of exception handling in Java?
**Answer:**
- **Robustness:** Ensures the application continues running even after encountering errors by providing structured handling of exceptions.
- **Error Isolation:** Provides a mechanism to separate error-handling code from regular business logic, making the code more modular.
- **Maintenance:** Improves code readability and maintainability by centralizing error handling in `try-catch` blocks.
- **Custom Exceptions:** Enables developers to create application-specific exceptions that describe issues more accurately.
- **Controlled Termination:** Allows graceful application termination by managing exceptions effectively.

---

### 2. How does the try-with-resources statement work in Java?
**Answer:**
- Introduced in Java 7, the `try-with-resources` statement is used to automatically close resources like files, sockets, and database connections after the `try` block is executed.
- The resources must implement the `AutoCloseable` interface to be compatible with this feature.
- This reduces boilerplate code and ensures resources are closed properly, even if an exception occurs.

Example:
```java
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```
In this example, the `BufferedReader` is automatically closed when the `try` block exits, whether normally or due to an exception.

---

### 3. Can we handle multiple exceptions in a single catch block? How?
**Answer:**
- Yes, starting from Java 7, multiple exceptions can be handled in a single `catch` block using a pipe (`|`) operator.
- This feature reduces redundancy and makes code more concise by avoiding repetitive `catch` blocks.

Example:
```java
try {
    int[] arr = new int[5];
    System.out.println(arr[10]); // ArrayIndexOutOfBoundsException
    String str = null;
    System.out.println(str.length()); // NullPointerException
} catch (ArrayIndexOutOfBoundsException | NullPointerException e) {
    System.out.println("An exception occurred: " + e.getMessage());
}
```
Here, both exceptions are handled in the same block without duplicating code.

---

### 4. What is the difference between Error and Exception?
**Answer:**
- **Error:**
  - Represents serious system-level issues that an application cannot reasonably handle (e.g., `OutOfMemoryError`, `StackOverflowError`).
  - Errors usually indicate problems with the JVM or hardware and are unchecked.
- **Exception:**
  - Represents conditions that applications might want to catch and handle (e.g., `IOException`, `ArithmeticException`).
  - Exceptions can be checked or unchecked.

Key Difference: Errors are unrecoverable, while exceptions are recoverable through proper handling.

---

### 5. What is the difference between IOException and FileNotFoundException?
**Answer:**
- **`IOException`:**
  - A general exception that occurs during input/output operations.
  - It is the parent class for many specific exceptions, including `FileNotFoundException`.
- **`FileNotFoundException`:**
  - A more specific exception that occurs when a file cannot be found or opened.
  - It is a subclass of `IOException`.

Example:
```java
try {
    FileReader reader = new FileReader("nonexistent.txt");
} catch (FileNotFoundException e) {
    System.out.println("File not found.");
} catch (IOException e) {
    System.out.println("I/O exception occurred.");
}
```

---

### 6. Can we rethrow an exception? Provide an example.
**Answer:**
- Yes, an exception can be rethrown to a higher-level method or caller using the `throw` keyword.
- This is useful when the current method cannot fully handle the exception and wants to delegate it.

Example:
```java
public void readFile() throws IOException {
    try {
        FileReader reader = new FileReader("file.txt");
    } catch (IOException e) {
        System.out.println("Logging the exception: " + e.getMessage());
        throw e; // Rethrowing the exception
    }
}
```
Here, the exception is logged and then rethrown for the caller to handle.

---

### 7. What happens when an exception is not handled in Java?
**Answer:**
- When an exception is not caught or handled, it propagates up the call stack.
- If it reaches the top of the stack without being caught, the JVM's default exception handler terminates the program and prints a stack trace.
- Example:
```java
public void divideByZero() {
    int result = 10 / 0; // Throws ArithmeticException
}
```
Output:
```
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at MyClass.divideByZero(MyClass.java:5)
	...
```

---

### 8. What is a stack trace, and how is it useful in debugging?
**Answer:**
- A stack trace is a report showing the active method call sequence at the time of an exception.
- It helps developers pinpoint the exact location and cause of errors in the code.

Example:
```java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    e.printStackTrace(); // Prints the stack trace
}
```
Output:
```
java.lang.ArithmeticException: / by zero
	at MyClass.main(MyClass.java:5)
```
The stack trace indicates the file name and line number where the error occurred.

---

### 9. Can you catch multiple exceptions in one catch block? Provide an example.
**Answer:**
- As mentioned earlier, multiple exceptions can be caught in a single block using the pipe (`|`) operator.
- This is especially useful when the handling logic is the same for multiple exceptions.

Example:
```java
try {
    String[] data = {"10", "abc"};
    int num = Integer.parseInt(data[1]); // NumberFormatException
} catch (ArrayIndexOutOfBoundsException | NumberFormatException e) {
    System.out.println("Exception occurred: " + e.getClass().getSimpleName());
}
```

---

### 10. What is a suppressed exception in Java?
**Answer:**
- A suppressed exception occurs during the closing of a resource in a `try-with-resources` block when another exception is already thrown.
- These exceptions are suppressed and can be retrieved using the `getSuppressed()` method.

Example:
```java
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    throw new IOException("Primary exception");
} catch (IOException e) {
    for (Throwable suppressed : e.getSuppressed()) {
        System.out.println("Suppressed: " + suppressed);
    }
}
```
Here, any exceptions that occur while closing the `BufferedReader` are suppressed and can be accessed for debugging purposes.
