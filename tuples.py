def get_coordinate(tup):
    tupli = tup[1]
    return tupli

def convert_coordinate(coordenada):
    v1 = coordenada[0:1]
    v2 = coordenada[1:]
    coord = v1, v2
    return coord

def create_record(tup1, tup2):
    coordenada = tup1[1]
    v1 = coordenada[0:1]
    v2 = coordenada[1:2]
    coord = v1, v2
    if coord == tup2[1]:
        return tup1 + tup2
    else:
        return "no coincide"
