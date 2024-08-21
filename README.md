# Sorting Visualizer

## Overview

This project is a sorting visualizer built using Pygame and Pygame Menu. It allows users to interactively choose and visualize various sorting algorithms through a graphical interface. The visualizer displays sorting operations in real-time, making it easier to understand and compare different sorting methods.

## Features

- **Interactive Menu**: Select from a variety of sorting algorithms and adjust sorting speed and the number of items to be sorted.
- **Real-Time Visualization**: Watch how different sorting algorithms process and sort data visually.

## Getting Started

1. **Install Dependencies**:
   Ensure you have `pygame` and `pygame-menu` installed. You can install them via pip:
   ```bash
   pip install pygame==2.5.2 pygame-menu==4.4.3
   ```

2. **Run the Program**:
   Execute the main script to start the visualizer:
   ```bash
   python main.py
   ```

3. **Using the Menu**:
   - **Sorting Algorithm**: Choose from available sorting algorithms (e.g., Bubble Sort, Quick Sort).
   - **Sorting Speed**: Adjust the speed of sorting (lower values are faster).
   - **Amount of Items**: Set the number of items to sort.

4. **Start Sorting**:
   Click the "Start Sorting" button to see the selected sorting algorithm in action.

## Sorting Algorithms

- **Bubble Sort**: A simple comparison-based sorting algorithm.
- **Insertion Sort**: Builds the sorted array one item at a time.
- **Selection Sort**: Selects the smallest element and places it in the correct position.
- **Quick Sort**: Uses a divide-and-conquer approach to sort data efficiently.
- **Merge Sort**: Divides the array into halves, sorts each half, and merges them.
