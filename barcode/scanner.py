# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

from structures import *
from api import *
from debug import *
from errors import *
from ctypes import byref, POINTER, cast, c_char, c_byte, c_ulong, string_at, pointer
from ctypes import sizeof, addressof
from ctypes.wintypes import DWORD, c_int

class ScannerNotFound(Exception):
    def __init__(self, rc, device_name=None):
        if device_name:
            self.msg = "Could not find the scanner: %s" % str(device_name)
        else:
            self.msg = "Could not find a scanner"
        self.rc = rc

class ScannerError(Exception):
    def __init__(self, rc):
        self.rc = rc
        self.msg = "Encountered error 0x%X when trying to perform scanner action" % self.rc

class ScannedLabel(object):
    def __init__(self, scan_buffer, debug=None):
        self.debug = debug or DummyDebug()
        buf = scan_buffer.contents
        self.buffer_size = buf.dwDataBuffSize
        self.data_length = buf.dwDataLength
        self.data_offset = buf.dwOffsetDataBuff
        self.status = buf.dwStatus
        self.text = buf.bText and True or False
        self.label_type = LABELTYPEXREF[buf.dwLabelType]
        self.request_id = buf.dwRequestID
        self.timestamp = convert_timestamp(buf.TimeStamp)
        self.direction = buf.dwDirection
        self.source = buf.szSource
        self.multipart = buf.bIsMultiPart and True or False
        self._extract_label(scan_buffer)

    def _extract_label(self, scan_buffer):
        """ Extract the barcode from the SCAN_BUFFER """
        data = u'' 
        dt = cast(scan_buffer, POINTER(c_byte))
        t = addressof(dt.contents) + self.data_offset
        dp = pointer(TCHAR.from_address(t))
        for x in xrange(self.data_length):
            data += dp[x]
        self.data = data

    def get_label(self):
        return self.data

    def get_label_type(self):
        return self.source[5:]
        
    

class Scanner(object):
    """ Class representing a barcode scanner """

    def __init__(self, device_name=None, debug=None):
        """ Initiailizes the scanner specified by `device_name`

        If `device_name` is None, then the first scanner device found is used.
        """
        self.debug = debug or DummyDebug()
        self.scan_find_info = SCAN_FINDINFO()
        self.scanner_handle = HANDLE()
        self.device_info = DEVICE_INFO()
        find_handle = HANDLE()
        version_info = SCAN_VERSION_INFO()
        supported_decoders = DECODER_LIST()
        enabled_decoders = DECODER_LIST()

        rc = SCAN_FindFirst(byref(self.scan_find_info), byref(find_handle))
        if device_name:
            while not rc:
                if scan_find_info.szDeviceName == device_name:
                    break
                rc = SCAN_FindNext(byref(self.scan_find_info), byref(find_handle))
                continue
        if rc == E_SCN_NOMOREITEMS:
            raise ScannerNotFound(rc, device_name)
        elif rc != E_SCN_SUCCESS:
            raise ScannerError(rc)
        # This should not error, as we will have ejected prior to this point
        # in event of failure.
        self._call_api_function(SCAN_FindClose, find_handle)
        self._call_api_function(SCAN_Open, self.scan_find_info.szDeviceName, 
                                byref(self.scanner_handle))
        self._call_api_function(SCAN_Enable, self.scanner_handle)
        self._call_api_function(SCAN_GetVersionInfo, self.scanner_handle,
                                byref(version_info))
        self.version = {
                        'hardware' : version_info.dwHardwareVersion,
                        'decoder' : version_info.dwDecoderVersion,
                        'physical_device_driver' : version_info.dwPddVersion,
                        'model_device_driver' : version_info.dwMddVersion,
                        'capi' : version_info.dwCAPIVersion,
                        'decoder_build' : version_info.dwDecoderBuildVersion,
                       }
        self._call_api_function(SCAN_GetDeviceInfo, self.scanner_handle,
                                byref(self.device_info))
        self.supported_decoders = Decoders(self.device_info.Decoders)
        self._call_api_function(SCAN_GetEnabledDecoders, self.scanner_handle, 
                                byref(supported_decoders))
        self.enabled_decoders = Decoders(supported_decoders.Decoders)


#### Playing with junk
        scan_params = SCAN_PARAMS()
        self._call_api_function(SCAN_GetScanParameters, self.scanner_handle,
                                byref(scan_params))

        scan_params.dwDecodeBeepFrequency = 0
        scan_params.dwStartBeepFrequency = 0
        scan_params.dwActivityBeepFrequency = 0
        scan_params.dwNonfatalBeepFrequency = 0
        scan_params.dwFatalBeepFrequency = 0
        scan_params.dwInttermedBeepFrequency = 0
# This is how you can change the sounds of scans.
#        scan_params.szWaveFile = '\\Application\\WAVs\\evil.wav'
#        scan_params.szActvityWaveFile = '\\Application\\WAVs\\achieve.wav'
#        scan_params.szNonfatalWaveFile = '\\Application\\WAVs\\laugh.wav'
#        scan_params.szFatalWaveFile = '\\Application\\WAVs\\laugh.wav'
#        scan_params.szIntermedWaveFile = '\\Application\\WAVs\\laugh.wav'
#        scan_params.szStartWaveFile = '\\Application\\WAVs\\thotoughbread_of_sin.wav'

        scan_params.dwScanType = 1
        self._call_api_function(SCAN_SetScanParameters, self.scanner_handle,
                                byref(scan_params))
#### Foo

    def get_scan_parameters(self):
        """ Return the current Scan Parameters """
        scan_params = SCAN_PARAMS()
        self._call_api_function(SCAN_GetScanParameters, self.scanner_handle,
                                byref(scan_params))
        return scan_params

    def close_scanner(self):
        rc = SCAN_Flush(self.scanner_handle)
        rc = SCAN_Disable(self.scanner_handle)
        rc = SCAN_Close(self.scanner_handle)
    
    def __del__(self):
        """ Close the scanner object """
        self.close_scanner()

    def enable_decoder(self, decoder):
#        print("decoder: %s" % str(decoder))
#        decoder = isinstance(decoder, list) and decoder or [decoder]
#        for d in decoder:
#            print ("enabled_decoders: %s" % str(type(self.enabled_decoders)))
#            print ("decoder: %s" % str(type(d)))
#            self.enabled_decoders += d
#            continue
#        l = self.enabled_decoders.decoder_list()        
#        print("-- decoder list --: %s" % str(type(l)))
        l = DECODER_LIST()
        l.Decoders.dwDecoderCount = 1
        l.Decoders.byList[0] = 34
        l.Decoders.byList[2] = 0
        self._call_api_function(SCAN_SetEnabledDecoders, self.scanner_handle, 
                                byref(l))

    def disable_decoder(self, decoder):
        decoder = isinstance(decoder, list) and decoder or [decoder]
        for d in decoder:
            self.enabled_decoders -= d
            continue
        self._call_api_function(SCAN_SetEnabledDecoders, self.scanner_handle, 
                                byref(decoder_list))


    def get_enabled_decoders(self, text=True):
        """ Return a list of decoders

        By default, this is a list if their short text names.  Set 
        `text=False` to receive a Decoders object
        """
#        if text:
#            return self.enabled_decoders.get_text_list()
#        else:
#            return self.enabled_decoders
        supported_decoders = DECODER_LIST()
        self._call_api_function(SCAN_GetEnabledDecoders, self.scanner_handle, 
                                byref(supported_decoders))
        x = 0
        l = []
        while supported_decoders.Decoders.byList[x]:
            l.append(DECODERTYPEXREF[supported_decoders.Decoders.byList[x]][1])
            x += 1
            continue
        return l
        
        

    def get_decoder_param(self, decoder):
        params = DECODER_PARAMS()
        self._call_api_function(SCAN_GetDecoderParams, self.scanner_handle,
                                byref(decoder), byref(params))
        return params

    def _call_api_function(self, apifunc, *args):
        """ Wraps a call to an api function so that errors are raised as 
        exceptions """
        rc = apifunc(*args)
        if rc:
            raise ScannerError(rc)

    def queue_read_msg(self, handle):
        scan_buffer = SCAN_AllocateBuffer(BOOL(1), DWORD(64))
        requestId = DWORD()
        self._call_api_function(SCAN_ReadLabelMsg, self.scanner_handle,
                        scan_buffer, handle, BARCODE_MSG, DWORD(0), byref(requestId))
        return requestId

    def get_barcode(self, scan_buffer):
        if isinstance(scan_buffer, long):
            scan_buffer = pointer(SCAN_BUFFER.from_address(scan_buffer))
        data = ScannedLabel(scan_buffer)
        self._call_api_function(SCAN_DeallocateBuffer, scan_buffer)
        return data

    def read(self):
        scan_buffer = SCAN_AllocateBuffer(BOOL(1), DWORD(64))
        self._call_api_function(SCAN_ReadLabelWait, self.scanner_handle, 
                                scan_buffer, DWORD(0))
        read_data = ScannedLabel(scan_buffer)
        self._call_api_function(SCAN_DeallocateBuffer, scan_buffer)

#def print_structure(struct):
#    msg = []
#    if isinstance(struct, AllocatedStructure):
#        msg.append("StructInfo.dwAllocated: %d" % 
#                    struct.StructInfo.dwAllocated)
#        msg.append("StructInfo.dwUsed: %d" %
#                    struct.StructInfo.dwUsed)
#    for f in struct._fields_:
        
        
