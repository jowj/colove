import subprocess

def dockerrun():
    args = [
        'docker', 'run',
        '--rm',
        '--interactive',
        '--tty',
        '--mount', 'source=agares,target=/colove',
        'colove:latest']
    subprocess.run(args)

if __name__ == '__main__':
    dockerrun()