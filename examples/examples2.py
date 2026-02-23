import matplotlib.pyplot as plt
import numpy as np
import XiDianPlots

XiDianPlots.use_style()

# 准备数据
x = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x) * np.exp(-0.1 * x)
y2 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1, label=r"Theory: $e^{-\alpha t} \sin(\omega t)$")
ax.plot(x, y2, label=r"Experiment: $\cos(\theta)$")

ax.set_xlabel(r"时间 Time (s) $(s)$ (\si{\second})")
ax.set_ylabel(r"幅值 Amplitude (\si{\volt})")
ax.set_title(r"系统响应 System Response (\SI{10}{\hertz})")

ax.legend(loc="upper right")

# 默认后端
fig.savefig("demo_standard.png", dpi=600)
print("[Success] demo_standard.png 已生成")

fig.savefig("demo_standard.svg")
print("[Success] demo_standard.svg 已生成")

fig.savefig("demo_standard.pdf")
print("[Success] demo_standard.pdf 已生成")

# 使用pgf后端，调用xelatex生成图片
fig.savefig("demo_latex.png", dpi=600, backend="pgf")
print("[Success] demo_latex.png 已生成")

fig.savefig("demo_latex.pdf", backend="pgf")
print("[Success] demo_latex.pdf 已生成")

# pgf不能导出svg图片，使用pdf中转
XiDianPlots.savefig(fig, "demo_latex.svg", backend="pgf")
print("[Success] demo_latex.svg 已生成")

plt.show()
