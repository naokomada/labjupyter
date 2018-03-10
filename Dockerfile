FROM jupyter/datascience-notebook
MAINTAINER NK

RUN pip install jupyterlab tensorflow keras
RUN jupyter serverextension enable --py jupyterlab
