from qiskit import QuantumCircuit
import numpy as np

def apply_pauli_noise(input_circuit, alpha, beta, debug=False):
    """
    Adds simulated Pauli noise to a quantum circuit based on specified probabilities.
    
    Parameters:
    - input_circuit (QuantumCircuit): The quantum circuit to which noise will be added.
    - alpha (float): Probability of adding a random Pauli error after single-qubit gates.
    - beta (float): Probability of adding random Pauli errors after two-qubit gates.
    - debug (bool): If True, prints debug information showing each noise addition step-by-step.
    
    Returns:
    - QuantumCircuit: The new quantum circuit with noise applied.
    """
    
    # Helper function to randomly select a Pauli operator (X, Y, Z)
    def get_random_pauli():
        return np.random.choice(['x', 'y', 'z'])
    
    # Create a copy of the input circuit to apply noise
    noisy_circuit = QuantumCircuit(input_circuit.num_qubits)
    
    # Iterate through each instruction in the circuit
    for gate, qubits, clbits in input_circuit:
        noisy_circuit.append(gate, qubits, clbits)
        
        # Determine if noise should be applied based on gate type (1-qubit or 2-qubit)
        if gate.num_qubits == 1 and np.random.rand() < alpha:
            pauli_type = get_random_pauli()
            getattr(noisy_circuit, pauli_type)(qubits[0])
            if debug:
                print(f"Applied {pauli_type.upper()} noise to qubit {qubits[0]} after a 1-qubit gate.")
                
        elif gate.num_qubits == 2 and np.random.rand() < beta:
            pauli_type = get_random_pauli()
            getattr(noisy_circuit, pauli_type)(qubits[0])
            getattr(noisy_circuit, pauli_type)(qubits[1])
            if debug:
                print(f"Applied {pauli_type.upper()} noise to qubits {qubits[0]} and {qubits[1]} after a 2-qubit gate.")
    
    return noisy_circuit
