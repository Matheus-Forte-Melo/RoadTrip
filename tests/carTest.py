from src.car import Car


def test_brake_acelleration(brake, accel):
        c1 = Car(250)
        print(f'Car is running at {c1.get_speed()} speed unit!')
        print(f"If the car brakes {brake}%, it will be at {c1.brake(brake)} speed unit!")
        print(f'If the car accelerates {accel}%, it will be at {c1.accelerate(accel)}')


test_brake_acelleration(50, 75)