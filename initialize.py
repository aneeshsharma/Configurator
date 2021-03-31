import os
from subprocess import Popen, PIPE
import yaml

from util import prompt_yn, log, error, warning, success


# Name of the dotfiles directory
DOTFILES = 'dotfiles'

# The initial configuration
default_config = {
    'name': 'Config'
}


def initialize_new_config():
    CURRENT_DIR = os.getcwd()
    USER_HOME = os.environ.get('HOME', None)

    CONFIG_DIR = None

    if not USER_HOME:
        error('ERROR: User home directory not found')
    elif CURRENT_DIR != USER_HOME:
        # If current directory is not home ask where to initialize
        log('The current directory is not the user\'s home directory')
        log('It is recommended to store the dotfiles directory in the home directory')
        try:
            if prompt_yn('Would you like to choose switch to the home directory?'):
                CONFIG_DIR = f'{USER_HOME}/{DOTFILES}'
            else:
                CONFIG_DIR = f'{CURRENT_DIR}/{DOTFILES}'
        except Exception:
            error('Invalid choice! exiting...')
            exit(-1)

    print(f'Creating dotfiles repository at {CONFIG_DIR}')
    try:
        os.mkdir(CONFIG_DIR)
    except FileExistsError:
        warning('Given location already exists!')
        try:
            if not prompt_yn('Initialize at the location anyways? (WARNING: This might cause LOSS OF DATA)', default='N'):
                exit(-1)
        except Exception:
            error('Invalid choice exiting...')
            exit(-1)

    os.chdir(CONFIG_DIR)

    # Initialize a git repository in the configuration directory
    git_process = Popen(['git',  'init'], stdout=PIPE, stderr=PIPE)

    if git_process.wait() != 0:
        error('Error initializing git repository')
        exit(-1)

    # Create an initial configuration file
    config_file = open('configuration.yaml', 'w')

    config_file.write(yaml.dump(default_config))

    config_file.close()

    success('Dotfiles directory initialized successfully')

    return CONFIG_DIR
