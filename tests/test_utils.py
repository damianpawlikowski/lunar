from lunar.utils import text_to_sha1


def test_text_to_sha1():
    """Hashing word "secret" should return following SHA1:
    "e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4".
    """
    text = "secret"
    assert text_to_sha1(text) == "e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4"
