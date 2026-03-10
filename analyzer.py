def analyze_code(code, language):

    loop_count = 0

    lines = code.split("\n")

    for line in lines:

        line=line.strip()

        if language=="python":

            if line.startswith("for") or line.startswith("while"):
                loop_count += 1

        elif language=="java" or language=="cpp":

            if "for(" in line or "for (" in line:
                loop_count += 1

            if "while(" in line or "while (" in line:
                loop_count += 1

    if loop_count == 0:
        return "Estimated Time Complexity: O(1)"

    elif loop_count == 1:
        return "Estimated Time Complexity: O(n)"

    elif loop_count == 2:
        return "Estimated Time Complexity: O(n^2)"

    else:
        return "Estimated Time Complexity: O(n^3)"