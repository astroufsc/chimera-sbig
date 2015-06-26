from ctypes import Structure, c_ushort, c_ulong, c_double, c_byte, c_char_p, c_char, c_ubyte


class OpenDeviceParams(Structure):
    _fields_ = [
        ('deviceType', c_ushort),  # SBIG_DEVICE_TYPE, specifies LPT, Ethernet, etc
        ('lptBaseAddress', c_ushort),  # DEV_LPTN: Windows 9x Only, Win NT uses deviceSelect
        ('ipAddress', c_ulong),  # DEV_ETH:  Ethernet address
    ]


class StartExposureParams(Structure):
    _fields_ = [('ccd', c_ushort),  # CCD_REQUEST
                ('exposureTime', c_ulong),
                ('abgState', c_ushort),  # ABG_STATE7
                ('openShutter', c_ushort),  # SHUTTER_COMMAND
                ]


class StartExposureParams2(Structure):
    _fields_ = [('ccd', c_ushort),  # CCD_REQUEST
                ('exposureTime', c_ulong),
                ('abgState', c_ushort),  # ABG_STATE7
                ('openShutter', c_ushort),  # SHUTTER_COMMAND
                ('readoutMode', c_ushort),
                ('top', c_ushort),
                ('left', c_ushort),
                ('height', c_ushort),
                ('width', c_ushort),
                ]


class QueryTemperatureStatusParams(Structure):
    _fields_ = [('request', c_ushort),  # TEMP_STATUS_REQUEST
                ]

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
                ('trackingCCDSetpoint', c_double),
                ]

class EstablishLinkParams(Structure):
    _fields_ = [('sbigUseOnly', c_ushort)]


class EstablishLinkResults(Structure):
    _fields_ = [('cameraType', c_ushort)]

class GetErrorStringParams(Structure):
    _fields_ = [('errorNo', c_ushort)]

class GetErrorStringResults(Structure):
    _fields_ = [('errorString', c_char*64)]
    # _fields_ = [('errorString',  c_char_p)]


class GetLinkStatusResults(Structure):
    _fields_ = [
        ('linkEstablished', c_ushort),
        ('baseAddress', c_ushort),
        ('cameraType', c_ushort),  # CAMERA_TYPE
        ('comTotal', c_ulong),
        ('comFailed', c_ulong)]


class MiscellaneousControlParams(Structure):
    _fields_ = [
        ('fanEnable', c_ushort),
        ('shutterCommand', c_ushort),  # SHUTTER_COMMAND
        ('ledState', c_ushort)  # LED_STATE
    ]


class GetDriverInfoParams(Structure):
    _fields_ = [
        ('request', c_ushort)  # DRIVER_REQUEST
    ]


class GetDriverInfoResults0(Structure):
    _fields_ = [
        ('version', c_ushort),
        ('name', c_char*64),
        ('maxRequest', c_ushort)
    ]


class SetTemperatureRegulationParams2(Structure):
    _fields_ = [
        ('regulation', c_ushort),  # TEMPERATURE_REGULATION
        ('ccdSetpoint', c_double)
    ]


class GetCCDInfoParams(Structure):
    _fields_ = [
        ('request', c_ushort)  # CCD_INFO_REQUEST
    ]


class READOUT_INFO(Structure):
    _fields_ = [
        ('mode', c_ushort),
        ('width', c_ushort),
        ('height', c_ushort),
        ('gain', c_ushort),
        ('pixel_width', c_ulong),
        ('pixel_height', c_ulong)
    ]


class GetCCDInfoResults0(Structure):
    _fields_ = [
        ('firmwareVersion', c_ushort),
        ('cameraType', c_ushort),  # CAMERA_TYPE
        ('name', c_char*64),
        ('readoutModes', c_ushort),
        ('readoutInfo', READOUT_INFO*20)
    ]

class CFWParams(Structure):
    _fields_ = [
        ('cfwModel', c_ushort),  #  CFW_MODEL_SELECT
        ('cfwCommand', c_ushort),  #  CFW_COMMAND
        ('cfwParam1', c_ulong),
        ('cfwParam2', c_ulong),
        ('outLength', c_ushort),
        ('outPtr', c_char_p),
        ('inLength', c_ushort),
        ('inPtr', c_char_p)
    ]


class CFWResults(Structure):
    _fields_ = [
        ('cfwModel', c_ushort),  #  CFW_MODEL_SELECT
        ('cfwPosition', c_ushort),  #  CFW_POSITION
        ('cfwStatus', c_ushort),  #  CFW_STATUS
        ('cfwError', c_ushort),  #  CFW_ERROR
        ('cfwResult1', c_ulong),
        ('cfwResult2', c_ulong)
    ]


class QUERY_USB_INFO(Structure):
    _fields_ = [
        ('cameraFound', c_ushort),
        ('cameraType', c_ushort),
        ('name', c_char*64),
        ('serialNumber', c_byte*10)
    ]

class QueryUSBResults(Structure):
    _fields_ = [
        ('camerasFound', c_ushort),
        ('QUERY_USB_INFO', QUERY_USB_INFO*4)
    ]


class StartExposureParams(Structure):
    _fields_ = [
        ('ccd', c_ushort),  # CCD_REQUEST
        ('exposureTime', c_ulong),
        ('abgState', c_ushort),  # ABG_STATE7
        ('openShutter', c_ushort)  # SHUTTER_COMMAND
    ]


class StartExposureParams2(Structure):
    _fields_ = [
        ('ccd', c_ushort),  # CCD_REQUEST
        ('exposureTime', c_ulong),
        ('abgState', c_ushort),  # ABG_STATE7
        ('openShutter', c_ushort),  # SHUTTER_COMMAND
        ('readoutMode', c_ushort),
        ('top', c_ushort),
        ('left', c_ushort),
        ('height', c_ushort),
        ('width', c_ushort)
    ]


class EndExposureParams(Structure):
    _fields_ = [
        ('ccd', c_ushort)  # CCD_REQUEST
    ]


class EndReadoutParams(Structure):
    _fields_ = [
        ('ccd', c_ushort),  # CCD_REQUEST
    ]


class StartReadoutParams(Structure):
    _fields_ = [
        ('ccd', c_ushort),  # CCD_REQUEST
        ('readoutMode', c_ushort),
        ('top', c_ushort),
        ('left', c_ushort),
        ('height', c_ushort),
        ('width', c_ushort)
    ]


class ReadoutLineParams(Structure):
    _fields_ = [
        ('ccd', c_ushort),  # CCD_REQUEST
        ('readoutMode', c_ushort),
        ('pixelStart', c_ushort),
        ('pixelLength', c_ushort)
    ]


class QueryCommandStatusParams(Structure):
    _fields_ = [
        ('command', c_ushort)
    ]


class QueryCommandStatusResults(Structure):
    _fields_ = [
        ('status', c_ushort)
    ]
