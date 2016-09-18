import vector

v1 = [3, 4, 5]
v3 = [7, 8, 9]
v2 = [3, 4, 5]

v5 = [3, 5]
v6 = [3, 4]
v7 = [5, 3, 2]

# test vector equal
print '%s = %s is %s' %(v1, v2, vector.equals(v1, v2))
print '%s = %s is %s' %(v1, v3, vector.equals(v1, v3))
print '%s = %s is %s' %(v2, v3, vector.equals(v2, v3))

# test unit vector
print 'This is the unit vector of e%s = %s' %(u'\u2080', vector.unit_vector(0, 2))
print 'This is the unit vector of e%s = %s' %(u'\u2081', vector.unit_vector(1, 3))
print 'This is the unit vector of e%s = %s' %(u'\u2081', vector.unit_vector(1, 2))
print 'This is the unit vector of e%s = %s' %(u'\u2082', vector.unit_vector(2, 3))

# test convert point to vector
points = [(-1, 2), (0, 0)]
print '%s p2v %s' %(points, vector.p2v(points))

points = [(1, -2), (5, 1)]
print '%s p2v %s' %(points, vector.p2v(points))

points = [(-1, 2, 4), (0, 0, 1)]
print '%s p2v %s' %(points, vector.p2v(points))

# test vector length(magnitude)
print 'length of %s = %.2f' %(v1, vector.length(v1))
print 'length of %s = %.2f' %(v5, vector.length(v5))
print 'length of %s = %.2f' %(v6, vector.length(v6))

# test scaling
print 'Scaling %s by %d = %s' %(v5, 2, vector.scale(v5, 2))
print 'Scaling %s by %d = %s' %(v7, 1.5, vector.scale(v7, 1.5))

# test substract
va = [2, -2]
vb = [1, 4]
print '%s - %s = %s' %(va, vb, vector.substract(va, vb))
print '%s - %s = %s' %(vb, va, vector.substract(vb, va))

# test axpy
va = [-1, 2, 1]
vb = [-2, 3, -3]
alpha = 2

print '%s%s + %s = %s' %(alpha, va, vb, vector.axpy(alpha, va, vb))

# test dot product

va = [3, 2, 1]
vb = [4, 2, 1]

print '%s . %s = %s' %(va, vb, vector.dot_product(va, vb))
