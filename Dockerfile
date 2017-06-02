# use a debian base image
FROM debian
# install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
&& apt-get -y install python3 \
python-pysnmp4 python-pysnmp4-mibs \
python-matplotlib
# clean up
RUN apt-get clean
# install our demo application
COPY web7.5.py /src/web7.5.py
COPY generator.py /src/generator.py
COPY snmp.py /src/snmp.py
# port 80 will be reachable
EXPOSE 80
CMD ["python3", "/src/web7.5.py"]
# BUGS
# - installs a lot of unneeded stuff in the Docker image
