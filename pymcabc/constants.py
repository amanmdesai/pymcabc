from __future__ import annotations

import math

pi = math.pi
alpha = 1 / 132.507  # alpha QED
delta = 2.0  # delta theta (radian)
convert = 3.894e8  # GeV^-2 to pb
g = 1.0
# m = 0.000511  # mass of electron in gev


def outgoing_p(Ecm, m3, m4):
    p = (Ecm**2 + m3**2 - m4**2) / (2 * Ecm)
    p = p**2
    p = p - m3**2
    return math.sqrt(p)
