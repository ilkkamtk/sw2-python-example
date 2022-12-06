# Software 2 back-end example
- Compare period1.py to period2.py
- Front-end is [here](https://github.com/ilkkamtk/sw2-example-web)
- Add your own db-credentials to database.py for testing
- I'm using parameterized query. `%s` is a placeholder and it gets value from the *tuple* in `cursor.execute()`
- With `dictionary=True` the result of the database query outputs a dictionary instead of a list. To study the difference, see the `print()` results of period1.py with and without `dictionary=True`