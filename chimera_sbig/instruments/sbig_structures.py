from ctypes import Structure, c_ushort, c_ulong, c_double


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
