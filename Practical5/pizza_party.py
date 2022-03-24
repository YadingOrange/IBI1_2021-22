#n represents a given number of straight cuts.
#p represents the maximum number of pizza that can be made with n straight cuts.
n = 0
p = 1
number = 64
while p < number:
    p = (n**2+n+2)/2
    n += 1
    print("the number of cuts is:",n)
    
