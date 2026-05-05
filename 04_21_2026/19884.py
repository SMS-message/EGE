import re
with open("24_19884.txt") as f:
    s = f.readline().strip()

# s = '*567-8**09-30-'
st = set()

print("Adding to set...")
for i in range(len(s)):
    print(len(s) - i)
    st |= set(re.findall(r"^(\s*(\d+(\.\d+)?|\(|\))\s*[\+\-\*\/\s]*\s*)+$", s[i:i + 200]))
print("Done")
print()

print("Going through set...")
st1 = set()
for i in st:
    for j in range(len(i), 0, -1):
        try:
            eval(i[:j])
            if '-' in i[:j] or '*' in i[:j]:
                st1 |= {i[:j], }
        except SyntaxError:
            pass

print("Done")

st |= st1
print(st)
print(len(st))
