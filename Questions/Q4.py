#************LIst comprehension Question.

#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise

x = int(input("Enter co-ordinate: "))
y = int(input("Enter co-ordinate: "))
z = int(input("Enter co-ordinate: "))
n = int(input("Enter co-ordinate: "))

 #list comprehension.
newlist = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if i + j + k != n ]

print(newlist)

#without list comprehension
newlist_2 = []
for i in range(x+1):
    
    for j in range(y+1):
        
        for k in range(z+1):
            
            if i+j+k != n:
                
                newlist_2.append([i,j,k])
            
print(newlist_2)
