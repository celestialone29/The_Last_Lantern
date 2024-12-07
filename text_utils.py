def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = []
    for word in words:
        current_line.append(word)
        if len(current_line) >= 7:
            lines.append(" ".join(current_line))
            current_line = []
    if current_line:
        lines.append(" ".join(current_line))
    return lines

