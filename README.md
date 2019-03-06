Example robot URDFs
===============================================

## <img align="center" height="20" src="https://i.imgur.com/vAYeCzC.png"/> Introduction

This repository includes a set of robot descriptions that are aimed to be used in benchmarking. These source files do not intend to substitute original their repositories.


**Authors:** Carlos Mastalli <br />
**With additional support from the Gepetto team at LAAS-CNRS.**

[![pipeline status](https://gepgitlab.laas.fr/gepetto/example-robot-data/badges/master/build.svg)](https://gepgitlab.laas.fr/Gepetto/example-robot-data/commits/master)


## <img align="center" height="20" src="https://i.imgur.com/x1morBF.png"/> Installation
You can install this package throught robotpkg. robotpkg is a package manager tailored for robotics softwares. It greatly simplifies the release of new versions along with the management of their dependencies. You just need to add the robotpkg apt repository to your sources.list and then use `sudo apt install robotpkg-example-robot-data`:

### Add robotpkg apt repository
If you have never added robotpkg as a softwares repository, please follow first the instructions from 1 to 4. Otherwise, go directly to instruction 5. Those instructions are similar to the installation procedures presented in [http://robotpkg.openrobots.org/debian.html](http://robotpkg.openrobots.org/debian.html).

1. Check your distribution codename in a terminal with the following command:

		$ lsb_release -c
		Codename:       xenial

2. Add robotpkg as source repository to apt:

		sudo sh -c "echo 'deb [arch=amd64] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -sc) robotpkg' >> /etc/apt/sources.list.d/robotpkg.list"

3. Register the authentication certificate of robotpkg:

		curl http://robotpkg.openrobots.org/packages/debian/robotpkg.key | sudo apt-key add -

4. You need to run at least once apt update to fetch the package descriptions:

		sudo apt-get update

5. The installation of example-robot-data:

		sudo apt install robotpkg-example-robot-data
