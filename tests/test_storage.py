from src.storage import JsonStorage


def test_load():
    storage = JsonStorage("tests/test_data/data.json")
    vac = storage.load()
    assert len(vac) == 2
    assert vac[0].pk == "123"
    assert vac[1].pk == "321"
