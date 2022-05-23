from argparse import Namespace
import re
<<<<<<< HEAD
genes=input()
file = open(genes, "r")
out = open("count_genes.fa", "w")

Names = []
cuts = []
=======
file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
out = open("cut_genes.fa", "w")
Names = []
Lengths = []
>>>>>>> d5a6fb4142746598b2ab345d6ead21ae34b8831e
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
<<<<<<< HEAD
    cuts.append(len(re.findall("GAATTC",Sequences[i]))+1)
=======
    Lengths.append(len(Sequences[i]))
>>>>>>> d5a6fb4142746598b2ab345d6ead21ae34b8831e

for i in range(len(Names)):
    if len(re.findall("GAATTC", Sequences[i])) != 0:
        out.write(Names[i])
        out.write("           ")
<<<<<<< HEAD
        out.write(str(cuts[i]))
=======
        out.write(str(Lengths[i]))
>>>>>>> d5a6fb4142746598b2ab345d6ead21ae34b8831e
        out.write("\n")
        out.write(Sequences[i])
        out.write("\n")

out.close()
