# quantum_noise_sim_task2
QOSF Noise Simulator, Task 2

Quantum Addition with Noise Simulation

Overview

This project is a basic exploration of how noise affects quantum addition. I used the Draper adder algorithm to add two numbers on a quantum circuit and then added noise to see what happens. The noise is introduced using Pauli operators (like X, Y, Z gates), which simulate real-world errors that can mess up the calculations.

Details of My Solution

Noise Model:
I added noise based on two probabilities:
alpha: Chance of noise after single-qubit gates.
beta: Chance of noise after two-qubit gates.
This randomness simulates real errors that happen in quantum circuits.
Gate Basis Conversion:
I converted the circuit to use a specific set of gates {CX, ID, RZ, SX, X} because not all quantum hardware can handle every gate.
Some gates (H, CP, swap, etc.) needed extra steps because they aren’t part of this set. Messages in the output show when a gate requires additional conversion.
Draper Adder:
This function is a version of quantum addition that uses a Quantum Fourier Transform (QFT).
The program prints out each step so you can follow the progress of the addition, including noise and transformations.
Results and Observations:
How Noise Affects Results: As alpha and beta get higher, more noise is added, which means there are more random gates disrupting the circuit.
Possible Ways to Reduce Noise: Fewer gates or maybe some form of error correction might help reduce noise effects, though this is more advanced.
Gate Count and Errors: The more gates there are, the more chances for error, so optimizing the circuit could help with accuracy.
How to Run the Program

Make sure you have Qiskit installed.
Run test_noise_simulation.py to see the circuit output with different levels of noise and transformations.
