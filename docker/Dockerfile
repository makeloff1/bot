FROM centos:7 AS LineDesign

# Install python
ENV LC_ALL en_US.utf8
ENV LANG C
USER root
WORKDIR /usr/src
RUN yum install -y which gcc make openssl-devel bzip2-devel libffi-devel wget nmap-ncat telnet
RUN wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
RUN tar xzf Python-3.7.3.tgz
WORKDIR /usr/src/Python-3.7.3
RUN ./configure --enable-optimizations
RUN make altinstall
WORKDIR /usr/src
RUN rm Python-3.7.3.tgz

# pipenv installation
RUN pip3.7 install pipenv
RUN ln -s /usr/bin/pip3.7 /bin/pip

# python must be pointing to python3.7
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3.7 /usr/bin/python

WORKDIR /home/admin/linedesign

# config
ENV DEVELOPMENT True
ENV FLASK_DEBUG True

# execute flask
# COPY --chown=admin:admin . .
COPY . .
RUN pipenv install
# RUN FLASK_APP=app.py pipenv run flask run --host=0.0.0.0 --port=10090
