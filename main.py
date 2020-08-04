import math

# ley de coseno

tipo = input("angulo o lado?")
if tipo == "l":
    a = input("primer lado?")
    b = input("segundo lado?")
    C = input("angulo?")
    ang = input("deg o rad?")

    a = float(a)
    b = float(b)
    C = float(C)
    if ang == "r":
        c = math.sqrt((pow(a, 2) + pow(b, 2)) - (2 * a * b * (math.cos(C))))
        A = math.asin((a * (math.sin(C))) / c)
        B = math.asin((b * (math.sin(C))) / c)
        print("c=" + str(c))
        print("A=" + str(A))
        print("B=" + str(B))
    if ang == "d":
        C = math.radians(C)
        c = math.sqrt((pow(a, 2) + pow(b, 2)) - (2 * a * b * (math.cos(C))))
        A = math.asin((a * (math.sin(C))) / c)
        B = math.asin((b * (math.sin(C))) / c)
        A = math.degrees(A)
        B = math.degrees(B)
        print("c=" + str(c))
        print("A=" + str(A))
        print("B=" + str(B))
elif tipo == "a":
    a = input("primer lado?")
    b = input("segundo lado?")
    c = input("tercer lado?")
    ang = input("deg o rad?")

    a = float(a)
    b = float(b)
    c = float(c)

    if ang == "r":
        A = math.acos(((math.pow(b, 2)) + (math.pow(c, 2)) - (math.pow(a, 2))) / (2 * b * c))
        B = math.acos(((math.pow(a, 2)) + (math.pow(c, 2)) - (math.pow(b, 2))) / (2 * a * c))
        C = math.acos(((math.pow(a, 2)) + (math.pow(b, 2)) - (math.pow(c, 2))) / (2 * a * b))
        print("A=" + str(A))
        print("B=" + str(B))
        print("C=" + str(C))
    elif ang == "d":

        A = math.acos(((math.pow(b, 2)) + (math.pow(c, 2)) - (math.pow(a, 2))) / (2 * b * c))
        B = math.acos(((math.pow(a, 2)) + (math.pow(c, 2)) - (math.pow(b, 2))) / (2 * a * c))
        C = math.acos(((math.pow(a, 2)) + (math.pow(b, 2)) - (math.pow(c, 2))) / (2 * a * b))

        print("A=" + str(A))
        print("B=" + str(B))
        print("C=" + str(C))
        A = math.degrees(A)
        B = math.degrees(B)
        C = math.degrees(C)
        print("-----------")
        print("A=" + str(A))
        print("B=" + str(B))
        print("C=" + str(C))
