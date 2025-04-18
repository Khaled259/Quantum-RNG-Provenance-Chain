from quantum.random_bits import generate_random_bits

def test_length():
    bits = generate_random_bits(300)
    assert len(bits) == 300
