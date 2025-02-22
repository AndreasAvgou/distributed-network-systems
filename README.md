# Distributed Network Systems

## Overview

This repository contains implementations of various **distributed network algorithms**, including **flooding**, **echo**, and **real-time flooding**. These algorithms demonstrate fundamental concepts in distributed computing, such as message passing, network communication, and fault tolerance.

## Algorithms Implemented

### 1. Flooding Algorithm

- Implements a simple flooding mechanism where a message is broadcast to all neighbors.
- Ensures that each node forwards the message exactly once.
- Useful for network discovery and message propagation.

📂 **Location**: `flooding-algorithm/`

### 2. Echo Algorithm

- A wave algorithm where a root node initiates a message, which propagates and returns through a spanning tree.
- Used for leader election and distributed synchronization.

📂 **Location**: `echo-algorithm/`

### 3. Real-Time Flooding Algorithm

- Enhances the flooding algorithm with real-time message input.
- Avoids message loops using unique message IDs.
- Can be used for real-time network-wide notifications.

📂 **Location**: `real-time-flooding/`

## Installation & Setup

### Requirements

- Python 3.7+
- `socket` (built-in module)
- `threading` (built-in module)

### Running an Algorithm

Each algorithm has its own directory with a corresponding `README.md` for detailed instructions.

Example (Running Flooding Algorithm):

```bash
cd flooding-algorithm
python flooding.py
```

## Repository Structure

```
📂 distributed-network-systems
│── 📂 flooding-algorithm
│   ├── flooding.py
│   ├── README.md
│── 📂 echo-algorithm
│   ├── echo.py
│   ├── README.md
│── 📂 real-time-flooding
│   ├── real_time_flooding.py
│   ├── README.md
│── LICENSE
│── CONTRIBUTING.md
│── README.md
```

## Contribution

We welcome contributions! If you'd like to add an improvement, follow these steps:

1. **Fork** this repository.
2. **Clone** your fork: `git clone https://github.com/your-username/distributed-network-systems.git`
3. **Create a new branch**: `git checkout -b feature-new-algorithm`
4. **Commit your changes** and push.
5. **Open a Pull Request (PR)**.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
