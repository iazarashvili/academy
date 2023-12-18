# tuple

class Human:
    def __init__(self, name, company):
        if not name:
            raise ValueError('Missing name attr')
        self.name = name
        self.company = company


def main():
    human = get_human()
    print(f'{human.name} from {human.company}')


def get_human():
    name = input('Whats your name: ')
    company = input('Where do you work at: ')
    human = Human(name, company)
    return human


if __name__ == "__main__":
    main()
