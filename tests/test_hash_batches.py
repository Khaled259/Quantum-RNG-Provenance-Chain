from quantum.random_bits import hash_batches

def test_hash():
    bit_str = '0'*256
    hashes = hash_batches(bit_str)
    assert len(hashes) == 1
    assert len(hashes[0]) == 64
