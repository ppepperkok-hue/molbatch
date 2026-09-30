# molbatch

Batch-generate 2D and 3D chemical structures from a list of compound names.

`molbatch` takes a list of compound identifiers (names, SMILES, molecular formulas)
and produces 2D structure images and 3D structure files in one run. It is meant to
be simple enough for coursework and lab reports: give it a list, get files back.

## Design decision: reuse ChemDraw / Chem3D

This tool does **not** reimplement chemical drawing or 3D conformer generation.
It drives the ChemDraw / Chem3D installation already present on the machine.
Name-to-structure parsing and 3D geometry are the vendor's engine's job; this
project is the batch driver around it.

See [`docs/00-立项规划.md`](docs/00-立项规划.md) for the feasibility study on
which call paths actually work (measured, not assumed).

## Status

Early development. Phase 0 (project definition) in progress.

## Requirements

- Windows
- ChemDraw / Chem3D (Revvity ChemDraw Suite)
- Python 3.10+ with RDKit

## Repository layout

```
docs/          project documents (Phase 0 checklist, architecture, ...)
src/           application source
tests/         tests
```
