from rsa import RSA
from random import randbytes

rsa = RSA(key_length = 44)

#rsa.generate()

rsa.import_keys_from_file('keys.data')

def encode_file(path: str) -> None:
    with open(path, "rb") as file:
        bytes = file.read()
        payload = rsa.encode(bytes)
        zeros = randbytes(1024 * (len(payload) % 1024) - len(payload))
        encoded = len(zeros).to_bytes(4, "big") + payload + zeros
        with open(f'{path.split(".")[0]}.enc', "wb") as _file:
            _file.write(encoded)


def decoded_file(path: str) -> None:
    with open(path, "rb") as file:
        bytes = file.read()
        sizeof = int.from_bytes(bytes[:4], "big")
        payload =  bytes[4:len(bytes) - sizeof]
        decoded = rsa.decode(payload)
        with open(f'{path.split(".")[0]}.dec', "wb") as _file:
            _file.write(decoded)


encode_file("test.txt")

decoded_file("test.enc")

#rsa.save_keys("keys.data")