# PySNMP SMI module. Autogenerated from smidump -f python UCD-DLMOD-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")
( ucdExperimental, ) = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")

# Objects

ucdDlmodMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 14)).setRevisions(("1999-12-10 00:00",))
if mibBuilder.loadTexts: ucdDlmodMIB.setOrganization("University of California, Davis")
if mibBuilder.loadTexts: ucdDlmodMIB.setContactInfo("This mib is no longer being maintained by the University of\nCalifornia and is now in life-support-mode and being\nmaintained by the net-snmp project.  The best place to write\nfor public questions about the net-snmp-coders mailing list\nat net-snmp-coders@lists.sourceforge.net.\n\npostal:   Wes Hardaker\n         P.O. Box 382\n         Davis CA  95617\n\nemail:    net-snmp-coders@lists.sourceforge.net")
if mibBuilder.loadTexts: ucdDlmodMIB.setDescription("This file defines the MIB objects for dynamic \nloadable MIB modules.")
dlmodNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2021, 13, 14, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmodNextIndex.setDescription("The index number of next appropiate unassigned entry\nin the dlmodTable.")
dlmodTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2))
if mibBuilder.loadTexts: dlmodTable.setDescription("A table of dlmodEntry.")
dlmodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1)).setIndexNames((0, "UCD-DLMOD-MIB", "dlmodIndex"))
if mibBuilder.loadTexts: dlmodEntry.setDescription("The parameters of dynamically loaded MIB module.")
dlmodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: dlmodIndex.setDescription("An index that uniqely identifies an entry in the dlmodTable.")
dlmodName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodName.setDescription("The module name.")
dlmodPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodPath.setDescription("The path of the module executable file.")
dlmodError = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmodError.setDescription("The last error from dlmod_load_module.")
dlmodStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(4,7,1,6,3,2,5,)).subtype(namedValues=NamedValues(("loaded", 1), ("unloaded", 2), ("error", 3), ("load", 4), ("unload", 5), ("create", 6), ("delete", 7), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodStatus.setDescription("The current status of the loaded module.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("UCD-DLMOD-MIB", PYSNMP_MODULE_ID=ucdDlmodMIB)

# Objects
mibBuilder.exportSymbols("UCD-DLMOD-MIB", ucdDlmodMIB=ucdDlmodMIB, dlmodNextIndex=dlmodNextIndex, dlmodTable=dlmodTable, dlmodEntry=dlmodEntry, dlmodIndex=dlmodIndex, dlmodName=dlmodName, dlmodPath=dlmodPath, dlmodError=dlmodError, dlmodStatus=dlmodStatus)
