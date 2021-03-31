class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'


def warning(message):
    print(bcolors.ITALIC + bcolors.WARNING + message + bcolors.ENDC)


def log(message):
    print(bcolors.OKBLUE + message + bcolors.ENDC)


def success(message):
    print(bcolors.BOLD + bcolors.OKGREEN + message + bcolors.ENDC)


def error(message):
    print(bcolors.FAIL + message + bcolors.ENDC)


def prompt_yn(prompt, default='Y'):
    options = '[y/n]'
    if default == 'Y':
        options = '[Y/n]'
    elif default == 'N':
        options = '[y/N]'

    choice = input(bcolors.BOLD + str(prompt) + ' ' + options + bcolors.ENDC)

    if choice == 'y' or choice == 'Y':
        return True
    elif choice == 'n' or choice == 'N':
        return False
    else:
        if len(choice) == 0:
            if default == 'Y':
                return True
            elif default == 'N':
                return False
            else:
                raise Exception('Invalid choice')
        else:
            raise Exception('Invalid choice')
