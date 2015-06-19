# CTYPES wrapper for SBIGUDrv library
# SBIGUDrv library documentation can be found at: http://archive.sbig.com/pdffiles/SBIGUDrv.pdf

import math

import numpy

import logging
log = logging.getLogger(__name__)

from chimera.core.exceptions import ChimeraException
from chimera.interfaces.camera import ReadoutMode

import ctypes
import os
import sys

from ctypes import Structure, c_ushort, c_ulong, POINTER, c_char, byref, c_double

import sbig_structures, sbig_constants



class GetErrorStringResults(Structure):
    _fields_ = [('errorString', c_char * 64)]


class GetErrorStringParams(Structure):
    _fields_ = [('errorNo', ctypes.c_int)]

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
        pass


class SBIGDrv(object):


    def __init__(self):
        if sys.platform.startswith('linux'):
            self._driver = ctypes.CDLL('libsbigudrv.so')
        elif sys.platform.startswith('win'):
            import platform

            bits, linkage = platform.architecture()
            if bits.beginswith('32'):
                self._driver = ctypes.windll.LoadLibrary('sbigudrv.dll')
            else:
                print 'Invalid Python distribution. Should be 32bits.'

    def openDriver(self):
        '''
        Opens SBIG driver. Library command: CC_OPEN_DRIVER.
        See driver doc page 7.
        :return:
        '''

        try:
            return self._cmd(sbig_constants.PAR_COMMAND.CC_OPEN_DRIVER, None, None)


        except SBIGException, e:
            if e.code == sbig_constants.PAR_ERROR.CE_DRIVER_NOT_CLOSED:
                #   driver already open (are you trying to use the tracking ccd?)
                return True
            else:
                raise

    def closeDriver(self):
        '''
        Opens SBIG driver. Library command: CC_CLOSE_DRIVER.
        See driver doc page 7.
        :return:
        '''

        cdp = None

        cdr = None

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cdp), POINTER(cdr)]

        try:

            ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_CLOSE_DRIVER, None, None)

            if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
                return True
            else:
                raise self._error(ret)

        except SBIGException, e:
            if e.code == sbig_constants.CE_DRIVER_NOT_OPEN:
                # driver not open, so there is no point in raising an exception.
                return True
            else:
                raise

    def openDevice(self, device):
        '''
        Opens SBIG camera device. Library command: CC_OPEN_DEVICE.
        See driver doc page 7.
        :param device: TODO: docme
        :return:
        '''
        # FIXME: USB and ETHERNET?

        odp = sbig_structures.OpenDeviceParams

        odr = None

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(odp), POINTER(odr)]

        try:

            odp = odp(deviceType = sbig_constants.SBIG_DEVICE_TYPE.DEV_USB)

            ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_OPEN_DEVICE, byref(odp), None)

            if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
                return True
            else:
                raise self._error(ret)

        except SBIGException, e:
            if e.code == sbig_constants.CE_DEVICE_NOT_CLOSED:
                # device already open (are you trying to use the tracking ccd?)
                return True
            else:
                raise

    def closeDevice(self):
        '''
        Closes SBIG camera device. Library command: CC_CLOSE_DEVICE.
        See driver doc page 7.
        :return:
        '''
        # return self._cmd(sbig_constants.CC_CLOSE_DEVICE, None, None)

        cdp = None

        cdr = None

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cdp), POINTER(cdr)]

        try:

            ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_CLOSE_DEVICE, None, None)

            if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
                return True
            else:
                raise self._error(ret)

        except SBIGException, e:
            if e.code == sbig_constants.CE_DEVICE_NOT_OPEN:
                # device not open, so there is no point in raising an exception.
                return True
            else:
                raise

    def establishLink(self):
        '''
        Establishes a communications link with the camera. Library command: CC_ESTABLISH_LINK.
        See driver doc page 26.
        :return:
        '''

        elp = sbig_structures.EstablishLinkParams
        elr = sbig_structures.EstablishLinkResults

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(elp), POINTER(elr)]

        elp = elp(sbigUseOnly=0)
        elr = elr()

        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_ESTABLISH_LINK, byref(elp), byref(elr))

        #print ret, elr.cameraType


        return elr.cameraType


        # elp = sbig_constants.EstablishLinkParams()
        # elr = sbig_constants.EstablishLinkResults()
        # err = self._cmd(sbig_constants.CC_ESTABLISH_LINK, elp, elr)
        #
        # if not err:
        #     self.queryCCDInfo()
        #
        # return err

    def isLinked(self):
        '''
        Returns True if camera link is up. Otherwise, returns False. Library command: CC_GET_LINK_STATUS.
        See driver doc page 32.
        :return:
        '''
        # # FIXME: ask SBIG to get a better CC_GET_LINK_STATUS.. this one it too bogus

        glsp = None

        glsr = sbig_structures.GetLinkStatusResults

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(glsp), POINTER(glsr)]

        glsr = glsr()

        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_LINK_STATUS, None, byref(glsr))

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return bool(glsr.linkEstablished)
        else:
            raise self._error(ret)




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

        # sep = sbig_constants.StartExposureParams()
        #
        # sep.ccd = ccd
        # sep.openShutter = shutter
        # sep.abgState = 0
        # sep.exposureTime = exp_time
        #
        # return self._cmd(sbig_constants.CC_START_EXPOSURE, sep, None)
        return NotImplementedError()

    def endExposure(self, ccd):
        '''
        End Exposure command is used after the integration is complete to prepare the CCD for readout or to terminate an
        exposure prematurely. Library command: CC_END_EXPOSURE
        See driver doc page 12.
        :param ccd:
        :return:
        '''
        # eep = sbig_constants.EndExposureParams()
        # eep.ccd = ccd
        #
        # return self._cmd(sbig_constants.CC_END_EXPOSURE, eep, None)
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
        #         (self._status(sbig_constants.CC_START_EXPOSURE) & self._imgComplete) == self._imgInProgress)
        #
        # if ccd == self.tracking:
        #     return (
        #         (self._status(sbig_constants.CC_START_EXPOSURE) & self._trkComplete) == self._trkInProgress)
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
        # srp = sbig_constants.StartReadoutParams()
        # srp.ccd = ccd
        # srp.readoutMode = mode
        # srp.top = window[0]
        # srp.left = window[1]
        # srp.width = window[2]
        # srp.height = window[3]
        #
        # return self._cmd(sbig_constants.CC_START_READOUT, srp, None)
        return NotImplementedError()

    def endReadout(self, ccd):
        '''
        Called after readout process to prepare the camera to the idle state. Library command: CC_END_READOUT
        See driver doc page 15.
        :param ccd:
        :return:
        '''
        # erp = sbig_constants.EndReadoutParams()
        # erp.ccd = ccd
        # return self._cmd(sbig_constants.CC_END_READOUT, erp, None)
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
        # rolp = sbig_constants.ReadoutLineParams()
        # rolp.ccd = ccd
        # rolp.readoutMode = mode
        # rolp.pixelStart = line[0]
        # rolp.pixelLength = line[1]
        #
        # # create a numpy array to hold the line
        # buff = numpy.zeros(line[1], numpy.uint16)
        #
        # self._cmd(sbig_constants.CC_READOUT_LINE, rolp, buff)
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
        # usb = sbig_constants.QueryUSBResults()
        #
        # self._cmd(sbig_constants.CC_QUERY_USB, None, usb)
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
        '''
        The Get Driver Info command is used to determine the version and capabilities of the DLL/Driver.
        Library command: CC_GET_DRIVER_INFO
        See driver doc page 8.
        :return: (version, name, maxRequest)
        '''

        gdip = sbig_structures.GetDriverInfoParams

        gdir = sbig_structures.GetDriverInfoResults0

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(gdip), POINTER(gdir)]

        gdip = gdip(request=2)
        gdir = gdir()

        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_DRIVER_INFO, byref(gdip), byref(gdir))

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return gdir.version, gdir.name, gdir.maxRequest
        else:
            raise self._error(ret)


    def queryCCDInfoImg(self):

        gcip = sbig_structures.GetCCDInfoParams
        info_img = sbig_structures.GetCCDInfoResults0

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(gcip), POINTER(info_img)]

        gcip = gcip(request=sbig_constants.CCD_INFO_REQUEST.CCD_INFO_IMAGING)
        info_img = info_img()

        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_CCD_INFO, byref(gcip), byref(info_img))

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return info_img
        else:
            raise self._error(ret)

    def queryCCDInfoTrk(self):

        gcip = sbig_structures.GetCCDInfoParams
        info_trk = sbig_structures.GetCCDInfoResults0

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(gcip), POINTER(info_trk)]

        gcip = gcip(request=sbig_constants.CCD_INFO_REQUEST.CCD_INFO_TRACKING)
        info_trk = info_trk()

        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_CCD_INFO, byref(gcip), byref(info_trk))

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return info_trk
        else:
            raise self._error(ret)


    def queryCCDInfo(self):
        '''
        Updates CCD info for imaging and (if exists) tracking CCD. Library command: CCD_INFO_IMAGING
        See driver doc page 26.
        :return:
        '''

        info_img = self.queryCCDInfoImg()
        info_trk = self.queryCCDInfoTrk()

        self.cameraNames[sbig_constants.CCD_REQUEST.CCD_IMAGING]  = info_img.name
        self.cameraNames[sbig_constants.CCD_REQUEST.CCD_TRACKING] = info_trk.name

        #
        # # imaging ccd readout modes
        # for i in range(info_img.readoutModes):
        #     mode = info_img.readoutInfo[i]
        #     self.readoutModes[sbig_constants.CCD_REQUEST.CCD_IMAGING][mode.mode] = SBIGReadoutMode(mode)
        #
        # for i in range(info_trk.readoutModes):
        #     mode = info_trk.readoutInfo[i]
        #     self.readoutModes[sbig_constants.CCD_REQUEST.CCD_TRACKING][mode.mode] = SBIGReadoutMode(mode)

        return True

    def queryCCDInfoOld(self):
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
        # gcip.request = sbig_constants.CCD_INFO_IMAGING
        # self._cmd(sbig_constants.CC_GET_CCD_INFO, gcip, infoImg)
        #
        # gcip.request = sbig_constants.CCD_INFO_TRACKING
        # self._cmd(sbig_constants.CC_GET_CCD_INFO, gcip, infoTrk)
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

        tempRegulation = sbig_constants.TEMPERATURE_REGULATION.REGULATION_ON

        if regulation is False:
            tempRegulation = sbig_constants.TEMPERATURE_REGULATION.REGULATION_OFF

        strp = sbig_structures.SetTemperatureRegulationParams2

        str = None

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(strp), POINTER(str)]

        strp = strp(regulation=tempRegulation, ccdSetpoint=setpoint)

        # First call must set temperature parameters
        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_SET_TEMPERATURE_REGULATION, byref(strp), None)

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR and autofreeze is False:
            return True
        elif ret == sbig_constants.PAR_ERROR.CE_NO_ERROR and autofreeze is True:

            strp = sbig_structures.SetTemperatureRegulationParams2

            str = None

            self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(strp), POINTER(str)]

            strp = strp(regulation=sbig_constants.TEMPERATURE_REGULATION.REGULATION_ENABLE_AUTOFREEZE)

            # Second call sets the Freezing
            ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_SET_TEMPERATURE_REGULATION, byref(strp), None)

            if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
                return True
            else:
                raise self._error(ret)

        else:
            raise self._error(ret)


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

        # Function parameter

        qsp = sbig_structures.QueryTemperatureStatusParams
        qtsr = sbig_structures.QueryTemperatureStatusResults2

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(qsp), POINTER(qtsr)]

        qsp = qsp(request=sbig_constants.QUERY_TEMP_STATUS_REQUEST.TEMP_STATUS_ADVANCED2)

        qtsr = qtsr()

        ret = self._driver.SBIGUnivDrvCommand(
            sbig_constants.PAR_COMMAND.CC_QUERY_TEMPERATURE_STATUS, byref(qsp), byref(qtsr))

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return (qtsr.fanEnabled,
                    (qtsr.fanPower / 255.0) * 100.0,
                    qtsr.ccdSetpoint,
                    qtsr.imagingCCDTemperature)
        else:
            raise self._error(ret)





    def startFan(self):
        '''
        Starts Fan. Library command: MiscellaneousControl
        See driver doc page 30.
        :return:
        '''

        mcp = sbig_structures.MiscellaneousControlParams

        mcr = None

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(mcp), POINTER(mcr)]

        mcp = mcp(fanEnable=True)

        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_MISCELLANEOUS_CONTROL, byref(mcp), None)

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return True
        else:
            raise self._error(ret)


    def stopFan(self):
        '''
        Stops Fan. Library command: MiscellaneousControl
        See driver doc page 30.
        :return:
        '''
        mcp = sbig_structures.MiscellaneousControlParams

        mcr = None

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(mcp), POINTER(mcr)]

        mcp = mcp(fanEnable=False)

        ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_MISCELLANEOUS_CONTROL, byref(mcp), None)

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return True
        else:
            raise self._error(ret)

    def isFanning(self):
        '''
        Returns True if fan is ON and False otherwise. Library command: ????
        See driver doc page 19.
        :return:
        '''

        qsp = sbig_structures.QueryTemperatureStatusParams
        qtsr = sbig_structures.QueryTemperatureStatusResults2

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(qsp), POINTER(qtsr)]

        qsp = qsp(request=sbig_constants.QUERY_TEMP_STATUS_REQUEST.TEMP_STATUS_ADVANCED2)

        qtsr = qtsr()

        ret = self._driver.SBIGUnivDrvCommand(
            sbig_constants.PAR_COMMAND.CC_QUERY_TEMPERATURE_STATUS, byref(qsp), byref(qtsr))

        if ret == sbig_constants.PAR_ERROR.CE_NO_ERROR:
            return True if qtsr.fanEnabled == 1 else False
        else:
            raise self._error(ret)

    # filter wheel
    def getFilterPosition(self):
        '''
        Returns the actual Filter Wheel position. Library command: ????
        See driver doc page 22.
        :return:
        '''
        # cfwp = udrv.CFWParams()
        # cfwp.cfwModel = sbig_constants.CFWSEL_CFW8
        # cfwp.cfwCommand = sbig_constants.CFWC_QUERY
        #
        # cfwr = udrv.CFWResults()
        #
        # self._cmd(sbig_constants.CC_CFW, cfwp, cfwr)
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


    def _cmd(self, ccc, cin, cout):

        #self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]

        if cin is not None:
            cin = cin()
            cin = byref(cin)
        if cout is not None:
            cout = cout()
            cout = byref(cout)

        err = self._driver.SBIGUnivDrvCommand(ccc, cin, cout)

        if err == 0:
            return True

        if ccc == sbig_constants.PAR_COMMAND.CC_OPEN_DRIVER and err == sbig_constants.PAR_ERROR.CE_DRIVER_NOT_CLOSED:
            print 'Driver already open'
            return True
        elif ccc == sbig_constants.PAR_COMMAND.CC_OPEN_DEVICE and err == sbig_constants.PAR_ERROR.CE_DEVICE_NOT_CLOSED:
            print 'Device already open'
            return True
        elif err:
            cin = GetErrorStringParams
            cout = GetErrorStringResults
            self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
            cin = cin(errorNo=err)
            cout = cout()
            ret = self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_ERROR_STRING, byref(cin), byref(cout))
            return ret, cout.errorString

    def _error(self, errorNo):

        #log.error('Got a problem here! Dumping error params')
        gesp = sbig_structures.GetErrorStringParams
        gesr = sbig_structures.GetErrorStringResults

        self._driver.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(gesp), POINTER(gesr)]

        gesp = gesp(errorNo=errorNo)
        gesr = gesr()


        self._driver.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_ERROR_STRING, byref(gesp), byref(gesr))


        # dumpObj(gesp)
        # dumpObj(gesr)

        #log.warning('You may need to restart the SBIGDriver!')

        raise SBIGException(errorNo, gesr.errorString)

    def _cmd_OLD(self, cmd, cin, cout):

        err = self._driver.SBIGUnivDrvCommand(cmd, cin, cout)

        if err == sbig_constants.CE_NO_ERROR:
            return True
        else:
            #log.error('Got a problem here! Dumping error params')
            gesp = self._driver.GetErrorStringParams()
            gesr = self._driver.GetErrorStringResults()

            gesp.errorNo = err

            self._driver.SBIGUnivDrvCommand(sbig_constants.CC_GET_ERROR_STRING, gesp, gesr)

            # dumpObj(gesp)
            # dumpObj(gesr)

            #log.warning('You may need to restart the SBIGDriver!')

            raise SBIGException(err, gesr.errorString)

    def _status(self, cmd):

        qcsp = self._driver.QueryCommandStatusParams()
        qcsr = self._driver.QueryCommandStatusResults()
        qcsp.command = cmd

        if not self._cmd(sbig_constants.CC_QUERY_COMMAND_STATUS, qcsp, qcsr):
            return False

        return qcsr.status

if __name__ == '__main__':
    sbig = SBIGDrv()


    try:
        print 'Testing sbigdrv...'

        print "openDriver = " + str(sbig.openDriver())

        print "queryDriverInfo = (version, name, maxRequest) -> " + str(tuple(sbig.queryDriverInfo()))

        print "openDevice = " + str(sbig.openDevice(1))

        print "establishLink = " + str(sbig.establishLink())

        # fanEnabled, fanPower, ccdSetpoint, imagingCCDTemperature
        print "getTemperature = (fanEnabled, fanPower, ccdSetpoint, imagingCCDTemperature) -> " + str(tuple(sbig.getTemperature(ccd=True))) #OK

        print "startFan = " + str(sbig.startFan()) #OK

        print "isFanning = " + str(sbig.isFanning()) #OK

        print "stopFan = " + str(sbig.stopFan()) #OK

        print "setTemperature = " + str(sbig.setTemperature(regulation=True, setpoint=-15, autofreeze=True)) #OK

        print "isLinked = " + str(sbig.isLinked())

        sbig.queryCCDInfo() #Not tested

        print "imaging = " + sbig.cameraNames[sbig.imaging]
        print "tracking = " + sbig.cameraNames[sbig.tracking]

        #for i in range(sbig.readoutModes):
        #    mode = info_img.readoutInfo[i]
        #    self.readoutModes[sbig_constants.CCD_REQUEST.CCD_IMAGING][mode.mode] = SBIGReadoutMode(mode)

        sbig.closeDevice() # Not tested
        sbig.closeDriver() # Not tested

    except SBIGException, e:
        print "Exception: " + e.message

'''
On the works
============
queryCCDInfo

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
queryDriverInfo
setTemperature

Implemented but not tested
==========================

Not Implemented Yet
===================

startExposure
endExposure
exposing
startReadout
endReadout
readoutLine
queryUSB
getFilterPosition
setFilterPosition
getFilterStatus

'''