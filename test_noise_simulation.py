from qiskit import QuantumCircuit, transpile
from noise_model import apply_pauli_noise
from gate_basis_conv import convert_to_gate_basis
from quantum_adder import draper_adder

def test_quantum_addition_with_noise(a_val, b_val, alpha, beta, debug=False):
    """
    Test the Draper adder with added noise and analyze results.

    Parameters:
    - a_val (int): First number to add.
    - b_val (int): Second number to add.
    - alpha (float): Noise probability after single-qubit gates.
    - beta (float): Noise probability after two-qubit gates.
    - debug (bool): If True, prints debug information for each step.
    """
    
    # Create registers and a quantum circuit
    num_qubits = max(a_val.bit_length(), b_val.bit_length()) + 1
    a_qubits = list(range(num_qubits))
    b_qubits = list(range(num_qubits, 2 * num_qubits))
    qc = QuantumCircuit(2 * num_qubits)

    # Initialize a and b in the circuit
    for i in range(a_val.bit_length()):
        if (a_val >> i) & 1:
            qc.x(a_qubits[i])
    for i in range(b_val.bit_length()):
        if (b_val >> i) & 1:
            qc.x(b_qubits[i])

    # Apply Draper Adder
    draper_adder(qc, a_qubits, b_qubits, debug=debug)

    # Apply noise and convert to gate basis
    noisy_qc = apply_pauli_noise(qc, alpha, beta, debug=debug)
    converted_qc = convert_to_gate_basis(noisy_qc, debug=debug)

    # Print out the circuit instead of running on simulator
    print(f"\nCircuit with noise and gate basis for α={alpha}, β={beta}:")
    print(converted_qc)

# Run tests with different noise levels
test_quantum_addition_with_noise(3, 5, alpha=0.1, beta=0.2, debug=True)
test_quantum_addition_with_noise(3, 5, alpha=0.3, beta=0.5, debug=True)
test_quantum_addition_with_noise(3, 5, alpha=0.5, beta=0.8, debug=True)
