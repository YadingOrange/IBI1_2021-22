from argparse import Namespace
import re
genes = input()
file = open(genes, "r")
out = open("count_genes.fa", "w")

Names = []
cuts = []
Sequences = []

i = 0
for line in file:
    if line.startswith(">"):
        Name = ">"+re.findall(r"gene:(\w+)", line)[0]
        Names.append(Name)
        i += 1
    if not line.startswith(">"):
        new_line = line.strip("\n")
        if len(Sequences) < i:
            Sequences.append(new_line)
        else:
            Sequences[i-1] = Sequences[i-1]+new_line

for i in range(len(Sequences)):
    cuts.append(len(re.findall("GAATTC", Sequences[i]))+1)

for i in range(len(Names)):
    if len(re.findall("GAATTC", Sequences[i])) != 0:
        out.write(Names[i])
        out.write("           ")
        out.write(str(cuts[i]))
        out.write("\n")
        out.write(Sequences[i])
        out.write("\n")

out.close()
