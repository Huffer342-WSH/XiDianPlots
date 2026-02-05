import os
from matplotlib.figure import Figure
from .convert import pdf_to_svg

def savefig(fig: Figure, filename, dpi=600, backend="pgf", **kwargs):
    """
    增强版保存函数。

    特性:
    1. 默认使用 pgf 后端以支持高质量 LaTeX 渲染。
    2. 当保存为 .svg 且 backend='pgf' 时，自动经由 PDF 中转转换，
       并修正 Word 插入时的尺寸问题。
    """
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    # --- 特殊处理: SVG via PGF ---
    if ext == ".svg" and backend == "pgf":
        # 定义临时 PDF 文件名 (放在同目录下，避免跨盘符问题)
        temp_pdf = filename + ".tmp.pdf"

        try:
            fig.savefig(temp_pdf, dpi=dpi, backend=backend, **kwargs)
            pdf_to_svg(temp_pdf, output_svg_path=filename)

        except Exception as e:
            print(f"[XiDianPlots] SVG 生成失败: {e}")
            # 如果转换失败，且存在生成的 PDF，可以选择不删除以便调试，或者这里保持删除
            # raise e # 可选：抛出异常

        finally:
            # 3. 清理临时 PDF 文件
            if os.path.exists(temp_pdf):
                try:
                    os.remove(temp_pdf)
                except OSError:
                    pass
    else:
        fig.savefig(filename, dpi=dpi, backend=backend, **kwargs)
