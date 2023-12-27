from Linear_Combination import t,vw,check_vector_span
import numpy as np

print("Equation 1:")
print("Matrix vw:")
print(vw)
print("Vector t:")
print(t)
s= check_vector_span(vw,t)

#Call to check a new set of vectors vw2 and t2
vw2=np.array([[1,2], [2,4]])
t2= np.array([6,12])

s2 = check_vector_span(vw2,t2)

vw3 = np.array([[1,2],[1,2]])
t3= np.array([6,10])

s3= check_vector_span(vw3,t3)