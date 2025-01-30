surname = {"husnu": "sensoy", "alvin": "sensoy", "emre": "yahşi", "ersin": "fidan"}

print(surname["emre"])
print(surname.keys())
print(surname.values())


# TODO: Build a 5 x 50 one matrix Dense representation

# 250 * 4 = 1000 byte
matrix = []

matrix.append([1] * 50)
matrix.append([1] * 50)
matrix.append([1] * 50)
matrix.append([1] * 50)
matrix.append([1] * 50)

print(matrix[3][2])


# pp(matrix)


# Build a document word matrix

n_words = 1_000_000
n_doc = 100_000_000

estimated_memory_size = (n_words * n_doc * 4) / 1024 / 1024 / 1024 / 1024
print(f"Estimated memory requirement is {estimated_memory_size} TB")

estimated_memory_size = (1000 * n_doc * 4) / 1024 / 1024 / 1024 / 1024
print(f"Estimated memory requirement is {estimated_memory_size} TB")


# Sparse

matrix = {}

matrix[(1, 1, 1, 1, 1)] = 1
matrix[(2, 2)] = 1

index_requested = (3, 2)

if index_requested in matrix:
    print(matrix[index_requested])
else:
    print(0)

value = matrix.get(index_requested, 0)
print(value)


index = (1, 1)

i, j = index

print(f"row {i} and col {j}")


i, j, *rest = 1, 1, 0, 1, 4
i, j, *_ = 1, 1, 0, 1, 4

a = 1
b = 0

print(i)
print(j)
print(tuple(rest))

doc_1 = "the brown fox jumps over dog"
doc_2 = "the quick fox jumps over the lazy dog"


matrix = {
    ("the", 1): 1,
    ("the", 2): 1,
    ("brown", 1): 1,
    ("fox", 1): 1,
    ("fox", 2): 1,
    ("jumps", 1): 1,
    ("jumps", 2): 1,
    ("over", 1): 1,
    ("over", 2): 1,
    ("dog", 1): 1,
    ("quick", 2): 1,
    ("lazy", 2): 1,
    ("dog", 2): 1,
}

matrix_1 = {
    ("the",): [1, 2],
    ("brown",): [1],
    ("fox",): [1, 2],
    ("jumps",): [1, 2],
    ("over",): [1, 2],
    ("dog",): [1, 2],
    ("quick",): [1],
    ("lazy",): [1],
}

matrix_2 = [doc_1.split(), doc_2.split()]


words = ["the", "brown", "fox", "jumps", "over", "dog", "quick", "lazy", "dog"]

print(f"Memory requirement for toy corpus is {len(words) * 2 * 4} ")
