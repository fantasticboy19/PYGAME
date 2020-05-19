from Crypto.PublicKey import RSA
import Crypto.Signature.PKCS1_v1_5 as sign_PKCS1_v1_5  # 用于签名/验签
from Crypto.Cipher import PKCS1_v1_5  # 用于加密
from Crypto import Random
from Crypto.Hash import SHA256
import base64
# x = rsa.generate(2048)
# pri_key = x.export_key()
# pub_key = x.publickey().export_key()
# print(x.export_key(), pub_key.export_key)
# print(pri_key,pub_key,x.export_key('DER'))
# with open('private_key.pem','wb') as f:
#     f.write(pri_key)
#
# with open('public_key.pem','wb') as f:
#     f.write(pub_key)

with open('private_key.pem','rb')as f:
    # data = f.read()
    pri_key = RSA.import_key(f.read())

my_private_key = pri_key.export_key()
my_public_key = pri_key.publickey().export_key()


def encrypt_with_rsa(plain_text):
    # 先公钥加密
    cipher_pub_obj = PKCS1_v1_5.new(RSA.importKey(my_public_key))
    _secret_byte_obj = cipher_pub_obj.encrypt(plain_text.encode())

    return _secret_byte_obj


def decrypt_with_rsa(_secret_byte_obj):
    # 后私钥解密
    cipher_pri_obj = PKCS1_v1_5.new(RSA.importKey(my_private_key))
    # decrypt(self, ciphertext, sentinel)
    # the sentinel is the object to return whenever the error happened
    # type sentinel: any type
    _byte_obj = cipher_pri_obj.decrypt(_secret_byte_obj, Random.new().read)
    plain_text = _byte_obj.decode()

    return plain_text


def executer_without_signature():
    # 加解密验证
    # print(Random.new().read)
    secret_text = encrypt_with_rsa('i love you!')
    secret_text_base64_en = base64.b64encode(secret_text)
    print('我收到以后使用私钥解密：')

    secret_text_base64_de = base64.b64decode(secret_text_base64_en)
    print(decrypt_with_rsa(secret_text_base64_de))


def to_sign_with_private_key(plain_text):
    # 私钥签名
    signer_pri_obj = sign_PKCS1_v1_5.new(RSA.importKey(my_private_key))
    rand_hash = SHA256.new()
    rand_hash.update(plain_text.encode())
    # 使用hash函数必须传入bytes类型的数据
    signature = signer_pri_obj.sign(rand_hash)

    return signature


def to_verify_with_public_key(signature, plain_text):
    # 公钥验签
    verifier = sign_PKCS1_v1_5.new(RSA.importKey(my_public_key))
    _rand_hash = SHA256.new()
    _rand_hash.update(plain_text.encode())
    verify = verifier.verify(_rand_hash, signature)

    return verify  # true / false


def executer_with_signature():
    # 签名/验签
    text = "I love CA!"
    assert to_verify_with_public_key(to_sign_with_private_key(text), text)
    print("rsa Signature verified!")


if __name__ == '__main__':
    # executer_with_signature()
    print(Random.new())