#FROM jupyter/datascience-notebook
FROM jupyter/tensorflow-notebook
MAINTAINER NK

RUN pip install jupyterlab
RUN jupyter serverextension enable --py jupyterlab
