# Copilot Instructions for problem-solving Repository

## Project Overview

This is a **competitive programming solutions repository** containing problems solved from multiple online judge platforms (HackerEarth, HackerRank, LeetCode, Project Euler, SPOJ, Rosalind, CodeWars, URI, CodeChef, and others). Each platform has its own directory containing solutions in multiple programming languages.

## Directory Structure & Patterns

**Organization by Platform:**
- `leet-code/` - Organized by language (python/, cpp/, go/) with files named by problem number (e.g., `0001_two_sum.py`)
- `project-euler/` - All C++ solutions, numbered and titled (e.g., `0001 - Multiples of 3 and 5.cpp`)
- `code-wars/` - Flat structure with descriptive problem names (e.g., `Multiply.js`, `Directions Reduction.js`)
- `rosalind/` - Python-focused bioinformatics problems (e.g., `1 - dna.py`)
- `hacker-rank/`, `hacker-earth/`, `spoj/`, `uri/`, `codechef/` - Each contains language-specific subdirectories

## Naming Conventions

**LeetCode Python:** `NNNN_problem_name.py` (zero-padded problem number + snake_case name)
- Example: `0001_two_sum.py`, `0200_number_of_islands.py`

**Project Euler C++:** `NNNN - Problem Name.cpp` (zero-padded + title case)
- Example: `0001 - Multiples of 3 and 5.cpp`

**CodeWars:** Space-separated descriptive names
- Example: `Multiply.js`, `RGB To Hex Conversion.js`

**Rosalind Python:** `N - problem_name.py` (sequential number)
- Example: `1 - dna.py`, `4 - fib.py`

## Solution Structure Patterns

**LeetCode Python (Object-Oriented):**
```python
class Solution:
  def methodName(self, params: Type) -> ReturnType:
    # Implementation using helper methods or nested functions
    pass
```

**Project Euler C++ (Procedural):**
```cpp
/* 
   Project Euler
   Problem N
   Problem Name: Title
*/

#include <iostream>
using namespace std;

int main() {
  // Implementation
  return 0;
}
```

**Rosalind Python (Functional with docstring):**
```python
"""
Rosalind
Problem Name: Title
"""

def helper_function(param):
  # Implementation
  pass

# Main logic: read input, call functions, print results
```

**CodeWars JavaScript (Function-focused):**
- Single function solution or minimal wrapper
- Often includes commented "BEST" solutions showing idiomatic approaches

## Common Implementation Patterns

- **Graph/Tree Traversal:** DFS using recursion (see `0200_number_of_islands.py`)
- **Hash Maps/Dictionaries:** Used extensively for O(1) lookups (see `0001_two_sum.py`)
- **Dynamic Programming:** Common in LeetCode solutions
- **Stack-based Operations:** Used for bracket matching, reversal problems (see `Directions Reduction.js`)
- **Bit Manipulation:** Frequent in lower-numbered LeetCode problems

## Language Distribution

- **Python:** Dominant (LeetCode, Rosalind, many HackerRank/Earth)
- **C++:** Project Euler, competitive programming focus
- **JavaScript:** CodeWars platform
- **Java:** Selected HackerRank problems

## When Adding New Solutions

1. **Determine Platform:** Identify which online judge the problem comes from
2. **Follow Naming:** Use the platform's established naming convention
3. **Pick Language:** Match the language used in existing solutions for that platform
4. **Include Headers:** Add comment headers for clarity (especially Project Euler style with problem name)
5. **Maintain Structure:** If language subdirectories exist (e.g., `leet-code/python/`), place the file there
6. **Reusable Utils:** No shared utility files—each solution is self-contained and independent

## Testing & Validation

- Solutions are typically tested directly on platform judges
- Compile Project Euler C++ with: `g++ -o program "0001 - Multiples of 3 and 5.cpp"`
- Run LeetCode/Rosalind Python: `python solution.py`
- No local test infrastructure present—rely on platform feedback

## Key Files & Examples

- `leet-code/python/0001_two_sum.py` - Exemplary hash map approach
- `leet-code/python/0200_number_of_islands.py` - DFS traversal pattern
- `project-euler/0001 - Multiples of 3 and 5.cpp` - Project Euler style
- `rosalind/1 - dna.py` - Rosalind bioinformatics pattern
- `code-wars/Directions Reduction.js` - CodeWars JavaScript with alternative solutions

## Notes for AI Agents

- **No build system:** Solutions are standalone files, not part of a build pipeline
- **No dependencies:** Avoid adding external libraries unless required by platform constraints
- **Platform-specific styles:** Match the conventions already established for each platform
- **Comments:** Keep minimal but include problem context headers (especially for Project Euler/Rosalind)
- **No configuration files:** No package.json, requirements.txt, or Makefile needed
