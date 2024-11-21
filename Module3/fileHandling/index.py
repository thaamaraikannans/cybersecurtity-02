import os

html = """<html>
<body>
<center>
<h1> Welcome to Python file Handling class</h1>
</center>
</body>
</html>
"""

os.chmod("F:/IMS/dummy.xlsx", 0o777)
file_permissions = os.access("F:/IMS/dummy.xlsx", os.W_OK)
if file_permissions:
    print("You have Write Access")
    print(os.stat("F:/IMS/dummy.xlsx"))
else:
    print("You don't have Write Access")