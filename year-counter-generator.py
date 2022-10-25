import time
from datetime import datetime


def generate_years():
    for ano in range(1, int(datetime.now().year) + 1):
        print(f'Estamos no ano {ano}')
    should_run_again()


def should_run_again():
    answer = input('Executar novamente?(y/n) : ')
    if answer == 'y':
        generate_years()
    if answer == 'n':
        print('Saindo do programa agora... Tchau :)')


if __name__ == '__main__':
    generate_years()