# CTYPES wrapper for SBIGUDrv library
# SBIGUDrv library documentation can be found at: http://archive.sbig.com/pdffiles/SBIGUDrv.pdf

import math

import numpy
import sbigudrv as udrv

import logging
log = logging.getLogger(__name__)

from chimera.core.exceptions import ChimeraException
from chimera.interfaces.camera import ReadoutMode

import ctypes

class SBIGException (ChimeraException):

    def __init__(self, code, msg=""):
        ChimeraException.__init__(self, msg)
        self.code = code

    def __str__(self):
        return "%s (%d)" % (self.message, self.code)


class SBIGReadoutMode(ReadoutMode):

    def __init__(self, mode):
        # FIXME: Is this needed?
        # self.mode = mode.mode
        # self.gain = float(hex(mode.gain).split('x')[1]) / 100.0
        # self.width = mode.width
        # self.height = mode.height
        # self.pixelWidth = float(hex(mode.pixel_width).split('x')[1]) / 100.0
        # self.pixelHeight = float(hex(mode.pixel_height).split('x')[1]) / 100.0
        self._udrv = ctypes.CDLL('/usr/lib/libsbigudrv.so')  #FIXME:
        pass


class SBIGDrv(object):

    def __init__(self):
        # FIXME: check device permissions and module status
        pass

    def openDriver(self):
        '''
        Opens SBIG driver. Library command: CC_OPEN_DRIVER.
        See driver doc page 7.
        :return:
        '''
        # try:
        #     return self._cmd(udrv.CC_OPEN_DRIVER, None, None)
        # except SBIGException, e:
        #     if e.code == udrv.CE_DRIVER_NOT_CLOSED:
        #         # driver already open (are you trying to use the tracking ccd?)
        #         return True
        #     else:
        #         raise
        self._udrv.SBIGUnivDrvCommand(10, None, None) #FIXME: ... this is an example ...

        return NotImplementedError()

    def closeDriver(self):
        '''
        Opens SBIG driver. Library command: CC_CLOSE_DRIVER.
        See driver doc page 7.
        :return:
        '''
        # return self._cmd(udrv.CC_CLOSE_DRIVER, None, None)
        return NotImplementedError()

    def openDevice(self, device):
        '''
        Opens SBIG camera device. Library command: CC_OPEN_DEVICE.
        See driver doc page 7.
        :param device: TODO: docme
        :return:
        '''
        # FIXME: USB and ETHERNET?

        # odp = udrv.OpenDeviceParams()
        # odp.deviceType = device
        #
        # try:
        #     return self._cmd(udrv.CC_OPEN_DEVICE, odp, None)
        # except SBIGException, e:
        #     if e.code == udrv.CE_DEVICE_NOT_CLOSED:
        #         # device already open (are you trying to use the tracking ccd?)
        #         return True
        #     else:
        #         raise

        return NotImplementedError()

    def closeDevice(self):
        '''
        Closes SBIG camera device. Library command: CC_CLOSE_DEVICE.
        See driver doc page 7.
        :return:
        '''
        # return self._cmd(udrv.CC_CLOSE_DEVICE, None, None)
        return NotImplementedError()

    def establishLink(self):
        '''
        Establishes a communications link with the camera. Library command: CC_ESTABLISH_LINK.
        See driver doc page 26.
        :return:
        '''
        # elp = udrv.EstablishLinkParams()
        # elr = udrv.EstablishLinkResults()
        # err = self._cmd(udrv.CC_ESTABLISH_LINK, elp, elr)
        #
        # if not err:
        #     self.queryCCDInfo()
        #
        # return err
        return NotImplementedError()

    def isLinked(self):
        '''
        Returns True if camera link is up. Otherwise, returns False. Library command: CC_GET_LINK_STATUS.
        See driver doc page 32.
        :return:
        '''
        # # FIXME: ask SBIG to get a better CC_GET_LINK_STATUS.. this one it too
        # # bogus
        # glsr = udrv.GetLinkStatusResults()
        # self._cmd(udrv.CC_GET_LINK_STATUS, None, glsr)
        # return bool(glsr.linkEstablished)
        return NotImplementedError()

    def startExposure(self, ccd, exp_time, shutter):
        '''
        Start camera exposure. Library command: CC_START_EXPOSURE2
        See driver doc page 9.
        :param ccd:
        :param exp_time:
        :param shutter:
        :return:
        '''
        # TODO: Note that I've changed the old StartExposure by the new StartExposure2. See documentation.

        # sep = udrv.StartExposureParams()
        #
        # sep.ccd = ccd
        # sep.openShutter = shutter
        # sep.abgState = 0
        # sep.exposureTime = exp_time
        #
        # return self._cmd(udrv.CC_START_EXPOSURE, sep, None)
        return NotImplementedError()

    def endExposure(self, ccd):
        '''
        End Exposure command is used after the integration is complete to prepare the CCD for readout or to terminate an
        exposure prematurely. Library command: CC_END_EXPOSURE
        See driver doc page 12.
        :param ccd:
        :return:
        '''
        # eep = udrv.EndExposureParams()
        # eep.ccd = ccd
        #
        # return self._cmd(udrv.CC_END_EXPOSURE, eep, None)
        return NotImplementedError()

    def exposing(self, ccd):
        '''
        Returns True if ccd is exposing. Library command: ???
        See driver doc page ????.
        :param ccd:
        :return:
        '''
        # if ccd == self.imaging:
        #     return (
        #         (self._status(udrv.CC_START_EXPOSURE) & self._imgComplete) == self._imgInProgress)
        #
        # if ccd == self.tracking:
        #     return (
        #         (self._status(udrv.CC_START_EXPOSURE) & self._trkComplete) == self._trkInProgress)
        return NotImplementedError()

    def startReadout(self, ccd, mode=0, window=None):
        '''
        Inform the camera that we will readout it. It is optional, but recommended to increase the readout speed.
        Library command: CC_START_READOUT
        See driver doc page 12.
        :param ccd:
        :param mode:
        :param window:
        :return:
        '''
        # if mode not in self.readoutModes[ccd].keys():
        #     raise ValueError("Invalid readout mode")
        #
        # # geometry checking
        # readoutMode = self.readoutModes[ccd][mode]
        #
        # window = (window or []) or readoutMode.getWindow()
        #
        # if (window[0] < 0 or window[0] > readoutMode.height):
        #     raise ValueError("Invalid window top point")
        #
        # if (window[1] < 0 or window[1] > readoutMode.width):
        #     raise ValueError("Invalid window left point")
        #
        # if (window[2] < 0 or window[2] > readoutMode.width):
        #     raise ValueError("Invalid window width")
        #
        # if (window[3] < 0 or window[3] > readoutMode.height):
        #     raise ValueError("Invalid window height")
        #
        # srp = udrv.StartReadoutParams()
        # srp.ccd = ccd
        # srp.readoutMode = mode
        # srp.top = window[0]
        # srp.left = window[1]
        # srp.width = window[2]
        # srp.height = window[3]
        #
        # return self._cmd(udrv.CC_START_READOUT, srp, None)
        return NotImplementedError()

    def endReadout(self, ccd):
        '''
        Called after readout process to prepare the camera to the idle state. Library command: CC_END_READOUT
        See driver doc page 15.
        :param ccd:
        :return:
        '''
        # erp = udrv.EndReadoutParams()
        # erp.ccd = ccd
        # return self._cmd(udrv.CC_END_READOUT, erp, None)
        return NotImplementedError()

    def readoutLine(self, ccd, mode=0, line=None):
        '''
        Reads out a CCD line. Library command: CC_READOUT_LINE
        See driver doc page 13.
        :param ccd:
        :param mode:
        :param line:
        :return:
        '''
        # if mode not in self.readoutModes[ccd].keys():
        #     raise ValueError("Invalid readout mode")
        #
        # # geometry check
        # readoutMode = self.readoutModes[ccd][mode]
        #
        # line = line or readoutMode.getLine()
        #
        # if (line[0] < 0 or line[0] > readoutMode.width):
        #     raise ValueError("Invalid pixel start")
        #
        # if (line[1] < 0 or line[1] > readoutMode.width):
        #     raise ValueError("Invalid pixel lenght")
        #
        # rolp = udrv.ReadoutLineParams()
        # rolp.ccd = ccd
        # rolp.readoutMode = mode
        # rolp.pixelStart = line[0]
        # rolp.pixelLength = line[1]
        #
        # # create a numpy array to hold the line
        # buff = numpy.zeros(line[1], numpy.uint16)
        #
        # self._cmd(udrv.CC_READOUT_LINE, rolp, buff)
        #
        # return buff
        return NotImplementedError()

    # query and info functions

    def queryUSB(self):
        '''
        See driver doc page 35.
        :return:
        '''
        #
        # usb = udrv.QueryUSBResults()
        #
        # self._cmd(udrv.CC_QUERY_USB, None, usb)
        #
        # cams = []
        #
        # for cam in usb.usbInfo:
        #     if cam.cameraFound:
        #         cams.append(cam.name)
        #
        # return cams
        return NotImplementedError()

    def queryDriverInfo(self):
        pass

    def queryCCDInfo(self):
        '''
        Updates CCD info for imaging and (if exists) tracking CCD. Library command: CC_READOUT_LINE
        See driver doc page 26.
        :return:
        '''
        #
        # infoImg = udrv.GetCCDInfoResults0()
        # infoTrk = udrv.GetCCDInfoResults0()
        #
        # gcip = udrv.GetCCDInfoParams()
        #
        # gcip.request = udrv.CCD_INFO_IMAGING
        # self._cmd(udrv.CC_GET_CCD_INFO, gcip, infoImg)
        #
        # gcip.request = udrv.CCD_INFO_TRACKING
        # self._cmd(udrv.CC_GET_CCD_INFO, gcip, infoTrk)
        #
        # self.cameraNames[self.imaging] = infoImg.name
        # self.cameraNames[self.tracking] = infoTrk.name
        #
        # # imaging ccd readout modes
        # for i in range(infoImg.readoutModes):
        #     mode = infoImg.readoutInfo[i]
        #     self.readoutModes[self.imaging][mode.mode] = SBIGReadoutMode(mode)
        #
        # for i in range(infoTrk.readoutModes):
        #     mode = infoTrk.readoutInfo[i]
        #     self.readoutModes[self.tracking][mode.mode] = SBIGReadoutMode(mode)
        #
        # return True
        return NotImplementedError()

    # temperature
    def setTemperature(self, regulation, setpoint, autofreeze=True):
        '''
        Sets the temperature regulation ON/OFF and its setpoint. Library command: CC_SET_TEMPERATURE_REGULATION2
        See driver doc page 18.
        :param regulation:
        :param setpoint:
        :param autofreeze:
        :return:
        '''
        # FIXME: As the exposure, this should be changed to the more recent SBIG API. The CC_SET_TEMPERATURE_REGULATION2
        # FIXME: already converts the units from A/D to Celsius.

        # strp = udrv.SetTemperatureRegulationParams()
        #
        # if regulation is True:
        #     strp.regulation = udrv.REGULATION_ON
        # else:
        #     strp.regulation = udrv.REGULATION_OFF
        #
        # strp.ccdSetpoint = TemperatureSetPoint.toAD(setpoint)
        #
        # self._cmd(udrv.CC_SET_TEMPERATURE_REGULATION, strp, None)
        #
        # # activate autofreeze if enabled
        # if autofreeze is True:
        #     strp = udrv.SetTemperatureRegulationParams()
        #     strp.regulation = udrv.REGULATION_ENABLE_AUTOFREEZE
        #     return self._cmd(udrv.CC_SET_TEMPERATURE_REGULATION, strp, None)
        #
        # return True
        return NotImplementedError()

    def getTemperature(self, ccd=True):
        '''
        Returns a tuple with (is cooling enabled, current cooling power (0-100), setpoint temperature, current ccd
        temperature). Library command: TEMP_STATUS_ADVANCED2
        See driver doc page 19.
        :param ccd:
        :return:
        '''
        # """
        # @returns: a tuple with (is cooling enabled, current cooling power (0-100), setpoint temperature, current ccd temperature)
        # """
        #
        # # USB based cameras have only one thermistor on the top of the CCD
        # # Ambient thermistor value will be always 25.0 oC
        #
        # # ccdSetPoint value will be always equal to ambient thermistor
        # # when regulation not enabled (not documented)
        #
        # qtsr = udrv.QueryTemperatureStatusResults()
        #
        # self._cmd(udrv.CC_QUERY_TEMPERATURE_STATUS, None, qtsr)
        #
        # return (qtsr.enabled,
        #         (qtsr.power / 255.0) * 100.0,
        #         TemperatureSetPoint.toDegrees(qtsr.ccdSetpoint, "ccd"),
        #         TemperatureSetPoint.toDegrees(qtsr.ccdThermistor, "ccd"))
        return NotImplementedError()


    def startFan(self):
        '''
        Starts Fan. Library command: ????
        See driver doc page 30.
        :return:
        '''
        # mcp = udrv.MiscellaneousControlParams()
        # mcp.fanEnable = 1
        # return self._cmd(udrv.CC_MISCELLANEOUS_CONTROL, mcp, None)

    def stopFan(self):
        '''
        Stops Fan. Library command: ????
        See driver doc page 30.
        :return:
        '''
        mcp = udrv.MiscellaneousControlParams()
        mcp.fanEnable = 0
        return self._cmd(udrv.CC_MISCELLANEOUS_CONTROL, mcp, None)

    def isFanning(self):
        '''
        Returns True if fan is ON and False otherwise. Library command: ????
        See driver doc page 19.
        :return:
        '''
        # status = self._status(udrv.CC_MISCELLANEOUS_CONTROL)
        # return bool(int(status & 0x8))
        return NotImplementedError()

    # filter wheel
    def getFilterPosition(self):
        '''
        Returns the actual Filter Wheel position. Library command: ????
        See driver doc page 22.
        :return:
        '''
        # cfwp = udrv.CFWParams()
        # cfwp.cfwModel = udrv.CFWSEL_CFW8
        # cfwp.cfwCommand = udrv.CFWC_QUERY
        #
        # cfwr = udrv.CFWResults()
        #
        # self._cmd(udrv.CC_CFW, cfwp, cfwr)
        #
        # return cfwr.cfwPosition
        return NotImplementedError()

    def setFilterPosition(self, position):
        '''
        Moves the filter wheel. Library command: CFWC_GOTO
        See driver doc page 23.
        :param position:
        :return:
        '''
        # cfwp = udrv.CFWParams()
        # cfwp.cfwModel = udrv.CFWSEL_CFW8
        # cfwp.cfwCommand = udrv.CFWC_GOTO
        # cfwp.cfwParam1 = position
        #
        # cfwr = udrv.CFWResults()
        #
        # return self._cmd(udrv.CC_CFW, cfwp, cfwr)
        return NotImplementedError()

    def getFilterStatus(self):
        '''
        Get the filter wheel status. Library command: ???
        See driver doc page ???.
        :return:
        '''
        # cfwp = udrv.CFWParams()
        # cfwp.cfwModel = udrv.CFWSEL_CFW8
        # cfwp.cfwCommand = udrv.CFWC_QUERY
        #
        # cfwr = udrv.CFWResults()
        #
        # self._cmd(udrv.CC_CFW, cfwp, cfwr)
        #
        # return cfwr.cfwStatus
        return NotImplementedError()

    # low-level commands

    def _cmd(self, cmd, cin, cout):

        err = udrv.SBIGUnivDrvCommand(cmd, cin, cout)

        if err == udrv.CE_NO_ERROR:
            return True
        else:
            #log.error('Got a problem here! Dumping error params')
            gesp = udrv.GetErrorStringParams()
            gesr = udrv.GetErrorStringResults()

            gesp.errorNo = err

            udrv.SBIGUnivDrvCommand(udrv.CC_GET_ERROR_STRING, gesp, gesr)

            # dumpObj(gesp)
            # dumpObj(gesr)

            #log.warning('You may need to restart the SBIGDriver!')

            raise SBIGException(err, gesr.errorString)

    def _status(self, cmd):

        qcsp = udrv.QueryCommandStatusParams()
        qcsr = udrv.QueryCommandStatusResults()
        qcsp.command = cmd

        if not self._cmd(udrv.CC_QUERY_COMMAND_STATUS, qcsp, qcsr):
            return False

        return qcsr.status

if __name__ == '__main__':
    print 'Testing sbigdrv...'
    s = SBIGDrv()
    #TODO: ...