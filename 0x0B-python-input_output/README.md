0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
1. Write to a file
mandatory
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

Prototype: def write_file(filename="", text=""):
You must use the with statement
You don’t need to manage file permission exceptions.
Your function should create the file if doesn’t exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module
2. Append to a file
mandatory
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
3. To JSON string
mandatory
Write a function that returns the JSON representation of an object (string):

Prototype: def to_json_string(my_obj):
You don’t need to manage exceptions if the object can’t be serialized.
4. From JSON string to Object
mandatory
Write a function that returns an object (Python data structure) represented by a JSON string:

Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if the JSON string doesn’t represent an object.
