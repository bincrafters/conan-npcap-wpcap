# Npcap is the Nmap Project's packet sniffing library for Windows.

[Conan.io](https://conan.io) package for [Npcap](https://github.com/nmap/npcap) project

Note: This package is for a subproject referred to as wpcap.  It is a subproject and dependency of the complete NPCap package here: 
	
	https://github.com/bincrafters/conan-npcap

The packages generated with this **conanfile** can be found in [conan.io](https://bintray.com/bincrafters/public-conan/npcap-wpcap).

# To consume this package

## Basic setup

    $ conan install npcap-wpcap/0.93@bincrafters/testing

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    npcap-wpcap/0.93@bincrafters/testing
	
    [generators]
    txt
    cmake

## Actual Install 

    conan install . 

Installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
	
# To build the package

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload npcap-wpcap/0.93@bincrafters/testing --all
