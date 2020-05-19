import hashlib
import numpy as np

apparent_str = 'y50024019923677*'
# print(hashlib.algorithms_available) {'md5', 'blake2s', 'sha224', 'mdc2', 'sha3_224', 'ripemd160', 'sha3_512',
# 'md4', 'md5-sha1', 'sha3_384', 'sha3_256', 'shake_256', 'sha1', 'shake_128', 'sha512_256', 'sha256', 'sha512',
# 'sha512_224', 'sm3', 'sha384', 'blake2b', 'whirlpool'}

# encrypted_str = hashlib.md5(apparent_str.encode('utf-8'))
# digest = encrypted_str.hexdigest()
# print(digest)

def md5(str):
    salt = np.random.randint(100)
    print(salt)
    salt = salt.__str__()

    # # solution 1
    # md5 = hashlib.md5()
    # md5.update(str.encode('utf-8'))
    # md5.update(bytes(salt, encoding='utf-8'))
    # print(md5.hexdigest())

    # solution 2
    hash_res = hashlib.md5(str.encode('utf-8')+(f'{salt}'+'1').encode('utf-8'))
    print(hash_res.hexdigest())
    return hash_res


if __name__ == '__main__':
    encrypted_mess = md5(apparent_str)
    print(encrypted_mess)
