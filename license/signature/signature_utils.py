#!/usr/bin/env python
# coding:utf-8
import rsa

PRIVATE_KEY = '''
    -----BEGIN RSA PRIVATE KEY-----
    MIIBPQIBAAJBAJgmeNmPuL8rdakG00PhEQFhZS0qEC2xH1TyUdChB2rRLLlSebGq
    qqhvkjZeH7tc7IOUwdwybBC/uM0c1uEx1tMCAwEAAQJAYAaX6yeMAAtbvQvztjmL
    1AU2J+UOROgu0BwHita2FvIYVedGMMMIrqX3wxunjDliqWM+XdPit0oKju/NU+9y
    IQIjAOiFDSGj16qPEfikzBDlchnVAamV/rnWySSZhkeV/oFbOdsCHwCng8MXubO/
    yq7AsT8KrbJoxfmB3spAjVlbpH9mFGkCIlviSCAlCNKjmuxw4xtCMGa43+FOHsz9
    bZsC+CdNxLcFf8UCHwCIVWqAcrjiTTjwxtDCBh//ubCZjBMbem7RcQ3mrJECIwCj
    YP1gQCOyPp5WoU9rBcs5U1vYeoLX69NuEQHWNY83bEFd
    -----END RSA PRIVATE KEY-----
    '''

PUBKEY = '''
    -----BEGIN RSA PUBLIC KEY-----
    MEgCQQCYJnjZj7i/K3WpBtND4REBYWUtKhAtsR9U8lHQoQdq0Sy5Unmxqqqob5I2
    Xh+7XOyDlMHcMmwQv7jNHNbhMdbTAgMBAAE=
    -----END RSA PUBLIC KEY-----
    '''


class SignatureUtils(object):
    def __init__(self):
        self.private_key = rsa.PrivateKey.load_pkcs1(PRIVATE_KEY)
        self.pubkey = rsa.PublicKey.load_pkcs1(PUBKEY)

    def generate_sign_string(self, message, hash_type):
        signature = rsa.sign(message, self.private_key, hash_type)

    def verify(self, message, signature):
        result = rsa.verify(message, signature, self.pubkey)

    def encrypt(self, message):
        rsa.encrypt(message, self.pubkey)

    def decrypt(self, crypto):
        rsa.decrypt(crypto, self.private_key)
