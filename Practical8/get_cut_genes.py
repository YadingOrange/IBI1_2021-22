from argparse import Namespace
import re
file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
out = open("cut_genes.fa", "w")
Names = []
Lengths = []
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
    Lengths.append(len(Sequences[i]))

for i in range(len(Names)):
    if len(re.findall("GAATTC", Sequences[i])) != 0:
        out.write(Names[i])
        out.write("           ")
        out.write(str(Lengths[i]))
        out.write("\n")
        out.write(Sequences[i])
        out.write("\n")

out.close()
