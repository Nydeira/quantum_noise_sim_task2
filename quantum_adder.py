from qiskit import QuantumCircuit
import numpy as np

def quantum_fourier_transform(circuit, n, debug=False):
    """
    Applies the Quantum Fourier Transform to the first n qubits of the circuit.
    
    Parameters:
    - circuit (QuantumCircuit): The quantum circuit where QFT will be applied.
    - n (int): The number of qubits to apply the QFT on.
    - debug (bool): If True, prints each step for tracking the QFT process.
    """
    
    for i in range(n):
        circuit.h(i)
        if debug:
            print(f"Applied H gate to qubit {i}.")
            
        # Apply controlled phase shifts
        for j in range(i + 1, n):
            angle = np.pi / 2**(j - i)
            circuit.cp(angle, j, i)
            if debug:
                print(f"Applied CP gate with angle {angle} between qubits {j} and {i}.")
    
    # Swap qubits for correct QFT ordering
    for i in range(n // 2):
        circuit.swap(i, n - i - 1)
        if debug:
            print(f"Swapped qubit {i} with qubit {n - i - 1}.")

def draper_adder(circuit, a_qubits, b_qubits, debug=False):
    """
    Performs quantum addition on qubits in registers a and b using the Draper Adder algorithm.
    
    Parameters:
    - circuit (QuantumCircuit): The quantum circuit for the adder.
    - a_qubits (list[int]): List of qubits representing the first number.
    - b_qubits (list[int]): List of qubits representing the second number.
    - debug (bool): If True, prints each addition step for traceability.
    """
    
    n = max(len(a_qubits), len(b_qubits))
    
    # Apply QFT to the 'a' register
    quantum_fourier_transform(circuit, len(a_qubits), debug)
    
    # Apply controlled-phase rotations based on the 'b' qubits
    for i, aq in enumerate(a_qubits):
        for j, bq in enumerate(b_qubits):
            if i + j < len(a_qubits):
                angle = np.pi / 2**(j + 1)
                circuit.cp(angle, bq, aq)
                if debug:
                    print(f"Applied CP rotation with angle {angle} between b[{j}] and a[{i}].")
    
    # Apply inverse QFT to the 'a' register
    circuit.inverse()  # Efficient inverse of QFT
    if debug:
        print("Applied inverse QFT to 'a' register.")
