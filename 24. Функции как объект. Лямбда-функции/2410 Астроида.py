import math

min_dist = float('inf')
target_x, target_y = 0.75, 0

# Перебираем t с маленьким шагом
for i in range(100000):
    t = 2 * math.pi * i / 100000
    x = math.cos(t) ** 3
    y = math.sin(t) ** 3
    dist = math.hypot(x - target_x, y - target_y)
    if dist < min_dist:
        min_dist = dist

print(f"{min_dist:.4f}")
