# bdb-2021

This repository contains files used in the course "Biomedical Data Bases" (BDB)
at the University of Bologna, Academic Year 2020-2021, taught by prof. Davide Salomoni.

For details, see the course slides.

For more information on the course, see [here](https://www.unibo.it/it/didattica/insegnamenti/insegnamento/2020/366280).

## Command to run the Jupyter notebook

### Create a docker network to connect to (all operating systems):

`docker network create bdb-net`

### If you run Linux or MacOS:

`docker run -d --rm --name my_jupyter -v $HOME/bdb:/home/jovyan -p 8888:8888 --network bdb-net -e JUPYTER_TOKEN="bdb_password" jupyter/datascience-notebook`

### If you run Windows 10:

`docker run -d --rm --name my_jupyter -v C:\bdb:/home/jovyan -p 8888:8888 --network bdb-net -e JUPYTER_TOKEN="bdb_password" jupyter/datascience-notebook`

## Command to run the redis server

### If you run Linux or MacOS:

`docker run -d --rm --name my_redis -v $HOME/bdb:/data --network bdb-net redis redis-server --maxmemory 32mb`

### If you run Windows 10:

`docker run -d --rm --name my_redis -v C:\bdb:/data --network bdb-net redis redis-server --maxmemory 32mb`
