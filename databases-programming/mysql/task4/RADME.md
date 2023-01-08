Write a function get_instruments_count which will show the number of instruments for each category. The function should take a connection as an argument. It will return records consisting of dictionaries with two keys - 'family' and 'count'. Sample function call:

```Python
...
result = get_instruments_count(connection)
print(result)
({'family': 'keyboard', 'count': 2}, ...)

```