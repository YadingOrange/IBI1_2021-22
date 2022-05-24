from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import re
import matplotlib.pyplot as plt
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")  # Find all the term elements.

# Define a dictionary whose keys are parentnodes and values are childnodes.
dic = {}
total_list = []
translation_list = []
number_of_terms = 0

# Calculate the total number of terms.
number_of_terms = len(terms)
print("The total number of terms currently recorded in the Gene Ontology is: ",
      number_of_terms)

# Define a function to calculate the total number of childnodes.


def counter(list):
    for i in list:
        if i not in list_:
            list_.append(i)
            if i in dic:
                counter(dic[i])
    return len(list_)


for term in terms:
    is_a_list = []
    for i in term.getElementsByTagName("is_a"):
        is_a_list.append(i.childNodes[0].data)
    id_all = term.getElementsByTagName("id")[0].childNodes[0].data
    for is_a in is_a_list:
        if is_a in dic:
            dic[is_a].append(id_all)
        else:
            dic[is_a] = [id_all]

for term in terms:
    childnodes_number = 0
    list_ = []
    id_all = term.getElementsByTagName('id')[0].childNodes[0].data
    if id_all in dic:
        childnodes_number = counter(dic[id_all])
    total_list.append(childnodes_number)
    if 'translation' in term.getElementsByTagName("defstr")[0].childNodes[0].data:
        translation_list.append(childnodes_number)


# Print a boxplot describing the distribution of childnodes.
plt.boxplot(total_list, labels=["Gene Ontology"])
plt.title("The distribution of childnodes across terms in the Gene Ontology")
plt.xlabel("terms")
plt.ylabel("the number of childnodes")
plt.show()

# Print a boxplot describing the distribution of childnodes related to translation.
plt.boxplot(translation_list, labels=["translation Gene Ontology"])
plt.title("The distribution of childnodes across terms associated with translation")
plt.xlabel("terms with translation")
plt.ylabel("the number of childnodes")
plt.show()

# Calculate and compare the average childnodes between the overall GO and the "translation" terms.
total_average = sum(total_list)/len(total_list)
translation_average = sum(translation_list)/len(translation_list)
x = "The translation terms contain, on average, a smaller number of childnodes than the overall Gene Ontology."
y = "The translation terms contain, on average, a greater number of childnodes than the overall Gene Ontology."
if total_average > translation_average:
    print(x)
if total_average < translation_average:
    print(y)
# The translation terms contain, on average, a great number of childnodes than the overall Gene Oncology.
