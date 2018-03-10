FROM jupyter/datascience-notebook
MAINTAINER NK

RUN pip install jupyterlab
RUN jupyter serverextension enable --py jupyterlab
