import re

file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
out = open("cut_genes.fa", "w")

# Set up lists.
Names = []
cuts = []
Sequences = []
# Seperate the names from the sequences.
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
# Write the desired information in the output file.
for i in range(len(Names)):
    if len(re.findall("GAATTC", Sequences[i])) != 0:
        out.write(Names[i])
        out.write("           ")
        out.write(str(cuts[i]))
        out.write("\n")
        out.write(Sequences[i])
        out.write("\n")

out.close()
