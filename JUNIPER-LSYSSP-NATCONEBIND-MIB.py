# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-LSYSSP-NATCONEBIND-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:52 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxLsysSpNATconebind, ) = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATconebind")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxLsysSpNATconebindMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1)).setRevisions(("2010-05-19 16:44",))
if mibBuilder.loadTexts: jnxLsysSpNATconebindMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxLsysSpNATconebindMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\n\nE-mail: support@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: jnxLsysSpNATconebindMIB.setDescription("This module defines the NAT-cone-bind-specific MIB for \nJuniper Enterprise Logical-System (LSYS) security profiles.  \nJuniper documentation is recommended as the reference. \n\nThe LSYS security profile provides various static and dynamic \nresource management by observing resource quota limits. \nSecurity NAT-cone-bind resource is the focus in this MIB. ")
jnxLsysSpNATconebindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1))
jnxLsysSpNATconebindTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1))
if mibBuilder.loadTexts: jnxLsysSpNATconebindTable.setDescription("LSYSPROFILE NAT-cone-bind objects for NAT-cone-bind \nresource consumption per LSYS.")
jnxLsysSpNATconebindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1)).setIndexNames((1, "JUNIPER-LSYSSP-NATCONEBIND-MIB", "jnxLsysSpNATconebindLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATconebindEntry.setDescription("An entry in NAT-cone-bind resource table.")
jnxLsysSpNATconebindLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxLsysSpNATconebindLsysName.setDescription("The name of the logical system for which NAT-cone-bind \nresource information is retrieved. ")
jnxLsysSpNATconebindProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindProfileName.setDescription("The security profile name string for the LSYS.")
jnxLsysSpNATconebindUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindUsage.setDescription("The current resource usage count for the LSYS.")
jnxLsysSpNATconebindReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindReserved.setDescription("The reserved resource count for the LSYS.")
jnxLsysSpNATconebindMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindMaximum.setDescription("The maximum allowed resource usage count for the LSYS.")
jnxLsysSpNATconebindSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2))
jnxLsysSpNATconebindUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindUsedAmount.setDescription("The NAT-cone-bind resource consumption over all LSYS.")
jnxLsysSpNATconebindMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindMaxQuota.setDescription("The NAT-cone-bind resource maximum quota for the whole \ndevice for all LSYS.")
jnxLsysSpNATconebindAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindAvailableAmount.setDescription("The NAT-cone-bind resource available in the whole device.")
jnxLsysSpNATconebindHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindHeaviestUsage.setDescription("The most amount of NAT-cone-bind resource consumed of a \nLSYS.")
jnxLsysSpNATconebindHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindHeaviestUser.setDescription("The LSYS name that consume the most NAT-cone-bind resource.")
jnxLsysSpNATconebindLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindLightestUsage.setDescription("The least amount of NAT-cone-bind resource consumed of a \nLSYS.")
jnxLsysSpNATconebindLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATconebindLightestUser.setDescription("The LSYS name that consume the least NAT-cone-bind resource.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATCONEBIND-MIB", PYSNMP_MODULE_ID=jnxLsysSpNATconebindMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATCONEBIND-MIB", jnxLsysSpNATconebindMIB=jnxLsysSpNATconebindMIB, jnxLsysSpNATconebindObjects=jnxLsysSpNATconebindObjects, jnxLsysSpNATconebindTable=jnxLsysSpNATconebindTable, jnxLsysSpNATconebindEntry=jnxLsysSpNATconebindEntry, jnxLsysSpNATconebindLsysName=jnxLsysSpNATconebindLsysName, jnxLsysSpNATconebindProfileName=jnxLsysSpNATconebindProfileName, jnxLsysSpNATconebindUsage=jnxLsysSpNATconebindUsage, jnxLsysSpNATconebindReserved=jnxLsysSpNATconebindReserved, jnxLsysSpNATconebindMaximum=jnxLsysSpNATconebindMaximum, jnxLsysSpNATconebindSummary=jnxLsysSpNATconebindSummary, jnxLsysSpNATconebindUsedAmount=jnxLsysSpNATconebindUsedAmount, jnxLsysSpNATconebindMaxQuota=jnxLsysSpNATconebindMaxQuota, jnxLsysSpNATconebindAvailableAmount=jnxLsysSpNATconebindAvailableAmount, jnxLsysSpNATconebindHeaviestUsage=jnxLsysSpNATconebindHeaviestUsage, jnxLsysSpNATconebindHeaviestUser=jnxLsysSpNATconebindHeaviestUser, jnxLsysSpNATconebindLightestUsage=jnxLsysSpNATconebindLightestUsage, jnxLsysSpNATconebindLightestUser=jnxLsysSpNATconebindLightestUser)
