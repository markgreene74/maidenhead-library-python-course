import pytest

import helpers
import main


def test_missing_config_file(monkeypatch) -> None:
    mockvalue = "this-is-not-a-real-file"
    monkeypatch.setattr(main, "FILENAME", mockvalue)
    with pytest.raises(SystemExit) as excinfo:
        helpers.read_config_file(main.FILENAME)

    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Config file this-is-not-a-real-file does not exist"


def test_good_config(monkeypatch, capsys) -> None:
    mockvalue = "data/test-config-01"
    monkeypatch.setattr(main, "FILENAME", mockvalue)
    main.main()
    out, _ = capsys.readouterr()

    assert "'colour': <Colour.WHITE: 'white'>" in out
    assert "'class': <CharacterClass.WIZARD: 'wizard'>" in out
    assert "'name': 'test character 01'" in out
    assert "'weapon': <Weapon.STAFF: 'staff'>" in out
    assert "'defence': <Defence.SHIELD_SPELL: 'shield spell'>" in out
    assert "'armour': <Armour.NO_ARMOUR: 'no armour'>" in out
    assert "'notes': 'this is a test note for character 01.'" in out


def test_partially_good_config(monkeypatch, capsys) -> None:
    mockvalue = "data/test-config-02"
    monkeypatch.setattr(main, "FILENAME", mockvalue)
    main.main()
    out, _ = capsys.readouterr()

    assert "Invalid colour value: not a real colour" in out
    assert "Invalid weapon value: not a real weapon" in out
    assert "'colour': None" in out
    assert "'class': <CharacterClass.ARCHER: 'archer'>" in out
    assert "'name': 'test character 02'" in out
    assert "'weapon': None" in out
    assert "'defence': <Defence.NO_DEFENCE: 'no defence'>" in out
    assert "'armour': <Armour.NO_ARMOUR: 'no armour'>" in out
    assert "'notes': 'this is a test note for character 02.'" in out


def test_bad_config(monkeypatch, capsys) -> None:
    mockvalue = "data/test-config-03"
    monkeypatch.setattr(main, "FILENAME", mockvalue)
    main.main()
    out, _ = capsys.readouterr()

    assert "Invalid class value: not a valid class" in out
    assert "Invalid defence value: not a valid defence" in out
    assert "Invalid armour value: not a valid armour" in out
    assert "There was a problem extracting the label" in out
    assert "line='not a valid label: not a valid value" in out
    assert "label='not a valid label'" in out
    assert "value='not a valid value'" in out
    assert "Invalid line format: also:not:a:valid:line" in out
