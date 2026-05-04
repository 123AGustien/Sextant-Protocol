# Sextant Protocol – Cascade Lens V2 (v1.0)

## Deterministic Sandbox Simulation Engine for Dependency Graph Modeling & Failure Propagation Analysis

Cascade Lens V2 is a non-custodial, deterministic simulation framework designed to model cross-border settlement behaviour in multi-currency environments under controlled sandbox conditions.

---

## Core Capabilities
- Dependency graph modelling
- Liquidity flow simulation
- Failure propagation analysis
- Deterministic event execution
- Replayable simulation outputs

---

## System Constraints
- No execution of real financial transactions
- No connection to banking or payment systems
- No custody or handling of funds
- Sandbox-only execution environment
- Synthetic or anonymised data only

---

## Architecture
API → Event Processing → Cascade Engine → Graph Model → Output Layer

---

## System Characteristics
- Deterministic: identical input produces identical output  
- Non-custodial: no interaction with real assets or funds  
- Isolated: operates independently from financial infrastructure  

---

## Status
v1.0 – Stable foundational release (Cascade Lens Core Doctrine complete)

This project is designed for sandbox and research evaluation purposes only.  
It is not a production financial system and does not process real transactions.

---

## 🚀 POC Execution (Simulation Demo)

This repository contains a deterministic failure propagation simulator.

### Run POC:
```bash
python poc_demo.py
