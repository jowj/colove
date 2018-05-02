import subprocess

def dockerrun():
    args = [
        'docker', 'run',
        '--rm',
        '--interactive',
        '--tty',
        'colove:latest']
    subprocess.run(args)

if __name__ == '__main__':
    dockerrun()