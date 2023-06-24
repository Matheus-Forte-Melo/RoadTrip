from src import util
from time import sleep
from src.car import Car
color = ['\033[32m', '\033[0m']
car = Car(50)


def car_controls():
    util.draw_line(20)
    user_input = int(input('Choose one option: '))

    if user_input == 1:
        percentage = util.input_percentage('Input the acceleration percentage: ')
        car.accelerate(percentage)

        print(color[0])

        if percentage >= 80:
            print("With determination and a forcefull grip on the wheel you firmly press down the cars\n"
                  "accelerator, unleashing all the power you were eager to experience.\nThe engine roared to life,"
                  "its revving sound echoing\nthrough the air, as the tires screeches against the treacherous terrain.")
        elif percentage < 80 and percentage >= 40:
            print("With a steady grip on the steering wheel you gently press the accelerator with a regular force\n"
                  "causing a smooth increase in the car's speed. The engine begins to purr steadily\nemitting a"
                  "confident and consistent sound, providing a sense of calm and confident control.")
        else:
            print("With a gentle grip on the steering wheel, you delicately apply pressure to the accelerator,\n"
                  "initiating a subtle acceleration of the car. The engine hums softly, emitting a subdued and \n"
                  "harmonious tone. As you carefully adjusted the pedal, you move forward with a graceful motion")
        sleep(2)
        print(color[1])
    elif user_input == 2:
        percentage = util.input_percentage('Input the brake percentage: ')
        car.brake(percentage)

        print(color[0])
        if car.get_speed() >= 60 and percentage >= 75:
            print("A surge of urgency fills your senses as you forcefully press your foot down on the brake pedal. \n"
                  "The screech of tires fills the air, echoing through the surroundings. The vehicle begins to\n"
                  "decelerate rapidly, the powerful brakes exerting their force as the speedometer needle rapidly drops")
        elif car.get_speed() < 60 and percentage > 50 and percentage < 75:
            print("You press foot down on the brake pedal, instigating an intense but controlled deceleration of the\n"
                  "car. The speedometer needle descends steadily.")
        else:
            print("With a composed grip on the steering wheel, you gently ease your foot onto the brake pedal\n"
                  "gradually exerting pressure to slow down the car. The vehicle begins to decelerate smoothly\n"
                  "gliding through the air with a controlled grace. The speedometer needle gradually descends")
        sleep(2)
        print(color[1])
    elif user_input == 3:
        print()
    elif user_input == 4:
        print()
    elif user_input == 5:
        print(color[0])
        if car.get_speed() == 200:

            print('You realize you are going too fast. You take a worried look at the speedometer, it points to its\n'
                  f'maximum speed indicator{car.get_speed()}KM/h. You may need to slow down, or something \n'
                  f'is going to happen...')
        elif car.get_speed() == 0:
            print(f"You know the car is stopped, but you glance the speedometer anyways. It marks {car.get_speed()}KM/h")
        else:
            print(f'You take a quick glance at the speedometer, it marks {car.get_speed()}KM/h')

        print(color[1])
        sleep(1.5)
    elif user_input == 6:
        print(f'{color[0]}You quickly open the glove compartment and retrive a small compass that lies inside,'
              f'\nAfter you analize the compass, the pointer indicates {car.get_direction()}. After examining it\n'
              f'briefy, you put it back into its original compartment.{color[1]}.')
        sleep(1.5)
    else:
        print()