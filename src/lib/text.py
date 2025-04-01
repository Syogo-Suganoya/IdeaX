import re


def read_text_file(file_path):
    """指定したテキストファイルの内容を文字列として返す"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりません。")
        return ""
    except Exception as e:
        print(f"エラー: {e}")
        return ""


def remove_code_blocks(text):
    """先頭と末尾の連続クォーテーションを削除"""
    lines = text.splitlines()

    code_block_pattern = re.compile(r"^```[\w-]*$")
    if code_block_pattern.match(lines[0]):
        lines.pop(0)  # 先頭削除
        if code_block_pattern.match(lines[-1]):
            lines.pop(-1)  # 末尾削除
    return "\n".join(lines)
