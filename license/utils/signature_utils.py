#!/usr/bin/env python
# coding:utf-8
import rsa
import base64

PRIVATE_KEY = '''
    -----BEGIN RSA PRIVATE KEY-----
    MIIBPAIBAAJBALZbR0yn8pJLBo58cWnVtviYkFQ2KRZ7WG17Mdc4ABl1tKRMJtR4
    6o8TdVxjFFfhwpBFQSPMtoCmmaIsZiWEKBUCAwEAAQJAembuht+8jMHbVszk+5s+
    Q8N0LXJlRffpNSOaItIteIe4nu+kEd5FyK1/IwnciyPBXjFrtT/SEXRVkqJhHuTN
    yQIjAOAJoXcgL5uJluV0aAf9ySdsaiy8IYGnUANaeXaHLHcWnQsCHwDQX1wGRPIC
    K8M3bUMyCK9n3xpSVLWR02HfMGLSQ18CIwCyD/V9MN+lx11fUX29nD/cTZa1p3Ea
    E1jM0YPoaNc2b4qxAh4BJDSV2DTXLDQyjoeqs396ey9iuhIQjW7g0RwJeNMCIgJV
    ILVzYIWdl1cD/Dpi4Qm+oLKiALlKhycbrFAc3iPFp6Y=
    -----END RSA PRIVATE KEY-----
    '''

PUBKEY = '''
    -----BEGIN RSA PUBLIC KEY-----
    MEgCQQC2W0dMp/KSSwaOfHFp1bb4mJBUNikWe1htezHXOAAZdbSkTCbUeOqPE3Vc
    YxRX4cKQRUEjzLaAppmiLGYlhCgVAgMBAAE=
    -----END RSA PUBLIC KEY-----
    '''
TOKEN = 'fsabe3minbkpxjiu'


class SignatureUtils(object):
    def __init__(self):
        # TODO design readonly
        self.private_key = rsa.PrivateKey.load_pkcs1(PRIVATE_KEY)
        self.pubkey = rsa.PublicKey.load_pkcs1(PUBKEY)
        self.token = TOKEN

    def generate_sign_string(self, message, hash_type):
        signature = rsa.sign(self.token + message, self.private_key, hash_type)
        return base64.b64encode(signature)

    def verify(self, message, signature):
        try:
            signature = base64.b64decode(signature)
            result = rsa.verify(self.token + message, signature, self.pubkey)
        except Exception as e:
            return False
        return result

    def encrypt(self, message):
        rsa.encrypt(message, self.pubkey)

    def decrypt(self, crypto):
        rsa.decrypt(crypto, self.private_key)


signature_instance = SignatureUtils()
