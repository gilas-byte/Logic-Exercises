# Logic-Exercises

![License: MIT](https://img.shields.io/badge/License-MIT-blue) ![Python](https://img.shields.io/badge/Language-Python-blue)

Logic exercises for personal study, including LeetCode problems and original exercises.
Currently contains a Python solution to the Two Sum problem.

## What it does

The Two Sum script reads integers and a target from the terminal, then prints the
indices of two numbers whose sum equals the target. It prints `None` when no pair
is found.

This is a study repository with one exercise, not a complete course or a library.
Input validation is incomplete: invalid input can cause the script to fail or
continue with fewer numbers than requested. There is no automated test suite.

## Repository structure

- `python/twoSum.py` — Two Sum solution and interactive terminal interface.
- `README.md` — repository overview and usage instructions.
- `LICENSE` — MIT license.

## How to run

Requires Python 3. The script uses only the standard library; no additional
packages are needed.

Clone the repository and run the script from its root directory:

```sh
git clone https://github.com/gilas-byte/Logic-Exercises
cd Logic-Exercises
python3 python/twoSum.py
```

Enter the number of integers, each integer separately, and then the target when
prompted. For example, enter `4`, then `2`, `7`, `11`, `15`, and finally `9`.
The result is `The solution is: [0, 1]` (zero-based indices).

## Status

Study project.

## License

Licensed under the [MIT License](LICENSE).
