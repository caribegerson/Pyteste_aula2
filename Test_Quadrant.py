from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinate_first():
    # Arrange / Setup
    a = 10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "First"

def test_should_get_quadrant_coordinate_second():
    # Arrange / Setup
    a = -10
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"

def test_should_get_quadrant_coordinate_third():
    # Arrange / Setup
    a = -10
    b = -20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"

def test_should_get_quadrant_coordinate_fourth():
    # Arrange / Setup
    a = 10
    b = -20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Fourth"