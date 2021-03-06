/*
//-
// ==========================================================================
// Copyright (C) 1995 - 2006 Autodesk, Inc. and/or its licensors.  All 
// rights reserved.
//
// The coded instructions, statements, computer programs, and/or related 
// material (collectively the "Data") in these files contain unpublished 
// information proprietary to Autodesk, Inc. ("Autodesk") and/or its 
// licensors, which is protected by U.S. and Canadian federal copyright 
// law and by international treaties.
//
// The Data is provided for use exclusively by You. You have the right 
// to use, modify, and incorporate this Data into other products for 
// purposes authorized by the Autodesk software license agreement, 
// without fee.
//
// The copyright notices in the Software and this entire statement, 
// including the above license grant, this restriction and the 
// following disclaimer, must be included in all copies of the 
// Software, in whole or in part, and all derivative works of 
// the Software, unless such copies or derivative works are solely 
// in the form of machine-executable object code generated by a 
// source language processor.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. 
// AUTODESK DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR IMPLIED 
// WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES OF 
// NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
// PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR 
// TRADE PRACTICE. IN NO EVENT WILL AUTODESK AND/OR ITS LICENSORS 
// BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
// DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF AUTODESK 
// AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
// OR PROBABILITY OF SUCH DAMAGES.
//
// ==========================================================================
//+
*/

#ifndef _WIN32
#include <maya/mocapserver.h>
#else
#include <mocapserver.h>
#endif

#define kScaleStride 3
enum channelInfoOpCode {
	kInvalid    = -999,
	kFactors    = -5,
	kStartParse = -4,
	kEndParse   = -3,
	kUnit       = -2,
	kRotOrder   = -1,
	
};

enum channelInfoAxis {
	kInval = -1,
	kXAxis = 0,
	kYAxis = 1,
	kZAxis = 2
};

enum channelScaleOffsetType {

	kOffset = 0,
	kMult   = 1
};
enum channelUsageType {
	kPosQuat  = -3,
	kPosRot   = -2,
	kRotation = 0,
	kPosition = 1,
	kScale    = 2,
};

enum channelInfoUnitType {
	kUnitRot,
	kUnitPos
};

typedef struct {
	const char *shortName;
	const char *longName;
	CapChannelUsage use;
	union {
		int dim;
		int count;
	} p1;

	union {
		int  extra;
		int  opCode;
	} p2;

	union {
		int axisOffset;
		int factorType;
	} p3;

	int typeOffset;

} channelParseInfo;

typedef struct channelParseUnits {
	const char  *shortName;
	const char  *longName;
	int	   parm;
	float value;
} channelParseUnits;

typedef struct {
	char  *shortName;
	char  *longName;
	CapRotationOrder   value;
} channelParseRotOrder;

typedef struct channelInfo {
	CapChannel       chan;
	channelParseInfo *info;
	int	             startingCol;
	float            factors[2][3][3];
	CapRotationOrder rotOrder;
	float			 *data; /* numColumn entries */
	char			 *name; /* string of exactly strlen(name) +1 */
	struct channelInfo *next;
} channelInfo;

void channelInfoSetData(channelInfo *chan, int follow, float *rawData);
channelInfo *channelInfoCreate(FILE *configFile, 
							   int lookForBegin,
							   channelInfo *head);
