import pymcabc


def test_boost():
    a = pymcabc.Particle(2.,0.,0.,2.)
    b = pymcabc.Particle(3.,0.,0.,1.)
    c = a.boost(b)
    assert c.px == 0
    assert c.py == 0
    assert c.pz**2 - c.E**2 <=1e-5 
    