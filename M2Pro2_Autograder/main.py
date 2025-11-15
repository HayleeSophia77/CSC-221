# Build a staged Python auto-grader that evolves from basic evaluation to a full GUI-based application.
# 10/02/2025
# M2Pro2
# Haylee Paredes

'''
Step 1: Display main menu w/ options to grade program 1 or 2, or exit.
Step 2: Get user’s menu input.
Step 3: If choice is program 1, ask for folder path & call grading func. for Program 1.
Step 4: If choice is program 2, ask for folder path & call the grading func. for program 2.
Step 5: Locate solution file & student files in program folders.
Step 6: Show student files list & let user pick 1 or all for grading.
Step 7: Grade each selected student file by comparing with solution & print rubric table.
Step 8: Repeat/loop menu until user chooses exit or 3.
'''

# ===============================
# MAIN EXECUTION
# ===============================
import os
from checks import find_solution_and_students
from grading import grade_program1, grade_program2, print_rubric_table

def main():
    choice = ""
    
    while choice != "3":
        print("\n-------------Menu----------------")
        print("1) Grade program1.py submission")
        print("2) Grade program2.py submission")
        print("3) Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            folder = input("Enter the folder path for Program 1 files: ").strip()
            run_grade(folder, 1)
        elif choice == "2":
            folder = input("Enter the folder path for Program 2 files: ").strip()
            run_grade(folder, 2)
        elif choice == "3":
            print("Goodbye.")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def run_grade(folder, program_id):
    if program_id == 1:
        sol_names = ["program1_solution.py", "solution.py"]
    else:
        sol_names = ["program2_solution.py", "solution.py"]

    solution, students = find_solution_and_students(folder, sol_names)
    
    if program_id == 1:
        if solution is None:
            print("Note: No solution file found. Grading code quality only (not comparing output).")
            
        if len(students) == 0:
            students = []
            if os.path.isdir(folder):
                for name in os.listdir(folder):
                    if name.lower().endswith(".py"):
                        abs_p = os.path.abspath(os.path.join(folder, name))
                        students.append(abs_p)
                students.sort()
    else:
        if solution is None:
            print("!! Could not find a solution file. Looked for:", ", ".join(sol_names))
            return
    
    if len(students) == 0:
        print("!! No student .py files found.")
        return

    print("\nFiles detected:")
    i = 0
    while i < len(students):
        print("  {0}) {1}".format(i + 1, os.path.basename(students[i])))
        i = i + 1
    print("  A) Grade ALL student files in this folder")
    selection = input("Choose a number or 'A': ").strip()

    chosen = []
    if selection.lower() == "a":
        chosen = students
    else:
        pick = None
        if selection.isdigit():
            n = int(selection)
            if 1 <= n <= len(students):
                pick = n - 1
        if pick is None:
            print("Invalid selection.")
            return
        chosen = [students[pick]]

    j = 0
    while j < len(chosen):
        p = chosen[j]
        print("\n" + "=" * 72)
        print("Grading:", os.path.basename(p))
        try:
            if program_id == 1:
                total, rows = grade_program1(solution, p)
            else:
                total, rows = grade_program2(solution, p)
            print_rubric_table(total, rows)
        except Exception as e:
            print("Error grading {}: {}".format(os.path.basename(p), e))
        j = j + 1

if __name__ == "__main__":
    main()