from config import STUDENT_MARKS, QUESTIONS


def workflow(question):

    text = question.lower()

    # Rule 1: Lokesh's mark
    if "lokesh" in text and "mark" in text:

        return f"Lokesh's mark is {STUDENT_MARKS['Lokesh']}."


    # Rule 2: Highest mark
    if "highest" in text:

        student = max(
            STUDENT_MARKS,
            key=STUDENT_MARKS.get
        )

        return (
            f"{student} scored the highest mark: "
            f"{STUDENT_MARKS[student]}."
        )


    # Rule 3: Average
    if "average" in text:

        total = (
            STUDENT_MARKS["Lokesh"]
            + STUDENT_MARKS["Arun"]
        )

        average = total / 2

        return f"The average mark is {average}."


    # Rule 4
    if "welcome" in text:

        return (
            "Welcome to our student learning program!\n"
            "Keep learning and keep improving!"
        )


    return "Sorry, I don't have a rule for this question."


if __name__ == "__main__":

    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW ===\n")

    for question in QUESTIONS:

        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)