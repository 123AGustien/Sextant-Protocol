# Sextant Protocol – Cascade Lens V2

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

This project is under active development for sandbox and research evaluation.

It is not a production financial system and does not process real transactions.

## 🚀 POC Execution (Simulation Demo)

This repository contains a deterministic failure propagation simulator.

### Run POC:
```bash
python poc_demo.py
## RP-02: Control Plane Independence Principle

### Classification
Core Resilience Principle

### Statement
System resilience requires separation between control plane functions and data or access layers to prevent systemic compromise during coordinated disruption events.

### Context
In tightly coupled architectures, control logic (routing, authentication, orchestration) can become a single point of systemic failure when shared with operational traffic flows.

### Principle Definition
Control systems must operate independently from access and transport layers to ensure governance and decision-making remain functional under partial infrastructure failure.

### Application in Cascade Lens V2
- Control plane functions are decoupled from user traffic paths  
- Authentication and routing logic operate on isolated infrastructure layers  
- Access layer failure does not automatically compromise system governance  

### Failure Containment Logic
| Layer         | Risk Exposure       | Independence Strategy        |
|---------------|--------------------|-----------------------------|
| Access Layer  | Network disruption  | Alternate transport channels |
| Data Layer    | Traffic loss        | Multi-path routing           |
| Control Plane | System compromise   | Isolated governance layer    |

### Dependency
References RP-01 as a foundational principle (non-binding dependency)

### Status
Active – Extends resilience architecture model
