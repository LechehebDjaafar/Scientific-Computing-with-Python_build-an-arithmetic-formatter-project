def arithmetic_arranger(problems, display_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists for each row
    first_operands = []
    second_operands = []
    operators = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Incorrect format."
        
        first, operator, second = parts

        # Check for valid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain only digits
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check operand length
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate width and prepare formatting
        width = max(len(first), len(second)) + 2  # Space for operator and alignment
        first_operands.append(first.rjust(width))
        second_operands.append(operator + " " + second.rjust(width - 2))
        dashes.append('-' * width)

        # Calculate answer if needed
        if display_answers:
            answer = str(eval(problem))
            answers.append(answer.rjust(width))

    # Combine all rows
    first_line = "    ".join(first_operands)
    second_line = "    ".join(second_operands)
    dash_line = "    ".join(dashes)
    result = "\n".join([first_line, second_line, dash_line])

    if display_answers:
        answer_line = "    ".join(answers)
        result += "\n" + answer_line

    return result


# Example Function Calls
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
