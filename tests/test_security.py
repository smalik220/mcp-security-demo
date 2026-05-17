from mcp_insecure import read_file as insecure_read_file
from mcp_secure import read_file as secure_read_file


# --- Insecure server tests ---

def test_insecure_leest_toegestaan_bestand():
    result = insecure_read_file("bestanden/leesbaar-bestand.md")
    assert result is not None


def test_insecure_lekt_secret():
    result = insecure_read_file("bestanden/secret.env")
    assert "Access denied" not in result


# --- Secure server tests ---

def test_secure_leest_toegestaan_bestand():
    result = secure_read_file("bestanden/leesbaar-bestand.md")
    assert "Access denied" not in result


def test_secure_blokkeert_secret():
    result = secure_read_file("bestanden/secret.env")
    assert "Access denied" in result


def test_secure_blokkeert_path_traversal():
    result = secure_read_file("../../etc/passwd")
    assert "Access denied" in result
