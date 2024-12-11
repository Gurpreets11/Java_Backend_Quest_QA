# Java String Questions and Answers

### 1. How is a String object created in Java?
**Answer:**
- A `String` object can be created in two primary ways:
  1. **Using string literals**:
     ```java
     String str = "Hello";
     ```
     - Stored in the **String pool**, a special memory area in the JVM for strings, for memory optimization.
  2. **Using the `new` keyword**:
     ```java
     String str = new String("Hello");
     ```
     - Creates a new `String` object in the heap memory, even if the same string exists in the pool.
     - Avoid unless explicitly needed to create a distinct object.

---

### 2. What is the difference between String and CharSequence?
**Answer:**
- `CharSequence` is an interface representing a sequence of characters, while `String` is a concrete implementation of `CharSequence`.
- **Key differences:**
  - `CharSequence` is a general-purpose API for various string-like objects (e.g., `String`, `StringBuilder`, `StringBuffer`).
  - `String` is immutable and provides additional methods for manipulating and comparing strings.

---

### 3. Explain the purpose of the String.intern() method.
**Answer:**
- The `intern()` method ensures that a string is stored in the **String pool**.
- If the string already exists in the pool, it returns the reference; otherwise, it adds the string to the pool.
- This helps in saving memory by avoiding duplicate string objects.

Example:
```java
String s1 = new String("Java").intern();
String s2 = "Java";
System.out.println(s1 == s2); // true
```

---

### 4. What is the use of the split() method in the String class?
**Answer:**
- The `split()` method splits a string into an array of substrings using a specified delimiter (regular expression).

Example:
```java
String str = "apple,banana,grape";
String[] fruits = str.split(",");
for (String fruit : fruits) {
    System.out.println(fruit);
}
```

---

### 5. How can you reverse a String in Java without using a library?
**Answer:**
- Reversing a string manually involves iterating over its characters in reverse order and building the reversed string.

Example:
```java
public class ReverseString {
    public static String reverse(String str) {
        StringBuilder reversed = new StringBuilder();
        for (int i = str.length() - 1; i >= 0; i--) {
            reversed.append(str.charAt(i));
        }
        return reversed.toString();
    }
}
```

---

### 6. How can you check if a String is a palindrome?
**Answer:**
- A palindrome reads the same backward as forward. This can be checked by comparing characters from the beginning and end of the string.

Example:
```java
public class PalindromeChecker {
    public static boolean isPalindrome(String str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```

---

### 7. Explain how String.format() works.
**Answer:**
- `String.format()` allows for dynamic construction of formatted strings using placeholders like `%s` (string), `%d` (integer), `%f` (float), etc.

Example:
```java
String name = "John";
int score = 85;
String formatted = String.format("Hello %s, you scored %d marks!", name, score);
System.out.println(formatted);
```

---

### 8. How does the String.join() method work?
**Answer:**
- The `join()` method concatenates multiple strings with a specified delimiter in between.

Example:
```java
String result = String.join(", ", "apple", "banana", "grape");
System.out.println(result); // Output: apple, banana, grape
```

---

### 9. What are escape sequences in strings? Provide examples.
**Answer:**
- Escape sequences are special characters prefixed with a backslash (`\`) that represent certain actions or characters.
  - Examples:
    - `\n`: Newline
    - `\t`: Tab
    - `\\`: Backslash
    - `\"`: Double quote

Example:
```java
String str = "Hello\nWorld";
System.out.println(str);
```
Output:
```
Hello
World
```

---

### 10. Compare the efficiency of String concatenation using + operator and StringBuilder.
**Answer:**
- **`+` operator:**
  - Creates new string objects for each concatenation, leading to higher memory usage.
  - Inefficient for repetitive concatenation in loops.

- **`StringBuilder`:**
  - Uses a mutable buffer, reducing memory overhead.
  - Best choice for multiple or repetitive string manipulations.

Example:
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");
System.out.println(sb.toString());
```
