"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

f = open("foo.txt", "r")
data = f.read()
print(data)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
text = "this is test of the writing ability of writing files to a file. \n I am just going to keep writing. \n Now i will stop"
g = open('bar.txt', 'w')
g.write(text)
g.close()

h = open("bar.txt", "r")
data = h.read()
print(data)
h.close()