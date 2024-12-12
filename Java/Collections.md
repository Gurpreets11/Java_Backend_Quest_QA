
# Java Collections Framework Questions and Answers

### 1. What is the hierarchy of the Java Collections Framework?
**Answer:**
The Java Collections Framework is a set of classes and interfaces for storing and manipulating groups of objects. Its hierarchy is structured as follows:

- **Interfaces:**
  - `Collection`
    - `List`
      - `ArrayList`, `LinkedList`, `Vector`, `Stack`
    - `Set`
      - `HashSet`, `LinkedHashSet`, `TreeSet`
    - `Queue`
      - `PriorityQueue`, `Deque`
  - `Map`
    - `HashMap`, `LinkedHashMap`, `TreeMap`, `Hashtable`

- **Root Interfaces:**
  - `Iterable`: Parent of `Collection`
  - `Map`: Separate interface for key-value pairs

**Key Points:**
- `List` is for ordered collections allowing duplicates.
- `Set` ensures uniqueness of elements.
- `Map` is for key-value pairs.

---

### 2. What is the difference between List, Set, and Map?
**Answer:**
| Feature       | `List`                   | `Set`                   | `Map`                                  |
|---------------|--------------------------|--------------------------|----------------------------------------|
| **Order**     | Maintains insertion order| No guaranteed order (except `LinkedHashSet`) | Maintains key-value mapping order (e.g., `TreeMap` sorts keys) |
| **Duplicates**| Allows duplicates        | Does not allow duplicates| Keys are unique; values can be duplicated |
| **Examples**  | `ArrayList`, `LinkedList`| `HashSet`, `TreeSet`     | `HashMap`, `TreeMap`                   |

**Example:**
```java
List<Integer> list = new ArrayList<>();
list.add(1); list.add(1); // Duplicates allowed

Set<Integer> set = new HashSet<>();
set.add(1); set.add(1); // Duplicate ignored

Map<Integer, String> map = new HashMap<>();
map.put(1, "One"); map.put(1, "Uno"); // Key overwritten
```

---

### 3. Explain the difference between LinkedHashMap and HashMap.
**Answer:**
- **`HashMap`**:
  - Does not maintain any order of its elements.
  - Faster than `LinkedHashMap` as it does not maintain ordering.

- **`LinkedHashMap`**:
  - Maintains insertion order of elements.
  - Slightly slower than `HashMap` due to ordering overhead.

**Example:**
```java
Map<Integer, String> hashMap = new HashMap<>();
hashMap.put(1, "One");
hashMap.put(2, "Two");
System.out.println(hashMap); // Random order

Map<Integer, String> linkedHashMap = new LinkedHashMap<>();
linkedHashMap.put(1, "One");
linkedHashMap.put(2, "Two");
System.out.println(linkedHashMap); // Insertion order
```

---

### 4. What is the difference between Queue and Deque?
**Answer:**
- **`Queue`**:
  - Follows the FIFO (First-In-First-Out) principle.
  - Examples: `PriorityQueue`, `LinkedList`.

- **`Deque`**:
  - Stands for Double-Ended Queue.
  - Allows insertion and deletion from both ends.
  - Examples: `ArrayDeque`, `LinkedList`.

**Example:**
```java
Queue<Integer> queue = new LinkedList<>();
queue.add(1); queue.add(2);
System.out.println(queue.poll()); // Removes 1 (FIFO)

Deque<Integer> deque = new ArrayDeque<>();
deque.addFirst(1); deque.addLast(2);
System.out.println(deque.pollLast()); // Removes 2
```

---

### 5. What are NavigableSet and NavigableMap? Give examples.
**Answer:**
- **`NavigableSet`**:
  - A `SortedSet` with additional methods for navigation like `lower()`, `higher()`, `ceiling()`, and `floor()`.
  - Example: `TreeSet`.

- **`NavigableMap`**:
  - A `SortedMap` with additional navigation methods.
  - Example: `TreeMap`.

**Example:**
```java
NavigableSet<Integer> navigableSet = new TreeSet<>();
navigableSet.add(10);
navigableSet.add(20);
System.out.println(navigableSet.lower(15)); // Output: 10

NavigableMap<Integer, String> navigableMap = new TreeMap<>();
navigableMap.put(1, "One");
navigableMap.put(2, "Two");
System.out.println(navigableMap.floorEntry(1).getValue()); // Output: One
```

---

### 6. How does a TreeMap maintain its order?
**Answer:**
- A `TreeMap` maintains its order using the natural ordering of its keys or a custom `Comparator` provided at the time of creation.
- It implements a Red-Black Tree internally, ensuring that the elements are always sorted.

**Example:**
```java
Map<Integer, String> treeMap = new TreeMap<>();
treeMap.put(2, "Two");
treeMap.put(1, "One");
System.out.println(treeMap); // Output: {1=One, 2=Two}
```

---

### 7. What is the difference between Comparable and Comparator?
**Answer:**
- **`Comparable`**:
  - Used to define natural ordering.
  - Implemented using the `compareTo()` method.
  - Example: `String`, `Integer`.

- **`Comparator`**:
  - Used for custom ordering.
  - Implemented using the `compare()` method.

**Example:**
```java
class Student implements Comparable<Student> {
    int rollNo;
    @Override
    public int compareTo(Student o) {
        return this.rollNo - o.rollNo;
    }
}

Comparator<Student> byName = Comparator.comparing(student -> student.name);
```

---

### 8. How is HashSet implemented internally in Java?
**Answer:**
- A `HashSet` is backed by a `HashMap`.
- Each element in the `HashSet` is stored as a key in the `HashMap` with a dummy value.
- The hashing mechanism ensures constant-time performance for basic operations like add, remove, and contains.

**Example:**
```java
Set<String> set = new HashSet<>();
set.add("One");
```
Internally:
```java
HashMap<String, Object> map = new HashMap<>();
map.put("One", PRESENT);
```

---

### 9. Explain the fail-fast behavior in iterators.
**Answer:**
- Fail-fast iterators throw a `ConcurrentModificationException` if the collection is structurally modified after the creation of the iterator.
- This mechanism prevents unpredictable behavior during iteration.

**Example:**
```java
List<Integer> list = new ArrayList<>();
list.add(1);
Iterator<Integer> iterator = list.iterator();
list.add(2); // Structural modification
iterator.next(); // Throws ConcurrentModificationException
```

---

### 10. How can you make a collection thread-safe?
**Answer:**
- **Using synchronized wrappers:** Use `Collections.synchronizedList()` or similar methods to synchronize a collection.
- **Using concurrent collections:** Use classes like `ConcurrentHashMap`, `CopyOnWriteArrayList`.

**Example:**
```java
List<Integer> synchronizedList = Collections.synchronizedList(new ArrayList<>());
Map<Integer, String> concurrentMap = new ConcurrentHashMap<>();
```


 
