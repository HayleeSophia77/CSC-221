import difflib

expected_output = "Hello World"
student_output = "Helo Wrold"

similarity = difflib.SequenceMatcher(None, expected_output, student_output).ratio()
grade = round(similarity * 100, 2)

print(f"Similarity: {similarity:.2f}, Grade: {grade}")
