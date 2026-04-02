# tdkg

**tdkg (Temporal Decaying Knowledge Graph)** is a lightweight Python library for building memory systems that evolve over time.

It is designed for applications where information should not just be stored, but **reinforced through usage and forgotten naturally over time**.

Think of it as a simple cognitive memory layer for AI systems, agents, or personal knowledge graphs.

---

## 🚀 Key Idea

Traditional storage systems treat all data equally.

`tdkg` introduces a different model:

- Frequently accessed information becomes stronger
- Rarely accessed information decays over time
- Memory behaves more like human cognition

---

## 🧠 Core Concept: Node

Each piece of information is stored as a `Node`:

- Has content
- Tracks access frequency
- Tracks last access time
- Has an evolving importance score

---

## 📦 Installation

```bash
pip install tdkg