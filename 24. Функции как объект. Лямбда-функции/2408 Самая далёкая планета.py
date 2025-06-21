def find_farthest_orbit(list_of_orbits):
    pi = 3.14159265
    elipses = [pi * a * b for a, b in list_of_orbits if a != b]
    return list_of_orbits[elipses.index(max(elipses))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
