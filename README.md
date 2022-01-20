# bdb-2022

This repository contains files used in the course "Biomedical Data Bases" (BDB)
at the University of Bologna, Academic Year 2021-2022, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see [here](https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2021/366280).

## Install Docker

Refer to the course slides for instructions on how to do that.

## Create a local directory

We are going to create a directory local to our laptop/PC called _bdb_.

### If you run Linux or MacOS:

`mkdir $HOME/bdb`

### If you run Windows 10/11:

**Note: changed on 19/1/2022, make sure you copy the line below!**

`mkdir C:\bdb`

This creates the folder called 'bdb' directly under the root of your C: drive. You should be able to see the bdb folder if you go to "My Computer", and then select the "C:" drive. Copy to this folder the files you want to make visible to Jupyter.

## Create a docker network

This is a Docker virtual network used by the containers that you will instantiate in this course.

`docker network create bdb-net`

## Start the Jupyter notebook

Remember to **change the password** to access Jupyter (parameter `JUPYTER_TOKEN` in the command below). Once the Docker container is started,
connect to http://127.0.0.1:8888. Note anyway that with the command below access is only permitted from the PC where Docker is running.

### If you run Linux or MacOS:

`docker run -d --rm --name my_jupyter -v $HOME/bdb:/home/jovyan -p 127.0.0.1:8888:8888 --network bdb-net -e JUPYTER_ENABLE_LAB=yes -e JUPYTER_TOKEN="bdb_password" --user root -e CHOWN_HOME=yes -e CHOWN_HOME_OPTS="-R" jupyter/datascience-notebook`

### If you run Windows 10/11:

**Note: changed on 19/1/2022, make sure you copy the line below!**

`docker run -d --rm --name my_jupyter --mount src=C:\bdb,dst=/home/jovyan,type=bind -p 127.0.0.1:8888:8888 --network bdb-net -e JUPYTER_ENABLE_LAB=yes -e JUPYTER_TOKEN="bdb_password" --user root -e CHOWN_HOME=yes -e CHOWN_HOME_OPTS="-R" jupyter/datascience-notebook`

## Start the redis server

### If you run Linux or MacOS:

#### Without persistence:
`docker run -d --rm --name my_redis -v $HOME/bdb:/data --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --maxmemory-policy allkeys-lru`

#### With persistence:
`docker run -d --rm --name my_redis -v $HOME/bdb:/data --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --save 180 1 --dbfilename my_database.rdb`

### If you run Windows 10/11:

#### Without persistence:
`docker run -d --rm --name my_redis --mount src=C:\bdb,dst=/data,type=bind --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --maxmemory-policy allkeys-lru`

#### With persistence:
`docker run -d --rm --name my_redis --mount src=C:\bdb,dst=/data,type=bind --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --save 180 1 --dbfilename my_database.rdb`

## Possible issues with Docker and how to fix them:

### A `docker run` command fails, or the `bdb` directory is not visible from Jupyter

- Make sure you type the `docker run` commands exactly as written in these instructions. 
- Double check that you have create the Docker virtual network with the `docker network create` command above. 
- **Pay special attention** to the the single quote (') and double quote (") characters, since they are prone to be copied wrongly with  "copy/paste" actions. If you copy/paste the commands above, manually type any single of double quote characters.

### `docker run` returns `docker: Error response from daemon: Conflict. The container name "/my_jupyter" is already in use ...`

- Type `docker stop my_jupyter`
- Type `docker rm my_jupyter`
- Type the `docker run` command again.

### On Windows, you get the message `"Error response ... : file exists."`
 
 If **on Windows** you get an error like the following when typing a `docker run` command:
> Error response from daemon: error while creating mount source path ... file exists.

you should restart the Docker daemon. Open the "Docker Desktop" application from the Windows main menu. If any updates to Docker are mentioned, apply them. After these updates (if any), make sure you select the option to restart the Docker daemon. Then issue the `docker run` command again.

### On Windows, after you install Docker Desktop you cannot run VirtualBox VMs anymore

This is a Windows issue that does not always happen. If you do not have VirtualBox installed, or if VirtualBox and Docker both work on your system, skip this part. 

If you have the issue, however, unfortunately there is only a workaround that seems to work, and that is to enable **either** Docker Desktop **or** VirtualBox. You can have both installed on your system, but only one at a time can be enabled.

Enabling one or the other is done via this procedure:

1. open the Windows Control Panel (in Italian: Impostazioni)
2. search for the string "Windows features" and select the item "Turn Windows features on or off". Those with an Italian version of Windows may search for the string "Attiva o disattiva funzionalità di Windows".

Now, in the windows that opens up:

- **if you want to use VirtualBox**, _deselect_ the items called "Virtual machine platform" and "Windows Hypervisor Platformn" and then click "OK". 
- **if you want to use Docker**, _select_ the items called "Virtual machine platform" and "Windows Hypervisor Platformn" and then click "OK". 

Those with an Italian version of Windows will see the two items mentioned above translated as "Piattaforma macchina virtuale" and "Piattaforma Windows Hypervisor".

In either case, you will have to reboot your system. When Windows boots up again, you will be able to run either VirtualBox or Docker, depedning on whether you deselected or selected the items above. If you find a different way to handle this issue, please let prof. Salomoni know.

### On Windows, you get the message `"docker_engine: Access is denied"`

This error may be due to several causes:

- make sure that Docker Desktop is properly installed and that when you open it it says "Docker is running". If Docker cannot start, make sure you have applied all suggested updates, including (if you are prompted about that) the "Windows Subsystem for Linux 2", or WSL 2. If all updates have been applied, deinstall and reinstall the Docker Desktop application, rebooting when prompted to do so.
- make sure you run the Windows terminal as "administrator". 

### Other errors

If you encounter other errors, contact prof. Salomoni through the usual University channels.