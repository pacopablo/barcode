# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

from ctypes import Structure, Union, c_long, c_wchar, c_char, POINTER, sizeof
from ctypes.wintypes import MAX_PATH, DWORD, BOOL, RECT, BYTE, WORD

__all__ = [
# Constants
"MAX_DEVICE_NAME",
"MAX_PATH",
"MAX_SRC",
"DECODERS_BUFLEN",
# Types
"TCHAR",
"DWORD",
"WORD",
"BOOL",
"RECT",
"BYTE",
"HANDLE",
"LPHANDLE",
"DECODER",
"LABELTYPE",
# Structures
"STRUCT_INFO",
"SYSTEMTIME",
"SCAN_FINDINFO",
"SCAN_VERSION_INFO",
"DECODERS",
"DEVICE_INFO",
"DECODER_LIST",
"SCAN_PARAMS",
"SCAN_BUFFER",
# Decoder Parameter Structures
"UPCE0_PARAMS",
"UPCE1_PARAMS",
"UPCA_PARAMS",
"MSI_PARAMS",
"EAN8_PARAMS",
"CODABAR_PARAMS",
"CODE39_PARAMS",
"D2OF5_PARAMS",
"I2OF5_PARAMS",
"CODE11_PARAMS",
"CODE93_PARAMS",
"CODE128_PARAMS",
"TRIOPTIC39_PARAMS",
"IMAGE_PARAMS",
"SIGNATURE_PARAMS",
"MACROPDF_PARAMS",
"MACROMICROPDF_PARAMS",
"WEBCODE_PARAMS",
"COMPOSITE_AB_PARAMS",
"KOREAN_3OF5_PARAMS",
# Decoders
"DECODER_UPCE0",
"DECODER_UPCE1",
"DECODER_UPCA",
"DECODER_MSI",
"DECODER_EAN8",
"DECODER_EAN13",
"DECODER_CODABAR",
"DECODER_CODE39",
"DECODER_D2OF5",
"DECODER_I2OF5",
"DECODER_CODE11",
"DECODER_CODE93",
"DECODER_CODE128",
"DECODER_PDF417",
"DECODER_TRIOPTIC39",
"DECODER_MICROPDF",
"DECODER_MACROPDF",
"DECODER_MAXICODE",
"DECODER_DATAMATRIX",
"DECODER_QRCODE",
"DECODER_MACROMICROPDF",
"DECODER_RSS14",
"DECODER_RSSLIM",
"DECODER_RSSEXP",
"DECODER_POINTER",
"DECODER_IMAGE",
"DECODER_SIGNATURE",
"DECODER_WEBCODE",
"DECODER_CUECODE",
"DECODER_COMPOSITE_AB",
"DECODER_COMPOSITE_C",
"DECODER_TLC39",
"DECODER_USPOSTNET",
"DECODER_USPLANET",
"DECODER_UKPOSTAL",
"DECODER_JAPPOSTAL",
"DECODER_AUSPOSTAL",
"DECODER_DUTCHPOSTAL",
"DECODER_CANPOSTAL",
"DECODER_CHINESE_2OF5",
"DECODER_AZTEC",
"DECODER_MICROQR",
"DECODER_KOREAN_3OF5",
"DECODER_US4STATE",
"DECODERTYPEXREF",
# Label Types
"LABELTYPE_UPCE0",
"LABELTYPE_UPCE1",
"LABELTYPE_UPCA",
"LABELTYPE_MSI",
"LABELTYPE_EAN8",
"LABELTYPE_EAN13",
"LABELTYPE_CODABAR",
"LABELTYPE_CODE39",
"LABELTYPE_D2OF5",
"LABELTYPE_I2OF5",
"LABELTYPE_CODE11",
"LABELTYPE_CODE93",
"LABELTYPE_CODE128",
"LABELTYPE_IATA2OF5",
"LABELTYPE_EAN128",
"LABELTYPE_PDF417",
"LABELTYPE_ISBT128",
"LABELTYPE_TRIOPTIC39",
"LABELTYPE_COUPON",
"LABELTYPE_BOOKLAND",
"LABELTYPE_MICROPDF",
"LABELTYPE_CODE32",
"LABELTYPE_MACROPDF",
"LABELTYPE_MAXICODE",
"LABELTYPE_DATAMATRIX",
"LABELTYPE_QRCODE",
"LABELTYPE_MACROMICROPDF",
"LABELTYPE_RSS14",
"LABELTYPE_RSSLIM",
"LABELTYPE_RSSEXP",
"LABELTYPE_IMAGE",
"LABELTYPE_SIGNATURE",
"LABELTYPE_WEBCODE",
"LABELTYPE_CUECODE",
"LABELTYPE_COMPOSITE_AB",
"LABELTYPE_COMPOSITE_C",
"LABELTYPE_TLC39",
"LABELTYPE_USPOSTNET",
"LABELTYPE_USPLANET",
"LABELTYPE_UKPOSTAL",
"LABELTYPE_JAPPOSTAL",
"LABELTYPE_AUSPOSTAL",
"LABELTYPE_DUTCHPOSTAL",
"LABELTYPE_CANPOSTAL",
"LABELTYPE_CHINESE_2OF5",
"LABELTYPE_AZTEC",
"LABELTYPE_MICROQR",
"LABELTYPE_KOREAN_3OF5",
"LABELTYPE_US4STATE",
"LABELTYPE_UNKNOWN",
"LABELTYPEXREF",
]

# Constants
MAX_SRC = 32
MAX_DEVICE_NAME = 128
DECODERS_BUFLEN = 128

# Typedef
TCHAR = c_wchar
HANDLE = POINTER(POINTER(c_long))
LPHANDLE = POINTER(HANDLE)
DECODER = c_char * 2
LABELTYPE = DWORD

class STRUCT_INFO(Structure):
    _fields_ = [("dwAllocated", DWORD),
                ("dwUsed", DWORD),]

class AllocatedStructure(Structure):
    """ Superclass for structures that contain StructInfo

    The `AllocatedStructure` class will automatically populate the
    `dwAllocated` member with the size of the structure.
    """

    _fields_ = [("StructInfo", STRUCT_INFO),]

    def __init__(self, *args, **kwargs):
        """ Populate the `dwAllocateed` member with the structure size """
        Structure.__init__(self, *args, **kwargs)
        self.StructInfo.dwAllocated = sizeof(self) - 4

class SYSTEMTIME(Structure):
    _fields_ = [("wYear", WORD),
                ("wMonth", WORD),
                ("wDayOfWeek", WORD),
                ("wDay", WORD),
                ("wHour", WORD),
                ("wMinute", WORD),
                ("wSecond", WORD),
                ("wMilliseconds", WORD),]

class SCAN_FINDINFO(AllocatedStructure):
    _fields_ = [("szDeviceName", TCHAR * MAX_DEVICE_NAME),
                ("szPortName", TCHAR * MAX_DEVICE_NAME),
                ("szFriendlyName", TCHAR * MAX_PATH),
                ("szRegistryBasePath", TCHAR * MAX_PATH),]

class SCAN_VERSION_INFO(AllocatedStructure):
    _fields_ = [("dwHardwareVersion", DWORD),
                ("dwDecoderVersion", DWORD),
                ("dwPddVersion", DWORD),
                ("dwMddVersion", DWORD),
                ("dwCAPIVersion", DWORD),
                ("dwDecoderBuildVersion", DWORD),]

class DECODERS(Structure):
    _fields_ = [("dwDecoderCount", DWORD),
                ("byList", BYTE * DECODERS_BUFLEN),]

class DEVICE_INFO(AllocatedStructure):
    _fields_ = [("Decoders", DECODERS),
                ("bBeamWidth", BOOL),
                ("bAimMode", BOOL),
                ("bDirection", BOOL),
                ("bFeedback", BOOL),
                ("dwSupportedImageFormats", DWORD),
                ("MaxImageRect", RECT),
                ("dwDPMCapable", DWORD),]

class DECODER_LIST(AllocatedStructure):
    _fields_ = [("Decoders", DECODERS)]

class UPCE0_PARAMS(Structure):
    _fields_ = [("bReportCheckDigit", BOOL),
                ("dwPreamble", DWORD),
                ("bConvertToUPCA", BOOL),]

class UPCE1_PARAMS(Structure):
    _fields_ = [("bReportCheckDigit", BOOL),
                ("dwPreamble", DWORD),
                ("bConvertToUPCA", BOOL),]

class UPCA_PARAMS(Structure):
    _fields_ = [("bReportCheckDigit", BOOL),
                ("dwPreamble", DWORD),]

class MSI_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),
                ("dwCheckDigits", DWORD),
                ("dwCheckDigitScheme", DWORD),
                ("bReportCheckDigit", BOOL),]

class EAN8_PARAMS(Structure):
    _fields = [("bConvertToEAN13", BOOL),]

class CODABAR_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),
                ("bClsiEditing", BOOL),
                ("bNotisEditing", BOOL),]

class CODE39_PARAMS(Structure):
    _fields_ = [("bVerifyCheckDigit", BOOL),
                ("bReportCheckDigit", BOOL),
                ("bConcatenation", BOOL),
                ("bFullAscii", BOOL),
                ("bRedundancy", BOOL),
                ("bConvertToCode32", BOOL),
                ("bCode32Prefix", BOOL),]

class D2OF5_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),]

class I2OF5_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),
                ("dwVerifyCheckDigit", DWORD),
                ("bReportCheckDigit", BOOL),
                ("bConvertToEAN13", BOOL),]

class CODE11_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),
                ("dwCheckDigitCount", DWORD),
                ("bReportCheckDigit", BOOL),]

class CODE93_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),]

class CODE128_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),
                ("bEAN128", BOOL),
                ("bISBT128", BOOL),
                ("bOther128", BOOL),]

class TRIOPTIC39_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),]

class IMAGE_PARAMS(Structure):
    _fields_ = [("CroppingRect", RECT),
                ("dwResolutionDivisor", DWORD),
                ("bEnableAiming", BOOL),
                ("bEnableIllumination", BOOL),
                ("dwImageFormat", DWORD),
                ("dwJpegImageQuality", DWORD),
                ("dwJpegImageSize", DWORD),]

class SIGNATURE_PARAMS(Structure):
    _fields_ = [("dwImageFormat", DWORD),
                ("dwJpegImageQuality", DWORD),
                ("dwJpegImageSize", DWORD),
                ("dwImageWidth", DWORD),
                ("dwImageHeight", DWORD),]

class MACROPDF_PARAMS(Structure):
    _fields_ = [("bReportAppendInfo", BOOL),
                ("bBufferLabels", BOOL),
                ("bExclusive", BOOL),
                ("bConvertToPDF417", BOOL),]

class MACROMICROPDF_PARAMS(Structure):
    _fields_ = [("bReportAppendInfo", BOOL),
                ("bBufferLabels", BOOL),
                ("bExclusive", BOOL),
                ("bConvertToMicroPDF", BOOL),]

class WEBCODE_PARAMS(Structure):
    _fields_ = [("bGTWebcode", BOOL),]

class COMPOSITE_AB_PARAMS(Structure):
    _fields_ = [("dwUCCLinkMode", DWORD),
                ("dwMultiMode", DWORD),]

class KOREAN_3OF5_PARAMS(Structure):
    _fields_ = [("bRedundancy", BOOL),]

class DECODER_SPECIFIC(Union):
    _fields_ = [("dwUntyped", DWORD * 20),
                ("upce0_params", UPCE0_PARAMS),
                ("upce1_params", UPCE1_PARAMS),
                ("upca_params", UPCA_PARAMS),
                ("msi_params", MSI_PARAMS),
                ("ean8_params", EAN8_PARAMS),
                ("codabar_params", CODABAR_PARAMS),
                ("code39_params", CODE39_PARAMS),
                ("d2of5_params", D2OF5_PARAMS),
                ("i2of5_params", I2OF5_PARAMS),
                ("code11_params", CODE11_PARAMS),
                ("code93_params", CODE93_PARAMS),
                ("code128_params", CODE128_PARAMS),
                ("trioptic39_params", TRIOPTIC39_PARAMS),
                ("image_params", IMAGE_PARAMS),
                ("signature_params", SIGNATURE_PARAMS),
                ("macropdf_params", MACROPDF_PARAMS),
                ("macromicropdf_params", MACROMICROPDF_PARAMS),
                ("webcode_params", WEBCODE_PARAMS),
                ("composite_ab_params", COMPOSITE_AB_PARAMS),
                ("korean_3of5_params", KOREAN_3OF5_PARAMS),]

class DECODER_PARAMS(AllocatedStructure):
    _fields_ = [("cDecoder", DECODER),
                ("dwMinLength", DWORD),
                ("dwMaxLength", DWORD),
                ("dec_specific", DECODER_SPECIFIC),]

class SCAN_PARAMS(AllocatedStructure):
    _fields_ = [("dwCodeldType", DWORD),
                ("dwScanType", DWORD),
                ("bLocalFeedback", BOOL),
                ("dwDecodeBeepTime", DWORD),
                ("dwDecodeBeepFrequency", DWORD),
                ("dwDecodeLedTime", DWORD),
                ("szWaveFile", TCHAR * MAX_PATH),
                ("dwStartBeepTime", DWORD),
                ("dwStartBeepFrequency", DWORD),
                ("dwStartLedTime", DWORD),
                ("szStartWaveFile", TCHAR * MAX_PATH),
                ("dwIntermedBeepTime", DWORD),
                ("dwIntermedBeepFrequency", DWORD),
                ("dwIntermedLedTime", DWORD),
                ("szIntermedWaveFile", TCHAR * MAX_PATH),
                ("dwFatalBeepTime", DWORD),
                ("dwFatalBeepFrequency", DWORD),
                ("dwFatalLedTime", DWORD),
                ("szFatalWaveFile", TCHAR * MAX_PATH),
                ("dwNonfatalBeepTime", DWORD),
                ("dwNonfatalBeepFrequency", DWORD),
                ("dwNonfatalLedTime", DWORD),
                ("szNonfatalWaveFile", TCHAR * MAX_PATH),
                ("dwActivityBeepTime", DWORD),
                ("dwActivityBeepFrequency", DWORD),
                ("dwActivityLedTime", DWORD),
                ("szActivityWaveFile", TCHAR * MAX_PATH),]

class SCAN_BUFFER(AllocatedStructure):
    _fields_ = [("dwDataBuffSize", DWORD),
                ("dwOffsetDataBuff", DWORD),
                ("dwDataLength", DWORD),
                ("dwTimeout", DWORD),
                ("dwStatus", DWORD),
                ("bText", BOOL),
                ("dwLabelType", LABELTYPE),
                ("dwRequestID", DWORD),
                ("TimeStamp", SYSTEMTIME),
                ("dwDirection", DWORD),
                ("szSource", TCHAR * MAX_SRC),
                ("bIsMultiPart", BOOL),
                ("dwScanID", DWORD),
                ("dwBarcodeID", DWORD),
                ("dwNumRenaming", DWORD),
                ("dwOffsetAuxDataBuff", DWORD),
                ("dwAuxDataLength", DWORD),]


DECODER_UPCE0         = DECODER("\x30")
DECODER_UPCE1         = DECODER("\x31")
DECODER_UPCA          = DECODER("\x32")
DECODER_MSI           = DECODER("\x33")
DECODER_EAN8          = DECODER("\x34")
DECODER_EAN13         = DECODER("\x35")
DECODER_CODABAR       = DECODER("\x36")
DECODER_CODE39        = DECODER("\x37")
DECODER_D2OF5         = DECODER("\x38")
DECODER_I2OF5         = DECODER("\x39")
DECODER_CODE11        = DECODER("\x3A")
DECODER_CODE93        = DECODER("\x3B")
DECODER_CODE128       = DECODER("\x3C")
DECODER_PDF417        = DECODER("\x40")
DECODER_TRIOPTIC39    = DECODER("\x42")
DECODER_MICROPDF      = DECODER("\x45")
DECODER_MACROPDF      = DECODER("\x47")
DECODER_MAXICODE      = DECODER("\x48")
DECODER_DATAMATRIX    = DECODER("\x49")
DECODER_QRCODE        = DECODER("\x4A")
DECODER_MACROMICROPDF = DECODER("\x4B")
DECODER_RSS14         = DECODER("\x4C")
DECODER_RSSLIM        = DECODER("\x4D")
DECODER_RSSEXP        = DECODER("\x4E")
DECODER_POINTER       = DECODER("\x50")
DECODER_IMAGE         = DECODER("\x51")
DECODER_SIGNATURE     = DECODER("\x52")
DECODER_WEBCODE       = DECODER("\x54")
DECODER_CUECODE       = DECODER("\x55")
DECODER_COMPOSITE_AB  = DECODER("\x56")
DECODER_COMPOSITE_C   = DECODER("\x57")
DECODER_TLC39         = DECODER("\x58")
DECODER_USPOSTNET     = DECODER("\x61")
DECODER_USPLANET      = DECODER("\x62")
DECODER_UKPOSTAL      = DECODER("\x63")
DECODER_JAPPOSTAL     = DECODER("\x64")
DECODER_AUSPOSTAL     = DECODER("\x65")
DECODER_DUTCHPOSTAL   = DECODER("\x66")
DECODER_CANPOSTAL     = DECODER("\x67")
DECODER_CHINESE_2OF5  = DECODER("\x70")
DECODER_AZTEC         = DECODER("\x74")
DECODER_MICROQR       = DECODER("\x75")
DECODER_KOREAN_3OF5   = DECODER("\x76")
DECODER_US4STATE      = DECODER("\x77")
 
DECODERTYPEXREF = {
'UPCE0'         : (0x30, 'UPCE0'),
'UPCE1'         : (0x31, 'UPCE1'),
'UPCA'          : (0x32, 'UPCA'),
'MSI'           : (0x33, 'MSI'),
'EAN8'          : (0x34, 'EAN8'),
'EAN13'         : (0x35, 'EAN13'),
'CODABAR'       : (0x36, 'CODABAR'),
'CODE39'        : (0x37, 'CODE39'),
'D2OF5'         : (0x38, 'D2OF5'),
'I2OF5'         : (0x39, 'I2OF5'),
'CODE11'        : (0x3A, 'CODE11'),
'CODE93'        : (0x3B, 'CODE93'),
'CODE128'       : (0x3C, 'CODE128'),
'PDF417'        : (0x40, 'PDF417'),
'TRIOPTIC39'    : (0x42, 'TRIOPTIC39'),
'MICROPDF'      : (0x45, 'MICROPDF'),
'MACROPDF'      : (0x47, 'MACROPDF'),
'MAXICODE'      : (0x48, 'MAXICODE'),
'DATAMATRIX'    : (0x49, 'DATAMATRIX'),
'QRCODE'        : (0x4A, 'QRCODE'),
'MACROMICROPDF' : (0x4B, 'MACROMICROPDF'),
'RSS14'         : (0x4C, 'RSS14'),
'RSSLIM'        : (0x4D, 'RSSLIM'),
'RSSEXP'        : (0x4E, 'RSSEXP'),
'POINTER'       : (0x50, 'POINTER'),
'IMAGE'         : (0x51, 'IMAGE'),
'SIGNATURE'     : (0x52, 'SIGNATURE'),
'WEBCODE'       : (0x54, 'WEBCODE'),
'CUECODE'       : (0x55, 'CUECODE'),
'COMPOSITE_AB'  : (0x56, 'COMPOSITE_AB'),
'COMPOSITE_C'   : (0x57, 'COMPOSITE_C'),
'TLC39'         : (0x58, 'TLC39'),
'USPOSTNET'     : (0x61, 'USPOSTNET'),
'USPLANET'      : (0x62, 'USPLANET'),
'UKPOSTAL'      : (0x63, 'UKPOSTAL'),
'JAPPOSTAL'     : (0x64, 'JAPPOSTAL'),
'AUSPOSTAL'     : (0x65, 'AUSPOSTAL'),
'DUTCHPOSTAL'   : (0x66, 'DUTCHPOSTAL'),
'CANPOSTAL'     : (0x67, 'CANPOSTAL'),
'CHINESE_2OF5'  : (0x70, 'CHINESE_2OF5'),
'AZTEC'         : (0x74, 'AZTEC'),
'MICROQR'       : (0x75, 'MICROQR'),
'KOREAN_3OF5'   : (0x76, 'KOREAN_3OF5'),
'US4STATE'      : (0x77, 'US4STATE'),
"\x30"          : (0x30, 'UPCE0'),
"\x31"          : (0x31, 'UPCE1'),
"\x32"          : (0x32, 'UPCA'),
"\x33"          : (0x33, 'MSI'),
"\x34"          : (0x34, 'EAN8'),
"\x35"          : (0x35, 'EAN13'),
"\x36"          : (0x36, 'CODABAR'),
"\x37"          : (0x37, 'CODE39'),
"\x38"          : (0x38, 'D2OF5'),
"\x39"          : (0x39, 'I2OF5'),
"\x3A"          : (0x3A, 'CODE11'),
"\x3B"          : (0x3B, 'CODE93'),
"\x3C"          : (0x3C, 'CODE128'),
"\x40"          : (0x40, 'PDF417'),
"\x42"          : (0x42, 'TRIOPTIC39'),
"\x45"          : (0x45, 'MICROPDF'),
"\x47"          : (0x47, 'MACROPDF'),
"\x48"          : (0x48, 'MAXICODE'),
"\x49"          : (0x49, 'DATAMATRIX'),
"\x4A"          : (0x4A, 'QRCODE'),
"\x4B"          : (0x4B, 'MACROMICROPDF'),
"\x4C"          : (0x4C, 'RSS14'),
"\x4D"          : (0x4D, 'RSSLIM'),
"\x4E"          : (0x4E, 'RSSEXP'),
"\x50"          : (0x50, 'POINTER'),
"\x51"          : (0x51, 'IMAGE'),
"\x52"          : (0x52, 'SIGNATURE'),
"\x54"          : (0x54, 'WEBCODE'),
"\x55"          : (0x55, 'CUECODE'),
"\x56"          : (0x56, 'COMPOSITE_AB'),
"\x57"          : (0x57, 'COMPOSITE_C'),
"\x58"          : (0x58, 'TLC39'),
"\x61"          : (0x61, 'USPOSTNET'),
"\x62"          : (0x62, 'USPLANET'),
"\x63"          : (0x63, 'UKPOSTAL'),
"\x64"          : (0x64, 'JAPPOSTAL'),
"\x65"          : (0x65, 'AUSPOSTAL'),
"\x66"          : (0x66, 'DUTCHPOSTAL'),
"\x67"          : (0x67, 'CANPOSTAL'),
"\x70"          : (0x70, 'CHINESE_2OF5'),
"\x74"          : (0x74, 'AZTEC'),
"\x75"          : (0x75, 'MICROQR'),
"\x76"          : (0x76, 'KOREAN_3OF5'),
"\x77"          : (0x77, 'US4STATE'),
0x30            : (0x30, 'UPCE0'),
0x31            : (0x31, 'UPCE1'),
0x32            : (0x32, 'UPCA'),
0x33            : (0x33, 'MSI'),
0x34            : (0x34, 'EAN8'),
0x35            : (0x35, 'EAN13'),
0x36            : (0x36, 'CODABAR'),
0x37            : (0x37, 'CODE39'),
0x38            : (0x38, 'D2OF5'),
0x39            : (0x39, 'I2OF5'),
0x3A            : (0x3A, 'CODE11'),
0x3B            : (0x3B, 'CODE93'),
0x3C            : (0x3C, 'CODE128'),
0x40            : (0x40, 'PDF417'),
0x42            : (0x42, 'TRIOPTIC39'),
0x45            : (0x45, 'MICROPDF'),
0x47            : (0x47, 'MACROPDF'),
0x48            : (0x48, 'MAXICODE'),
0x49            : (0x49, 'DATAMATRIX'),
0x4A            : (0x4A, 'QRCODE'),
0x4B            : (0x4B, 'MACROMICROPDF'),
0x4C            : (0x4C, 'RSS14'),
0x4D            : (0x4D, 'RSSLIM'),
0x4E            : (0x4E, 'RSSEXP'),
0x50            : (0x50, 'POINTER'),
0x51            : (0x51, 'IMAGE'),
0x52            : (0x52, 'SIGNATURE'),
0x54            : (0x54, 'WEBCODE'),
0x55            : (0x55, 'CUECODE'),
0x56            : (0x56, 'COMPOSITE_AB'),
0x57            : (0x57, 'COMPOSITE_C'),
0x58            : (0x58, 'TLC39'),
0x61            : (0x61, 'USPOSTNET'),
0x62            : (0x62, 'USPLANET'),
0x63            : (0x63, 'UKPOSTAL'),
0x64            : (0x64, 'JAPPOSTAL'),
0x65            : (0x65, 'AUSPOSTAL'),
0x66            : (0x66, 'DUTCHPOSTAL'),
0x67            : (0x67, 'CANPOSTAL'),
0x70            : (0x70, 'CHINESE_2OF5'),
0x74            : (0x74, 'AZTEC'),
0x75            : (0x75, 'MICROQR'),
0x76            : (0x76, 'KOREAN_3OF5'),
0x77            : (0x77, 'US4STATE'),
}


LABELTYPE_UPCE0         = LABELTYPE(0x30)
LABELTYPE_UPCE1         = LABELTYPE(0x31)
LABELTYPE_UPCA          = LABELTYPE(0x32)
LABELTYPE_MSI           = LABELTYPE(0x33)
LABELTYPE_EAN8          = LABELTYPE(0x34)
LABELTYPE_EAN13         = LABELTYPE(0x35)
LABELTYPE_CODABAR       = LABELTYPE(0x36)
LABELTYPE_CODE39        = LABELTYPE(0x37)
LABELTYPE_D2OF5         = LABELTYPE(0x38)
LABELTYPE_I2OF5         = LABELTYPE(0x39)
LABELTYPE_CODE11        = LABELTYPE(0x3A)
LABELTYPE_CODE93        = LABELTYPE(0x3B)
LABELTYPE_CODE128       = LABELTYPE(0x3C)
LABELTYPE_IATA2OF5      = LABELTYPE(0x3E)
LABELTYPE_EAN128        = LABELTYPE(0x3F)
LABELTYPE_PDF417        = LABELTYPE(0x40)
LABELTYPE_ISBT128       = LABELTYPE(0x41)
LABELTYPE_TRIOPTIC39    = LABELTYPE(0x42)
LABELTYPE_COUPON        = LABELTYPE(0x43)
LABELTYPE_BOOKLAND      = LABELTYPE(0x44)
LABELTYPE_MICROPDF      = LABELTYPE(0x45)
LABELTYPE_CODE32        = LABELTYPE(0x46)
LABELTYPE_MACROPDF      = LABELTYPE(0x47)
LABELTYPE_MAXICODE      = LABELTYPE(0x48)
LABELTYPE_DATAMATRIX    = LABELTYPE(0x49)
LABELTYPE_QRCODE        = LABELTYPE(0x4A)
LABELTYPE_MACROMICROPDF = LABELTYPE(0x4B)
LABELTYPE_RSS14         = LABELTYPE(0x4C)
LABELTYPE_RSSLIM        = LABELTYPE(0x4D)
LABELTYPE_RSSEXP        = LABELTYPE(0x4E)
LABELTYPE_IMAGE         = LABELTYPE(0x51)
LABELTYPE_SIGNATURE     = LABELTYPE(0x52)
LABELTYPE_WEBCODE       = LABELTYPE(0x54)
LABELTYPE_CUECODE       = LABELTYPE(0x55)
LABELTYPE_COMPOSITE_AB  = LABELTYPE(0x56)
LABELTYPE_COMPOSITE_C   = LABELTYPE(0x57)
LABELTYPE_TLC39         = LABELTYPE(0x58)
LABELTYPE_USPOSTNET     = LABELTYPE(0x61)
LABELTYPE_USPLANET      = LABELTYPE(0x62)
LABELTYPE_UKPOSTAL      = LABELTYPE(0x63)
LABELTYPE_JAPPOSTAL     = LABELTYPE(0x64)
LABELTYPE_AUSPOSTAL     = LABELTYPE(0x65)
LABELTYPE_DUTCHPOSTAL   = LABELTYPE(0x66)
LABELTYPE_CANPOSTAL     = LABELTYPE(0x67)
LABELTYPE_CHINESE_2OF5  = LABELTYPE(0x70)
LABELTYPE_AZTEC         = LABELTYPE(0x74)
LABELTYPE_MICROQR       = LABELTYPE(0x75)
LABELTYPE_KOREAN_3OF5   = LABELTYPE(0x76)
LABELTYPE_US4STATE      = LABELTYPE(0x77)
LABELTYPE_UNKNOWN       = LABELTYPE(0xFF)


LABELTYPEXREF = {
'UPCE0'         : LABELTYPE(0x30),
'UPCE1'         : LABELTYPE(0x31),
'UPCA'          : LABELTYPE(0x32),
'MSI'           : LABELTYPE(0x33),
'EAN8'          : LABELTYPE(0x34),
'EAN13'         : LABELTYPE(0x35),
'CODABAR'       : LABELTYPE(0x36),
'CODE39'        : LABELTYPE(0x37),
'D2OF5'         : LABELTYPE(0x38),
'I2OF5'         : LABELTYPE(0x39),
'CODE11'        : LABELTYPE(0x3A),
'CODE93'        : LABELTYPE(0x3B),
'CODE128'       : LABELTYPE(0x3C),
'IATA2OF5'      : LABELTYPE(0x3E),
'EAN128'        : LABELTYPE(0x3F),
'PDF417'        : LABELTYPE(0x40),
'ISBT128'       : LABELTYPE(0x41),
'TRIOPTIC39'    : LABELTYPE(0x42),
'COUPON'        : LABELTYPE(0x43),
'BOOKLAND'      : LABELTYPE(0x44),
'MICROPDF'      : LABELTYPE(0x45),
'CODE32'        : LABELTYPE(0x46),
'MACROPDF'      : LABELTYPE(0x47),
'MAXICODE'      : LABELTYPE(0x48),
'DATAMATRIX'    : LABELTYPE(0x49),
'QRCODE'        : LABELTYPE(0x4A),
'MACROMICROPDF' : LABELTYPE(0x4B),
'RSS14'         : LABELTYPE(0x4C),
'RSSLIM'        : LABELTYPE(0x4D),
'RSSEXP'        : LABELTYPE(0x4E),
'IMAGE'         : LABELTYPE(0x51),
'SIGNATURE'     : LABELTYPE(0x52),
'WEBCODE'       : LABELTYPE(0x54),
'CUECODE'       : LABELTYPE(0x55),
'COMPOSITE_AB'  : LABELTYPE(0x56),
'COMPOSITE_C'   : LABELTYPE(0x57),
'TLC39'         : LABELTYPE(0x58),
'USPOSTNET'     : LABELTYPE(0x61),
'USPLANET'      : LABELTYPE(0x62),
'UKPOSTAL'      : LABELTYPE(0x63),
'JAPPOSTAL'     : LABELTYPE(0x64),
'AUSPOSTAL'     : LABELTYPE(0x65),
'DUTCHPOSTAL'   : LABELTYPE(0x66),
'CANPOSTAL'     : LABELTYPE(0x67),
'CHINESE_2OF5'  : LABELTYPE(0x70),
'AZTEC'         : LABELTYPE(0x74),
'MICROQR'       : LABELTYPE(0x75),
'KOREAN_3OF5'   : LABELTYPE(0x76),
'US4STATE'      : LABELTYPE(0x77),
'UNKNOWN'       : LABELTYPE(0xFF),
0x30 : 'UPCE0',
0x31 : 'UPCE1',
0x32 : 'UPCA',
0x33 : 'MSI',
0x34 : 'EAN8',
0x35 : 'EAN13',
0x36 : 'CODABAR',
0x37 : 'CODE39',
0x38 : 'D2OF5',
0x39 : 'I2OF5',
0x3A : 'CODE11',
0x3B : 'CODE93',
0x3C : 'CODE128',
0x3E : 'IATA2OF5',
0x3F : 'EAN128',
0x40 : 'PDF417',
0x41 : 'ISBT128',
0x42 : 'TRIOPTIC39',
0x43 : 'COUPON',
0x44 : 'BOOKLAND',
0x45 : 'MICROPDF',
0x46 : 'CODE32',
0x47 : 'MACROPDF',
0x48 : 'MAXICODE',
0x49 : 'DATAMATRIX',
0x4A : 'QRCODE',
0x4B : 'MACROMICROPDF',
0x4C : 'RSS14',
0x4D : 'RSSLIM',
0x4E : 'RSSEXP',
0x51 : 'IMAGE',
0x52 : 'SIGNATURE',
0x54 : 'WEBCODE',
0x55 : 'CUECODE',
0x56 : 'COMPOSITE_AB',
0x57 : 'COMPOSITE_C',
0x58 : 'TLC39',
0x61 : 'USPOSTNET',
0x62 : 'USPLANET',
0x63 : 'UKPOSTAL',
0x64 : 'JAPPOSTAL',
0x65 : 'AUSPOSTAL',
0x66 : 'DUTCHPOSTAL',
0x67 : 'CANPOSTAL',
0x70 : 'CHINESE_2OF5',
0x74 : 'AZTEC',
0x75 : 'MICROQR',
0x76 : 'KOREAN_3OF5',
0x77 : 'US4STATE',
0xFF : 'UNKNOWN',
}
        
