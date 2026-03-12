<div align="center">

# 🌐 Network Simulation System

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, purely Python-based simulation environment for modeling network topologies, dynamic routing algorithms, and application-layer protocols.

</div>

---

## 📖 Overview

The **Network Simulation System** is a foundational framework designed to simulate the behavior of computer networks. It provides a modular approach to defining network architectures, allowing for the simulation of individual routers, connecting links with customizable delays, packet-level data transmission, and dynamic routing using a Distance Vector algorithm. 

This project also demonstrates the extensibility of the network by building application-layer protocols, such as a simulated SMTP, directly on top of the custom network stack.

---

## ✨ Features

- **🧱 Custom Topologies**: Build complex network topologies by creating Router nodes and defining connections with custom bandwidth and artificial latency.
- **🛣️ Dynamic Routing**: Implements **Distance Vector Routing** to automatically generate and maintain optimal routing tables for all nodes in the network, allowing for adaptive pathfinding.
- **📦 Packet Forwarding**: Granular, hop-by-hop packet forwarding mechanics mimicking real-world IP packet traversal.
- **✉️ Application-Layer Protocols**: Extensible `ProtocolBase` class that allows developers to write custom protocols. Currently includes a working **SMTP Simulation** demonstrating sending and receiving payloads across multiple hops.
- **⏱️ Latency Simulation**: Built-in time delay mechanisms to emulate real-world network propagation delays.

---

## 🏗️ Architecture

The project is structured entirely in Python without external dependencies, focusing on clean, object-oriented design:

```text
.
├── src/
│   ├── core/
│   │   ├── router.py       # Core Router logic and routing table management
│   │   ├── connection.py   # Bidirectional link simulation with latency
│   │   └── packet.py       # Datagram representation with source, dest, and payload
│   ├── routing/
│   │   └── vector_routing.py # Distance Vector Routing algorithm implementation
│   ├── protocols/
│   │   ├── protocol_base.py  # Abstract base class for custom protocols
│   │   └── smtp.py           # Simulated SMTP-like message delivery
│   └── main.py               # Main entry point and topology demonstration
└── tests/                    # Unit testing suite (Work in Progress)
```

---

## 🚀 Getting Started

### Prerequisites

All you need is a standard Python 3.x installation. The project is dependency-free out of the box.

```bash
python --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Network-Simulation-System.git
   cd Network-Simulation-System
   ```

2. **Run the simulation:**
   ```bash
   python src/main.py
   ```

### 🖥️ Expected Output

When running `main.py`, you will see a demonstration of a simple A -> B -> C topology dynamically calculating its routes, followed by a simulated SMTP packet being reliably forwarded from Router A to Router C.

```text
[SMTP] A sending message -> C
[SMTP] at router A
[SMTP] at router B
[SMTP] at router C
[SMTP] C received message: 'Hello C, this is A via SMTP' from A
[SMTP] message delivered. Path: A -> B -> C
```

### 🧑‍💻 Development Setup

If you plan to contribute, write tests, or modify the core routing protocols, you can optionally install the development dependencies:

1. **Install development requirements:**
   ```bash
   pip install -r requirements-dev.txt
   ```
2. **Run the testing suite:**
   ```bash
   pytest tests/
   ```
3. **Format your code before submitting:**
   ```bash
   black src/ tests/
   ```

---

## 🛠️ Built With

* **Python** - Core language

---

## 🔮 Future Improvements

- [ ] **Link State Routing**: Implement OSPF/Dijkstra's algorithm as an alternative to Distance Vector.
- [ ] **Packet Loss & Jitter**: Simulate unreliable network conditions (dropped packets, varying latency).
- [ ] **More Protocols**: Add HTTP, DNS, or FTP simulations on top of the platform.
- [ ] **Expanded Test Suite**: Comprehensive unit testing using `pytest`.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
