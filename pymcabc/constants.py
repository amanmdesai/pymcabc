from __future__ import annotations

import math

convert = 3.894e8  # GeV^-2 to pb
g = 1
#g = math.sqrt(math.sqrt(20/3))


def outgoing_p(Ecm, m3, m4):
    E = (Ecm**2 - m3**2 - m4**2) / (2 * Ecm)
    E2 = E**2
    return math.sqrt(E2)
