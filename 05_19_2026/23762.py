with open("24_23762.txt") as f:
    s = f.read().strip()

s = s.split("Y")

lst = []

for i in range(81, len(s)):
    win = s[i - 81:i]
    st = 'Y'.join(win)
    if st.count('2025') >= 90:
        lst.append(st)

string = max(lst, key=len)

print(string, len(string))
