def hacker_signature_compact(text="SCR BY LEV1N", char="#"):
    """
    Docstring for hacker_signature_compact
    Подпись для скриптов
    
    :param text: Фраза для подписи
    :param char: Символ отрисовки
    """
    
    ascii_chars = {
        'S': ["┌─┐", "└─┐", "└─┘"],
        'C': ["┌─┐", "│  ", "└─┘"],
        'R': ["┌─┐", "├─┘", "│ └"],
        'B': ["┌─┐", "├─┤", "└─┘"],
        'Y': ["┬ ┬", "└┬┘", " ┴ "],
        'L': ["│  ", "│  ", "└─┘"],
        'E': ["┌──", "├──", "└──"],
        'V': ["┬ ┬", "│ │", "└─┘"],
        '1': [" ┬ ", " │ ", "─┴─"],
        'N': ["┌┐ ┬", "│└┐│", "└─┘┴"],
        ' ': ["   ", "   ", "   "],
    }
    
    # Для очень компактного варианта можно использовать специальные символы
    # Или простой вариант:
    ascii_chars_simple = {
        'S': ["▄▀▀", "▄▀ ", " ▀▀"],
        'C': ["▄▀▀", "█  ", "▀▀▄"],
        'R': ["▄▀▀", "█▀▀", "█ ▀"],
        'B': ["▄▀▀", "█▀▀", "▀▀▄"],
        'Y': ["▀ ▀", " ▀ ", " ▄ "],
        'L': ["█  ", "█  ", "▀▀▀"],
        'E': ["▄▀▀", "█▀ ", "▀▀▀"],
        'V': ["▀ ▀", "▀ ▀", " ▀ "],
        '1': [" █ ", "██ ", " █ "],
        'N': ["█▄ █", "█ ██", "█ ██"],
        ' ': ["   ", "   ", "   "],
    }
    
    parts = text.split()
    ascii_lines = [[] for _ in range(3)]
    
    for part in parts:
        for letter in part:
            if letter in ascii_chars_simple:
                for i in range(3):
                    ascii_lines[i].append(ascii_chars_simple[letter][i])
            else:
                for i in range(3):
                    ascii_lines[i].append(ascii_chars_simple[' '][i])
        for i in range(3):
            ascii_lines[i].append("  ")
    
    result_lines = []
    for line in ascii_lines:
        result_line = " ".join(line)
        result_line = result_line.replace('█', char).replace('▄', char).replace('▀', char)
        result_lines.append(result_line.rstrip())
    
    # Простая рамка
    width = max(len(line) for line in result_lines) + 4
    border = "+" + "-" * (width - 2) + "+"
    
    print(border)
    for line in result_lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"|{' ' * left_pad}{line}{' ' * right_pad}|")
    print(border)

# Пример использования
if __name__ == "__main__":
    hacker_signature_compact("SCR BY LEV1N", "#")
    print("\n" +  "\n")