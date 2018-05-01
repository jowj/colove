import subprocess

def dockerrun():
    args = ['docker', 'run', '-it', '--name', 'mst3k','colove:latest']
    subprocess.Popen(args)

if __name__ == '__main__':
    dockerrun()