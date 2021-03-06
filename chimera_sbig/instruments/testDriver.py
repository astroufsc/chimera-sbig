#!/usr/bin/env python

import numpy
import time
import logging
log = logging.getLogger(__name__)


import os

from astropy.io import fits


import sbig_constants

import sbigdrv


testExposure = False


if __name__ == '__main__':
    sbig = sbigdrv.SBIGDrv()

    try:
        print '=> Testing sbigdrv...'

        print " openDriver = " + str(sbig.openDriver())

        # print "queryUSB => "
        #
        # cams = sbig.queryUSB() # OK
        #
        # for cam in cams:
        #     print cam

        print " openDevice = " + str(sbig.openDevice(1))

        print "queryDriverInfo = (version, name, maxRequest) -> " + str(tuple(sbig.queryDriverInfo())) # OK

        print " establishLink = " + str(sbig.establishLink())

        print " isLinked = " + str(sbig.isLinked())

        # fanEnabled, fanPower, ccdSetpoint, imagingCCDTemperature
        # print "getTemperature = (fanEnabled, fanPower, ccdSetpoint, imagingCCDTemperature) -> " + str(tuple(sbig.getTemperature(ccd=True))) #OK

        # print "startFan = " + str(sbig.startFan()) #OK

        # print "isFanning = " + str(sbig.isFanning()) #OK

        # print "stopFan = " + str(sbig.stopFan()) #OK

        # print "setTemperature = " + str(sbig.setTemperature(regulation=True, setpoint=-15, autofreeze=False)) #OK

        print " queryCCDInfo = " + str(sbig.queryCCDInfo()) # OK

        print " getFilterInfo = " + str(sbig.getFilterInfo())

        print " self.cameraNames = " + str(sbig.cameraNames[sbig.imaging]) # OK


        print " self.FilterConfigString = " + sbig.getFilterConfigString()


        print "getFilterStatus = " + str(sbig.getFilterStatus()) # OK

        # print "getFilterPosition BEFORE = " + str(sbig.getFilterPosition()) # OK

        print "setFilterPosition = " + str(sbig.setFilterPosition(sbig_constants.CFW_POSITION.CFWP_1))

        # print "startExposure = " + str(sbig.startExposure(0, 10, 0)) # NOT TESTED

        # print "endExposure = " + str(sbig.endExposure(0)) # NOT TESTED

        # print "startReadout = " + str(sbig.startReadout(0)) # NOT TESTED

        # print "readoutLine = " + str(sbig.readoutLine(0)) # NOT TESTED

        # print "endReadout = " + str(sbig.endReadout(0)) # NOT TESTED

        # Starting observation...

        if testExposure:

            print " startExposure = " \
                  + str(sbig.startExposure(sbig.imaging, 60*100, sbig_constants.SHUTTER_COMMAND.SC_OPEN_SHUTTER))

            for cont in range(10):  # CCD number of lines is the height.
                print "   exposing => " + str(sbig.exposing(sbig.imaging))
                time.sleep(1)

            time.sleep(60)

            print " endExposure = " + str(sbig.endExposure(sbig.imaging))

            print "   exposing => " + str(sbig.exposing(sbig.imaging))

            print " startReadout = " + str(sbig.startReadout(sbig.imaging))

            readout_mode = sbig.readoutModes[sbig.imaging][sbig_constants.READOUT_BINNING_MODE.RM_1X1]

            # attributes = vars(readout_mode)
            # print ', '.join("%s: %s" % item for item in attributes.items())

            img = numpy.zeros((readout_mode.height, readout_mode.width))  # TODO: Check -- Height x Width?

            heigth = readout_mode.height

            for i_line in range(heigth):  # CCD number of lines is the height.
                img[i_line] = sbig.readoutLine(sbig.imaging)

            try:
                os.unlink('test.fits')
            except OSError:
                pass

            fits.writeto('test.fits', img)

            print " endReadout = " + str(sbig.endReadout(sbig.imaging))

            print "   exposing => " + str(sbig.exposing(sbig.imaging))

        print " All tests performed."

    except sbigdrv.SBIGException, e:
        print "SBIGException: " + e.message
    finally:
        print "=> Finally block."
        print " closeDevice = " + str(sbig.closeDevice())
        print " closeDriver = " + str(sbig.closeDriver())




'''
ERROR
============

OK
==========================
openDriver
openDevice
establishLink
getTemperature
startFan
stopFan
isFanning
isLinked

setTemperature
getFilterStatus
getFilterPosition

queryCCDInfo
queryDriverInfo
queryUSB

startExposure
endExposure

endReadout
startReadout
readoutLine
exposing

setFilterPosition


'''