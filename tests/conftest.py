from pathlib import Path

import pytest
from pydantic_geojson import FeatureCollectionModel


@pytest.fixture()
def data_path():
    return Path(__file__).parent / "data"


@pytest.fixture()
def polygon_json(data_path):
    return open(data_path / "Organisation units.geojson").read()


@pytest.fixture()
def polygons(polygon_json):
    return FeatureCollectionModel.model_validate_json(polygon_json)
