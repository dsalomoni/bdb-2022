import subprocess

container_name = "my_redis"
sp = subprocess.run('docker ps --filter "name=%s"' % container_name,
                    shell=True,
                    capture_output=True,
                    text=True)
# split the output on newlines
lines = sp.stdout.split('\n')

# if there are 2 lines (the header and the final newline), the container is not running.
# if there are 3 lines, the container is running.
# if there are less than 2 or more than 3 lines, something went wrong with the docker ps command.

if len(lines) == 2:
    print("The container %s is not running." % container_name)
elif len(lines) == 3:
    print("The container %s is running." % container_name)
else:
    print("Something is wrong with the docker ps command!")
