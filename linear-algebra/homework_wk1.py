import vector

'''
    Decide if the two vectors are equal:
    1) The vector represented geometrically in R2 by an arrow from point (-1, 2) to point (0, 0) and the vector represented
    geometrically in R2 by an arrow from point (1, -2) to point (2, -1) are equal.

    2) The vector represented geometrically in R3 by an arrow from point (1, -1, 2) to point (0, 0 , 0) and the vector represented 
    geometrically in R3 by an arrow from point (1, -1, 2) to point (0, 2, -4) are equal
'''

points1 = [(-1, 2), (0, 0)]
points2 = [(1, -2), (2, -1)]

print '%s = %s is %s' %(points1, points2, vector.equals(vector.p2v(points1), vector.p2v(points2)))

points1 = [(1, -1, 2), (0, 0 , 0)]
points2 = [(1, -1, 2), (0, 2, -4)]

print '%s = %s is %s' %(points1, points2, vector.equals(vector.p2v(points1), vector.p2v(points2)))

# hw 1.3.2.1
v1 = [-1, 3]
v2 = [-3, -2]

print '%s + %s = %s' %(v1, v2, vector.add(v1, v2))

v1 = [-3, -2]
v2 = [-1, 2]
print '%s + %s = %s' %(v1, v2, vector.add(v1, v2))

v1 = [1, 1, 3]
v2 = [2, 2]
print '%s + %s = %s' %(v1, v2, vector.add(v1, v2))

# hw 1.4.2.1
vs = [[2, 4, -1, 0], [1, 0, 1, 0]]
coefficients = (3, 2)

print '%s linear_combination %s = %s' %(vs, coefficients, vector.linear_combination(vs, coefficients))
print '%s linear_combination2 %s = %s' %(vs, coefficients, vector.linear_combination2(vs, coefficients))

# hw 1.4.2.2
vs = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
coefficients = (-3, 2, 4)

print '%s linear_combination %s = %s' %(vs, coefficients, vector.linear_combination(vs, coefficients))
print '%s linear_combination2 %s = %s' %(vs, coefficients, vector.linear_combination2(vs, coefficients))

# hw 1.4.3.1
vs = [[2, 5, -6, 1], [1] * 6]
print '%s . %s = %s' %(vs[0], vs[1], vector.dot_product(vs[0], vs[1]))


