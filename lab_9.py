A=dict()
B=dict() 
Y=dict()

A={'0':0, '20':0.5, '40':0.65, '60':0.85, '80':1, '100':1}
B={'0':0, '20':0.35, '40':0.5, '60':0.75, '80':0.90, '100':1}

print('The First Fuzzy Set is :', A) 
print('The Second Fuzzy Set is :', B)

#Complement
for A_key in A: 
   Y[A_key]= 1-A[A_key] 
          
print('First Fuzzy Set Complement is :', Y)

for B_key in B: 
   Y[B_key]= 1-B[B_key] 
          
print('Second Fuzzy Set Complement is :', Y)

#Union
for A_key, B_key in zip(A, B): 
    A_value = A[A_key] 
    B_value = B[B_key] 
  
    if A_value > B_value: 
        Y[A_key] = A_value 
    else: 
        Y[B_key] = B_value 
          
print('Fuzzy Set Union is :', Y)

#Intersection
for A_key, B_key in zip(A, B): 
    A_value = A[A_key] 
    B_value = B[B_key] 
  
    if A_value < B_value: 
        Y[A_key] = A_value 
    else: 
        Y[B_key] = B_value 
print('Fuzzy Set Intersection is :', Y)

#De Morgans Law
for A_key, B_key in zip(A,B):
    A_value=1-A[A_key]
    B_value=1-B[B_key]

    if A_value < B_value:
        Y[A_key]=1-A[A_key]
    else:
        Y[B_key]=1-B[B_key]

print('Fuzzy set De morgans law LHS:',Y)

for A_key, B_key in zip(A,B):
    A_value=A[A_key]
    B_value=B[B_key]

    if A_value > B_value:
        Y[A_key]=1-A[A_key]
    else:
        Y[B_key]=1-B[B_key]

print('Fuzzy set De morgans law RHS:',Y)
