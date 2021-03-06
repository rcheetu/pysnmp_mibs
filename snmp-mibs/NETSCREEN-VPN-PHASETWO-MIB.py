# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-VPN-PHASETWO-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:57 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenVpn, netscreenVpnMibModule, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn", "netscreenVpnMibModule")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenVpnPhasetwoMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 4, 0, 6)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-13 00:00","2001-09-28 00:00","2001-05-14 00:00",))
if mibBuilder.loadTexts: netscreenVpnPhasetwoMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenVpnPhasetwoMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenVpnPhasetwoMibModule.setDescription("This module defines NetScreen private MIBs for VPN Phase two\nnegotiation.")
nsVpnPhaseTwoCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 6))
nsVpnPhTwoTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1))
if mibBuilder.loadTexts: nsVpnPhTwoTable.setDescription("To establish an IKE IPSec tunnel, two phases of negotiation\nare required. This table specifies the configuration attributes\nfor Phase Two negotiation. In Phase 2, the participants\nnegotiate the IPSec SAs for encrypting and  authenticating the\nensuing exchanges of user data.")
nsVpnPhTwoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1)).setIndexNames((0, "NETSCREEN-VPN-PHASETWO-MIB", "nsVpnPhTwoIndex"))
if mibBuilder.loadTexts: nsVpnPhTwoEntry.setDescription("Each entry in the nsVpnPhTwoTable holds a set of configuration\nparameters associated with an instance of Phase 2 setting.")
nsVpnPhTwoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoIndex.setDescription("A unique value for phase Two table.  Its value ranges between\n1 and 65535 and may not be contiguous.  The index has no other\nmeaning but a pure index")
nsVpnPhTwoName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoName.setDescription("Phase two proposal name.")
nsVpnPhTwoPFS = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoPFS.setDescription("Perfect Forward Secrecy - Diffie-Hellman exchange group.")
nsVpnPhTwoEncapMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("ah", 0), ("esp", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoEncapMethod.setDescription("Phase two proposal encapsulation method.")
nsVpnPhTwoESPEncryp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(3,5,1,4,2,0,)).subtype(namedValues=NamedValues(("null", 0), ("des", 1), ("triple-des", 2), ("aes", 3), ("aes-192", 4), ("aes-256", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoESPEncryp.setDescription("Phase two proposal ESP encryption algorithm.")
nsVpnPhTwoESPAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(2,0,3,1,)).subtype(namedValues=NamedValues(("null", 0), ("md5", 1), ("sha", 2), ("sha-256", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoESPAuth.setDescription("Phase two proposal ESP authentication Algorithm.")
nsVpnPhTwoAhAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,0,1,)).subtype(namedValues=NamedValues(("null", 0), ("md5", 1), ("sha", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoAhAuth.setDescription("Phase two proposal AH authentication Algorithm.")
nsVpnPhTwoLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoLifetime.setDescription("Lifetime in time")
nsVpnPhTwoLifetimeMeasure = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(2,0,3,1,)).subtype(namedValues=NamedValues(("second", 0), ("minute", 1), ("hours", 2), ("days", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoLifetimeMeasure.setDescription("life time measurement.")
nsVpnPhTwoLifetimeKb = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoLifetimeKb.setDescription("Lifetime in KBytes")
nsVpnPhTwoVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhTwoVsys.setDescription("vsys this proposal configuration belongs to.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-VPN-PHASETWO-MIB", PYSNMP_MODULE_ID=netscreenVpnPhasetwoMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-VPN-PHASETWO-MIB", netscreenVpnPhasetwoMibModule=netscreenVpnPhasetwoMibModule, nsVpnPhaseTwoCfg=nsVpnPhaseTwoCfg, nsVpnPhTwoTable=nsVpnPhTwoTable, nsVpnPhTwoEntry=nsVpnPhTwoEntry, nsVpnPhTwoIndex=nsVpnPhTwoIndex, nsVpnPhTwoName=nsVpnPhTwoName, nsVpnPhTwoPFS=nsVpnPhTwoPFS, nsVpnPhTwoEncapMethod=nsVpnPhTwoEncapMethod, nsVpnPhTwoESPEncryp=nsVpnPhTwoESPEncryp, nsVpnPhTwoESPAuth=nsVpnPhTwoESPAuth, nsVpnPhTwoAhAuth=nsVpnPhTwoAhAuth, nsVpnPhTwoLifetime=nsVpnPhTwoLifetime, nsVpnPhTwoLifetimeMeasure=nsVpnPhTwoLifetimeMeasure, nsVpnPhTwoLifetimeKb=nsVpnPhTwoLifetimeKb, nsVpnPhTwoVsys=nsVpnPhTwoVsys)

