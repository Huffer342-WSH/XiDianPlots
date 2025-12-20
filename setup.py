import os
import sys
import urllib.request
from setuptools import setup
from setuptools.command.build_py import build_py

# 配置信息
PACKAGE_NAME = "XiDianPlots"
STYLE_DIR = os.path.join(PACKAGE_NAME, "style")
FONT_FILENAME = "RomanSong.ttf"
FONT_URL = "https://cdn.jsdelivr.net/gh/AaaGss/Font_RomanSong@main/RomanSong.ttf"
FONT_PATH = os.path.join(STYLE_DIR, FONT_FILENAME)

class CustomBuildPy(build_py):
    """自定义构建命令：在构建/安装前下载字体"""
    def run(self):
        self.download_font()
        super().run()

    def download_font(self):
        # 检查是否已经是本地文件（避免重复下载）
        if os.path.exists(FONT_PATH):
            print(f"[{PACKAGE_NAME}] 字体已存在，跳过下载: {FONT_PATH}")
            return

        print(f"[{PACKAGE_NAME}] Setup 正在下载字体...")
        print(f"[{PACKAGE_NAME}] 源: {FONT_URL}")

        try:
            # 确保目录存在
            os.makedirs(STYLE_DIR, exist_ok=True)
            # 使用 urllib 下载，避免 setup 阶段依赖 requests
            urllib.request.urlretrieve(FONT_URL, FONT_PATH)
            print(f"[{PACKAGE_NAME}] 字体下载成功！")
        except Exception as e:
            print(f"[{PACKAGE_NAME}] 警告: 字体下载失败 - {e}")
            print(f"[{PACKAGE_NAME}] 安装将继续，但字体可能缺失。")

# 为了兼容 pip install -e . (Editable mode)，有时也需要覆盖 develop
from setuptools.command.develop import develop
class CustomDevelop(develop):
    def run(self):
        CustomBuildPy(self.distribution).download_font()
        super().run()

# 即使有 pyproject.toml，当我们需要自定义 cmdclass 时，
# setup() 调用依然是必须的
setup(
    cmdclass={
        'build_py': CustomBuildPy,
        'develop': CustomDevelop,
    },
)
