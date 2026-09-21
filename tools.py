from config import STUDENT_MARKS


def get_mark(student):

    student = student.strip().title()

    mark = STUDENT_MARKS.get(student)

    if mark is None:
        return f"Student {student} was not found."

    return str(mark)


def calculator(expression):

    try:
        return str(eval(expression))
    except:
        return "Calculation error."


TOOL_FUNCTIONS = {
    "get_mark": get_mark,
    "calculator": calculator
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_mark",
            "description": "Get the private mark of a student.",
            "parameters": {
                "type": "object",
                "properties": {
                    "student": {
                        "type": "string"
                    }
                },
                "required": ["student"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a simple arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


if __name__ == "__main__":

    print(
        "get_mark('Lokesh') ->",
        get_mark("Lokesh")
    )

    print(
        "calculator('85 + 72') ->",
        calculator("85 + 72")
    )