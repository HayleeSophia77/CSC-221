# Build a staged Python auto-grader that evolves from basic evaluation to a full GUI-based application.
# 10/02/2025
# M2Pro2
# Haylee Paredes

'''
Step 1: Import required check func. from checks mod.
Step 2: Define grading criteria & output weight.
Step 3: Create func. to assign points based on pass/fail results.
Step 4: Create func. to print rubric & final grade.
Step 5: Create func. to test if student program runs successfully.
Step 6: Define grading func. for program 1 using checks & execution results.
Step 7: Define grading func. for program 2 using checks, options, & string usage.
Step 8: Define main grading func. to select Program 1 or Program 2 evaluation.
'''

from checks import(check_loops, check_functions, check_comments, check_variables, run_program, read_text)

# ===============================
# CONFIGURATION
# ===============================
CRITERIA_P1 = {"structure": 30, "output": 50, "functions": 0, "pseudocode": 10, "variables": 10} 

CRITERIA_P2_BASE = {"structure": 20, "functions": 10, "pseudocode": 5, "variables": 5} 
P2_OUTPUT_SUBPOINTS = {"Option 1": 10, "Option 2": 5, "Option 3": 10, "Option 4": 10, "Option 5": 10, "Option 6": 5,}
P2_OUTPUT_WEIGHT_TOTAL = 50

def _set_points(row, weight):
    """
    Parameters:
        row (dict)
        weight (int)
    
    Returns:
        dict
"""
    row["weight"] = weight
    if row["passed"]:
        row["points"] = weight
    else: 
        row["points"] = 0
    return row

def print_rubric_table(total, rows):
    """
    Parameters:
        total (int)
        rows (list)
    
    Returns:
        None
    """
    print("=== Rubric ===")
    print("{:<35} {:<8} {:<6} {:<6} {}".format("Criterion", "Passed", "Weight", "Points", "Feedback"))
    print("-" * 100)
    
    denom = 0
    i = 0 
    while i < len(rows):
        r = rows[i]
        denom = denom + int(r.get("weight", 0))
        fb = "; ".join(r.get("messages", []))
        print("{:<35} {:<8} {:<6} {:<6} {}".format(str(r["name"]), str(r["passed"]), int(r["weight"]), int(r["points"]), fb))
        i = i + 1
    print("\n=== Final Grade ===")
    print("Score: {}/{}".format(total, denom))

def check_program_runs(student_file, timeout_sec=5):
    """
    Parameters:
        student_file (str)
        timeout_sec (int)
    
    Returns:
        dict
    """
    test_inputs = [
        "Done\n",
        "John\n40\n15\nDone\n",
        "John\n45\n15\nDone\n"
    ]
    
    i = 0
    while i < len(test_inputs):
        stu_out, stu_err, stu_rc = run_program(student_file, test_inputs[i], timeout_sec)
        
        if stu_rc == 0:
            msgs = ["Program runs successfully."]
            if len(stu_out.strip()) > 0:
                msgs.append("Produces output ({} chars).".format(len(stu_out.strip())))
            return {
                "name": "Program Execution",
                "passed": True,
                "messages": msgs,
                "weight": 0,
                "points": 0
            }
        i = i + 1
    
    cut_err = stu_err[:200] if isinstance(stu_err, str) else ""
    return {
        "name": "Program Execution",
        "passed": False,
        "messages": ["Program failed to run. Error: {}".format(cut_err)],
        "weight": 0,
        "points": 0
    }
    
def grade_program1(solution, student, input_text=""):
    """
    Parameters:
        solution (str or None)
        student (str)
        input_text (str)
    
    Returns:
        tuple
    """
    rows = []
    total = 0

    r = check_loops(student); r = _set_points(r, CRITERIA_P1["structure"]); total = total + r["points"]; rows.append(r)
    r = check_functions(student); r = _set_points(r, CRITERIA_P1["functions"]); total = total + r["points"]; rows.append(r)
    r = check_comments(student); r = _set_points(r, CRITERIA_P1["pseudocode"]); total = total + r["points"]; rows.append(r)
    r = check_variables(student); r = _set_points(r, CRITERIA_P1["variables"]); total = total + r["points"]; rows.append(r)
    
    r = check_program_runs(student)
    if r["passed"]:
        r = _set_points(r, CRITERIA_P1["output"])
        r["name"] = "Output (Program Runs)"
    else:
        r = _set_points(r, CRITERIA_P1["output"])
        r["name"] = "Output (Program Runs)"
    
    total = total + r["points"]
    rows.append(r)

    return total, rows

def _uses_string_methods(src_text):
    """
    Parameters:
        src_text (str)
    
    Returns:
        bool
    """
    s = src_text.lower()
    tokens = ["lower(", "upper(", "title(", "strip(", "replace(", "split(", "startswith(", "endswith("]
    i = 0
    found = False
    while i < len(tokens) and not found:
        if tokens[i] in s:
            found = True
        i = i + 1
    return found

def grade_program2(solution, student):
    """
    Parameters:
        solution (str)
        student (str)
    
    Returns:
        tuple
    """
    rows = []
    total = 0

    r = check_loops(student); r = _set_points(r, CRITERIA_P2_BASE["structure"]); total = total + r["points"]; rows.append(r)
    r = check_functions(student); r = _set_points(r, CRITERIA_P2_BASE["functions"]); total = total + r["points"]; rows.append(r)
    r = check_comments(student); r = _set_points(r, CRITERIA_P2_BASE["pseudocode"]); total = total + r["points"]; rows.append(r)
    r = check_variables(student); r = _set_points(r, CRITERIA_P2_BASE["variables"]); total = total + r["points"]; rows.append(r)

    out_points = 0
    src = read_text(student)
    
    test_add = "1\nJohn\nDoe\n(555)123-4567\njohn@test.com\n6\n"
    stu_out, stu_err, stu_rc = run_program(student, test_add, timeout_sec=5)
    if stu_rc == 0 and ("success" in stu_out.lower() or "added" in stu_out.lower()):
        out_points = out_points + P2_OUTPUT_SUBPOINTS["Option 1"]
    
    test_view = "2\n6\n"
    stu_out, stu_err, stu_rc = run_program(student, test_view, timeout_sec=5)
    if stu_rc == 0 and len(stu_out.strip()) > 0:
        out_points = out_points + P2_OUTPUT_SUBPOINTS["Option 2"]

    if "def search_contact" in src:
        func_start = src.find("def search_contact")
        func_end = src.find("\ndef ", func_start + 1)
        if func_end == -1:
            func_end = len(src)
        func_text = src[func_start:func_end].lower()
        if ".capitalize(" in func_text or ".lower(" in func_text or ".upper(" in func_text or ".strip(" in func_text:
            out_points = out_points + P2_OUTPUT_SUBPOINTS["Option 3"]
    
    if "def remove_contact" in src:
        func_start = src.find("def remove_contact")
        func_end = src.find("\ndef ", func_start + 1)
        if func_end == -1:
            func_end = len(src)
        func_text = src[func_start:func_end].lower()
        if ".capitalize(" in func_text or ".lower(" in func_text or ".upper(" in func_text or ".strip(" in func_text:
            out_points = out_points + P2_OUTPUT_SUBPOINTS["Option 4"]
    
    if "def update_contact" in src:
        func_start = src.find("def update_contact")
        func_end = src.find("\ndef ", func_start + 1)
        if func_end == -1:
            func_end = len(src)
        func_text = src[func_start:func_end].lower()
        if ".capitalize(" in func_text or ".lower(" in func_text or ".upper(" in func_text or ".strip(" in func_text:
            out_points = out_points + P2_OUTPUT_SUBPOINTS["Option 5"]
    
    src_lower = src.lower()
    has_exit = ("exit()" in src_lower or "sys.exit" in src_lower or "quit()" in src_lower)
    
    test_exit = "6\n"
    stu_out, stu_err, stu_rc = run_program(student, test_exit, timeout_sec=5)
    terminates_properly = (stu_rc == 0)
    
    if not has_exit and terminates_properly:
        out_points = out_points + P2_OUTPUT_SUBPOINTS["Option 6"]

    if out_points > P2_OUTPUT_WEIGHT_TOTAL:
        out_points = P2_OUTPUT_WEIGHT_TOTAL

    rows.append({
        "name": "Output (options 1-6)",
        "passed": (out_points == P2_OUTPUT_WEIGHT_TOTAL),
        "messages": ["Output points: {}/{}.".format(out_points, P2_OUTPUT_WEIGHT_TOTAL)],
        "weight": P2_OUTPUT_WEIGHT_TOTAL,
        "points": out_points
    })
    total = total + out_points

    return total, rows

# ===============================
# FUNCTION: Grade student
# ===============================
def grade_student(solution, student, which="p1"):
    """
    Parameters:
        solution (str)
        student (str)
        which (str)
    
    Returns:
        tuple
    """
    if str(which).lower() == "p2":
        return grade_program2(solution, student)
    return grade_program1(solution, student)