import math
# Función para calcular el azimut entre dos puntos (x1, y1) y (x2, y2)
def azimut(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle_rad = math.atan2(dx, dy)   # atan2(dx, dy) → orientación geográfica
    angle_deg = math.degrees(angle_rad)
    return angle_deg % 360

# Termiando el programa principal:

p1_x = float(input("Ingrese la coordenada Este de P1: "))
p1_y = float(input("Ingrese la coordenada Norte de P1: "))
p1 = (p1_x, p1_y)

p2_x = float(input("Ingrese la coordenada Este de P2: "))
p2_y = float(input("Ingrese la coordenada Norte de P2: "))
p2 = (p2_x, p2_y)

print(f"Azimut de P1 a P2: {azimut(*p1, *p2):.2f}°")