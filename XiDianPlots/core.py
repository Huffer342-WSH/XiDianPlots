import matplotlib.pyplot as plt

def use_style(styles=None):
    """
    全局应用 XiDianPlots 风格。
    默认应用 ["xidian", "grid"]。
    """
    if styles is None:
        styles = ["xidian", "grid"]

    # plt.style.use() 会全局应用风格，直到被新的 use() 调用覆盖
    plt.style.use(styles)

    print(f"[XiDianPlots] 风格已全局设置为: {styles}")

def reset_style():
    """
    将 Matplotlib 风格重置为默认值。
    """
    plt.style.use('default')
    print("[XiDianPlots] 风格已重置为 Matplotlib 默认值。")
