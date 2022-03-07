# CLI to use the different modules of Pyxcel

import argparse

import sys
import os

# import modules

###
#  Migrators for IMS and KA
# Appendinator for control and concatination of IMS Template Files
# Divider for creating files in the format of the KA template based on concatinated IMS file
# Migrator to transform exported files from MySoft to IMS formatted files
from Appendinator import Appendinator as ims_appendinator
from Divider import DivideFile as ims_to_ka
from Migrator import Migrator as mysoft_to_ims

# parser setup
magic_snake = argparse.ArgumentParser(
    prog='magic_snake',
    description='Magic Snake that will perform wizardry to create migration files for KA and IMS',
    epilog='The Magic Snake will pull upon Dark Magics to make your files when you are ready!'
)

magic_snake.version = '0.0'

# arguments setup
magic_snake.add_argument(
    'ENV_FILE',
    '-e',
    '--env_path',
    action='store',
    help='Set the path to the .txt containing required environment variables to run the different Migrators',
    default='files/env_file.txt'
)

magic_snake.add_argument(
    '-c',
    '--config',
    action='store',
    choices=['a', 'm'],
    default='a',
    help='Set config to manual, or automatic, where\nm= require manual input of all envs\na= automatically set envs from env_file at env_path'
)


magic_snake.add_argument(
    'MIGRATOR',
    metavar='MIGRATOR',
    action='store',
    choices=['ims', 'ka', 'mysoft'],
    help='which migrator to run, where\nims= Basis files are in the IMS format and you want appended and controlled IMS Migration File\nka= Create KA formatted files from a single combined IMS Migration File\nmysoft= Parse and create IMS Formatted Files from MySoft formatted basis files'
)



magic_snake.add_argument(
    '-v',
    '--version',
    action='version',
    help='print Magic Snake version'
)



# execute parser
args = magic_snake.parse_args()

env_path = args.ENV_FILE

if not os.path.isdir(env_path):
    print('The env_path specified does not exist')
    sys.exit()

print('\nMagic Snake has Magicced Snakily\n')
print(vars(args))