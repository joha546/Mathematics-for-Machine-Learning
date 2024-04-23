a=[[2,3],
   [4,5]]

b=[[6,7],
   [8,9]]

result=[[0,0],
        [0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):  # I have written 0 here to extract columns just.
        result[i][j] = b[i][j] - a[i][j]

print(result)

for r in result:
    print(r)


'''Complexity analysis:

Time Complexity: O(N*M)
Auxiliary Space: O(N*M)'''