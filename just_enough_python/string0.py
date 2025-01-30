s = "Hello World"

print(s)

name = "husnu"
surname = "sensoy"

welcome = f"Hello {name} {surname}"

print(welcome)

welcome = f"Hello {name.title()} {surname.title()}"

print(welcome)


text = "The quick brown fox"

print(text.split())


def test_indexing_and_slice_in_python():
    assert text[0] == "T"
    assert text[:3] == "The"
    assert text[-3:] == "fox"
    assert text[1:3] == "he"
    assert text[-4] == " "
