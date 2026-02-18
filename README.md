# Data Structures & Algorithms — Course Repository

This repository contains my notes, exercises, and implementations from a Data Structures & Algorithms course. It collects solved problems, utility scripts, and Jupyter notebooks used while learning and practicing core DSA concepts.

Table of Contents
- Overview
- Repo structure
- Getting started
- How to run examples
- Notebooks
- Common utilities
- Contribution
- License

## Overview

This folder organizes exercises and examples by topic (arrays, strings, linked lists, sorting, etc.). The materials include:

- Python scripts with problem solutions and helpers.
- Jupyter notebooks used for interactive exploration and experimentation.
- Small utilities and example datasets used by the exercises.

The work here is intended for learning and reference — not production-ready libraries.

## Repo structure

- `1-d-array/`, `2d-array/`, `linked-list/`, `sorting/`, `string/`, `two_pointer/`, etc. — topic folders containing solutions and practice problems.
- `daily-dsa-problems/` — daily practice problem sets.
- `find_*` scripts (e.g., `find_alphabets.py`) — small single-file exercises.
- `list_files.py` — helper script used for listing or inspecting files.
- `README.md` — this file.

Example top-level files and folders:

- `1-d-array/`
- `2d-array/`
- `linked-list/`
- `sorting/`
- `string/`
- `daily-dsa-problems/`

## Getting started

Prerequisites
- Python 3.8+ is recommended.

Setup (recommended)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (there is no central `requirements.txt` by default; install packages only as needed for notebooks):

```powershell
pip install jupyterlab numpy pandas matplotlib
```

If you prefer conda:

```powershell
conda create -n dsa python=3.10
conda activate dsa
pip install jupyterlab numpy pandas matplotlib
```

## How to run examples

- Run a Python script:

```powershell
python "1-d-array/find_sorted_sum.py"
```

## Common utilities

- `list_files.py` — small utility that lists files in directories (useful for quick inspection).
- Single-file exercises named `find_*.py` — self-contained scripts demonstrating algorithms.

## Style & conventions

- Solutions are written in readable Python, prioritizing clarity over micro-optimizations.
- Filename conventions: folders group topics; individual solutions are placed in topic folders.

## Contributing

Contributions and suggestions are welcome. If you want to add a solution, please:

1. Add your solution in the appropriate topic folder.
2. Follow the repository's style (clear function names, short docstrings).
3. Open a pull request with a brief description of the added problems/solutions.

If you want me to add tests or a `requirements.txt`, tell me which packages you want pinned and I can add them.

## License

This repository is for personal learning. If you want to add an explicit license, add a `LICENSE` file and update this section.

---

If you want, I can also:

- Add a `requirements.txt` based on the notebooks used.
- Add example unit tests for a few solutions.
- Create a small CLI to run selected problems by name.

Tell me which of the above you'd like next.
