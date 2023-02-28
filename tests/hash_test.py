import unittest

from libwat import hash


class TestHashMatching(unittest.TestCase):
    """
    Test hash matching.

    Test hashes and naming from: https://hashcat.net/wiki/doku.php?id=example_hashes
    """

    def setUp(self):
        self.hashes = hash.load_data()

    def test_md4(self):
        result = hash.check_hash(self.hashes, 'afe04867ec7a3845145579a95f72eca7')
        self.assertEqual('MD4' in result, True)

    def test_md5(self):
        result = hash.check_hash(self.hashes, '8743b52063cd84097a65d1633f5c74f5')
        self.assertEqual('MD5' in result, True)

    def test_sha1(self):
        result = hash.check_hash(self.hashes, 'b89eaac7e61417341b710b727768294d0e6a277b')
        self.assertEqual('SHA1' in result, True)

    def test_sha2_224(self):
        result = hash.check_hash(self.hashes, 'e4fa1555ad877bf0ec455483371867200eee89550a93eff2f95a6198')
        self.assertEqual('SHA2-224' in result, True)

    def test_sha2_256(self):
        result = hash.check_hash(self.hashes, '127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935')
        self.assertEqual('SHA2-256' in result, True)

    def test_sha2_512(self):
        result = hash.check_hash(self.hashes,
                                 '82a9dda829eb7f8ffe9fbe49e45d47d2dad9664fbb7adf72492e3c81ebd3e29134d9bc12212bf83c6840f10e8246b9db54a4859b7ccd0123d86e5872c1e5082f')
        self.assertEqual('SHA2-512' in result, True)

    def test_ntlm(self):
        result = hash.check_hash(self.hashes, 'b4b9b02e6f09a9bd760f388b67351e2b')
        self.assertEqual('NTLM' in result, True)

    def test_md5crypt(self):
        result = hash.check_hash(self.hashes, '$1$28772684$iEwNOgGugqO9.bIz5sk8k/')
        self.assertEqual('md5crypt' in result, True)

    def test_mysql323(self):
        result = hash.check_hash(self.hashes, '7196759210defdc0')
        self.assertEqual('MySQL323' in result, True)

    def test_mysql41_mysql5(self):
        result = hash.check_hash(self.hashes, 'fcf7c1b8749cf99d88e5f34271d636178fb5d130')
        self.assertEqual('MySQL4.1/MySQL5' in result, True)

    def test_sha256crypt(self):
        result = hash.check_hash(self.hashes, '$5$28772684$YhYkY7q3d4Q1Q2X9Z6U1Q6U5Z6U1Q6U5')
        self.assertEqual('sha256crypt' in result, True)

    def test_sha512crypt(self):
        result = hash.check_hash(self.hashes, '$6$28772684$YhYkY7q3d4Q1Q2X9Z6U1Q6U5Z6U1Q6U5')
        self.assertEqual('sha512crypt' in result, True)

    def test_sha1crypt(self):
        result = hash.check_hash(self.hashes, '$sha1$15100$jiJDkz0E$E8C7RQAD3NetbSDz7puNAY.5Y2jr')
        self.assertEqual('Juniper/NetBSD sha1crypt' in result, True)

    def test_md5crypt_apr1(self):
        result = hash.check_hash(self.hashes, '$apr1$71850310$gh9m4xcAn3MGxogwX/ztb.')
        self.assertEqual('Apache $apr1$ MD5' in result, True)

    def test_phpass(self):
        result = hash.check_hash(self.hashes, '$P$B4b9b02e6f09a9bd760f388b67351e2b')
        self.assertEqual('phpass' in result, True)

    def test_phpass_md5(self):
        result = hash.check_hash(self.hashes, '$H$B4b9b02e6f09a9bd760f388b67351e2b')
        self.assertEqual('phpass-md5' in result, True)

    def test_bcrypt(self):
        result = hash.check_hash(self.hashes, '$2a$12$KhivLhCuLhSyMBOxLxCyLu78x4z2X/EJdZNfS3Gy36fvRt56P2jbS')
        self.assertEqual('bcrypt' in result, True)

    def test_hmac_sha1(self):
        result = hash.check_hash(self.hashes, 'c898896f3f70f61bc3fb19bef222aa860e5ea717:1234')
        self.assertEqual('HMAC-SHA1' in result, True)

    def test_hmac_sha256(self):
        result = hash.check_hash(self.hashes, 'abaf88d66bf2334a4a8b207cc61a96fb46c3e38e882e6f6f886742f688b8588c:1234')
        self.assertEqual('HMAC-SHA256' in result, True)

    def test_hmac_sha512(self):
        result = hash.check_hash(self.hashes,
                                 '94cb9e31137913665dbea7b058e10be5f050cc356062a2c9679ed0ad6119648e7be620e9d4e1199220cd02b9efb2b1c78234fa1000c728f82bf9f14ed82c1976:1234')
        self.assertEqual('HMAC-SHA512' in result, True)

    def test_hmac_md5(self):
        result = hash.check_hash(self.hashes, 'b4b9b02e6f09a9bd760f388b67351e2b:1234')
        self.assertEqual('HMAC-MD5' in result, True)

    def test_descrypt(self):
        result = hash.check_hash(self.hashes, '48c/R8JAv757A')
        self.assertEqual('descrypt' in result, True)

    def test_lm(self):
        result = hash.check_hash(self.hashes, '299bd128c1101fd6')
        self.assertEqual('LM' in result, True)

    def test_half_md5(self):
        result = hash.check_hash(self.hashes, '8743b52063cd8409')
        self.assertEqual('Half MD5' in result, True)

    def test_ripemd160(self):
        result = hash.check_hash(self.hashes, '012cb9b334ec1aeb71a9c8ce85586082467f7eb6')
        self.assertEqual('RIPEMD-160' in result, True)

    def test_whirlpool(self):
        result = hash.check_hash(self.hashes,
                                 '7ca8eaaaa15eaa4c038b4c47b9313e92da827c06940e69947f85bc0fbef3eb8fd254da220ad9e208b6b28f6bb9be31dd760f1fdb26112d83f87d96b416a4d258')
        self.assertEqual('Whirlpool' in result, True)


if __name__ == '__main__':
    unittest.main()
