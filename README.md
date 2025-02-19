
# Algorithms Collection

## Overview
This repository contains various AI-related algorithms and fundamental computer science concepts, implemented in Python. It includes sorting algorithms, graph algorithms, cryptographic functions, and deep learning models. Each algorithm is provided with clear explanations and code to enhance understanding.

## Contents

### Sorting Algorithms (Sorting_Algorithm/)
Efficient sorting techniques used in AI preprocessing:

- **`bubble_sort.py`**:  
  *Bubble Sort* is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This continues until the list is sorted. Although simple, it is inefficient for large datasets.

  **Time Complexity**: O(n²)  
  **Space Complexity**: O(1)  

- **`heap_sort.py`**:  
  *Heap Sort* is an efficient, comparison-based sorting algorithm that uses a binary heap data structure. The array is first turned into a max heap and then sorted by repeatedly removing the largest element from the heap.

  **Time Complexity**: O(n log n)  
  **Space Complexity**: O(1)  

- **`insertion_sort.py`**:  
  *Insertion Sort* builds the final sorted array one element at a time. It takes each element from the input and inserts it into the correct position within the already sorted section of the array.

  **Time Complexity**: O(n²)  
  **Space Complexity**: O(1)  

- **`Merge Sort.py`**:  
  *Merge Sort* is a divide-and-conquer algorithm that divides the unsorted list into n sublists, each containing one element, and then merges the sublists to produce the sorted output.

  **Time Complexity**: O(n log n)  
  **Space Complexity**: O(n)  

- **`quick_sort.py`**:  
  *Quick Sort* is an efficient, divide-and-conquer algorithm that picks a pivot element and partitions the other elements into two sub-arrays, according to whether they are smaller or greater than the pivot. It recursively sorts the sub-arrays.

  **Time Complexity**: O(n log n) on average  
  **Space Complexity**: O(log n)  

- **`selection_sort.py`**:  
  *Selection Sort* works by selecting the smallest (or largest) element from the unsorted portion of the list and swapping it with the first unsorted element.

  **Time Complexity**: O(n²)  
  **Space Complexity**: O(1)  

### Graph Algorithms
- **`dijkstra_algo.ipynb`**:  
  *Dijkstra’s Algorithm* is used to find the shortest paths between nodes in a graph. It is widely used in routing and as a subroutine in other graph algorithms.

  **Time Complexity**: O(V²) with basic implementation (can be improved with min-heaps)  
  **Space Complexity**: O(V)  

### Cryptographic Algorithms
- **`RSA_Algorithm.ipynb`**:  
  *RSA Algorithm* is a public-key encryption system that uses two keys: a public key for encryption and a private key for decryption. It relies on the difficulty of factoring large prime numbers.

  **Time Complexity**: O(n²) for key generation  
  **Space Complexity**: O(n)  

- **`SHA_512_Authentication.ipynb`**:  
  *SHA-512* is a cryptographic hash function that produces a 512-bit (64-byte) hash value from the input data. It is commonly used for securing data and generating unique identifiers.

  **Time Complexity**: O(n) for message length  
  **Space Complexity**: O(1)  

### Mathematical Algorithms
- **`Prime_factor.ipynb`**:  
  *Prime Factorization* involves breaking down a number into its prime number factors. It’s used in many areas of mathematics and cryptography.

  **Time Complexity**: O(√n)  
  **Space Complexity**: O(1)  

### Deep Learning & NLP
- **`CNN.ipynb`**:  
  *Convolutional Neural Networks (CNNs)* are deep learning algorithms primarily used for image recognition tasks. CNNs are made up of layers that use convolution and pooling operations to extract features and reduce dimensionality.

  **Time Complexity**: Depends on the architecture (generally O(n²) for image processing tasks)  
  **Space Complexity**: O(n²) for images, depending on the number of layers  

- **`Transformers_in_NLP.ipynb`**:  
  *Transformers* are a deep learning model architecture that has revolutionized Natural Language Processing (NLP). It relies on self-attention mechanisms to process sequences of data in parallel rather than sequentially.

  **Time Complexity**: O(n²) for attention mechanism  
  **Space Complexity**: O(n²) for storing attention matrices

  
## Installation & Usage
1. Clone the repository:
   git clone 

