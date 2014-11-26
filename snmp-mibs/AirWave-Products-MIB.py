# PySNMP SMI module. Autogenerated from smidump -f python AirWave-Products-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jun  3 12:38:35 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( airwaveModules, airwaveProducts, ) = mibBuilder.importSymbols("AirWave-SMI-MIB", "airwaveModules", "airwaveProducts")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks")

# Objects

airwaveAMP = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 1, 1))
if mibBuilder.loadTexts: airwaveAMP.setDescription("AirWave Management Platform.")
airwaveOemAMP = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 1, 2))
if mibBuilder.loadTexts: airwaveOemAMP.setDescription("OEM version of AirWave Management Platform.")
airwaveAML = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 1, 3))
if mibBuilder.loadTexts: airwaveAML.setDescription("AirWave Management Link NMS plugin.")
airwaveSnmpLibrary = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 1, 4))
if mibBuilder.loadTexts: airwaveSnmpLibrary.setDescription("AirWave's SNMP library.")
airwaveProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12028, 2, 1)).setRevisions(("2011-12-19 00:00","2003-04-17 00:01",))
if mibBuilder.loadTexts: airwaveProductsMIB.setOrganization("AirWave Wireless")
if mibBuilder.loadTexts: airwaveProductsMIB.setContactInfo("        Paul Gray\n\nPostal: Aruba Networks, Inc.\n        1344 Crossman Ave\n        Sunnyvale, CA 94402\n        \n   Tel: +1 408 227 4500\n   \n Email: paul@arubanetworks.com\n   Web: http://www.arubanetworks.com/")
if mibBuilder.loadTexts: airwaveProductsMIB.setDescription("AirWave product line.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("AirWave-Products-MIB", PYSNMP_MODULE_ID=airwaveProductsMIB)

# Objects
mibBuilder.exportSymbols("AirWave-Products-MIB", airwaveAMP=airwaveAMP, airwaveOemAMP=airwaveOemAMP, airwaveAML=airwaveAML, airwaveSnmpLibrary=airwaveSnmpLibrary, airwaveProductsMIB=airwaveProductsMIB)
