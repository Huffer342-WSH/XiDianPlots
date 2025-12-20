import os
import fitz  # PyMuPDF


def pdf_to_svg(pdf_path, output_svg_path=None):
    """
    将 PDF 转换为 SVG，并针对 Word 插入尺寸偏小的问题进行修正。
    """
    if output_svg_path is None:
        output_svg_path = os.path.splitext(pdf_path)[0] + ".svg"

    try:
        doc = fitz.open(pdf_path)
        page = doc[0]  # 默认只转换第一页

        # --- 核心修复逻辑 ---
        # PDF 原生单位是 72 DPI (Points)
        # Word/Office 默认将 SVG 的单位视为 96 DPI (Pixels)
        # 如果不处理，Word 中的图片会比实际物理尺寸小 (72/96 = 0.75倍)
        # 解决方案：应用 96/72 的放大矩阵，使数值匹配 Word 的 96 DPI 标准
        zoom = 96 / 72  # = 1.3333...
        matrix = fitz.Matrix(zoom, zoom)

        # 使用矩阵生成 SVG，这样 viewBox 和 width/height 都会被放大
        svg_content = page.get_svg_image(matrix=matrix)

        with open(output_svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)

        return output_svg_path

    except ImportError:
        print("[Error] 请先安装 pymupdf: pip install pymupdf")
    except Exception as e:
        print(f"[Error] 转换失败: {e}")


# 测试用
if __name__ == "__main__":
    # 替换为你实际的 pdf 路径
    import sys

    if len(sys.argv) > 1:
        pdf_to_svg(sys.argv[1])
    else:
        print("请拖入或指定一个 PDF 文件路径")
