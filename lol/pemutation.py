def toString(List): 
    return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string.
z=0;
def permute(a, l, r,z): 
    if l == r: 
        print (toString(a)) 
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            #print(a,i,z)
            z=z+1
            permute(a, l + 1, r,z) 
            z=z-1
            a[l], a[i] = a[i], a[l] # backtrack 
            #print(a,i,"ea",z)
            
# Driver program to test the above function 
string = "1234567890"
n = len(string) 
a = list(string) 
permute(a, 0, n-1,z) 
