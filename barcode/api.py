# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

from ctypes import cdll, c_ulong, POINTER, c_uint
from structures import *
from datetime import datetime



__all__ = [
# Functions
"SCAN_AllocateBuffer",
"SCAN_CancelRead",
"SCAN_Close",
"SCAN_DeallocateBuffer",
"SCAN_DeregisterScanMessage",
"SCAN_Disable",
"SCAN_Enable",
"SCAN_FindClose",
"SCAN_FindFirst",
"SCAN_FindNext",
"SCAN_Flush",
"SCAN_GetDecoderParams",
"SCAN_GetDeviceInfo",
"SCAN_GetEnabledDecoders",
"SCAN_GetInterfacePrams",
"SCAN_GetReaderParams",
"SCAN_GetScanParameters",
"SCAN_GetScanStatus",
"SCAN_GetSoftTrigger",
"SCAN_GetSupportedDecoders",
"SCAN_GetUPCEANParams",
"SCAN_GetVersionInfo",
"SCAN_Open",
"SCAN_ReadLabelEvent",
"SCAN_ReadLabelMsg",
"SCAN_ReadLabelWait",
"SCAN_RegisterScanMessage",
"SCAN_SetDecoderParams",
"SCAN_SetEnabledDecoders",
"SCAN_SetInterfaceParams",
"SCAN_SetReaderParams",
"SCAN_SetScanParameters",
"SCAN_SetSoftTrigger",
"SCAN_SetUPCEANParams",
# Decoders
"Decoders",
# Helper Functions
"HIWORD",
"LOWORD",
"convert_timestamp",
# Windows Message
"BARCODE_MSG",
]

scan = cdll.SCNAPI32

SCAN_AllocateBuffer = scan.SCAN_AllocateBuffer_W
SCAN_AllocateBuffer.restype = POINTER(SCAN_BUFFER)
SCAN_CancelRead = scan.SCAN_CancelRead
SCAN_Close = scan.SCAN_Close
SCAN_DeallocateBuffer = scan.SCAN_DeallocateBuffer_W
SCAN_DeregisterScanMessage = scan.SCAN_DeregisterScanMessage
SCAN_Disable = scan.SCAN_Disable
SCAN_Enable = scan.SCAN_Enable
SCAN_FindClose = scan.SCAN_FindClose
SCAN_FindFirst = scan.SCAN_FindFirst_W
SCAN_FindNext = scan.SCAN_FindNext_W
SCAN_Flush = scan.SCAN_Flush
SCAN_GetDecoderParams = scan.SCAN_GetDecoderParams
SCAN_GetDeviceInfo = scan.SCAN_GetDeviceInfo
SCAN_GetEnabledDecoders = scan.SCAN_GetEnabledDecoders
SCAN_GetInterfacePrams = scan.SCAN_GetInterfaceParams
SCAN_GetReaderParams = scan.SCAN_GetReaderParams
SCAN_GetScanParameters = scan.SCAN_GetScanParameters_W
SCAN_GetScanStatus = scan.SCAN_GetScanStatus
SCAN_GetSoftTrigger = scan.SCAN_GetSoftTrigger
SCAN_GetSupportedDecoders = scan.SCAN_GetSupportedDecoders
SCAN_GetUPCEANParams = scan.SCAN_GetUPCEANParams
SCAN_GetVersionInfo = scan.SCAN_GetVersionInfo
SCAN_Open = scan.SCAN_Open
SCAN_ReadLabelEvent = scan.SCAN_ReadLabelEvent_W
SCAN_ReadLabelMsg = scan.SCAN_ReadLabelMsg_W
SCAN_ReadLabelWait = scan.SCAN_ReadLabelWait_W
SCAN_RegisterScanMessage = scan.SCAN_RegisterScanMessage
SCAN_SetDecoderParams = scan.SCAN_SetDecoderParams
SCAN_SetEnabledDecoders = scan.SCAN_SetEnabledDecoders
SCAN_SetInterfaceParams = scan.SCAN_SetInterfaceParams
SCAN_SetReaderParams = scan.SCAN_SetReaderParams
SCAN_SetScanParameters = scan.SCAN_SetScanParameters_W
SCAN_SetSoftTrigger = scan.SCAN_SetSoftTrigger
SCAN_SetUPCEANParams = scan.SCAN_SetUPCEANParams

BARCODE_MSG = c_uint(0x8003)

def HIWORD(dword):
    """ Return the HIWROD portion of a DWORD """
    if isinstace(c_ulong):
        dword = dword.value
    return dword >> 16

def LOWORD(dword):
    """ Return the HIWROD portion of a DWORD """
    if isinstace(c_ulong):
        dword = dword.value
    return dword & 0x0000FFFF

def convert_timestamp(ts):
    """ Convert Windows SYSTEMTIME structure to a datatime object """
    return datetime(ts.wYear, ts.wMonth, ts.wDay,
                    ts.wHour, ts.wMinute, ts.wSecond,
                    ts.wMilliseconds * 1000)

class Decoders(object):
    """ Class for dealing with decoder lists """

    def __init__(self, decoders=None):
        """ Create a Decoder object

        `decoders` can be one of:
         * a single DECODER object
         * a DECODER_LIST object
         * a DECODERS object
         * a list of single byte characters corresponding to DECODER_* values
           or strings containing DECODERTYPEXREF values
        """
        self.decoders = []
        l, byList = self._find_byList(decoders)
        self._append_decoder(l, byList, check=False)
        pass 

    
    def _append_decoder(self, l, byList, check=True):
        """ Add a list of decoders 

        By default it will check to make sure the decoder isn't already in
        the list.  Specify `check=False` to unconditionally append the 
        decoders to the internal list
        """
        for i in xrange(l):
            try:
                d = DECODERTYPEXREF[byList[i]][0]
                if check:
                    if d in self.decoders:
                        self.decoders.append(d)
                else:
                    self.decoders.append(d)
            except KeyError:
                raise
                continue
            continue


    def _remove_decoder(self, l, byList):
        """ Remove a list of decoders """

        for i in xrange(l):
            try:
                d = DECODERTYPEXREF[byList[i]][0]
                try:
                    del self.decoders[self.decoders.index(d)]
                except ValueError:
                    continue
            except KeyError:
                continue
            continue
    

    def _find_byList(self, decoders=None):
        if isinstance(decoders, DECODERS):
            l = decoders.dwDecoderCount
            byList = decoders.byList
        elif isinstance(decoders, DECODER_LIST):
            l = decoders.Decoders.dwDecoderCount
            byList = decoders.Decoders.byList
        elif isinstance(decoders, DECODER):
            l = 1
            byList = decoders
        elif isinstance(decoders, basestring):
            l = 1
            byList = [decoders]
        else:
            l = 0
            byList = []
        return (l, byList)


    def __getitem__(self, key):
        """ Return a DECODER object

        Given a string or DECODER_*  type, return the corresponding DECODER 
        object.  If the given decoder does not exist in `self.decoders`, a
        KeyError is raised
        """

        decoder = DECODERTYPEXREF[key][0]
        if decoder in self.decoders:
            return DECODER(decoder)
        else:
            raise KeyError

  
    def __isub__(self, b):
        """ Remove the specified decoders from `self.decoders`

        `b` can be one of:
         * a single DECODER object
         * a DECODER_LIST object
         * a DECODERS object
         * a list of single byte characters corresponding to DECODER_* values
           or strings containing DECODERTYPEXREF values
        """
        l, byList = self._find_byList(b)
        self._remove_decoder(l, byList)
        return self


    def __iadd__(self, b):
        """ Add the specified decoders to `self.decoders`

        `b` can be one of:
         * a single DECODER object
         * a DECODER_LIST object
         * a DECODERS object
         * a list of single byte characters corresponding to DECODER_* values
           or strings containing DECODERTYPEXREF values
        """
        l, byList = self._find_byList(b)
        self._append_decoder(l, byList)
        return self


    def decoder_list(self):
        """ Return a DECODER_LIST object with the decoders set """
        d = DECODER_LIST()
        l = len(self.decoders)
        for i, x in enumerate(self.decoders):
            d.Decoders.byList[i] = x
        d.Decoders.dwDecoderCount = l
        d.Decoders.byList[l] = 0x0
        return d

    def get_text_list(self):
        """ Return a list of the text decoder names """
        return [DECODERTYPEXREF[x][1] for x in self.decoders]
             
