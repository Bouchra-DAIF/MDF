import math
import cv2


def Show(L):
    img = cv2.imread("gr.jpeg")
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (749, 365)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    img = cv2.putText(img, '= ' + str(round(L, 4)) + ' mm', org, font, fontScale, color, thickness, cv2.LINE_AA)
    return img


def LDeltaP(D1, V1, V2, alpha, Rou, show=True):
    L = (-D1 / (2 * math.tan(10 * math.pi / 180))) * ((math.sqrt(V1) / math.sqrt(V2)) - 1)
    DeltaP = 1 / 2 * Rou * (math.pow(V1, 2) - math.pow(V2, 2))
    print("L = " + str(L) + " mm")
    print("P2 - P1 = " + str(DeltaP) + " Pa")
    img = Show(L)
    if (show == True):
        cv2.imwrite('result.jpeg', img)


if _name_ == "_main_":
    D1 = float(input("Entrer la valeur de D1 : "))
    V1 = float(input("Entrer la valeur de V1 : "))
    V2 = float(input("Entrer la valeur de V2 : "))
    alpha = float(input("Entrer la valeur d'Alpha : "))
    Rou = float(input("Entrer la valeur de Rou : "))
    LDeltaP(D1, V1, V2, alpha, Rou, True)