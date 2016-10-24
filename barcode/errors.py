# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 John Hampton <pacopablo@pacopablo.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: John Hampton <pacopablo@pacopablo.com>

__all__ = [
# Return Codes
"E_SCN_SUCCESS",
"E_SCN_OPENINGACTIVEKEY",
"E_SCN_READINGACTIVEKEY",
"E_SCN_OPENINGPARAMKEY",
"E_SCN_READINGPARAMKEY",
"E_SCN_NOTENOUGHMEMORY",
"E_SCN_INVALIDDVCCONTEXT",
"E_SCN_INVALIDOPENCONTEXT",
"E_SCN_NOTINITIALIZED",
"E_SCN_CANTLOADDEVICE",
"E_SCN_INVALIDDEVICE",
"E_SCN_DEVICEFAILURE",
"E_SCN_CANTSTARTDEVICE",
"E_SCN_CANTGETDEFAULTS",
"E_SCN_NOTSTARTED",
"E_SCN_ALREADYSTARTED",
"E_SCN_NOTENABLED",
"E_SCN_ALREADYENABLED",
"E_SCN_INVALIDIOCTRL",
"E_SCN_NULLPTR",
"E_SCN_INVALIDARG",
"E_SCN_BUFFERSIZEIN",
"E_SCN_BUFFERSIZEOUT",
"E_SCN_STRUCTSIZE",
"E_SCN_MISSINGFIELD",
"E_SCN_INVALIDHANDLE",
"E_SCN_INVALIDPARAM",
"E_SCN_CREATEEVENT",
"E_SCN_CREATETHREAD",
"E_SCN_READCANCELLED",
"E_SCN_READTIMEOUT",
"E_SCN_READNOTPENDING",
"E_SCN_READPENDING",
"E_SCN_BUFFERTOOSMALL",
"E_SCN_INVALIDSCANBUFFER",
"E_SCN_READINCOMPATIBLE",
"E_SCN_NOFEEDBACK",
"E_SCN_NOTSUPPORTED",
"E_SCN_WRONGSTATE",
"E_SCN_NOMOREITEMS",
"E_SCN_CANTOPENREGKEY",
"E_SCN_CANTREADREGVAL",
"E_SCN_EXCEPTION",
"E_SCN_WIN32ERROR",
"E_SCN_ALREADYINUSE",
"E_SCN_NOTINUSE",
"E_SCN_CANTLOADDECODERDLL",
"E_SCN_INVALIDDECODERDLL",
"E_SCN_INVALIDSYMBOL",
"E_SCN_INVALIDLICENSE",
"E_SCN_NOTINSEQUENCE",
"E_SCN_DUPLICATESYMBOL",
"E_SCN_CANTLOADHALDLL",
"E_SCN_INVALIDHALDLL",
"E_SCN_CANTLOADCOMPRESSIONDLL",
"E_SCN_I2CFAILURE",
]

# Return Code Definitions 

# The function completed successfully
E_SCN_SUCCESS                = 0x00000000

# An error occurred opening the active driver registry key.
E_SCN_OPENINGACTIVEKEY       = 0xA0000001

# An error occurred reading the active driver registry key.
E_SCN_READINGACTIVEKEY       = 0xA0000002

# An error occurred opening the registry key containing the driver's settings.
E_SCN_OPENINGPARAMKEY        = 0xA0000003

# An error occurred reading the registry key containing the driver's settings.
E_SCN_READINGPARAMKEY        = 0xA0000004

# An attempt to allocate memory failed.
E_SCN_NOTENOUGHMEMORY        = 0xA0000005

# An invalid device context ID was used.
E_SCN_INVALIDDVCCONTEXT      = 0xA0000006

# An attempt was made to access an invalid open context.
E_SCN_INVALIDOPENCONTEXT     = 0xA0000007

# The driver was accessed before a successful initialization.
E_SCN_NOTINITIALIZED         = 0xA0000008

# The physical device driver (PDD) could not be loaded.
E_SCN_CANTLOADDEVICE         = 0xA0000009

# The physical device driver (PDD) DLL did not contain the required entry 
# points.
E_SCN_INVALIDDEVICE          = 0xA000000A

# Required device is not present, already in use or not functioning properly.
E_SCN_DEVICEFAILURE          = 0xA000000B

# The device could not be started.
E_SCN_CANTSTARTDEVICE        = 0xA000000C

# The default parameters could not be obtained from the physical device driver
# (PDD).
E_SCN_CANTGETDEFAULTS        = 0xA000000D

# An attempt was made to use or stop the scanner device and it was not started.
E_SCN_NOTSTARTED             = 0xA000000E

# An attempt was made to start the device when the device was already started.
E_SCN_ALREADYSTARTED         = 0xA000000F

# An attempt was made to access the scanner device and it was not enabled.
E_SCN_NOTENABLED             = 0xA0000010

# An attempt was made to enable scanning when scanning was already enabled.
E_SCN_ALREADYENABLED         = 0xA0000011

# The control code passed to DeviceIoControl is invalid.
E_SCN_INVALIDIOCTRL          = 0xA0000012

# A NULL pointer was passed for a required argument
E_SCN_NULLPTR                = 0xA0000013

# A passed argument is out of range.
E_SCN_INVALIDARG             = 0xA0000014

# The size of the buffer passed as an input to DeviceIoControl is less than
# sizeof(STRUCT_INFO) or is less than the size specified in StructInfo.dwUsed.
E_SCN_BUFFERSIZEIN           = 0xA0000015

# The size of the buffer passed as an output to DeviceIoControl is less than
# sizeof(STRUCT_INFO) or is less than the size specified in 
# StructInfo.dwAllocated.
E_SCN_BUFFERSIZEOUT          = 0xA0000016

# A STRUCT_INFO structure field is invalid. Either dwAllocated or dwUsed is 
# less than the size of STRUCT_INFO or dwUsed is greater than dwAllocated.
E_SCN_STRUCTSIZE             = 0xA0000017

# The size of a structure specified in a StructInfo is too small to contain a
# required field.
E_SCN_MISSINGFIELD           = 0xA0000018

# An invalid handle was passed to a function.
E_SCN_INVALIDHANDLE          = 0xA0000019

# The value of a parameter either passed as an argument to a function or as a
# member of a structure is out of range or conflicts with other parameters.
E_SCN_INVALIDPARAM           = 0xA000001A

# Unable to create a required event.
E_SCN_CREATEEVENT            = 0xA000001B

# Unable to create a required thread.
E_SCN_CREATETHREAD           = 0xA000001C

# A read request was cancelled.
E_SCN_READCANCELLED          = 0xA000001D

# A read request timed out.
E_SCN_READTIMEOUT            = 0xA000001E

# Attempt to cancel a read that is not pending.
E_SCN_READNOTPENDING         = 0xA000001F

# Attempt to start a read when one is pending.
E_SCN_READPENDING            = 0xA0000020

# Data buffer is too small for incoming data.
E_SCN_BUFFERTOOSMALL         = 0xA0000021

# Attempt to access fields of an invalid scan buffer.
E_SCN_INVALIDSCANBUFFER      = 0xA0000022

# Attempt to submit a read that is incompatible with reads already queued.
E_SCN_READINCOMPATIBLE       = 0xA0000023

# Attempt to perform physical device driver (PDD) feedback with no feedback
# capabilities.
E_SCN_NOFEEDBACK             = 0xA0000024

# Version of function not supported (e.g. ANSI vs. UNICODE).
E_SCN_NOTSUPPORTED           = 0xA0000026

# The requested operation is inconsistent with the current state of the device.
E_SCN_WRONGSTATE             = 0xA0000027

# No more items are available to be returned from SCAN_FindFirst/SCAN_FindNext.
E_SCN_NOMOREITEMS            = 0xA0000028

# A required registry key could not be opened.
E_SCN_CANTOPENREGKEY         = 0xA0000029

# A required registry value could not be read.
E_SCN_CANTREADREGVAL         = 0xA000002A

# An exception occurred while trying to call the scanner driver.
E_SCN_EXCEPTION              = 0xA000002B

# A scanner API function failed with a non-scanner API error code. Call
# GetLastError to get extended error code.
E_SCN_WIN32ERROR             = 0xA000002C

# A requested scanner resource is already in use.
E_SCN_ALREADYINUSE           = 0xA000002D

# The specified scanner resource was not allocated.
E_SCN_NOTINUSE               = 0xA000002E

# The specified decoder DLL can not be loaded.
E_SCN_CANTLOADDECODERDLL     = 0xA000002F

# At least one API is missing in Decoder DLL.
E_SCN_INVALIDDECODERDLL      = 0xA0000030

# The symbol's format is invalid.
E_SCN_INVALIDSYMBOL          = 0xA0000031

# The platform does not have a valid license key.
E_SCN_INVALIDLICENSE         = 0xA0000032

# The scanned macro symbol is not part of the current macro sequence.
E_SCN_NOTINSEQUENCE          = 0xA0000033

# The scanned macro symbol has already been scanned into the current macro
# sequence.
E_SCN_DUPLICATESYMBOL        = 0xA0000034

# The Image HAL DLL can not be loaded.
E_SCN_CANTLOADHALDLL         = 0xA0000035

# At least one API function is missing in Image HAL DLL.
E_SCN_INVALIDHALDLL          = 0xA0000036

# The Image Compression DLL can not be loaded.
E_SCN_CANTLOADCOMPRESSIONDLL = 0xA0000037

# I2C communication failed
E_SCN_I2CFAILURE             = 0xA0000038

 
