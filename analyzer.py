import re

def analyze_code(code, language):

    lines = code.split("\n")

    loops = 0
    conditions = 0
    max_depth = 0

    for line in lines:

        stripped = line.strip()

        if "for " in stripped or "while " in stripped:
            loops += 1

            indent = len(line) - len(line.lstrip())
            depth = indent // 4 + 1

            if depth > max_depth:
                max_depth = depth

        if "if " in stripped:
            conditions += 1

    # Decide time complexity

    x = [1,2,3,4,5,6,7,8,9,10]

    if max_depth == 0:
        complexity = "O(1)"
        y = [1 for i in x]
        explanation = "The code has no loops. Execution time stays constant."

    elif max_depth == 1:
        complexity = "O(n)"
        y = [i for i in x]
        explanation = "The code contains one loop that runs n times."

    elif max_depth == 2:
        complexity = "O(n²)"
        y = [i*i for i in x]
        explanation = "The code contains two nested loops. Each loop runs n times."

    elif max_depth == 3:
        complexity = "O(n³)"
        y = [i**3 for i in x]
        explanation = "The code contains three nested loops."

    else:
        complexity = "O(n^k)"
        y = [i**max_depth for i in x]
        explanation = "The code contains multiple nested loops increasing the complexity."

    return {
        "complexity": complexity,
        "loops": loops,
        "conditions": conditions,
        "explanation": explanation,
        "x": x,
        "y": y
    }