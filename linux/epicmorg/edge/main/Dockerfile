FROM epicmorg/prod
LABEL maintainer="EpicMorg DevTeam, developer@epicm.org"
ARG DEBIAN_FRONTEND=noninteractive

##################################################################
#                   sid sources list
##################################################################
COPY  sources.sid.list /etc/apt/sources.list.d/sources.sid.list
RUN  apt update && \
     apt autoremove -y && \
     apt-get install -y -o APT::Immediate-Configure=0 -t sid libc6  && \
     apt dist-upgrade -y && \
     apt autoremove -y

##################################################################
#                   cleaninig up
##################################################################
RUN apt purge policykit-1 -y && \
    apt clean -y && \
    apt autoclean -y && \
    rm -rfv /var/lib/apt/lists/* && \
    rm -rfv /var/cache/apt/archives/*.deb
