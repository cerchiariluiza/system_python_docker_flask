FROM python:3.7-slim-stretch as app
RUN python -m pip install --upgrade pip
RUN apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update
RUN apt-get update -y
RUN apt-get install build-essential python-dev wkhtmltopdf xvfb -y
RUN printf '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh
RUN chmod a+x /usr/bin/wkhtmltopdf.sh
RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf
RUN mkdir -p /app
WORKDIR /app
COPY app/requirements.txt/ /app/
RUN pip install -r requirements.txt