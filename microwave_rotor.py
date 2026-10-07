"""Rigid rotor microwave calculator.
Takes rotational peak spacing, returns bond length (and reverse).
Usage:
  python microwave_rotor.py --mr1 1.008 --mr2 35.45 --spacing-ev 1.2e-6
  python microwave_rotor.py --mr1 1.008 --mr2 35.45 --bond-ang 1.27
"""
import argparse
from scipy import constants

def bond_length_ang(mr1, mr2, spacing_ev):
    m_u = constants.atomic_mass
    m1, m2 = mr1 * m_u, mr2 * m_u
    spacing_j = spacing_ev * constants.e
    h, pi = constants.h, constants.pi
    num = h**2 * (m1 + m2)
    den = 4 * pi**2 * m1 * m2 * spacing_j
    return (num / den) ** 0.5 * 1e10

def peak_spacing_ev(mr1, mr2, bond_ang):
    m_u = constants.atomic_mass
    m1, m2 = mr1 * m_u, mr2 * m_u
    r = bond_ang * 1e-10
    h, pi = constants.h, constants.pi
    mu = m1 * m2 / (m1 + m2)
    return h**2 / (4 * pi**2 * mu * r**2) / constants.e

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--mr1", type=float, required=True)
    p.add_argument("--mr2", type=float, required=True)
    p.add_argument("--spacing-ev", type=float, default=None)
    p.add_argument("--bond-ang", type=float, default=None)
    a = p.parse_args()
    if a.spacing_ev:
        print(f"{bond_length_ang(a.mr1, a.mr2, a.spacing_ev):.3f} Angstrom")
    elif a.bond_ang:
        print(f"{peak_spacing_ev(a.mr1, a.mr2, a.bond_ang):.3e} eV")
    else:
        p.error("give --spacing-ev or --bond-ang")
