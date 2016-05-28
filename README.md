# python-taskpaper

Provides an API for working with TaskPaper formatted documents in Python.

## Example of usage

A simple example that reads in then prints the contents of a TaskPaper file.

```
import codecs

from taskpaper.taskpaper import TaskPaper

f = codecs.open('todo.taskpaper', 'r', 'utf8')
todo = TaskPaper.parse(f)
f.close()

print(todo)
```
