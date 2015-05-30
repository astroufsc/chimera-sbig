chimera_sbig plugin
===================

A chimera_ plugin for `Santa Barbara Instrument Group`_ cameras and filter wheels.

Usage
-----

Install chimera_ on your computer, and then, this package. Edit the configuration like the example below. The type of
the ``camera`` instrument section should be ``SBIG``.


Installation
------------

This plugin depends on the SBIG Universal Driver library ``libsbigudrv.so`` installed on the system ``LD_LIBRARY_PATH``.
There is a package on Ubuntu Server 14.04.2 which installs it:

::

    sudo apt-get install libsbigudrv2-dev


Then, install the package.
::

    pip install -U git+https://github.com/astroufsc/chimera_sbig.git


Configuration Example
---------------------

::

    camera:
      name: st7
      type: SBIG
      filters: R G B RGB CLEAR


Tested Hardware
---------------

This plugin was tested on:

* SBIG ST7 USB + ??? fwheel


.. _Santa Barbara Instrument Group: http://www.sbig.com/
.. _chimera: https://github.com/astroufsc/chimera