# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-SCU-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( Bits, Counter64, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

jnxScu = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 16)).setRevisions(("2003-07-18 21:53","2002-02-25 00:00",))
if mibBuilder.loadTexts: jnxScu.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxScu.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxScu.setDescription("This is Juniper Networks' enterprise-specific MIB for \nSource Class Usage (SCU)")
jnxScuStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1))
jnxScuStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1))
if mibBuilder.loadTexts: jnxScuStatsTable.setDescription("A list of SCUs entries.")
jnxScuStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1)).setIndexNames((0, "JUNIPER-SCU-MIB", "jnxScuStatsDstIfIndex"), (0, "JUNIPER-SCU-MIB", "jnxScuStatsAddrFamily"), (0, "JUNIPER-SCU-MIB", "jnxScuStatsClassName"))
if mibBuilder.loadTexts: jnxScuStatsEntry.setDescription("An entry of SCUs table.")
jnxScuStatsDstIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxScuStatsDstIfIndex.setDescription("The destination interface index.  This is the egress interface \nof traffic that is counted by this table entry.")
jnxScuStatsAddrFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxScuStatsAddrFamily.setDescription("The address family of this entry's traffic.")
jnxScuStatsClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 112))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxScuStatsClassName.setDescription("The name of the source class.  All traffic counted in this\ntable entry satisfies the requirements defined by this\nsource class.")
jnxScuStatsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxScuStatsPackets.setDescription("The number of packets sent out of jnxScuStatsDstIfIndex that\nmatch the source class (jnxScuStatsClassName) and match\nthe address type (jnxScuStatsAddrFamily) defined for this \ntable entry.")
jnxScuStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxScuStatsBytes.setDescription("The number of bytes sent out of jnxScuStatsDstIfIndex that\nmatch the source class (jnxScuStatsClassName) and match\nthe address type (jnxScuStatsAddrFamily) defined for this \ntable entry.")
jnxScuStatsClName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 112))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxScuStatsClName.setDescription("The name of the source class.  This object is a duplicate\nof jnxScuStatsClassName and is included to satisfy those\nNM applications that can't extract the class name from the\ninstance portion of the OID.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-SCU-MIB", PYSNMP_MODULE_ID=jnxScu)

# Objects
mibBuilder.exportSymbols("JUNIPER-SCU-MIB", jnxScu=jnxScu, jnxScuStats=jnxScuStats, jnxScuStatsTable=jnxScuStatsTable, jnxScuStatsEntry=jnxScuStatsEntry, jnxScuStatsDstIfIndex=jnxScuStatsDstIfIndex, jnxScuStatsAddrFamily=jnxScuStatsAddrFamily, jnxScuStatsClassName=jnxScuStatsClassName, jnxScuStatsPackets=jnxScuStatsPackets, jnxScuStatsBytes=jnxScuStatsBytes, jnxScuStatsClName=jnxScuStatsClName)
