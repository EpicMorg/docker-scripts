FROM epicmorg/devel
LABEL maintainer="EpicMorg DevTeam, developer@epicm.org"
ARG DEBIAN_FRONTEND=noninteractive

##################################################################
#                   installing java7
##################################################################
RUN wget -qO - http://repos.azulsystems.com/RPM-GPG-KEY-azulsystems | apt-key add - && \
    echo 'deb http://repos.azulsystems.com/debian stable main' > /etc/apt/sources.list.d/zulu.list && \
    apt-get update -y && \
    apt-get install -y --allow-unauthenticated zulu-7 && \
    java -version

##################################################################
#                   cleaninig up
##################################################################
RUN apt clean -y && \
    apt autoclean -y && \
    rm -rfv /var/lib/apt/lists/* && \
    rm -rfv /var/cache/apt/archives/*.deb
