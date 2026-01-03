# C Code Error Correction using Decision Tree

## Overview
This project implements an **automatic error detection and correction tool for C code** using a **decision tree approach**. It helps programmers identify common syntax and logical errors in their C programs and suggests possible fixes, improving code quality and reducing debugging time.

## Features
- Detects syntax errors in C code.
- Suggests corrections based on learned patterns.
- Uses a **decision tree algorithm** for error classification.
- Lightweight and easy to integrate with other C projects.
- Provides a simple command-line interface for testing C code.

## How it Works
1. **Input:** The tool takes a C source code file (`.c`) as input.
2. **Analysis:** It scans the code to detect errors using pre-defined patterns.
3. **Decision Tree:** Each error is classified with a decision tree to suggest the most probable correction.
4. **Output:** Displays the error location and suggested correction to the user.
