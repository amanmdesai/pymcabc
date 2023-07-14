from __future__ import annotations

import math

convert = 3.894e8  # GeV^-2 to pb
g = 1
#g = math.sqrt(math.sqrt(20/3))


def outgoing_p(Ecm, m3, m4):
    E = (Ecm**2 - m3**2 - m4**2) / (2 * Ecm)
    return E

def f_lambda(mA, mB, mC, mX):
    p = mA**4 + mB**4 + mC**4 - 2*(mA**2)*(mB**2) - 2*(mA**2)*(mC**2) - 2*(mB**2)*(mC**2)
    return math.sqrt(p/(2*mX))
