import os

with open("main.txt", "r", encoding="utf8") as f:
    content = f.read()

# main
with open("Eng_To_Ta.txt", "r", encoding="utf8") as f:
    content1 = f.read()
content1 = content1.split("\n")
for i, j in enumerate(content1):
    content1[i] = j.split(" > ")
for i in content1:
    content = content.replace(i[0], i[1])
# ---------------------------------

addition = """with open("output.txt", "w", encoding="utf8") as f:
    f.write("")


def output(a):
    with open("output.txt", "a", encoding="utf8") as f:
        f.write(str(a) + "\\n")
"""

with open("tamil.py", "w", encoding="utf8") as f:
    f.write(addition + content)

os.system("py tamil.py")
os.system("notepad output.txt")
