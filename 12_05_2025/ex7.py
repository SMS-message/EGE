from math import ceil

k = 4
K = 32000
i = 8
tracks = 26
t = 89 * 60 + 27
v = 335061779

time = 479

I = K * k * i * t


I1 = v * time
print(I1, I)

x = (I1 - I) / tracks

print(ceil(x / 2 ** 13))