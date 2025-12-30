from typing import Optional

def generate_greeting(name: str, age: Optional[int] = None) -> dict:
    return {
        "message": f"Hello, {name}",
        "age": age
    }

