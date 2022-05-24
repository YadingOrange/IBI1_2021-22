import re


file = open(input("file name:"), "r")
out = open("count_cut_genes.fa", "w")
# Set up some lists.
Names = []
cuts = []
Lengths = []
Sequences = []

i = 0
for line in file:
    if line.startswith(">"):
        Name = ">"+re.findall(r"gene:(\w+)", line)[0]
        Names.append(Name)
        i += 1  # Count the number of genes.
    if not line.startswith(">"):
        new_line = line.strip("\n")
        if len(Sequences) < i:
            Sequences.append(new_line)
        else:
            # Skip the "\n" by using the list.
            Sequences[i-1] = Sequences[i-1]+new_line

for i in range(len(Sequences)):
    cuts.append(len(re.findall("GAATTC", Sequences[i]))+1)
    Lengths.append(len(Sequences[i]))

# Write the desired information in the output file.
for i in range(len(Names)):
    if len(re.findall("GAATTC", Sequences[i])) != 0:
        out.write(Names[i])
        out.write("           ")
        out.write(str(cuts[i]))
        out.write(str(Lengths[i]))
        out.write("\n")
        out.write(Sequences[i])
        out.write("\n")

out.close()
