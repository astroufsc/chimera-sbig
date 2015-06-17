from ctypes import Structure, c_ushort, c_ulong, c_double, c_byte


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
    _fields_ = [('errorString[64]', c_byte)]


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
        ('  shutterCommand', c_ushort),  # SHUTTER_COMMAND
        ('  ledState', c_ushort)  # LED_STATE
    ]


class GetDriverInfoParams(Structure):
    _fields_ = [
        ('  request', c_ushort)  # DRIVER_REQUEST
    ]


class GetDriverInfoResults0(Structure):
    _fields_ = [
        ('version', c_ushort),
        ('name[64]', c_byte),
        ('maxRequest', c_ushort)]


class SetTemperatureRegulationParams2(Structure):
    _fields_ = [
        ('  regulation', c_ushort),  # TEMPERATURE_REGULATION
        ('ccdSetpoint', c_double)
    ]
