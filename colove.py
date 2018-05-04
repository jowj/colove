import os
import sys
import argparse
import subprocess
import pdb

SCRIPTPATH = os.path.realpath(__file__)
SCRIPTDIR = os.path.dirname(SCRIPTPATH)
DOCKERDIR = os.path.join(SCRIPTDIR, 'docker')
COLOVEDIR = '/colove'

def dockerrun(
    colovevolperms='rw', hostname='colove'):
    args = [
        'docker', 'run',
        '--rm',
        '--interactive',
        '--tty',
        '--volume', f'{SCRIPTDIR}:{COLOVEDIR}:{colovevolperms}',
        '--hostname', hostname,
        'colove:latest']
    subprocess.run(args)

def dockerbuild():
    args = [
        'docker', 'build',
        DOCKERDIR,
        '--tag',
        'colove:latest']
    subprocess.run(args)

def main(argv):
    if argv == ['-r']:
        dockerrun()
    if argv == ['-b']:
        dockerbuild()

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='what docker operation do you want?')
    parse.add_argument('-r','--run',help='runs the container',action='store_true')
    parse.add_argument('-b','--build',help='builds the container',action='store_true')

    args = parse.parse_args()
    main(sys.argv[1:])
