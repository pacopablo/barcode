# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

from ctypes import cdll, c_ulong, POINTER, c_uint, Structure, byref
from structures import TCHAR, DWORD, AllocatedStructure, MAX_PATH

__all__ = [
# Functions
"AUDIO_GetBeeperVolume",
"AUDIO_SetBeeperVolume",
"AUDIO_GetEarSaveDelay",
"AUDIO_SetEarSaveDelay",
"AUDIO_GetBeeperVolumeLevels",
"AUDIO_PlayBeeper",
"AUDIO_GetVersion",
# Structures
"AUDIO_VERSION_INFO",
"AUDIO_INFO",
# Classes
"Audio",
]

scan = cdll.AudioApi32

AUDIO_GetBeeperVolume = scan.AUDIO_GetBeeperVolume
AUDIO_SetBeeperVolume = scan.AUDIO_SetBeeperVolume
AUDIO_GetEarSaveDelay = scan.AUDIO_GetEarSaveDelay
AUDIO_SetEarSaveDelay = scan.AUDIO_SetEarSaveDelay
AUDIO_GetBeeperVolumeLevels = scan.AUDIO_GetBeeperVolumeLevels
AUDIO_PlayBeeper = scan.AUDIO_PlayBeeper
AUDIO_GetVersion = scan.AUDIO_GetVersion

class AUDIO_INFO(Structure):
    _fields_ = [("szSound", TCHAR * MAX_PATH),
                ("dwDuration", DWORD),
                ("dwFrequency", DWORD),]

class AUDIO_VERSION_INFO(AllocatedStructure):
    _fields_ = [("dwNotifyAPIVersion", DWORD),
                ("dwCAPIVersion", DWORD),]

class Audio(object):
    """ Wrapper around the audio subsystem """
    def __init__(self):
        self.version_info = AUDIO_VERSION_INFO() 
        rc = AUDIO_GetVersion(byref(self.version_info))

    def play(self, wav):
        """Play a wave file"""
        audio_info = AUDIO_INFO()
        audio_info.szSound = wav
        audio_info.dwFrequency = 0
        return AUDIO_PlayBeeper(byref(audio_info))
        
        
    

    

