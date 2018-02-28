# Andalusian Mapping Software


## Summary:  
Andalusian Mapping Software is based on [**Andalusian Mapping**](https://github.com/fabfabBesnard/Andalusian_Mapping) pipeline created by [**Fabrice Besnard**](https://github.com/fabfabBesnard/Andalusian_Mapping). The software proposes a Graphical User Interface (GUI) developped in PyQt5 in order to simplify the use of the pipeline. It can be run locally and it doesn't need the use of a distant server. You can adapt it to any reference genome and study non-model organisms.  
The third-party softwares are all installed in a Docker container so you don't need to install any software into your local machine.   
The Docker container includes :

- Program: **bwa** (alignment via Burrows-Wheeler transformation)
Version: 0.7.13-r1126
- Program: **samtools** (Tools for alignments in the SAM format)
Version: 0.1.19-96b5f2294a
- Program: **PICARD** (A set of command line tools (in Java) for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.)  
Version: 2 .17.4
-  Program: **GATK** (Genome Analysis Toolkit ,Variant Discovery in High-Throughput Sequencing Data)  
Version: 3.6
- Program: **SnpEff** (Annotate variants / calculate effects)  
Version: 4_1d
- Program : **R** (a language and environment for statistical computing and graphics)  
Version: 3.2.3
- Program:  **Python** (an interpreted high-level programming language for general-purpose programming)  
Version: Python 3.5.2  
**PyQt5** is also installed in order to run python GUIs.  
**Java** is installed to run picard, GATK, SnpEff.

The final goal of the software is to provide :
1. Plots of allele frequency (mutant strain allele / mapping-strain allele) for each scaffolds/Chromosome present in the reference genome. This allows to visualy map the region linked to the mutation selected in the F2 population.
2. An annotated vcf file containing the mutations linked to the phenotype-causing mutations with their functional impacts.
3. The best candidate mutations based on the predicted functional impact.

All the final information will be summarized in a HTML file that can be shared will others.

## Installation

### Python

Make sure that you have installed a python 3     version in your machine. In order to see the python version that you possess type the command below in your bash terminal :

```
python3 --version
```
### PyQt5
The Andalusian Mapping GUI is developped in PyQt5.
The GUI has to be downloded and run in your local machine so it can use the X11 server who provides the tools needed to use graphical applications.  
If you haven't already installed PyQt5, please do so.

* Install PyQt5 using *pip* :
```
pip3 install pyqt5
```

* Install using *apt-get*
```
sudo apt-get install python3-pyqt5
```
You can also install it from the source. Please see the [**PyQt5**](http://pyqt.sourceforge.net/Docs/PyQt5/installation.html) documentation.

### Docker
All the third-party softwares, as described in the Summary section, used by Andalusian Mapping are installed in a Docker container.  
Install and configure Docker for Linux :

1. Update the server
```
sudo apt-get update
```

2. Install docker.io
```
sudo apt-get install -y docker.io
```
3. Verify the installation

```
sudo docker --version
```
#### Post-installation steps for Linux
Manage Docker as a non-root user.  
If you don’t want to use sudo when you use the docker command, create a Unix group called docker and add users to it. When the docker daemon starts, it makes the ownership of the Unix socket read/writable by the docker group.

To create the docker group and add your user:

1. Create the docker group.

```
sudo groupadd docker
```

2. Add your user to the docker group.

```
sudo usermod -aG docker $USER
```


Log out and log back in so that your group membership is re-evaluated.  
If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

Verify that you can run docker commands without sudo.
```
docker run hello-world
```

This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.

Now you can pull the Andalusian Mapping container from the Docker hub.

```
docker pull hermespara/andalusian_mapping
```
This process might take some time.
The docker container of the Andalusian Mapping is now ready to be launched.

## GUI
Download the GUI's files by clonning the GitHub repository.
```
git clone https://github.com/JulietteGeoffray/ProjetS2.git
```
Or just by downloading the ZIP file.

The GUI can be launched by clicking the Andalusian Mapping file. Once the GUI launched, a window will appear. In the first page you will notice a description of the software. At your left is situated the software menu :

* Home
* New Analysis
* Old Analysis
* Results
* About

### New Analysis
To launch a new analysis click the *New Analysis* button. This procedure is composed by 4 steps where the user should fill all the information needed. Click *Next* when you have finish a step and *Run Analysis* at the last step.

#### Step 1

##### Analysis Title
Name your analysis. The software will create a directory with the same name at the same location as the Software files. It will also save a configuration file where all the information will be stocked. That will allow the user to charge the same information later on.

##### Reference Genome
Upload the reference genome by clicking the three dots ... button. A file dialog will appear. Choose the reference genome file. The file path will be printed in the text box at the left of the three dots button. You can also type the absolute file path at the text box.

##### Reads
Upload the read files the same way as the reference genome file. The analysis run by this software is adapted for pair end reads. You can add more read files by clicking the *+* button. You can add until 8 read files. The *+* button adds two read files. You have the possibility to remove two read files by *-* button.  
Click *Next* button. You can return back by clicking the *Back* button.

#### Step 2
Corresponds to the information needed by GATK program.

##### Platform or RGPL (Read Group Platform)
Fill this text box with the ploatform used to generate the read files *e.g. ILLUMINA*.  
**PL** = Platform/technology used to produce the read
This constitutes the only way to know what sequencing technology was used to generate the sequencing data.   
Valid values: ILLUMINA, SOLID, LS454, HELICOS and PACBIO.

Note that fq file names are are buit as follows:
```
{FlowCellID}-{sampleID}_Lane(=Lx)_Pair(=1/2).fq.gz
```
##### RGSM (Read Group Sample Name)
SM = biological sample name. (*e.g. mf76*)  
**SM** = Sample  
The name of the sample sequenced in this read group. GATK tools treat all read groups with the same SM value as containing sequencing data for the same sample, and this is also the name that will be used for the sample column in the VCF file. Therefore it's critical that the SM field be specified correctly. When sequencing pools of samples, use a pool name instead of an individual sample name.

##### RGLB (Read Group Library)
LB = name of DNA preparation library tube (*e.g. mf76_LB1*)
LB = DNA preparation library identifier  
MarkDuplicates uses the LB field to determine which read groups might contain molecular duplicates, in case the same DNA library was sequenced on multiple lanes.

##### RGID (Read Group Identifier)
ID = Read group identifier (e.g. FCH7TC7BBXX_mf55)
ID = Read group identifier  
This tag identifies which read group each read belongs to, so each read group's ID must be unique. It is referenced both in the read group definition line in the file header (starting with @RG) and in the RG:Z tag for each read record. Note that some Picard tools have the ability to modify IDs when merging SAM files in order to avoid collisions. In Illumina data, read group IDs are composed using the flowcell + lane name and number, making them a globally unique identifier across all sequencing data in the world.
Use for BQSR: ID is the lowest denominator that differentiates factors contributing to technical batch effects: therefore, a read group is effectively treated as a separate run of the instrument in data processing steps such as base quality score recalibration, since they are assumed to share the same error model.

##### RGPU (Read Group Platform Unit)
PU = Platform Unit (e.g. FCH7NLVBBXX_L8_mf55)
PU = Platform Unit  
The PU holds three types of information, the {FLOWCELL_BARCODE}.{LANE}.{SAMPLE_BARCODE}. The {FLOWCELL_BARCODE} refers to the unique identifier for a particular flow cell. The {LANE} indicates the lane of the flow cell and the {SAMPLE_BARCODE} is a sample/library-specific identifier. Although the PU is not required by GATK but takes precedence over ID for base recalibration if it is present. In the example shown earlier, two read group fields, ID and PU, appropriately differentiate flow cell lane, marked by .2, a factor that contributes to batch ef

For more information please see the [**GATK**](https://gatkforums.broadinstitute.org/gatk/discussion/6472/read-groups) documentation
#### Step 3
Design of the population for the mapping
##### Background strain ID

##### Referenced

##### Mapping strain ID

##### dbSNP

#### Step 4
Additionnal information

##### Liste of scaffolds ID and their size

##### "Invariant" Scaffolds

##### "warning" Scaffolds

### Run Analysis
Once you completed all the information asked by the GUI, click the *Run Analysis* button. If you have forgotten to give all the information asked, a Warning will show up and indicate the information that is missing. You can go back and fill the information.

### Old Anlaysis
You have the possibility to run an old experience by just loading the configuration file. Click *Old Analysis* button and choose the configuration file that you want to upload. You can change one or multiple details of this configuration file. Run the analysis as mention before.

### Results
The Results are organised in a html file saved in th

## About

This software is developped by :

- **_Juliette GEOFFRAY_**
- **_Eric CUMUNEL_**
- **_Hermes PARAQINDES_**

We are three students at [**Master 1 Molecular Bio-Informatic**](https://www.bioinfo-lyon.fr/) of [**Claude Bernard Lyon 1 University (UCBL)**](https://www.univ-lyon1.fr/)

The original pipeline is developped by **_Fabrice BESNARD_**, researcher at the [**Ecole Normale Superieure de Lyon (ENS)**](http://www.ens-lyon.fr/)
