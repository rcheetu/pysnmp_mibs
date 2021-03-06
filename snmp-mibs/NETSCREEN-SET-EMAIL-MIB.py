# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-SET-EMAIL-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenSetting, netscreenSettingMibModule, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenSetEmailMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 7)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-10 00:00","2001-09-28 00:00","2001-05-27 00:00",))
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setDescription("This module defines the object that are used to monitor \nthe email notification setting")
nsSetEmail = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 7))
nsSetEmailEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailEnable.setDescription("Enable E-mail Notification for Alarms")
nsSetEmailSMTP = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailSMTP.setDescription("SMTP server name")
nsSetEmailLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailLog.setDescription("Include Traffic Log in email")
nsSetEmailAddr1 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr1.setDescription("E-mail receiver address one")
nsSetEmailAddr2 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr2.setDescription("E-mail receiver address two")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-SET-EMAIL-MIB", PYSNMP_MODULE_ID=netscreenSetEmailMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-SET-EMAIL-MIB", netscreenSetEmailMibModule=netscreenSetEmailMibModule, nsSetEmail=nsSetEmail, nsSetEmailEnable=nsSetEmailEnable, nsSetEmailSMTP=nsSetEmailSMTP, nsSetEmailLog=nsSetEmailLog, nsSetEmailAddr1=nsSetEmailAddr1, nsSetEmailAddr2=nsSetEmailAddr2)

