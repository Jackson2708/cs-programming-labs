def is_valid_command(command):
    return command == '0' or command == '1' or command == '2' or command == 'exit'


def can_burn(power, fuel):
    return fuel >= power


def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    fuel = fuel - power
    speed = speed + gravity - thrust_step * power
    if speed < 0:
        speed = 0
    height = height - speed
    if height < 0:
        height = 0
    return (height, speed, fuel)


def get_status(height, speed, safe_speed=2):
    if height > 0:
        return 'В полете'
    if speed <= safe_speed:
        return 'Посадка успешна'
    return 'Авария'


def format_state(height, speed, fuel):
    return f'Высота: {height} | Скорость: {speed} | Топливо: {fuel}'


def main():
    height = 36
    speed = 3
    fuel = 10
    gravity = 3
    thrust_step = 4
    print(format_state(height, speed, fuel))
    while True:
        command = input()
        if not is_valid_command(command):
            print('Ошибка команды')
            continue
        if command == 'exit':
            print('Полет прерван')
            return
        power = int(command)
        if not can_burn(power, fuel):
            print('Недостаточно топлива')
            continue
        height, speed, fuel = simulate_step(
            height, speed, fuel, power, gravity, thrust_step)
        print(format_state(height, speed, fuel))
        status = get_status(height, speed)
        if status != 'В полете':
            print(status)
            return


main()
