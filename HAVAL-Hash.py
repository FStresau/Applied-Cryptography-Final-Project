def haval_pad(data):
    # Padding the data to a multiple of 32 bits
    data_len = len(data)
    pad_len = (32 - (data_len % 32)) % 32
    padded_data = data + bytes([0x80]) + bytes(pad_len - 1)
    return padded_data

def haval_compress(block, state):
    # Compression function
    for i in range(3):
        for j in range(32):
            state[j % 8] = state[j % 8] ^ block[j]
        state = haval_transform(state)
    return state


def haval_transform(state):
    # Transformation function
    rol = lambda x, n: ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF
    for i in range(5):
        a, b, c, d, e = state[:5]
        for j in range(5):
            tmp = rol(a, 7) + rol(e & (b ^ c) ^ d & b, 11) + state[j] + 0x00000000
            e, d, c, b, a = d, c, rol(b, 10), a, tmp
        state = [a, b, c, d, e] + state[5:]
    return state

def haval_hash(data, rounds=3):
    # Initialize the state
    state = [0x243F6A88, 0x85A308D3, 0x13198A2E, 0x03707344, 0xA4093822,
             0x299F31D0, 0x082EFA98, 0xEC4E6C89]
    
    # Padding the data
    padded_data = haval_pad(data)
    
    # Process each block
    for i in range(0, len(padded_data), 32):
        block = list(padded_data[i:i+32])
        state = haval_compress(block, state)
    
    # Finalize the hash
    hash_value = sum((state[i] << (32 * i)) for i in range(4))
    return '{:032x}'.format(hash_value)

# Example usage
data = b"Hello, World!"
hash_value = haval_hash(data)
print(hash_value)
