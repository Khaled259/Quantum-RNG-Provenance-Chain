import hashlib
from qiskit import QuantumCircuit, Aer, execute

def generate_random_bits(n_bits):
    simulator = Aer.get_backend('qasm_simulator')
    shots = (n_bits + 2) // 3
    qc = QuantumCircuit(3, 3)
    qc.h([0,1,2])
    qc.measure([0,1,2], [0,1,2])
    result = execute(qc, simulator, shots=shots).result()
    bits = []
    for outcome, count in result.get_counts().items():
        bs = outcome[::-1]
        bits.extend(list(bs) * count)
        if len(bits) >= n_bits: break
    return ''.join(bits[:n_bits])

def hash_batches(bit_string, batch_size=256):
    hashes = []
    for i in range(0, len(bit_string), batch_size):
        batch = bit_string[i:i+batch_size]
        data = int(batch, 2).to_bytes((len(batch)+7)//8, 'big')
        hashes.append(hashlib.sha256(data).hexdigest())
    return hashes

if __name__ == "__main__":
    bits = generate_random_bits(256)
    print(bits)
    print(hash_batches(bits))
