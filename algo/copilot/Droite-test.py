import droite

def test_droite():
    assert droite.triplet_droite(-2, 0, 1, 1.5) == (-0.5, 1, 1.0)
    assert droite.droite((0, -1), (0, -1)) is None
    assert droite.droite((0, -3), (0, 5)) == (1, 0, 0)

def test_appartient():
    d = (-0.5, 1, 1.0)
    assert droite.appartient(d, (-2, 0)) == True
    assert droite.appartient(d, (1, 1.5)) == True
    assert droite.appartient(d, (0, 0)) == False

def test_paralleles():
    assert droite.paralleles((-0.5, 1, 1.0), (0, 2, 3)) == False
    assert droite.paralleles((0, 1, 1), (0, 2, 3)) == True

def test_intersection():
    assert droite.intersection((-0.5, 1, 1.0), (0, 2, 3)) == (1.0, 1.5)
    assert droite.intersection((0, 1, 1), (0, 2, 3)) is None

def test_droite_normale():
    assert droite.droite_normale((-0.5, 1, 1.0), (-2, 0)) == (2.0, 1, -4.0)
    assert droite.droite_normale((-0.5, 1, 1.0), (3, 4)) == (2.0, 1, 10.0)

def test_symetrie_orthogonale():
    assert droite.symetrie_orthogonale((-0.5, 1, 1.0), (-2, 0)) == (-2.0, 0.0)
    sym = droite.symetrie_orthogonale((-0.5, 1, 1.0), (3, 4))
    assert abs(sym[0] - 4.2) < 1e-2 and abs(sym[1] - 1.6) < 1e-2

def test_distance_droite_point():
    assert droite.distance_droite_point((-0.5, 1, 1.0), (-2, 0)) == 0.0
    assert abs(droite.distance_droite_point((-0.5, 1, 1.0), (3, 4)) - 1.3416407864998741) < 1e-9

if __name__ == "__main__":
    test_droite()
    test_appartient()
    test_paralleles()
    test_intersection()
    test_droite_normale()
    test_symetrie_orthogonale()
    test_distance_droite_point()
    print("Tous les tests ont réussi !")
