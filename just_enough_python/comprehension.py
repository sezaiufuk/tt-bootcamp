name = ["Jack", "Joe", "William", "Avarel"]
surname = ["Dalton"] * len(name)


result = [(i + 1, f"{n} {s}") for i, (n, s) in enumerate(zip(name, surname))]


def test_comprehension():
    assert result == [
        (1, "Jack Dalton"),
        (2, "Joe Dalton"),
        (3, "William Dalton"),
        (4, "Avarel Dalton"),
    ]


even, odd = [], []

for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even = [i for i in range(1, 101) if i % 2 == 0]
odd = [i for i in range(1, 101) if i % 2 != 0]
