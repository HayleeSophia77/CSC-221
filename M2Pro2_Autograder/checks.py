# Build a staged Python auto-grader that evolves from basic evaluation to a full GUI-based application.
# 10/02/2025
# M2Pro2
# Haylee Paredes

'''
Step 1: Start program & import modules.
Step 2: Define func. to read text from file.
Step 3: Define func. to parse file into ast.
Step 4: Define func. to clean & normalize output.
Step 5: Define func. to run Python file with optional input.
Step 6: Define func. to find solution file & students' files.
Step 7: Define func. to check loops & structures.
Step 8: Define func. to check for user-defined functions.
Step 9: Define func. to check for comments & pseudocode.
Step 10: Define func. to check variable names & descriptiveness.
Step 11: Define func. to compare student output with solution output.
Step 12: Return results showing pass/fail messages for each check.
'''


import os
import ast
import subprocess

def read_text(path):
    """
    Parameters:
        path (str)
    
    Returns:
        str
"""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""

def parse_ast(path):
    """
    Parameters:
        path (str)

    Returns:
        ast.AST | None
    """
    text = read_text(path)
    try:
        return ast.parse(text)
    except:
        return None

def normalize_output(s):
    """
    Parameters:
        s (str)
    
    Returns:
        str
"""
    lines = s.strip().splitlines()
    cleaned = []
    i = 0
    while i < len(lines):
        line = " ".join(lines[i].strip().split())
        if line != "":
            cleaned.append(line)
        i = i + 1
    return "\n".join(cleaned)

# ===============================
# FUNCTION: Run a Python file
# ===============================
def run_program(path, input_text="", timeout_sec=5):
    """
    Parameters:
        path (str)
        input_text (str, optional)
        timeout_sec (int, optional)
    
    Returns:
        tuple[str, str, int]
    """
    try:
        res = subprocess.run(
            ["python", path],
            input=input_text,
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        return res.stdout.strip(), res.stderr.strip(), res.returncode
    except subprocess.TimeoutExpired:
        return "", "TIMEOUT", 124
    except FileNotFoundError:
        return "", "NOT FOUND", 127
    except Exception as e:
        return "", str(e), 1

def find_solution_and_students(folder, solution_names):
    """
    Parameters:
        folder (str)
        solution_names (list[str])

    Returns:
        tuple[str | None, list[str]]
    """
    if not os.path.isdir(folder):
        return None, []

    solution = None
    i = 0
    while i < len(solution_names) and solution is None:
        cand = os.path.join(folder, solution_names[i])
        if os.path.isfile(cand):
            solution = os.path.abspath(cand)
        i = i + 1

    if solution is None:
        return None, []

    students = []
    for name in os.listdir(folder):
        if name.lower().endswith(".py"):
            abs_p = os.path.abspath(os.path.join(folder, name))
            if abs_p != solution:
                students.append(abs_p)
    students.sort()
    return solution, students

# ===============================
# FUNCTION: Check loops / structure
# ===============================
def check_loops(path):
    """
    Parameters:
        path (str)

    Returns:
        dict
    """
    tree = parse_ast(path)
    messages = []
    passed = True

    if tree is None:
        messages.append("Syntax error: cannot analyze structure.")
        return {"name": "Loop/Structure", "passed": False, "messages": messages, "weight": 0, "points": 0}

    bad_found = False
    loops = 0
    decisions = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            loops = loops + 1
            t = node.test
            if isinstance(t, ast.Constant) and t.value is True:
                messages.append("Found 'while True'.")
                bad_found = True
            elif isinstance(t, ast.Name):
                messages.append("Found 'while {0}' (bare variable).".format(t.id))
                bad_found = True
        elif isinstance(node, ast.For):
            loops = loops + 1
        elif isinstance(node, ast.If):
            decisions = decisions + 1

    if not bad_found:
        messages.append("No disallowed while loops.")
    messages.append("Loops found: {0}".format(loops))
    messages.append("Decision structures (if/elif): {0}".format(decisions))

    if bad_found:
        passed = False

    return {"name": "Loop/Structure", "passed": passed, "messages": messages, "weight": 0, "points": 0}

# ===============================
# FUNCTION: Check function usage
# ===============================
def check_functions(path):
    """
    Parameters:
        path (str)

    Returns:
        dict
    """
    tree = parse_ast(path)
    if tree is None:
        return {"name": "Function Usage", "passed": False, "messages": ["Syntax error: cannot analyze functions."], "weight": 0, "points": 0}

    count = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            count = count + 1

    if count > 0:
        return {"name": "Function Usage", "passed": True, "messages": ["Found {0} function(s).".format(count)], "weight": 0, "points": 0}
    return {"name": "Function Usage", "passed": False, "messages": ["No function definitions found."], "weight": 0, "points": 0}

# ===============================
# FUNCTION: Check comments
# ===============================
def check_comments(path):
    """
    Parameters:
        path (str)

    Returns:
        dict
    """
    text = read_text(path)
    tree = parse_ast(path)
    if tree is None:
        return {"name": "Pseudocode/Comments", "passed": False, "messages": ["Syntax error: cannot analyze comments."], "weight": 0, "points": 0}

    lines = text.splitlines()
    total = 0
    comments = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() != "":
            total = total + 1
            if line.strip().startswith("#"):
                comments = comments + 1
        i = i + 1

    doc_ok = False
    try:
        doc = ast.get_docstring(tree)
        if doc is not None and str(doc).strip() != "":
            doc_ok = True
    except:
        doc_ok = False

    msgs = []
    if doc_ok:
        msgs.append("Module docstring present.")
    else:
        msgs.append("No module docstring.")
    pct = int((comments / float(total)) * 100) if total > 0 else 0
    msgs.append("Comment lines: {0}/{1} (~{2}%).".format(comments, total, pct))

    enough = doc_ok or (pct >= 5)
    if enough:
        msgs.append("Comments/pseudocode look OK.")
        return {"name": "Pseudocode/Comments", "passed": True, "messages": msgs, "weight": 0, "points": 0}
    msgs.append("Add more comments/pseudocode.")
    return {"name": "Pseudocode/Comments", "passed": False, "messages": msgs, "weight": 0, "points": 0}

# ===============================
# FUNCTION: Check variable usage
# ===============================
def check_variables(path):
    """
    Parameters:
        path (str)

    Returns:
        dict
    """
    tree = parse_ast(path)
    if tree is None:
        return {"name": "Variables", "passed": False, "messages": ["Syntax error: cannot analyze variables."], "weight": 0, "points": 0}

    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            t_i = 0
            while t_i < len(node.targets):
                t = node.targets[t_i]
                if isinstance(t, ast.Name):
                    names.append(t.id)
                elif isinstance(t, (ast.Tuple, ast.List)):
                    e_i = 0
                    while e_i < len(t.elts):
                        e = t.elts[e_i]
                        if isinstance(e, ast.Name):
                            names.append(e.id)
                        e_i = e_i + 1
                t_i = t_i + 1
        elif isinstance(node, ast.For):
            if isinstance(node.target, ast.Name):
                names.append(node.target.id)

    if len(names) == 0:
        return {"name": "Variables", "passed": False, "messages": ["No variables found."], "weight": 0, "points": 0}

    generic = set(["x","y","z","a","b","c","i","j","k","n","m","t"])
    good = 0
    i = 0
    while i < len(names):
        nm = names[i]
        if len(nm) >= 3 and (nm.lower() not in generic):
            good = good + 1
        i = i + 1

    ratio_ok = False
    if len(names) > 0:
        if (good / float(len(names))) >= 0.5:
            ratio_ok = True

    msgs = []
    msgs.append("Variables: " + ", ".join(sorted(list(set(names)))))
    msgs.append("Descriptive ratio: {0}/{1}".format(good, len(names)))
    if ratio_ok:
        msgs.append("Variable names look OK.")
        return {"name": "Variables", "passed": True, "messages": msgs, "weight": 0, "points": 0}
    msgs.append("Use more descriptive names (e.g., 'total_sum').")
    return {"name": "Variables", "passed": False, "messages": msgs, "weight": 0, "points": 0}

def _remove_prompt_lines(text):
    """
    Parameters:
        text (str)

    Returns:
        str
    """
    lines = text.splitlines()
    keep = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        low = ln.lower().strip()
        if low.endswith(":") or ("enter" in low) or ("input" in low):
            pass
        else:
            keep.append(ln)
        i = i + 1
    return "\n".join(keep)

def compare_outputs(solution_file, student_file, input_text="", timeout_sec=5):
    """
    Parameters:
        solution_file (str)
        student_file (str)
        input_text (str, optional)
        timeout_sec (int, optional)

    Returns:
        dict
    """
    tries = []
    if isinstance(input_text, str) and input_text != "":
        tries = [input_text]
    else:
        tries = [
            "",
            "Done\n",
            "done\n",
            "DONE\n",
            "John\n45\n20\nDone\n"
        ]

    k = 0
    last_status = []
    while k < len(tries):
        current = tries[k]

        sol_out, sol_err, sol_rc = run_program(solution_file, current, timeout_sec)
        stu_out, stu_err, stu_rc = run_program(student_file, current, timeout_sec)

        if sol_rc == 0 and stu_rc == 0:
            a = normalize_output(sol_out)
            b = normalize_output(stu_out)

            if a == b:
                return {
                    "name": "Output Correctness",
                    "passed": True,
                    "messages": ["Output matches solution (ignoring spaces/blank lines)."],
                    "weight": 0,
                    "points": 0
                }

            fa = _remove_prompt_lines(a)
            fb = _remove_prompt_lines(b)
            if fa == fb:
                return {
                    "name": "Output Correctness",
                    "passed": True,
                    "messages": ["Output matches solution (ignoring prompts and spacing)."],
                    "weight": 0,
                    "points": 0
                }
 
            a_lines = a.splitlines()
            b_lines = b.splitlines()
            i = 0
            first_diff = -1
            limit = min(len(a_lines), len(b_lines))
            while i < limit and first_diff == -1:
                if a_lines[i] != b_lines[i]:
                    first_diff = i + 1
                i = i + 1

            msgs = []
            if first_diff != -1:
                msgs.append("First difference at line {}.".format(first_diff))
            elif len(a_lines) != len(b_lines):
                msgs.append("Different number of lines: expected {}, got {}."
                            .format(len(a_lines), len(b_lines)))
            used = "no input" if current == "" else repr(current)
            msgs.append("Compared using: {}.".format(used))
            return {
                "name": "Output Correctness",
                "passed": False,
                "messages": msgs,
                "weight": 0,
                "points": 0
            }

        msg = []
        if sol_rc != 0:
            cut = sol_err[:120] if isinstance(sol_err, str) else ""
            msg.append("Solution rc {}{}".format(sol_rc, " (" + cut + ")" if cut else ""))
        if stu_rc != 0:
            cut = stu_err[:120] if isinstance(stu_err, str) else ""
            msg.append("Student rc {}{}".format(stu_rc, " (" + cut + ")" if cut else ""))
        if current == "":
            msg.append("attempt used: no input")
        else:
            msg.append("attempt used: {}".format(repr(current)))
        last_status.append("; ".join(msg))

        k = k + 1

    msgs = []
    i = 0
    while i < len(last_status):
        msgs.append(last_status[i])
        i = i + 1
    msgs.append("Programs may require interactive input; tried defaults like 'Done'.")
    return {
        "name": "Output Correctness",
        "passed": False,
        "messages": msgs,
        "weight": 0,
        "points": 0
    }