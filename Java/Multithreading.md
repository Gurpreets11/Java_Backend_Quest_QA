
# Java Threads Questions and Answers

### 1. What is the life cycle of a thread in Java?
**Answer:**
A thread in Java goes through the following life cycle states:
1. **New:** The thread is created but not yet started using the `new` keyword, e.g., `Thread t = new Thread();`. At this stage, it is not scheduled for execution.
2. **Runnable:** Once the `start()` method is invoked, the thread moves to the Runnable state. It is ready to run but waiting for the CPU scheduler to allocate time.
3. **Running:** When the thread is picked up by the thread scheduler, it enters the Running state and begins execution.
4. **Blocked/Waiting:** The thread can move to a Blocked or Waiting state if it encounters conditions such as waiting for I/O operations or synchronization locks.
5. **Terminated:** Once the thread completes its task or is explicitly stopped, it moves to the Terminated state and cannot be restarted.

Example:
```java
Thread t = new Thread(() -> System.out.println("Thread running"));
t.start();
```

---

### 2. What are daemon threads in Java? How do you create them?
**Answer:**
Daemon threads are low-priority threads that provide background services to user threads. They automatically terminate when all non-daemon (user) threads have finished execution. Examples include garbage collection and other JVM maintenance tasks.

- **Creating Daemon Threads:** Use the `setDaemon(true)` method before starting the thread.

Example:
```java
Thread daemonThread = new Thread(() -> {
    while (true) {
        System.out.println("Daemon thread running");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            break;
        }
    }
});
daemonThread.setDaemon(true);
daemonThread.start();
```

---

### 3. How does synchronized work in static and instance methods?
**Answer:**
The `synchronized` keyword ensures that only one thread can access a block of code or method at a time:
- **Instance Methods:** The lock is tied to the instance of the object.
- **Static Methods:** The lock is tied to the `Class` object.

Example:
```java
class Example {
    public synchronized void instanceMethod() {
        System.out.println("Instance lock acquired");
    }

    public static synchronized void staticMethod() {
        System.out.println("Class lock acquired");
    }
}
```

---

### 4. What are thread priorities, and how do they affect thread execution?
**Answer:**
Thread priorities are integers between `Thread.MIN_PRIORITY` (1) and `Thread.MAX_PRIORITY` (10). They act as hints to the thread scheduler about the importance of a thread. However, the actual execution depends on the JVM and operating system.

Example:
```java
Thread t1 = new Thread(() -> System.out.println("Thread 1"));
t1.setPriority(Thread.MIN_PRIORITY);
Thread t2 = new Thread(() -> System.out.println("Thread 2"));
t2.setPriority(Thread.MAX_PRIORITY);
t1.start();
t2.start();
```

---

### 5. Explain the purpose of the join() method in threads.
**Answer:**
The `join()` method allows one thread to wait for the completion of another thread before proceeding. This ensures sequential execution when needed.

Example:
```java
Thread t = new Thread(() -> System.out.println("Thread finished"));
t.start();
t.join();
System.out.println("Main thread continues after t completes");
```

---

### 6. What is the difference between Callable and Runnable?
**Answer:**
- **Runnable:** A functional interface with a `run()` method. It does not return any value or throw checked exceptions.
- **Callable:** A functional interface with a `call()` method. It can return a value and throw checked exceptions.

Example:
```java
Callable<Integer> callable = () -> 42;
Runnable runnable = () -> System.out.println("Runnable running");
ExecutorService executor = Executors.newFixedThreadPool(2);
Future<Integer> future = executor.submit(callable);
executor.submit(runnable);
System.out.println("Callable result: " + future.get());
executor.shutdown();
```

---

### 7. How does the ThreadLocal class work?
**Answer:**
`ThreadLocal` provides thread-local variables, where each thread accessing the variable has its own isolated copy. It is commonly used to maintain per-thread state, such as user sessions or transactions.

Example:
```java
ThreadLocal<Integer> threadLocal = ThreadLocal.withInitial(() -> 0);
Thread t1 = new Thread(() -> {
    threadLocal.set(100);
    System.out.println("Thread 1 value: " + threadLocal.get());
});
Thread t2 = new Thread(() -> {
    threadLocal.set(200);
    System.out.println("Thread 2 value: " + threadLocal.get());
});
t1.start();
t2.start();
```

---

### 8. What are the concurrency utilities available in Java?
**Answer:**
Java's `java.util.concurrent` package provides tools for efficient and thread-safe concurrency:
- **Executor Framework:** Manages thread pools.
- **Concurrent Collections:** e.g., `ConcurrentHashMap`, `CopyOnWriteArrayList`.
- **Locks:** e.g., `ReentrantLock`.
- **Synchronizers:** e.g., `CountDownLatch`, `CyclicBarrier`.
- **Atomic Variables:** e.g., `AtomicInteger`, `AtomicLong`.

Example:
```java
ExecutorService executor = Executors.newFixedThreadPool(2);
executor.submit(() -> System.out.println("Task executed"));
executor.shutdown();
```

---

### 9. What is the role of the ExecutorService in Java?
**Answer:**
`ExecutorService` simplifies thread management by providing a thread pool mechanism. It enables scheduling, submitting tasks, and managing thread lifecycle efficiently.

Example:
```java
ExecutorService executor = Executors.newSingleThreadExecutor();
executor.submit(() -> System.out.println("Single-threaded task"));
executor.shutdown();
```

---

### 10. Explain the difference between ReentrantLock and synchronized.
**Answer:**
- **`synchronized`:** Simple to use, handles locking automatically, but less flexible.
- **`ReentrantLock`:** Requires explicit locking and unlocking, supports advanced features like try-lock, interruptible locks, and fairness policies.

Example:
```java
ReentrantLock lock = new ReentrantLock();
lock.lock();
try {
    System.out.println("Critical section");
} finally {
    lock.unlock();
}
```
