import subprocess
import pdb

SCRIPTPATH = os.path.realpath(__file__)
SCRIPTDIR = os.path.dirname(SCRIPTPATH)
DOCKERDIR = os.path.join(SCRIPTDIR, 'docker')
COLOVEDIR = '/home/colove/host'

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

if __name__ == '__main__':
    dockerrun()