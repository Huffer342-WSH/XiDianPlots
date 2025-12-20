import os
import glob
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import rc_params_from_file

# --- 路径配置 ---
STYLE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_FILENAME = 'RomanSong.ttf'
FONT_PATH = os.path.join(STYLE_DIR, FONT_FILENAME)

def _register_font():
    """注册字体到 Matplotlib (仅对非 LaTeX 模式有效)"""
    if os.path.exists(FONT_PATH):
        try:
            font_manager.fontManager.addfont(FONT_PATH)
        except Exception as e:
            print(f"[XiDianPlots] 警告: 无法注册字体 {FONT_FILENAME} - {e}")
    else:
        # 仅提示，不阻断，因为 LaTeX 模式可能不需要此文件
        pass

def _register_styles():
    """自动注册当前目录下所有的 .mplstyle 文件"""
    # 查找所有 .mplstyle 文件
    style_files = glob.glob(os.path.join(STYLE_DIR, '*.mplstyle'))

    for style_file in style_files:
        try:
            # 获取文件名作为样式名称 (例如 xidian.mplstyle -> xidian)
            filename = os.path.basename(style_file)
            style_name = os.path.splitext(filename)[0]

            # 读取样式
            style_dict = rc_params_from_file(style_file, use_default_template=False)

            # 注册到 matplotlib
            plt.style.library[style_name] = style_dict
            # print(f"[XiDianPlots] 已注册样式: {style_name}")

        except Exception as e:
            print(f"[XiDianPlots] 样式 {style_file} 注册失败: {e}")

# --- 初始化执行 ---
_register_font()
_register_styles()
