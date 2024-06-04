# Method 1 : using flushing:
https://stackoverflow.com/questions/3167494/how-often-does-python-flush-to-a-file
```
import os
print (io.DEFAULT_BUFFER_SIZE)
with open('out.log', 'w+') as f:
    f.write('output is ')
    # some work
    s = 'OK.'
    f.write(s)
    f.write('\n')
    f.flush()
    # some other work
    f.write('done\n')
    f.flush()

with open('out.log', 'w+') as f:
    f.write('output is ')
    # some work
    s = 'OK.'
    f.write(s)
    f.write('\n')
    f.flush()
    # some other work
    f.write('done\n')
    f.flush()
    os.fsync() #flush() does not necessarily write the file’s data to disk. Use flush() followed by os.fsync() to ensure this behavior. 
```

# Method 2: setting flushing size
I think you would auto-flush in python this way (based from here)
```
#0 means there is no buffer, so all output
#will be auto-flushed
fsock = open('out.log', 'w', 0)
sys.stdout = fsock
#do whatever
fsock.close()
```




For file operations, Python uses the operating system's default buffering unless you configure it do otherwise. You can specify a buffer size, unbuffered, or line buffered.

For example, the open function takes a buffer size argument.

http://docs.python.org/library/functions.html#open

"The optional buffering argument specifies the file’s desired buffer size:"

0 means unbuffered,
1 means line buffered,
any other positive value means use a buffer of (approximately) that size.
A negative buffering means to use the system default, which is usually line buffered for tty devices and fully buffered for other files.
If omitted, the system default is used.
code:
```
bufsize = 0
f = open('file.txt', 'w', buffering=bufsize)
```