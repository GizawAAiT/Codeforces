def solve(polygon):
    _faces = {
        'Tetrahedron': 4,
        'Cube': 6,
        'Octahedron': 8,
        'Dodecahedron': 12,
        'Icosahedron': 20
    }
    
    total = 0
    for poly in polygon:
        total += _faces[poly]
    
    return total

n = int(input())
polygon = []
for _ in range(n):
    polygon.append(input().strip())

print(solve(polygon))