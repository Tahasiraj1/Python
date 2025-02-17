def arithmetic_arranger(problems, show_answers=False):

    top_row = []
    bottom_row = []
    dashes_row = []
    answers_row = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # Error handling for invalid operators
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Error handling for operands that are not digits
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        # Error handling for operands that are more than 4 digits
        if len(operand1) > 4 or len(operand2) > 4:
            return'Error: Numbers cannot be more than four digits.'
        
        # Determine the max length to align the problems correctly
        max_length = max(len(operand1), len(operand2)) + 2

        # Add the operands, operator, and dashes to their respective rows
        top_row.append(operand1.rjust(max_length))
        bottom_row.append(operator + ' ' + operand2.rjust(max_length - 2))
        dashes_row.append('-' * max_length)
        
        # Calculate the answer if show_answers is True
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            elif operator == '-':
                answer = str(int(operand1) - int(operand2))
            answers_row.append(answer.rjust(max_length))
        else:
            answers_row.append(' ' * max_length)
    
    # Join each row into a string with 4 spaces between each problem
    arranged_problems = '    '.join(top_row) + '\n' + '    '.join(bottom_row) + '\n' + '    '.join(dashes_row)

    if show_answers:
        arranged_problems += '\n' + '    '.join(answers_row)
        

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('\n')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))