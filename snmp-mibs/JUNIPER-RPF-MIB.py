# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-RPF-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
( Bits, Counter64, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

jnxRpf = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 17)).setRevisions(("2003-07-18 21:53","2002-02-25 00:00",))
if mibBuilder.loadTexts: jnxRpf.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxRpf.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxRpf.setDescription("This is Juniper Networks' enterprise-specific MIB for \nReverse Path Forwarding (RPF)")
jnxRpfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1))
jnxRpfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1))
if mibBuilder.loadTexts: jnxRpfStatsTable.setDescription("This table contains statistics for traffic that is rejected\ndue to RPF processing.")
jnxRpfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1)).setIndexNames((0, "JUNIPER-RPF-MIB", "jnxRpfStatsIfIndex"), (0, "JUNIPER-RPF-MIB", "jnxRpfStatsAddrFamily"))
if mibBuilder.loadTexts: jnxRpfStatsEntry.setDescription("Each entry in this table counts RPF-rejected traffic that\nis received on a particular interface and belongs to a\nparticular address family.")
jnxRpfStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxRpfStatsIfIndex.setDescription("The ingress interface for traffic that is counted in this\nRpfStats entry.")
jnxRpfStatsAddrFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxRpfStatsAddrFamily.setDescription("The address family of this entry's traffic.")
jnxRpfStatsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRpfStatsPackets.setDescription("The number of packets received on this interface, belonging\nto this address family, that have been rejected due to RPF\nprocessing.")
jnxRpfStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRpfStatsBytes.setDescription("The number of bytes received on this interface, belonging\nto this address family, that have been rejected due to RPF\nprocessing.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-RPF-MIB", PYSNMP_MODULE_ID=jnxRpf)

# Objects
mibBuilder.exportSymbols("JUNIPER-RPF-MIB", jnxRpf=jnxRpf, jnxRpfStats=jnxRpfStats, jnxRpfStatsTable=jnxRpfStatsTable, jnxRpfStatsEntry=jnxRpfStatsEntry, jnxRpfStatsIfIndex=jnxRpfStatsIfIndex, jnxRpfStatsAddrFamily=jnxRpfStatsAddrFamily, jnxRpfStatsPackets=jnxRpfStatsPackets, jnxRpfStatsBytes=jnxRpfStatsBytes)

