#!/usr/bin/env python
# coding:utf-8
import base64
from license.utils.signature_utils import SignatureUtils
from license.utils import signature_utils
import rsa

signature = SignatureUtils()

sign_string = signature.generate_sign_string(
    message="cpu=20,user_name=LB,used_time=600,expired_date=2018-1-1 00:00:01",
    hash_type="SHA-256")

b64_string = base64.b64encode(sign_string)

print signature.verify(message="cpu=20,user_name=LB,used_time=600,expired_date=2018-1-1 00:00:01",
                       signature=base64.b64decode(b64_string))

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

new_sign_string = rsa.sign(message="cpu=20,user_name=LB,used_time=600,expired_date=2018-1-1 00:00:00",
                           priv_key=rsa.PrivateKey.load_pkcs1(PRIVATE_KEY), hash="SHA-256")
newb64_string = base64.b64encode(new_sign_string)
print signature.verify(message="cpu=20,user_name=LB,used_time=600,expired_date=2018-1-1 00:00:00",
                       signature=base64.b64decode(newb64_string))
