import re
name = "Manesh"
pattern = r"^Man..sh$"
# pattern = r"^Man.{2}sh$"
# pattern = r"^Man?sh$"
print(re.match(pattern, name))