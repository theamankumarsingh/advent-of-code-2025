# Advent of Code 2025 – Solutions

## 🎄 Description
This repository contains my solutions to [**Advent of Code 2025**](https://adventofcode.com/2025), covering **12 Days** Total.

Each day's puzzles are solved in **Python** and organized as:

- `Day X/`
  - `X-1.py` — Part 1 solution  
  - `X-2.py` — Part 2 solution  
  - `X-input.txt` — Puzzle input for both parts  

The `utils/` folder includes helper utilities to auto-generate day folders and starter files.

> ⚠️ Utility scripts are designed for Linux/macOS.

## 📊 Progress Tracker

| Progress | Status |
|---------|--------|
| █████████░░░ | 9/12 Days Completed |

## ⭐ Daily Completion Status

| Day | Part 1 | Part 2 |
|-----|--------|--------|
| Day 1 | ⭐ | ⭐ |
| Day 2 | ⭐ | ⭐ |
| Day 3 | ⭐ | ⭐ |
| Day 4 | ⭐ | ⭐ |
| Day 5 | ⭐ | ⭐ |
| Day 6 | ⭐ | ⭐ |
| Day 7 | ⭐ | ⭐ |
| Day 8 | ⭐ | ⭐ |
| Day 9 | ⭐ | ☐ |
| Day 10 | ⭐ | ☐ |
| Day 11 | ⭐ | ⭐ |
| Day 12 | ☐ | ☐ |

## 🚀 Usage

### Clone the repository
```bash
git clone https://github.com/theamankumarsingh/advent-of-code-2025.git
cd advent-of-code-2025
```

### Virtual environment setup (one-time)
To enable helper utilities (`aoc`, `create_day`, `update_progress`) as commands, run:

```bash
python3 -m venv .venv && echo 'export PATH="$VIRTUAL_ENV/../utils:$PATH"' >> .venv/bin/activate
```

Activate the environment:

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

If you delete `.venv/`, simply run the setup command again.

### Running solutions (direct execution)
All solution files are executable and contain a shebang:
You can run them **directly**:

```bash
./"Day 1"/1-1.py
./"Day 1"/1-2.py
```

Or from inside a day folder:

```bash
cd "Day 1"
./1-1.py
```

If a file is not executable:

```bash
chmod +x "Day 1"/1-1.py
```

### Using the `aoc` helper
The `aoc` command is a convenience wrapper to run solutions without typing full paths.

```bash
aoc 5 2           # run solution for Day 5, Part 2
```

### Using other helper utilities
```bash
create_day 5      # creates the folder and starter files for Day 5
create_day        # uses today's date
update_progress   # updates README progress
```

For example, `create_day 5` generates:

```
Day 5/
  ├── 5-1.py
  ├── 5-2.py
  └── 5-input.txt
```

Thanks for checking this out! 🎅🎁
