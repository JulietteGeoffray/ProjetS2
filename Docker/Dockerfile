FROM ubuntu:16.04


# Add user

#samtools version

RUN mkdir -p /logiciel

ENV VERSION=0.1.19
ENV VERSION_BWA=0.7.13 
ENV VERSION_PICARD=2.17.4
ENV VERSION_SNPeff=4_1d

# Install Python 3, PyQt5, curl, bzip2, g++, ncurses-dev, zlib1g-dev
RUN apt-get update && apt-get install -y \
        python3 \
        python3-pyqt5 \
	curl \
	bzip2 \
	ncurses-dev \
	zlib1g-dev \
	g++ \
	make

#RUN apt-get install -y samtools. Problem : cannot choose samtools version

#Install tar for untar the packages
RUN apt-get install -y tar

WORKDIR /logiciel
RUN curl -L -o samtools-$VERSION.tar.gz https://github.com/samtools/samtools/archive/$VERSION.tar.gz
RUN tar xzf samtools-$VERSION.tar.gz
RUN rm -rf samtools-$VERSION.tar.gz
RUN cd samtools-$VERSION
WORKDIR /logiciel/samtools-$VERSION
RUN make
RUN cp samtools /usr/bin/

#bwa details 
WORKDIR /logiciel
RUN curl -L -o bwa-$VERSION_BWA.tar.gz https://github.com/lh3/bwa/releases/download/v$VERSION_BWA/bwa-$VERSION_BWA.tar.bz2
RUN tar xjf bwa-$VERSION_BWA.tar.gz
RUN rm -rf bwa-$VERSION_BWA.tar.gz
RUN cd bwa-$VERSION_BWA
WORKDIR /logiciel/bwa-$VERSION_BWA
RUN make
RUN cp bwa /usr/bin/
RUN cd ..

#PICARD details
WORKDIR /logiciel
RUN curl -L -o picard.jar https://github.com/broadinstitute/picard/releases/download/$VERSION_PICARD/picard.jar
#permission rights to acces .jar file
RUN chmod 777 picard.jar
#install java 
RUN apt-get install -y default-jre-headless

#GATK details
#GO to https://software.broadinstitute.org/gatk/download/archive to see all the GATK archives and VERSIONS

#RUN curl -L -o GenomeAnalysisTK-$VERSION_GATK.tar.bz2 https://software.broadinstitute.org/gatk/download/auth?package=GATK-archive&version=$VERSION_GATK

COPY GenomeAnalysisTK-3.7-0-gcfedb67.tar.bz2 GATK.tar.bz2
RUN tar xjf GATK.tar.bz2
RUN rm -rf GATK.tar.bz2
RUN chmod 777 GenomeAnalysisTK.jar





#R details
RUN apt-get install -y r-base \
	r-base-dev \
	r-recommended
RUN R -e "install.packages('ggplot2',repos='http://cran.us.r-project.org')"

#SNPeff details

RUN curl -L -o snpeff-$VERSION_SNPeff.zip http://downloads.sourceforge.net/project/snpeff/snpEff_v4_1d_core.zip

RUN unzip snpeff-$VERSION_SNPeff.zip
RUN rm -rf snpeff-$VERSION_SNPeff.zip

#ADD qt5.py qt5.py


#CMD ["python3", "qt5.py"]


