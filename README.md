CodeQL for Python
=================

[![](https://img.shields.io/pypi/v/codeql-python.svg)](https://pypi.python.org/pypi/codeql-python)

Python 3.x bindings for the CodeQL CLI application.

Install the package via:

```bash
pip install codeql-python
````

## Usage

```python
import codeql

db = codeql.Database('path/to/db.zip')

# Queries return a CSV-like array of arrays
results = db.query('select "Hello"')
assert(results[0][1] == 'Hello')

# Queries with external libraries are supported as well
codeql.set_search_path('path/to/codeql')
results = db.query('''
    import cpp
    from BlockStmt block    
    select block
''')
```
