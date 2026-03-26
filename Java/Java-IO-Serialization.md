
# Java File I/O Concepts Explained with Examples

## 1. What is the difference between byte streams and character streams?
- **Byte Streams**: Handle data in raw binary format (8-bit bytes). Used for reading and writing binary data such as images or audio files.
- **Character Streams**: Handle data in 16-bit Unicode format. Used for reading and writing text files.

### Example:
```java
// Byte Stream Example
FileInputStream fis = new FileInputStream("input.txt");
int data;
while ((data = fis.read()) != -1) {
    System.out.print((char) data);
}
fis.close();

// Character Stream Example
FileReader fr = new FileReader("input.txt");
int charData;
while ((charData = fr.read()) != -1) {
    System.out.print((char) charData);
}
fr.close();
```

## 2. What are the main classes used for file I/O in Java?
- **File**: Represents file or directory paths.
- **FileInputStream** and **FileOutputStream**: For byte stream operations.
- **FileReader** and **FileWriter**: For character stream operations.
- **BufferedReader** and **BufferedWriter**: For efficient character stream operations.
- **ObjectInputStream** and **ObjectOutputStream**: For serialization and deserialization.

### Example:
```java
File file = new File("example.txt");
if (file.exists()) {
    System.out.println("File exists: " + file.getName());
}
```

## 3. How do you read a file in Java line by line?
You can use `BufferedReader` to read a file line by line.

### Example:
```java
BufferedReader br = new BufferedReader(new FileReader("input.txt"));
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
br.close();
```

## 4. What is the purpose of the `ObjectOutputStream` and `ObjectInputStream` classes?
These classes are used for object serialization and deserialization.
- **`ObjectOutputStream`**: Writes objects to a file.
- **`ObjectInputStream`**: Reads objects from a file.

### Example:
```java
// Serialization
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("object.dat"));
oos.writeObject(new String("Hello World"));
oos.close();

// Deserialization
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("object.dat"));
String message = (String) ois.readObject();
System.out.println(message);
ois.close();
```

## 5. Explain the concept of file locking in Java.
File locking prevents other processes from accessing a file concurrently. It can be achieved using the `FileChannel` class.

### Example:
```java
FileChannel channel = new RandomAccessFile("file.txt", "rw").getChannel();
FileLock lock = channel.lock();

try {
    System.out.println("File is locked");
} finally {
    lock.release();
    channel.close();
}
```

## 6. How do you copy a file in Java?
You can use `Files.copy` from `java.nio.file` package or `FileInputStream` and `FileOutputStream`.

### Example:
```java
// Using Files.copy
Files.copy(Paths.get("source.txt"), Paths.get("destination.txt"), StandardCopyOption.REPLACE_EXISTING);

// Using Streams
FileInputStream fis = new FileInputStream("source.txt");
FileOutputStream fos = new FileOutputStream("destination.txt");
byte[] buffer = new byte[1024];
int length;
while ((length = fis.read(buffer)) > 0) {
    fos.write(buffer, 0, length);
}
fis.close();
fos.close();
```

## 7. What is the difference between `flush()` and `close()` methods in streams?
- **`flush()`**: Ensures all data in the stream's buffer is written to the destination without closing the stream.
- **`close()`**: Releases resources and closes the stream.

### Example:
```java
BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
bw.write("Hello World");
bw.flush(); // Data written to file
bw.close(); // Stream closed
```

## 8. What are random access files, and how are they used?
Random access files allow reading and writing at any position within a file. It is supported by the `RandomAccessFile` class.

### Example:
```java
RandomAccessFile raf = new RandomAccessFile("data.txt", "rw");
raf.seek(10); // Move to byte 10
raf.writeUTF("Hello");
raf.seek(0); // Move to the beginning
System.out.println(raf.readUTF());
raf.close();
```

## 9. What are Buffered Streams, and why are they important?
Buffered streams improve I/O performance by reducing the number of read and write operations. They use an internal buffer to batch operations.

### Example:
```java
BufferedReader br = new BufferedReader(new FileReader("input.txt"));
BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
String line;
while ((line = br.readLine()) != null) {
    bw.write(line);
    bw.newLine();
}
br.close();
bw.close();
```

## 10. What are `PipedInputStream` and `PipedOutputStream`?
These classes allow data to be transferred between threads using a pipe. They are useful for thread communication.

### Example:
```java
PipedOutputStream pos = new PipedOutputStream();
PipedInputStream pis = new PipedInputStream(pos);

new Thread(() -> {
    try {
        pos.write("Hello from producer".getBytes());
        pos.close();
    } catch (IOException e) {
        e.printStackTrace();
    }
}).start();

new Thread(() -> {
    try {
        int data;
        while ((data = pis.read()) != -1) {
            System.out.print((char) data);
        }
        pis.close();
    } catch (IOException e) {
        e.printStackTrace();
    }
}).start();
