# 🚀 Data Structures & Algorithms (DSA) Portfolio

A production-ready repository dedicated to mastering Computer Science fundamentals, algorithm design, and problem-solving patterns. Every problem is extracted from browser-based environments and implemented locally using clean code principles, rigorous Big-O analysis, and explicit automated test cases.

---

## 🛠️ Repository Architecture

The codebase is organized by specific algorithmic patterns to ensure scalability and quick retrieval. Each folder represents a distinct computational topic and contains sequentially numbered solutions:

```text
leetcode-portfolio/
│
├── Arrays_and_Hashing/      # Frequency tables, sliding windows, prefix sums
├── Two_Pointers/            # Bi-directional and fast/slow pointer techniques
├── Sliding_Window/          # Subarray optimization problems
├── Stack/                   # Monotonic stacks and LIFO operations
├── Binary_Search/           # Logarithmic time search boundaries
├── Linked_List/             # Pointer manipulation and traversal
├── Trees/                   # DFS, BFS, Binary Search Trees (BST)
├── Heap_Priority_Queue/     # K-way merge, top-K elements optimization
├── Backtracking/            # Combinations, permutations, and state-space search
├── Graphs/                  # Adjacency lists, matrix traversal, shortest path algorithms
└── Dynamic_Programming/     # Memoization and bottom-up state optimization
```

---

## 🧬 Code Engineering Standards

Every solution file follows a strict architectural contract to mirror enterprise-level software engineering:

1. **Type Hinting:** Explicit parameter and return type declarations for type safety and compilation-like validations.
2. **Comprehensive Docstrings:** Structured problem metadata including LeetCode URLs, explicit Time/Space Complexity metrics, and a clear thought process breakdown.
3. **Automated Local Verification:** Built-in `if __name__ == "__main__":` driver blocks executing deterministic test suites directly on the local machine without browser dependency.

---

## 💻 Local Execution & Verification

To run and verify any algorithm locally on your machine, clone the repository and execute the target script via python CLI:

```bash
# Example 1: Executing Max Consecutive Ones solution
python3 Arrays_and_Hashing/0485_max_consecutive_ones.py

# Example 2: Executing Find Numbers with Even Number of Digits solution
python3 Arrays_and_Hashing/1295_find_numbers_with_even_digits.py
```