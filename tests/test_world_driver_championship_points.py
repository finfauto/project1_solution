import pytest

from populate_data import load_data
from world_driver_championship_points import get_race_points_from_position, get_race_points_from_position_and_fastest_lap, get_driver_season_points

testdata_race_points = [
    ("1", 25),
    ("2", 18),
    ("3", 15),
    ("4", 12),
    ("5", 10),
    ("6", 8),
    ("7", 6),
    ("8", 4),
    ("9", 2),
    ("10", 1),
    ("11", 0),
    ("12", 0),
    ("13", 0),
    ("14", 0),
    ("15", 0),
    ("16", 0),
    ("17", 0),
    ("18", 0),
    ("19", 0),
    ("20", 0),
    ("R", 0),
]


@pytest.mark.parametrize("position, expected_points", testdata_race_points)
def test_get_race_points(position: str, expected_points: int):
    assert get_race_points_from_position(position) == expected_points


testdata_race_points_with_fastest_lap = [
    ("1", True, 26),
    ("1", False, 25),
    ("2", True, 19),
    ("2", False, 18),
    ("3", True, 16),
    ("3", False, 15),
    ("4", True, 13),
    ("4", False, 12),
    ("5", True, 11),
    ("5", False, 10),
    ("6", True, 9),
    ("6", False, 8),
    ("7", True, 7),
    ("7", False, 6),
    ("8", True, 5),
    ("8", False, 4),
    ("9", True, 3),
    ("9", False, 2),
    ("10", True, 2),
    ("10", False, 1),
    ("11", True, 0),
    ("11", False, 0),
    ("12", True, 0),
    ("12", False, 0),
    ("13", True, 0),
    ("13", False, 0),
    ("14", True, 0),
    ("14", False, 0),
    ("15", True, 0),
    ("15", False, 0),
    ("16", True, 0),
    ("16", False, 0),
    ("17", True, 0),
    ("17", False, 0),
    ("18", True, 0),
    ("18", False, 0),
    ("19", True, 0),
    ("19", False, 0),
    ("20", True, 0),
    ("20", False, 0),
    ("R", True, 0),
    ("R", False, 0),
]


@pytest.mark.parametrize("position, is_fastest_lap, expected_points", testdata_race_points_with_fastest_lap)
def test_get_race_points(position: str, is_fastest_lap: bool, expected_points: int):
    assert get_race_points_from_position_and_fastest_lap(position, is_fastest_lap) == expected_points


testdata_get_world_driver_championship_table = [
    ("hamilton", 393),
    ("leclerc", 161),
    ("latifi", 8),
    ("kubica", 0),
    ("nobody", 0)
]


@pytest.mark.parametrize("driver, expected_points", testdata_get_world_driver_championship_table)
def test_get_driver_season_points(driver, expected_points):
    try:
        data = load_data(2021)[driver]
    except KeyError:
        data = {}
    points = get_driver_season_points(data)
    assert points == expected_points
