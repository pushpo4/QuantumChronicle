import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Initialize quantum circuit
qc = QuantumCircuit(2, 2)

# Create an entangled state
qc.h(0)
qc.cx(0, 1)

# Measure qubits
qc.measure([0, 1], [0, 1])

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()

# Display measurement results
counts = result.get_counts(qc)
print("Measurement results:", counts)
