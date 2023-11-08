import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

delt = 56.2

with open("data\\calibration\\00 Pa.txt") as fl:
    _ = fl.readline()
    _ = fl.readline()
    _ = fl.readline()
    average_0 = 0
    count = 0
    for i in fl:
        average_0 += int(i)
        count += 1
    average_0 /= count
print(average_0)
with open("data\\calibration\\56,2 Pa.txt") as fl:
    _ = fl.readline()
    _ = fl.readline()
    _ = fl.readline()
    average_mx = 0
    count = 0
    for i in fl:
        average_mx += int(i)
        count += 1
    average_mx /= count

_, ax = plt.subplots()
# ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
ax.plot([0, delt], [average_0, average_mx])
ax.grid(True)
K = round((average_mx-average_0)/delt, 2)
ax.text(40, 1300, f"K = {K} st/Pa")
plt.title("График зависимости отчетов АЦП от показаний барометра")
plt.show()