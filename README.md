# bdb-2021

This repository contains files used in the course "Biomedical Data Bases" (BDB)
at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see [here](https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/366280).

## Create a docker network

`docker network create bdb-net`

## Command to start the Jupyter notebook

Remember to **change the password** to access Jupyter (parameter `JUPYTER_TOKEN` in the command below). Once the docker container is started,
connect to http://127.0.0.1:8888. Note that with the command below access is only permitted from the PC where docker is running.

### If you run Linux or MacOS:

`docker run -d --rm --name my_jupyter -v $HOME/bdb:/home/jovyan -p 127.0.0.1:8888:8888 --network bdb-net -e JUPYTER_TOKEN="bdb_password" jupyter/datascience-notebook`

### If you run Windows 10:

`docker run -d --rm --name my_jupyter -v C:\bdb:/home/jovyan -p 127.0.0.1:8888:8888 --network bdb-net -e JUPYTER_TOKEN="bdb_password" jupyter/datascience-notebook`

## Command to start the redis server

### If you run Linux or MacOS:

#### Without persistence:
`docker run -d --rm --name my_redis -v $HOME/bdb:/data --network bdb-net redis redis-server --maxmemory 32mb --maxmemory-policy allkeys-lru`

#### With persistence:
`docker run -d --rm --name my_redis -v $HOME/bdb:/data --network bdb-net redis redis-server --maxmemory 32mb --save 180 1 --dbfilename my_database.rdb`

### If you run Windows 10:

#### Without persistence:
`docker run -d --rm --name my_redis -v C:\bdb:/data --network bdb-net redis redis-server --maxmemory 32mb --maxmemory-policy allkeys-lru`

#### With persistence:
`docker run -d --rm --name my_redis -v C:\bdb:/data --network bdb-net redis redis-server --maxmemory 32mb --save 180 1 --dbfilename my_database.rdb`
