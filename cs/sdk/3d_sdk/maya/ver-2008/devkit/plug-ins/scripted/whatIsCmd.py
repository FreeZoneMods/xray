
#-
# ==========================================================================
# Copyright (C) 1995 - 2006 Autodesk, Inc. and/or its licensors.  All 
# rights reserved.
#
# The coded instructions, statements, computer programs, and/or related 
# material (collectively the "Data") in these files contain unpublished 
# information proprietary to Autodesk, Inc. ("Autodesk") and/or its 
# licensors, which is protected by U.S. and Canadian federal copyright 
# law and by international treaties.
#
# The Data is provided for use exclusively by You. You have the right 
# to use, modify, and incorporate this Data into other products for 
# purposes authorized by the Autodesk software license agreement, 
# without fee.
#
# The copyright notices in the Software and this entire statement, 
# including the above license grant, this restriction and the 
# following disclaimer, must be included in all copies of the 
# Software, in whole or in part, and all derivative works of 
# the Software, unless such copies or derivative works are solely 
# in the form of machine-executable object code generated by a 
# source language processor.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. 
# AUTODESK DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR IMPLIED 
# WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES OF 
# NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
# PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR 
# TRADE PRACTICE. IN NO EVENT WILL AUTODESK AND/OR ITS LICENSORS 
# BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
# DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF AUTODESK 
# AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
# OR PROBABILITY OF SUCH DAMAGES.
#
# ==========================================================================
#+

import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

# import maya.cmds
# maya.cmds.loadPlugin("whatIsCmd.py")
# maya.cmds.spWhatIs()

kPluginCmdName = "spWhatIs"

print "whatIsCmd.py has been imported...."

# command
class scriptedCommand(OpenMayaMPx.MPxCommand):
	def __init__(self):
		print "scriptedCommand.__init__()"
		OpenMayaMPx.MPxCommand.__init__(self)
	def doIt(self, args):
		print "doIt..."
		selectList = OpenMaya.MSelectionList()
	
		OpenMaya.MGlobal.getActiveSelectionList( selectList )
		
		node = OpenMaya.MObject()
		depFn = OpenMaya.MFnDependencyNode()
		
		iter = OpenMaya.MItSelectionList(selectList)

		while (iter.isDone() == 0):			
			iter.getDependNode( node )
			
			depFn.setObject(node)
			
			name = depFn.name()
			types = []
			OpenMaya.MGlobal.getFunctionSetList( node, types )
			
			print "Name: %s" % name
			print "Type: %s" % node.apiTypeStr()
			sys.stdout.write( "Function Sets: " )
			
			last = len( types )
			
			for i in range(0, last):
				if i > 0:
					sys.stdout.write( ", " )
				sys.stdout.write( "%s " % types[i] )
				
			sys.stdout.write( '\n' )
			
			iter.next()
		
# Creator
def cmdCreator():
	return OpenMayaMPx.asMPxPtr( scriptedCommand() )
	
# Initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerCommand( kPluginCmdName, cmdCreator )
	except:
		sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand( kPluginCmdName )
	except:
		sys.stderr.write( "Failed to unregister command: %s\n" % kPluginCmdName )

