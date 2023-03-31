def reverse_words(text: str) -> str:
    if " " in text or "  " in text:
        words = [i[::-1] for i in text.split(" ")]
        return " ".join(words)
    return text[::-1]
