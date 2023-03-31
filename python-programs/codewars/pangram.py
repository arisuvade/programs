def is_pangram(s: str) -> bool:
    alphabet = list(map(chr, range(97, 123)))
    formattedString = "".join(c for c in s if c.isalpha()).lower()
    return True if set(alphabet) == set(formattedString) else False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
