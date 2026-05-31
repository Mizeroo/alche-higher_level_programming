# Python - Input/Output

File I/O and JSON serialization tasks in Python, part of the ALX Higher Level Programming curriculum.

## Concepts Covered

- Reading, writing, and appending to files using the `with` statement
- JSON serialization (`json.dumps`, `json.loads`, `json.dump`, `json.load`)
- Converting Python objects to/from JSON strings
- Class serialization and deserialization using `__dict__`
- Pascal's Triangle (technical interview prep)

## Files

| File | Description |
|------|-------------|
| `0-read_file.py` | Reads a UTF-8 text file and prints it to stdout |
| `1-write_file.py` | Writes a string to a file, returns characters written |
| `2-append_write.py` | Appends a string to a file, returns characters added |
| `3-to_json_string.py` | Returns JSON string representation of an object |
| `4-from_json_string.py` | Returns a Python object from a JSON string |
| `5-save_to_json_file.py` | Saves an object to a file as JSON |
| `6-load_from_json_file.py` | Creates a Python object from a JSON file |
| `7-add_item.py` | Adds CLI arguments to a JSON list saved in `add_item.json` |
| `8-class_to_json.py` | Returns `__dict__` of an object for JSON serialization |
| `9-student.py` | Student class with `to_json()` method |
| `10-student.py` | Student class with filtered `to_json(attrs)` method |
| `11-student.py` | Student class with `to_json()` and `reload_from_json()` |
| `12-pascal_triangle.py` | Returns Pascal's triangle as a list of lists |

## Requirements

- Python 3.8.5 on Ubuntu 20.04 LTS
- pycodestyle 2.7.*
- All files executable with `#!/usr/bin/python3` as first line