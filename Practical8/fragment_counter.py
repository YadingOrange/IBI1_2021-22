import re
seq = "ATGCAATCGACTACGATCAATCGAGGGCC"
# The number of cuts plus 1 equals the number of cut genes.
number = len(re.findall("GAATTC", seq))+1
print(number)
