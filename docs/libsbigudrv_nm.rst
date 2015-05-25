Output of `nm -Ca /usr/lib/libsbigudrv.so` from libsbigudrv2 (2.0.0-0ubuntu1) on Ubuntu 14.04 LTS.

::

    000000000022d980 D ABG_STATE_STRINGS
    0000000000017ee0 T AmbientTemperatureFromSetpoint
    000000000001ceb0 t AOCenter
    0000000000018440 t AOSetFocus
    000000000001cc90 t AOTipTilt
    00000000000176b0 T bcd_nx
    000000000022d8e8 d bFirstPass
                     U bind@@GLIBC_2.2.5
    0000000000013ab0 T BitIOCommand
    000000000022e0e0 b .bss
    000000000022e0e0 A __bss_start
    0000000000007610 T BulkIOFlush
    0000000000007670 T BulkIORead
    0000000000007580 T BulkIOWrite
    0000000000479e68 B bWindowsNT
    00000000000101b0 T CalculateEEPROMChecksum
    00000000000068a0 t call_gmon_start
    000000000023a9a8 b callIndex.7877
    00000000000084e0 T CCDDigitizeLine
    00000000000082e0 T CCDDumpLines
    0000000000009310 T CCDMeasureBias
                     U cfsetispeed@@GLIBC_2.2.5
                     U cfsetospeed@@GLIBC_2.2.5
    000000000000b350 T CFWCommand
    000000000022dfa0 D CFW_COMMAND_STRINGS
    0000000000009b00 t CFWCommCommand
    0000000000009a10 t CFWCommFlush
    000000000023252e b cfwCommIn
    0000000000232528 b cfwCommOut
    000000000022e0c0 D CFW_COM_PORT_STRINGS
    000000000000ac40 t CFWDetectI2CModel
    000000000022e000 D CFW_ERROR_STRINGS
    000000000000a2f0 t CFWGoto
    000000000022df00 D CFW_MODEL_SELECT_STRINGS
    000000000000aa60 t CFWOpenComm
    000000000022e060 D CFW_POSITION_STRINGS
    0000000000009fd0 t CFWQuery
    0000000000009d30 t CFWStatus
    000000000022dfd0 D CFW_STATUS_STRINGS
    00000000000099b0 t CFWWaitForShutter
    0000000000015520 T CheckFeatherGateArray
    0000000000017a20 T clear
    0000000000008040 T ClearITArray
    0000000000007a20 T ClockAD
                     U clock@@GLIBC_2.2.5
                     U close@@GLIBC_2.2.5
    0000000000014ee0 T ColumnEEPROMCommand
    000000000023a8e0 b CommandInBuf
    000000000023a6c0 b CommandOutBuf
    000000000022dbe0 D COMMAND_STRINGS
    0000000000000000 n .comment
    000000000022e0e0 b completed.6341
                     U connect@@GLIBC_2.2.5
    00000000000178e0 T cpy
    0000000000000000 a crtstuff.c
    0000000000000000 a crtstuff.c
    00000000000233f4 r CSWTCH.212
    0000000000229008 d __CTOR_END__
    0000000000229000 d __CTOR_LIST__
    0000000000229000 d .ctors
                     w __cxa_finalize@@GLIBC_2.2.5
    0000000000229a40 d .data
    0000000000229040 d .data.rel.ro
    000000000000c400 T debug_log_message
    000000000023ef00 B debug_msg
    0000000000479d60 B det
    0000000000006970 T DetectI2CAO
    000000000023a9ac b diddle_line_counter
    000000000000c410 T DiffGuiderCommand
    0000000000229a60 D dllGlobals
    0000000000022120 t __do_global_ctors_aux
    00000000000068c0 t __do_global_dtors_aux
    0000000000479ca0 B driverControlParams
    0000000000229a40 d __dso_handle
    0000000000229018 d __DTOR_END__
    000000000022e0e8 b dtor_idx.6343
    0000000000229010 d __DTOR_LIST__
    0000000000229010 d .dtors
    000000000023a580 b dumpBuffer
    0000000000018540 t DumpLines
    0000000000229220 d .dynamic
    0000000000229220 a _DYNAMIC
    0000000000002228 r .dynstr
    0000000000000d70 r .dynsym
    000000000022e0e0 A _edata
    0000000000026f90 r .eh_frame
    0000000000026a68 r .eh_frame_hdr
    0000000000007730 T EnableVerticalFlush
    0000000000479e70 A _end
    000000000001a720 t EndExposure
    00000000000194f0 t EndReadout
    000000000023a940 b epAddr
    000000000022da80 D ERROR_STRINGS
    000000000001d0e0 t EstablishLink
    000000000000dec0 T ETHBulkRead
    000000000000de10 T ETHBulkWrite
    000000000000e8a0 T ETHComMicroBlock
    000000000000e170 T ETHDeviceIOControl
    000000000022d8e4 D ethDllGlobalsCount
    000000000000e6b0 T ETHGetDriverInfo
    000000000000e4f0 T ETHGetMicroBlock
    000000000000e3e0 T ETHGetPixels
    000000000000dc60 T ETHInitPixelReadout
    000000000000e050 t ETHRecvPacket
                     U exp
    000000000022d930 D FAN_STATE_STRINGS
                     U fclose@@GLIBC_2.2.5
                     U fcntl@@GLIBC_2.2.5
    0000000000017780 T fill
    0000000000022158 T _fini
    0000000000022158 t .fini
    000000000000ee20 T FirmwareCommand
                     U fopen@@GLIBC_2.2.5
                     U fprintf@@GLIBC_2.2.5
    0000000000006940 t frame_dummy
    0000000000028460 r __FRAME_END__
                     U fread@@GLIBC_2.2.5
    00000000000180b0 t FreezeTEControl
                     U fwrite@@GLIBC_2.2.5
    000000000023a6a0 b g_active_command
    00000000000148d0 T GetBootEEPROM
    000000000001be30 t GetCCDInfo
    0000000000018c70 T GetDriverInfo
    0000000000014b60 T GetEEPROM
    000000000000ff60 t GetExpectedReturnLen
    000000000000ee60 T GetLPTLDriverInfo
    0000000000018030 T GetNextUSBDevice
    0000000000014ab0 T GetRawEEPROM
    000000000000ee40 T GetWinIO
    00000000002294d8 a _GLOBAL_OFFSET_TABLE_
                     w __gmon_start__
    0000000000000848 r .gnu.hash
    0000000000002e54 r .gnu.version
    0000000000003010 r .gnu.version_r
    00000000002293d0 d .got
    00000000002294d8 d .got.plt
    00000000000001b8 r .hash
    0000000000017d00 T HFlipPixels
    000000000023eee0 B hot_count
    0000000000017d60 T HotPatchPixels
    0000000000232526 b hot_threshold
    00000000000074a0 T I2CAOCenter
    0000000000006dc0 T I2CAOTipTilt
    000000000023a680 b igap
                     U inet_addr@@GLIBC_2.2.5
                     U inet_ntoa@@GLIBC_2.2.5
    0000000000005de0 T _init
    0000000000005de0 t .init
    0000000000018de0 t InitGlobalData
    000000000001bc00 t InitTrackingCCDInfo
                     U ioctl@@GLIBC_2.2.5
    0000000000007710 T isAutoFilterSupported
    0000000000229020 d .jcr
    0000000000229020 d __JCR_END__
    0000000000229020 d __JCR_LIST__
                     w _Jv_RegisterClasses
    000000000023a9a4 b LastCommand.7878
    0000000000229a50 d lastCommand.8596
    000000000022e120 b last_line1
    0000000000230320 b last_line2
    0000000000229a4c d lastX.6576
    0000000000229a48 d lastY.6577
    000000000022d960 D LED_STATE_STRINGS
    000000000035c640 B leftSidePixelFifo
                     U libusb_bulk_transfer
                     U libusb_claim_interface
                     U libusb_close
                     U libusb_detach_kernel_driver
                     U libusb_free_device_list
                     U libusb_get_configuration
                     U libusb_get_device_descriptor
                     U libusb_get_device_list
                     U libusb_get_string_descriptor_ascii
                     U libusb_init
                     U libusb_open
                     U libusb_release_interface
                     U libusb_set_configuration
                     U log
    000000000000f5a0 T LPTCameraOut
    000000000000f110 T LPTClearImagingArray
    000000000000f0b0 T LPTClearTrackingArray
    000000000000f170 T LPTClockAD
    000000000000f340 T LPTDumpImagingLines
    000000000000f240 T LPTDumpST5CLines
    000000000000f2d0 T LPTDumpTrackingLines
    000000000000f030 T LPTGetIRQL
    000000000000f4c0 T LPTGetMicroBlock
    000000000000f3b0 T LPTGetPixels
    000000000000efd0 T LPTGetUSTimer
    000000000000f600 T LPTInitPort
    000000000000f530 T LPTSendMicroBlock
    000000000000f070 T LPTSetIRQL
    000000000000f1d0 T LPTSetVdd
    000000000001bab0 t make_n_modes
    0000000000232560 b m_buf
    000000000022d9a0 D MC_READOUT_SUBCOMMAND_STRINGS
                     U memcpy@@GLIBC_2.2.5
    000000000000f8b0 T MFCommand
    000000000000f650 t MFDetectModel
    000000000000f700 t MFQuery
    00000000000111d0 T MicroCommand
    0000000000013660 T MicroGetPixels
    0000000000010580 t MicroGetPixelsFromChannelA
    0000000000010260 t MicroGetPixelsFromChannelB
    0000000000013d40 T MicroInitADGain
    0000000000014110 T MicroInitPixelReadout
    00000000000195e0 t MiscellaneousControl
    0000000000229048 d m_pCommand
    0000000000229040 d m_pData
    0000000000229050 d m_pPacketLength
    0000000000229058 d m_pRxLen
    0000000000229060 d m_pStatus
    0000000000017f50 T ms_clock
    0000000000018000 T MyTickCount
                     U nanosleep@@GLIBC_2.2.5
    0000000000232548 b nBytesRd
    000000000023a920 b nBytesRd
    0000000000232550 b nBytesWr
    000000000023a928 b nBytesWr
    0000000000000190 r .note.gnu.build-id
    0000000000017b30 T OffHorzBinPixels
    0000000000232524 b offset
    00000000000080c0 T OffsetITArray
    0000000000017cc0 T OffsetPixels
    0000000000007a90 T OffsetST5CArray
    0000000000017ae0 T OffVertBinPixels
    0000000000019040 t OpenCloseDevice
    000000000000eeb0 T OpenCloseLPTLDevice
                     U open@@GLIBC_2.2.5
    0000000000000000 a parao.c
    0000000000000000 a parbulkio.c
    0000000000000000 a parccd.c
    0000000000000000 a parcfw.c
    000000000023a9a2 B parComActive
    0000000000000000 a pardebug.c
    0000000000000000 a pardiffg.c
    0000000000479d40 B pardrv_spm
    0000000000000000 a pareth.c
    0000000000000000 a parfirm.c
    0000000000000000 a parlpt.c
    0000000000000000 a parmf.c
    0000000000000000 a parmicro.c
    0000000000000000 a parreg.c
    0000000000000000 a parstf.c
    0000000000000000 a parstfclass.c
    0000000000000000 a parstx.c
    0000000000000000 a parusb.c
    0000000000000000 a parusbi.c
    0000000000000000 a parusbio.c
    0000000000000000 a parusbl.c
    0000000000000000 a parusbm.c
    0000000000000000 a parutil.c
    0000000000000000 a parwin64.c
    0000000000479c80 B pDllGlobals
    0000000000232540 b pipelineFull.8044
    0000000000005df8 t .plt
    0000000000018bd0 T PulseOut
    0000000000014ca0 T PutBootEEPROM
    0000000000014820 T PutEEPROM
    0000000000018660 T QueryCommandStatus
    000000000000d230 T QueryEthernet
    000000000000c780 T QueryEthernet2
    000000000001b630 t QueryTemperatureStatus
    00000000000180a0 T rdtsc
                     U read@@GLIBC_2.2.5
    000000000001cb10 t ReadOffset2
    0000000000010160 T ReadoutCommandGetsPixelData
    000000000001ac40 t ReadoutLine
                     U recvfrom@@GLIBC_2.2.5
                     U recv@@GLIBC_2.2.5
    0000000000003050 r .rela.dyn
    0000000000004e08 r .rela.plt
    00000000000176a0 T RelayClick
    000000000023f000 B rightSidePixelFifo
    0000000000022180 r .rodata
    00000000000233e0 r romMSNtoID
    000000000022e100 b rowCounter.8177
    0000000000016850 T RWUSBI2C
    0000000000232522 b saturation
    000000000022ddc0 D SBIG_COMMAND_NAME_STRINGS
    0000000000000000 a sbigudrv.c
    000000000023a9a0 B sbigUDRVHandle
    000000000001edd0 T SBIGUnivDrvCommand
    0000000000017a00 T scat
    00000000000179e0 T scpy
                     U send@@GLIBC_2.2.5
                     U sendto@@GLIBC_2.2.5
    000000000023a9c0 b serialDataOut
    0000000000017db0 T SetpointFromAmbientTemperature
    0000000000017e10 T SetpointFromTemperature
                     U setsockopt@@GLIBC_2.2.5
    00000000000182d0 t SetTemperatureRegulation
    000000000001b3f0 t SetTemperatureRegulation2
    00000000000078c0 T SetVdd
                     U shutdown@@GLIBC_2.2.5
    000000000022d900 D SHUTTER_COMMAND_STRINGS
    0000000000479d48 B shutterEdge
    000000000022d940 D SHUTTER_STATE_STRINGS
    0000000000017f60 T Sleep
                     U socket@@GLIBC_2.2.5
                     U sprintf@@GLIBC_2.2.5
                     U sqrt
    0000000000023ab0 r ST7_AD_REGS
    0000000000019780 t StartExposure
    000000000001cf80 t StartReadout
    000000000022de40 D ST_CAMERA_NAME_STRINGS
                     U stderr@@GLIBC_2.2.5
    0000000000024150 r STF8_BOTTOM
    0000000000229080 d STF8_CAMERA_NAME
    0000000000024100 r STF8_HEIGHT
    0000000000024140 r STF8_LEFT
    0000000000024120 r STF8_PIXEL_HEIGHT
    0000000000024110 r STF8_PIXEL_WIDTH
    0000000000024160 r STF8_RIGHT
    0000000000024130 r STF8_TOP
    00000000000240f0 r STF8_WIDTH
    00000000000240b0 r STF_BOTTOM
    00000000002291a0 d STF_CAMERA_NAME
    00000000000157c0 T STFDownloadReadoutParams
    0000000000023ff0 r STF_HEIGHT
    0000000000024090 r STF_LEFT
    0000000000024030 r STF_PIXEL_HEIGHT
    0000000000024050 r STF_PIXEL_WIDTH
    00000000000240d0 r STF_RIGHT
    0000000000024070 r STF_TOP
    0000000000024010 r STF_WIDTH
    0000000000023fb0 r STL_BOTTOM
    00000000002290a0 d STL_CAMERA_NAME
    0000000000023ef0 r STL_HEIGHT
    0000000000023f90 r STL_LEFT
    0000000000023f30 r STL_PIXEL_HEIGHT
    0000000000023f50 r STL_PIXEL_WIDTH
    0000000000023fd0 r STL_RIGHT
    0000000000023f70 r STL_TOP
    0000000000023f10 r STL_WIDTH
                     U strcmp@@GLIBC_2.2.5
                     U strcpy@@GLIBC_2.2.5
                     U strstr@@GLIBC_2.2.5
    0000000000024400 r STT_BOTTOM
    00000000002291e0 d STT_CAMERA_NAME
    0000000000024380 r STT_HEIGHT
    00000000000243e0 r STT_LEFT
    0000000000024440 r STT_PIXEL_HEIGHT
    0000000000024460 r STT_PIXEL_WIDTH
    0000000000024420 r STT_RIGHT
    00000000000243c0 r STT_TOP
    00000000000243a0 r STT_WIDTH
    00000000000165e0 T STXAdjustGains
    0000000000023a90 r STX_AD_REGS
    0000000000015ed0 T STXAutoFreeze
    0000000000024280 r STX_BOTTOM
    0000000000229140 d STX_CAMERA_NAME
    0000000000015f20 T STXDownloadReadoutParams
    0000000000016100 T STXGetCCDSizeInfo
    0000000000016550 T STXGetEzUSBVersion
    00000000000163b0 T STXGetTemperatureData
    0000000000024180 r STX_HEIGHT
    00000000002290e0 d STXL_CAMERA_NAME
    0000000000024240 r STX_LEFT
    0000000000024300 r STX_PIXEL_HEIGHT
    0000000000024340 r STX_PIXEL_WIDTH
    00000000000242c0 r STX_RIGHT
    0000000000024200 r STX_TOP
    00000000000241c0 r STX_WIDTH
    0000000000017c60 T SubtractPixels
    0000000000017640 T swap_bytes
    00000000000179a0 T swapcpy
    0000000000017660 T swap_long
    000000000001cd90 t T.443
                     U tcflush@@GLIBC_2.2.5
                     U tcgetattr@@GLIBC_2.2.5
                     U tcsetattr@@GLIBC_2.2.5
    0000000000017e70 T TemperatureFromSetpoint
    000000000023aae0 B temp_video
    000000000023cce0 B temp_video2
    00000000000068a0 t .text
    0000000000232520 b threshold
                     U time@@GLIBC_2.2.5
    0000000000017fb0 T TimerDelay
                     U times@@GLIBC_2.2.5
    00000000000150f0 t UploadFeatherGateArray
    00000000000168e0 T USBADControl
    0000000000016ab0 T USBClearArray
    000000000022d8e0 D usbDllGlobalsCount
    0000000000016a40 T USBDumpLines
    0000000000016770 T USBFlushPipes
    0000000000016710 T USBGetAlternateMicroBlock
    0000000000016790 T USBGetMicroBlock
    0000000000016b30 T USBGetPixels
    0000000000479c70 B usbIGA
    0000000000016d90 T USBLDRIVER_FlushPipes
    0000000000016f60 T USBLDRIVER_ReadAlternatePipe
    0000000000016fd0 T USBLDRIVER_ReadComPipe
    0000000000016e80 T USBLDRIVER_ReadPixelPipe
    0000000000016d80 T USBLDRIVER_ResetPipes
    0000000000016da0 T USBLDRIVER_WriteAlternatePipe
    0000000000016e10 T USBLDRIVER_WriteComPipe
    0000000000017040 T USBLGetDriverInfo
    00000000000170a0 T USBLOpenCloseDevice
    0000000000016af0 T USBManClocks
    0000000000016840 T USBOpenCloseDevice
    0000000000016740 T USBSendAlternateMicroBlock
    0000000000016810 T USBSendMicroBlock
    0000000000016a00 T USBSetVdd
    00000000000139c0 T UserEEPROMCommand
    0000000000011090 t ValGetMicroAck
    0000000000010890 t ValGetMicroBlock
    000000000000ef70 T WINDeviceIOControl
                     U write@@GLIBC_2.2.5
