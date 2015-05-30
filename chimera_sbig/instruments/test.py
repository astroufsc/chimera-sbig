import ctypes
import time

import numpy as np

import sbig_constants

udrv = ctypes.CDLL('libsbigudrv.so')

from ctypes import Structure, c_ushort, c_ulong, POINTER, c_char, byref, c_double


def cmd(ccc, cin, cout):
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    if cin is not None:
        cin = cin()
        cin = byref(cin)
    if cout is not None:
        cout = cout()
        cout = byref(cout)
    err = udrv.SBIGUnivDrvCommand(ccc, cin, cout)
    print 'err', err
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
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
        cin = cin(errorNo=err)
        cout = cout()
        ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_ERROR_STRING, byref(cin), byref(cout))
        return ret, cout.errorString


print 'Open Driver'
ret = cmd(sbig_constants.PAR_COMMAND.CC_OPEN_DRIVER, None, None)
print ret

print 'Test get Errors. This should return Device Not Found.'


class GetErrorStringResults(Structure):
    _fields_ = [('errorString', c_char * 64)]


class GetErrorStringParams(Structure):
    _fields_ = [('errorNo', ctypes.c_int)]


cin = GetErrorStringParams
cout = GetErrorStringResults
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(errorNo=27)
cout = cout()
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_ERROR_STRING, byref(cin), byref(cout))
print cout.errorString

print 'Open Device'


class OpenDeviceParams(Structure):
    _fields_ = [('deviceType', c_ushort),  # SBIG_DEVICE_TYPE, specifies LPT, Ethernet, etc
                ('lptBaseAddress', c_ushort),  # DEV_LPTN: Windows 9x Only, Win NT uses deviceSelect
                ('ipAddress', c_ulong)]


cin = OpenDeviceParams
cout = None
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(deviceType=sbig_constants.SBIG_DEVICE_TYPE.DEV_USB)
# ip = '150.162.131.92'
# ip = ip.split('.')
# ip_hex = hex(int(ip[0])).split('x')[1].rjust(2, '0') + hex(int(ip[1])).split('x')[1].rjust(2, '0') + \
#          hex(int(ip[2])).split('x')[1].rjust(2, '0') + hex(int(ip[3])).split('x')[1].rjust(2, '0')
# cin = cin(deviceType=sbig_constants.SBIG_DEVICE_TYPE.DEV_ETH, ipAddress=long(ip_hex, 16))
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_OPEN_DEVICE, byref(cin), cout)
print ret

print 'Establish Link'


class EstablishLinkParams(Structure):
    _fields_ = [('sbigUseOnly', c_ushort)]


class EstablishLinkResults(Structure):
    _fields_ = [('cameraType', c_ushort)]


cin = EstablishLinkParams
cout = EstablishLinkResults
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(sbigUseOnly=0)
cout = cout()
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_ESTABLISH_LINK, byref(cin), byref(cout))
print ret, cout.cameraType

print 'Get Link Status'


class GetLinkStatusResults(Structure):
    _fields_ = [('linkEstablished', c_ushort),
                ('baseAddress', c_ushort),
                ('cameraType', c_ushort),  # CAMERA_TYPE
                ('comTotal', c_ulong),
                ('comFailed', c_ulong)]


cin = None
cout = GetLinkStatusResults
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cout = cout()
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_LINK_STATUS, cin, byref(cout))
print ret, cout.linkEstablished, cout.baseAddress, cout.cameraType, cout.comTotal, cout.comFailed

print 'Get Temperature'


class QueryTemperatureStatusParams(Structure):
    _fields_ = [('request', c_ushort)]


class QueryTemperatureStatusResults2(Structure):
    _fields_ = [('coolingEnabled', c_ushort),
                ('fanEnabled', c_ushort),
                ('ccdSetpoint', c_double),
                ('imagingCCDTemperature', c_double),
                ('trackingCCDTemperature', c_double),
                ('externalTrackingCCDTemperature', c_double),
                ('ambientTemperature', c_double),
                ('imagingCCDPower', c_double),
                ('trackingCCDPower', c_double),
                ('externalTrackingCCDPower', c_double),
                ('heatsinkTemperature', c_double),
                ('fanPower', c_double),
                ('fanSpeed', c_double),
                ('trackingCCDSetpoint', c_double)]


cin = QueryTemperatureStatusParams
cout = QueryTemperatureStatusResults2
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(request=sbig_constants.QUERY_TEMP_STATUS_REQUEST.TEMP_STATUS_ADVANCED2)
cout = cout()
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_QUERY_TEMPERATURE_STATUS, byref(cin), byref(cout))
print ret, cout.coolingEnabled, cout.fanEnabled, cout.ccdSetpoint, cout.imagingCCDTemperature, \
    cout.trackingCCDTemperature, cout.externalTrackingCCDTemperature, cout.ambientTemperature, cout.imagingCCDPower, \
    cout.trackingCCDPower, cout.externalTrackingCCDPower, cout.heatsinkTemperature, cout.fanPower, cout.fanSpeed, \
    cout.trackingCCDSetpoint

print 'CCD Info'

for ccd in sbig_constants.CCD_INFO_REQUEST.CCD_INFO_IMAGING, \
           sbig_constants.CCD_INFO_REQUEST.CCD_INFO_TRACKING:

    class GetCCDInfoParams(Structure):
        _fields_ = [('request', c_ushort)]  # CCD_INFO_REQUEST

    class ReadOut_Info(Structure):
        _fields_ = [('mode', c_ushort),
                    ('width', c_ushort),
                    ('height', c_ushort),
                    ('gain', c_ushort),
                    ('pixel_width', c_ulong),
                    ('pixel_height', c_ulong)]

    class GetCCDInfoResults0(Structure):
        _fields_ = [('firmwareVersion', c_ushort),
                    ('cameraType', c_ushort),  # CAMERA_TYPE
                    ('name', c_char * 64),
                    ('readoutModes', c_ushort),
                    ('readoutInfo', ReadOut_Info * 20)]

    cin = ReadOut_Info
    cout = GetCCDInfoResults0
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    cin = cin(request=ccd)
    cout = cout()
    ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_GET_CCD_INFO, byref(cin), byref(cout))
    print ret, cout.firmwareVersion, cout.cameraType, cout.name, cout.readoutModes
    for i_mode in range(cout.readoutModes):
        print cout.readoutInfo[i_mode].mode, cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].height, \
            cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].gain, cout.readoutInfo[i_mode].pixel_width, \
            cout.readoutInfo[i_mode].pixel_height
        if ccd == sbig_constants.CCD_INFO_REQUEST.CCD_INFO_IMAGING and i_mode == 0:
            readout_mode = [
                cout.readoutInfo[i_mode].mode, cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].height,
                cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].gain, cout.readoutInfo[i_mode].pixel_width,
                cout.readoutInfo[i_mode].pixel_height]  # STORE FIRST MODE OF IMAGING CCD FOR EXPOSURE TEST

print 'GRAB IMAGE - Start Exposure'


class StartExposureParams2(Structure):
    _fields_ = [('ccd', c_ushort),  # CCD_REQUEST
                ('exposureTime', c_ulong),
                ('abgState', c_ushort),  # ABG_STATE7
                ('openShutter', c_ushort),  # SHUTTER_COMMAND
                ('readoutMode', c_ushort),
                ('top', c_ushort),
                ('left', c_ushort),
                ('height', c_ushort),
                ('width', c_ushort)]


cin = StartExposureParams2
cout = None
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(ccd=sbig_constants.CCD_REQUEST.CCD_IMAGING, exposureTime=60 * 100,  # 60 seconds integration
          openShutter=sbig_constants.SHUTTER_COMMAND.SC_OPEN_SHUTTER, readoutMode=0, top=0, left=0,
          height=readout_mode[2], width=readout_mode[1])
# TODO: 1 - Do I need to tell the camera always the height and width?
# TODO: 2 - Check the minimum exposure times. Like sbig_constants.MIN_ST7_EXPOSURE for ST7
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_START_EXPOSURE2, byref(cin), cout)

print 'ret', ret

print 'GRAB IMAGE - Query Command Status'

t0 = time.time()
status = 2
while status == 2:
    class QueryCommandStatusParams(Structure):
        _fields_ = [('command', c_ushort)]

    class QueryCommandStatusResults(Structure):
        _fields_ = [('status', c_ushort)]

    cin = QueryCommandStatusParams
    cout = QueryCommandStatusResults
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    cin = cin(command=sbig_constants.PAR_COMMAND.CC_START_EXPOSURE2)
    cout = cout()
    ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_QUERY_COMMAND_STATUS, byref(cin), byref(cout))
    status = cout.status
    print 'status: %3.2f sec - %s' % (time.time() - t0, status)
    time.sleep(.5)

print 'GRAB IMAGE - End Exposure'


class EndExposureParams(Structure):
    _fields_ = [('ccd', c_ushort)]


cin = EndExposureParams
cout = None
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(ccd=sbig_constants.CCD_REQUEST.CCD_IMAGING)
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_END_EXPOSURE, byref(cin), cout)

print 'GRAB IMAGE - Start Readout'


class StartReadoutParams(Structure):
    _fields_ = [('ccd', c_ushort),  # CCD_REQUEST
                ('readoutMode', c_ushort),
                ('top', c_ushort),
                ('left', c_ushort),
                ('height', c_ushort),
                ('width', c_ushort)]


cin = StartReadoutParams
cout = None
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(command=sbig_constants.PAR_COMMAND.CC_START_EXPOSURE2, readout_mode=0, top=0, left=0, height=readout_mode[2],
          width=readout_mode[1])
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_START_READOUT, byref(cin), cout)
print 'ret', ret

print sbig_constants.PAR_COMMAND.CC_START_READOUT

print 'GRAB IMAGE - Readout lines'

img = np.zeros((readout_mode[2], readout_mode[1]))  # TODO: Check -- Height x Width?

for i_line in range(readout_mode[2]):  # CCD number of lines is the height.
    class ReadoutLineParams(Structure):
        _fields_ = [('ccd', c_ushort),  # CCD_REQUEST
                    ('readoutMode', c_ushort),
                    ('pixelStart', c_ushort),
                    ('pixelLength', c_ushort)]

    cin = ReadoutLineParams
    cout = c_ushort * readout_mode[1]  # Array of width pixels
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    cin = cin(ccd=sbig_constants.CCD_REQUEST.CCD_IMAGING, readoutMode=0, pixelStart=0, pixelLength=readout_mode[1])
    cout = cout()
    ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_READOUT_LINE, byref(cin), byref(cout))
    img[i_line] = cout

print 'GRAB IMAGE - End Readout'


class EndReadoutParams(Structure):
    _fields_ = [('ccd', c_ushort)]


cin = EndReadoutParams
cout = None
udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
cin = cin(ccd=sbig_constants.CCD_REQUEST.CCD_IMAGING)
ret = udrv.SBIGUnivDrvCommand(sbig_constants.PAR_COMMAND.CC_END_READOUT, byref(cin), cout)
print 'ret', ret

print 'Close device'
cmd(sbig_constants.PAR_COMMAND.CC_CLOSE_DEVICE, None, None)

print 'Close driver'
cmd(sbig_constants.PAR_COMMAND.CC_CLOSE_DRIVER, None, None)

print 'Adios'
