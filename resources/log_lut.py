import math

import numpy as np
import scipy.signal as sig

import matplotlib.pyplot as plt


def print_hex_array(data):
    lines = [data[i : i + 16] for i in range(0, len(data), 16)]
    for line in lines:
        line_str = ", ".join(map(lambda x: "0x{:04X}".format(x), line))
        print("    " + line_str + ",")


x = np.arange(1, 100000, 0.1)
x3 = [0]
y3 = [0]

x_prev = 1.0
y_prev = round(math.log10(x_prev / 100) * 128)
x3.append(round(x_prev))
y3.append(256 + y_prev)

for i in x[1:]:
    a = round(math.log10(i / 100) * 128)
    if (i - x_prev) < 1.0:
        continue
    if (a - y_prev) >= 1:
        x3.append(round(i))
        y3.append(256 + a)
    y_prev = a
    x_prev = i

plt.plot(x3, y3, marker=".")
plt.grid(True)
plt.show()

for i, x in enumerate(x3):
    if x >= 0x10000:
        print(f"#define LOG_EXT_IDX ({i - 1})")
        break

x3 = list(map(lambda x: x if x < 0x10000 else x - 0x10000, x3))

print(f"#define LOG_LUT_LEN ({len(x3)})")
print(y3[1])
print_hex_array(x3)
print()
print_hex_array(y3)
