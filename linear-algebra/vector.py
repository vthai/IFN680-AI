import math

def _amend(v1, v2):
    diff = len(v2) - len(v1)
    v1.extend([0] * (diff if diff > 0 else 0))
    v2.extend([0] * (abs(diff) if diff < 0 else 0))

def equals(v1, v2):
    if len(v1) != len(v2):
        return False

    for index in range(0, len(v1)):
        if v1[index] != v2[index]:
            return False

    return True

def unit_vector(index, size):
    v = [0] * size
    v[index] = 1
    return v

def p2v(points):
    v = []
    for p1, p2 in zip(points[0::2], points[1::2]):
        for index in range(0, len(p1)):
            v.append(abs(p1[index] - p2[index]))
    return v

def length(v):
    return math.sqrt(sum(v_e * v_e for v_e in v ))

def add(v1, v2):
    _amend(v1, v2)

    return [c1 + c2 for c1, c2 in zip(v1, v2)]

def substract(v1, v2):
    _amend(v1, v2)

    return [c1 - c2 for c1, c2 in zip(v1, v2)]

def scale(v1, alpha):
    return [x * alpha for x in v1]

def axpy(alpha, v1, v2):
    v1 = scale(v1, alpha)
    return add(v1, v2)

def linear_combination(vectors, coefficients):
    vnew = [0] * len(vectors)
    for index in range(0, len(vectors)):
        vnew[index] = scale(vectors[index], coefficients[index])

    v = vnew[0]
    for index in range(1, len(vnew)):
        v = add(v, vnew[index])
    return v

def linear_combination2(vectors, coefficients):
    vnew = [0] * len(vectors[0])
    for index in range(0, len(vectors)):
        vnew = axpy(coefficients[index], vectors[index], vnew)
    return vnew

def dot_product(v1, v2):
    _amend(v1, v2)
    dotp = 0
    for index in range(0, len(v1)):
        dotp += v1[index] * v2[index]
    return dotp

