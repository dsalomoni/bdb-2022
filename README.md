# bdb-2022

This repository contains files used in the course "Biomedical Data Bases" (BDB)
at the University of Bologna, Academic Year 2021-2022, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see [here](https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2021/366280).

## Install Docker

Refer to the course slides for information on how to do that.

## Create a local directory

We are going to create a directory local to our laptop/PC called _bdb_.

### If you run Linux or MacOS:

`mkdir $HOME/bdb`

### If you run Windows 10:

`mkdir %USERPROFILE%\bdb`

## Create a docker network

This is a Docker virtual network used by the containers that you will instantiate in this course.

`docker network create bdb-net`

## Start the Jupyter notebook

Remember to **change the password** to access Jupyter (parameter `JUPYTER_TOKEN` in the command below). Once the Docker container is started,
connect to http://127.0.0.1:8888. Note that with the command below access is only permitted from the PC where Docker is running.

### If you run Linux or MacOS:

`docker run -d --rm --name my_jupyter -v $HOME/bdb:/home/jovyan -p 127.0.0.1:8888:8888 --network bdb-net -e JUPYTER_TOKEN="bdb_password" --user root -e CHOWN_HOME=yes -e CHOWN_HOME_OPTS="-R" jupyter/datascience-notebook`

### If you run Windows 10:

`docker run -d --rm --name my_jupyter -v %USERPROFILE%\bdb:/home/jovyan -p 127.0.0.1:8888:8888 --network bdb-net -e JUPYTER_TOKEN="bdb_password" --user root -e CHOWN_HOME=yes -e CHOWN_HOME_OPTS="-R" jupyter/datascience-notebook`

## Start the redis server

### If you run Linux or MacOS:

#### Without persistence:
`docker run -d --rm --name my_redis -v $HOME/bdb:/data --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --maxmemory-policy allkeys-lru`

#### With persistence:
`docker run -d --rm --name my_redis -v $HOME/bdb:/data --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --save 180 1 --dbfilename my_database.rdb`

### If you run Windows 10:

#### Without persistence:
`docker run -d --rm --name my_redis -v %USERPROFILE%\bdb:/data --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --maxmemory-policy allkeys-lru`

#### With persistence:
`docker run -d --rm --name my_redis -v %USERPROFILE%\bdb:/data --network bdb-net --user 1000 redis redis-server --maxmemory 32mb --save 180 1 --dbfilename my_database.rdb`

## Possible issues with the `docker` commands and how to fix them:

### A `docker run` command fails, or the `bdb` directory is not visible from Jupyter

- Make sure you type the `docker run` commands exactly as written in these instructions. 
- Double check that you have create the Docker virtual network with the `docker network create` command above. 
- **Pay special attention** to the the single quote (') and double quote (") characters, since they are prone to be copied wrongly with  "copy/paste" actions. If you copy/paste the commands above, manually type any single of double quote characters.

### `docker run` returns `docker: Error response from daemon: Conflict. The container name "/my_jupyter" is already in use ...`

- Type `docker stop my_jupyter`
- Type `docker rm my_jupyter`
- Type the `docker run` command again.

### On Windows you get the message `"Error response ... : file exists."`
 
 If **on Windows** you get an error like the following when typing a `docker run` command:
> Error response from daemon: error while creating mount source path ... file exists.

you should restart the Docker daemon. Open the "Docker Desktop" application from the Windows main menu. If any updates to Docker are mentioned, apply them. After these updates (if any), make sure you select the option to restart the Docker daemon. Then issue the `docker run` command again.

### Other errors

If you encounter other errors, contact prof. Salomoni through the usual University channels.