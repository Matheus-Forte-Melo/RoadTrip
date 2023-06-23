from src.auto.direction import Compass


def test_current_direc():
    d1 = Compass()
    print(f'The current direction is {d1.current_direction}')


def test_steer():
    d1 = Compass()
    print(d1.current_direction)
    d1.turn_right()
    print(d1.current_direction)

test_steer()