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


Then, install the plugin running:
::

    pip install -U git+https://github.com/astroufsc/chimera_sbig.git

This plugin works both on Windows and Linux. For Windows installation, make sure that you have a **32bit** Pyhton
distribution and the latest drivers which can be downloaded from the SBIG website http://www.sbig.com/support/software/
(Windows DriverChecker).

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


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera_sbig/


.. _Santa Barbara Instrument Group: http://www.sbig.com/
.. _chimera: https://github.com/astroufsc/chimera