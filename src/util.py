def draw_line(length):
    print('=' * length)


def input_percentage(txt):
    while True:
        try:
            percentage = int(input(txt))
            if percentage < 0:
                percentage = percentage * 1
            return percentage
        except (TypeError, ValueError):
            print('\033[32mPlease, input a interger value!\033[0m')

