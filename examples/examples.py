import matplotlib.pyplot as plt
import numpy as np

def run_test():
    print("-" * 50)
    print("[Test] 正在导入 XiDianPlots...")
    try:
        import XiDianPlots
        print("[Test] 导入成功！")
    except ImportError:
        print("[Test] 错误：无法导入 XiDianPlots，请先安装库。")
        exit(1)

    # 准备数据
    x = np.linspace(0, 4 * np.pi, 100)
    y1 = np.sin(x) * np.exp(-0.1 * x)
    y2 = np.cos(x)

    try:
        with plt.style.context(["xidian", "grid"]):
            fig, ax = plt.subplots()

            ax.plot(x, y1, label=r"Theory: $e^{-\alpha t} \sin(\omega t)$")
            ax.plot(x, y2, label=r"Experiment: $\cos(\theta)$")

            ax.set_xlabel(r"时间 Time ($t$)")
            ax.set_ylabel(r"幅值 Amplitude ($A$)")
            ax.set_title(r"系统响应 System Response")
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

    except Exception as e:
        print(f"[Fail] 绘图失败: {e}")



if __name__ == "__main__":
    run_test()
