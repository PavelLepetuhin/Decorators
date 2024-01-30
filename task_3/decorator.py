
import time

def logger(old_function):
    def new_function(*args, **kwargs):
        with open('main.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} {old_function.__name__}(')
            for arg in args:
                log_file.write(f'{arg}, ')
            for key, value in kwargs.items():
                log_file.write(f'{key}={value}, ')
            log_file.write(')\n')
            log_file.write(f'{old_function(*args, **kwargs)}\n')
        return old_function(*args, **kwargs)
    return new_function