human = open("DLX5_human.fa")
for line in human:
    if not line.startswith(">"):
        seq_human = line

mouse = open("DLX5_mouse.fa")
for line in mouse:
    if not line.startswith(">"):
        seq_mouse = line

random = open("RandomSeq.fa")
for line in random:
    if not line.startswith(">"):
        seq_random = line


amino_acid = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
              'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X']

BLOSUM = [
    [4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -
        1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0],
    [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -
        1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1],
    [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -
        2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1],
    [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -
        1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1],
    [0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -
        3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2],
    [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,
        0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1],
    [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -
        2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
    [0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -
        2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1],
    [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -
        1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1],
    [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,
        1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1],
    [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,
        2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1],
    [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -
        1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1],
    [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,
        5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1],
    [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,
        0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1],
    [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -
        1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2],
    [1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -
        1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0],
    [0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -
        1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0],
    [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -
        3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2],
    [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -
        2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1],
    [0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,
        1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1],
    [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -
        3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1],
    [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -
        1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
    [0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -
        1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1]
]


human_mouse_ed = 0
for i in range(len(seq_human)):
    if seq_human[i] != seq_mouse[i]:
        human_mouse_ed += 1

mouse_random_ed = 0
for i in range(len(seq_mouse)):
    if seq_mouse[i] != seq_random[i]:
        mouse_random_ed += 1

human_random_ed = 0
for i in range(len(seq_human)):
    if seq_human[i] != seq_random[i]:
        human_random_ed += 1


def BLOSUM_value(seq1, seq2):
    value = 0
    for i in range(len(seq1)):
        for m in range(len(amino_acid)):
            if amino_acid[m] == seq1[i]:
                x = m
                break
        for n in range(len(amino_acid)):
            if amino_acid[n] == seq2[i]:
                y = n
                break
        value += BLOSUM[x][y]
    return value


# the "\n" should not be included
human_mouse_percentage = 1-human_mouse_ed/(len(seq_human)-1)
mouse_random_percentage = 1-mouse_random_ed/(len(seq_mouse)-1)
human_random_percentage = 1-human_random_ed/(len(seq_random)-1)

print("The alignment score of human and mouse is",
      BLOSUM_value(seq_human, seq_mouse))
print("The alignment score of human and random is",
      BLOSUM_value(seq_human, seq_random))
print("The alignment score of mouse and random is",
      BLOSUM_value(seq_mouse, seq_random))

print("The percentage of identical amino acids for human and mouse is",
      human_mouse_percentage)
print("The percentage of identical amino acids for human and random is",
      human_random_percentage)
print("The percentage of identical amino acids for mouse and random is",
      mouse_random_percentage)
