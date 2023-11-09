import os
os.system('cls')

student = {
    "name": "Alice",
    "age": int(20),
    "major": "Computer Science",
    "grades": {
        "math": 95,
        "english": 88,
        "history": 92
    }
}

a = student["grades"]
print(a['math'])