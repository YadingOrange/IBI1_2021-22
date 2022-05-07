# n represents a given number of straight cuts.
# p represents the maximum number of pizza that can be made with n straight cuts.
# initialize n and p
# use a while loop to compute the minimum value of n when p >= 64
# print the answer



n = 0
p = 0
number = 64
while p < number:
    n += 1
    p = (n**2+n+2)/2

print("the number of cuts is:", n)
print("the number of pieces created at n cuts is", p)
