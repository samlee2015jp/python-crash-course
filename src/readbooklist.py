import os
path = "/Users/samli/books/toreadbooks/"
files = [f for f in os.listdir(path) if f.endswith(".pdf")]
files.sort()
for f in files:
    print(f)
