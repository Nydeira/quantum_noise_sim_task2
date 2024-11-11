from qiskit import QuantumCircuit
from qiskit.circuit import Gate

def convert_to_gate_basis(input_circuit, debug=False):
    """
    Converts a quantum circuit to use only the specified gate basis {CX, ID, RZ, SX, X}.
    
    Parameters:
    - input_circuit (QuantumCircuit): The original quantum circuit.
    - debug (bool): If True, prints each gate conversion for better traceability.
    
    Returns:
    - QuantumCircuit: A new quantum circuit using only the specified gate basis.
    """
    
    # Define the specific gate basis set
    allowed_gates = {'cx', 'id', 'rz', 'sx', 'x'}
    
    # Create a new circuit with the same number of qubits
    converted_circuit = QuantumCircuit(input_circuit.num_qubits)
    
    # Iterate over each gate in the input circuit
    for gate, qubits, clbits in input_circuit:
        # Check if the gate is in the allowed gate basis
        if gate.name in allowed_gates:
            converted_circuit.append(gate, qubits, clbits)
            if debug:
                print(f"Appended gate '{gate.name}' directly to converted circuit.")
        else:
            # Conversion logic for unsupported gates, e.g., 'u3'
            if gate.name == 'u3':
                theta, phi, lam = gate.params
                converted_circuit.rz(lam, qubits[0])
                converted_circuit.sx(qubits[0])
                converted_circuit.rz(theta, qubits[0])
                if debug:
                    print(f"Converted 'u3' gate to RZ, SX, and RZ with parameters {theta}, {phi}, {lam}.")
            else:
                if debug:
                    print(f"Gate '{gate.name}' is not supported in this basis and requires additional conversion logic.")
    
    return converted_circuit
