s = "- -* - 123 456 789 123   - - -  *"
s = s.strip("- *")
s = s.replace("123", "")
print(s)