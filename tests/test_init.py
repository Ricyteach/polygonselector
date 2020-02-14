import pytest
import polygonselector as ps


@pytest.fixture()
def shp_file():
    return r"Africa.shp"


@pytest.fixture()
def open_result(shp_file):
    return ps.open(shp_file)


def test_open_shp(open_result):
    assert open_result


def test_show(open_result):
    open_result.show()
