# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import difflib

def grade_output(expected_output, student_output, result_weight=0.8, prompt_weight=0.2):
    # Split into lines
    exp_lines = expected_output.strip().splitlines()
    stu_lines = student_output.strip().splitlines()

    # Assume prompts come first, results later
    exp_prompt = exp_lines[:-1]
    exp_result = exp_lines[-1] if exp_lines else ""
    
    stu_prompt = stu_lines[:-1]
    stu_result = stu_lines[-1] if stu_lines else ""

    # Compare prompts (string similarity)
    prompt_similarity = difflib.SequenceMatcher(None, "\n".join(exp_prompt), "\n".join(stu_prompt)).ratio()

    # Compare results (try numeric first, fallback to string similarity)
    try:
        exp_result_num = float(exp_result)
        stu_result_num = float(stu_result)
        result_similarity = 1 - min(abs(exp_result_num - stu_result_num) / (abs(exp_result_num) + 1e-9), 1)
    except ValueError:
        result_similarity = difflib.SequenceMatcher(None, exp_result, stu_result).ratio()

    # Weighted grade
    grade = (prompt_similarity * prompt_weight + result_similarity * result_weight) * 100
    return round(grade, 2)

# Example usage
expected = """Enter a number:
42"""
student = """Please enter a number:
41"""

print("Grade:", grade_output(expected, student))
