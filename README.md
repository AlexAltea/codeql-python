CodeQL for Python
=================

<!--
[![](https://img.shields.io/pypi/v/codeql-python.svg)](https://pypi.python.org/pypi/codeql-python)
-->

Unofficial Python 3.x bindings for the CodeQL CLI application.

Install the package via:

```bash
pip install git+https://github.com/AlexAltea/codeql-python.git
````

## Usage

```python
import codeql

# Open databases from files or folders
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

# Create temporary databases from inlined sources
db = codeql.Database.from_cpp('''
    int main() {
        return 1337 + 1337 + 1337;
    }
''')
results = db.query('''
    import cpp
    from Literal literal where
        literal.getType() instanceof IntType and
        literal.getValue().toInt() = 1337
    select literal
''')
assert(len(results[1:]) == 3)
```
