# microwave-rotor

Rigid-rotor calculator from microwave peak spacing. Written while studying physical chemistry at York, cleaned up for reuse.

What it does: takes peak spacing in eV and reduced mass from Mr values, returns bond length in Angstrom. Also runs reverse.

## Use

```
pip install -r requirements.txt
python microwave_rotor.py --mr1 1.008 --mr2 35.45 --spacing-ev 1.32e-6
python microwave_rotor.py --mr1 1.008 --mr2 35.45 --bond-ang 1.27
```

## Why

I kept mixing up the hc and eV conversions on paper, so I put it in code with scipy constants. Part of my dry-lab work toward enzyme site calculations.
