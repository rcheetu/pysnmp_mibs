# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-SIP-COMMON-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
( jnxVoip, ) = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxVoip")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxSip = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2))
jnxSipCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1)).setRevisions(("2009-02-09 20:00",))
if mibBuilder.loadTexts: jnxSipCommonMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxSipCommonMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxSipCommonMIB.setDescription("This is Juniper Networks' implementation of enterprise specific\nMIB for SIP. This module defines objects which may be common to\nall SIP entities.")
jnxSipCommonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1))
jnxSipCommonCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1))
if mibBuilder.loadTexts: jnxSipCommonCfgTable.setDescription("This table contains the common configuration objects applicable\nto all SIP entities.")
jnxSipCommonCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1)).setIndexNames((0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCfgApplName"))
if mibBuilder.loadTexts: jnxSipCommonCfgEntry.setDescription("A row of common configuration.\n\nEach row represents objects for a particular SIP entity\ninstance present in this system.")
jnxSipCfgApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipCfgApplName.setDescription("The name of the network application which uniquely\nidentifies the application to which this entry is\napplicable.")
jnxSipCommonCfgProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgProtocolVersion.setDescription("This object will reflect the version of SIP supported by this\nSIP entity.  It will follow the same format as SIP version\ninformation contained in the SIP messages generated by this SIP\nentity.  For example, entities supporting SIP version 2 will\nreturn 'SIP/2.0' as dictated by the standard.")
jnxSipCommonCfgServiceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,)).subtype(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgServiceOperStatus.setDescription("This object contains the current operational state of\nthe  SIP application.\n\nunknown    : The operational status cannot be determined\n             for some reason.\nup         : The application is operating normally, and is\n             processing (receiving and possibly issuing) SIP\n             requests and responses.\ndown       : The application is currently unable to process\n             SIP messages.")
jnxSipCommonCfgServiceStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgServiceStartTime.setDescription("The value of sysUpTime at the time the SIP entity was last\nstarted. If started prior to the last re-initialization of the\nlocal network management subsystem, then this object contains a\nzero value.")
jnxSipCommonCfgServiceLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgServiceLastChange.setDescription("The value of sysUpTime at the time the SIP entity entered its\ncurrent operational state.  If the current state was entered\nprior to the last re-initialization of the local network\nmanagement subsystem, then this object contains a zero value.")
jnxSipCommonCfgOrganization = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgOrganization.setDescription("This object contains the organization name which the SIP entity\ninserts into Organization headers of SIP messages processed by\nthis system.  If the string is empty, no Organization header is\nto be generated.")
jnxSipCommonCfgMaxTransactions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgMaxTransactions.setDescription("This object indicates the maximum number of simultaneous\ntransactions per second that the SIP entity can manage.  In\ngeneral, the value of this object SHOULD reflect a level of\ntransaction processing per second that is considered high\nenough to impact the system's CPU and/or memory resources to\nthe point of deteriorating SIP call processing but not high\nenough to cause catastrophic system failure.")
jnxSipCommonCfgEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 8), Bits().subtype(namedValues=NamedValues(("other", 0), ("userAgent", 1), ("proxyServer", 2), ("redirectServer", 3), ("registrarServer", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgEntityType.setDescription("This object identifies the list of SIP entities this row is\nrelated to. It is defined as a bit map.  Each bit represents a\ntype of SIP entity.  If a bit has value 1, the SIP entity\nrepresented by this row plays the role of this entity type.  If\na bit has value 0, the SIP entity represented by this row does\nnot act as this entity type Combinations of bits can be set\nwhen the SIP entity plays multiple SIP roles.")
jnxSipCommonPortTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2))
if mibBuilder.loadTexts: jnxSipCommonPortTable.setDescription("This table contains the list of ports that each SIP entity in\nthis system is allowed to use.  These ports can be advertised\nusing the Contact header in a REGISTER request or response.")
jnxSipCommonPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1)).setIndexNames((0, "JUNIPER-SIP-COMMON-MIB", "jnxSipPortApplName"), (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCommonPort"))
if mibBuilder.loadTexts: jnxSipCommonPortEntry.setDescription("Specification of a particular port.\nEach row represents those objects for a particular SIP entity\npresent in this system.")
jnxSipPortApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipPortApplName.setDescription("The name of the network application which uniquely\nidentifies the application to which this entry is\napplicable.")
jnxSipCommonPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1, 2), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipCommonPort.setDescription("This object reflects a particular port that can be used by the\nSIP application.")
jnxSipCommonPortTransportRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1, 3), Bits().subtype(namedValues=NamedValues(("other", 0), ("udp", 1), ("tcp", 2), ("sctp", 3), ("tlsTcp", 4), ("tlsSctp", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonPortTransportRcv.setDescription("This object will specify the transport protocol the SIP entity\nwill use to receive SIP messages.\nThis object is a bit map.  Each bit represents a transport\nprotocol.  If a bit has value 1, then that transport protocol\nis currently being used.  If a bit has value 0, then that\ntransport protocol is currently not being used.")
jnxSipCommonOptionTagTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3))
if mibBuilder.loadTexts: jnxSipCommonOptionTagTable.setDescription("This table contains a list of the SIP option tags (SIP\nextensions) that either required, supported, or unsupported by\nthe SIP entity.  These option tags are used in the Require,\nProxy-Require, Supported and Unsupported header fields.\n\nExample: if a user agent client supports and requires the\nserver to support reliability of provisional responses (IETF\nRFC 3262), this table contains a row with the option tag string\n'100rel' in jnxSipCommonOptionTag and the OCTET STRING value of\n'1010 0000' or '0xA0' in jnxSipCommonOptionTagHeaderField.\n\nIf a server does not support the required feature (indicated in\na Require header to a UAS, or in a Proxy-Require to a Proxy\nServer), the server returns a 420 Bad Extension listing the\nfeature in an Unsupported header.\n\nNormally the list of such features supported by an entity is\nstatic (i.e. will not change over time).")
jnxSipCommonOptionTagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1)).setIndexNames((0, "JUNIPER-SIP-COMMON-MIB", "jnxSipOptionTagApplName"), (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCommonOptionTagIndex"))
if mibBuilder.loadTexts: jnxSipCommonOptionTagEntry.setDescription("A particular SIP option tag (extension) supported or\nunsupported by the SIP entity, and which may be supported or\nrequired by a peer.\nEach row represents those objects for a particular SIP entity\n present in this system.")
jnxSipOptionTagApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipOptionTagApplName.setDescription("The name of the network application which uniquely\nidentifies the application to which this entry is\napplicable.")
jnxSipCommonOptionTagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipCommonOptionTagIndex.setDescription("This object uniquely identifies a conceptual row in the table.")
jnxSipCommonOptionTag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonOptionTag.setDescription("This object indicates the SIP option tag.  The option tag names\nare registered with IANA and available at http://www.iana.org/.")
jnxSipCommonOptionTagHeaderField = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 4), Bits().subtype(namedValues=NamedValues(("require", 0), ("proxyRequire", 1), ("supported", 2), ("unsupported", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonOptionTagHeaderField.setDescription("This object indicates whether the SIP option tag is supported\n(Supported header), unsupported (Unsupported header), required\n(Require or Proxy-Require header) by the SIP entity.  A SIP\noption tag may be both supported and required.")
jnxSipCommonMethodSupportedTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4))
if mibBuilder.loadTexts: jnxSipCommonMethodSupportedTable.setDescription("This table contains a list of methods supported by each SIP\nentity in this system (see the standard set of SIP methods in\nSection 7.1 of RFC 3261).  Any additional methods that may be\nincorporated into the SIP protocol can be represented by this\ntable without any requirement to update this MIB module.\n\nThe table is informational in nature; conveying to the NMS\ncapabilities of the managed system.")
jnxSipCommonMethodSupportedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1)).setIndexNames((0, "JUNIPER-SIP-COMMON-MIB", "jnxSipMethodSupportedApplName"), (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCommonMethodSupportedIndex"))
if mibBuilder.loadTexts: jnxSipCommonMethodSupportedEntry.setDescription("A particular method supported by the SIP entity.\nEach row represents those objects for a particular SIP entity\npresent in this system.")
jnxSipMethodSupportedApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipMethodSupportedApplName.setDescription("The name of the network application which uniquely\nidentifies the application to which this entry is\napplicable.")
jnxSipCommonMethodSupportedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipCommonMethodSupportedIndex.setDescription("This object uniquely identifies a conceptual row in the table\nfor a specific SIP method.")
jnxSipCommonMethodSupportedName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonMethodSupportedName.setDescription("This object reflects the supported method's name.  The method\nname MUST be all upper case (e.g, 'INVITE').")
jnxSipCommonCfgTimerTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5))
if mibBuilder.loadTexts: jnxSipCommonCfgTimerTable.setDescription("This table contains timer configuration objects applicable to\nSIP user agent and SIP stateful Proxy Server entities.")
jnxSipCommonCfgTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1)).setIndexNames((0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCfgTimerApplName"))
if mibBuilder.loadTexts: jnxSipCommonCfgTimerEntry.setDescription("A row of timer configuration.\n\nEach row represents those objects for a particular SIP entity\npresent in this system.")
jnxSipCfgTimerApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxSipCfgTimerApplName.setDescription("The name of the network application which uniquely\nidentifies the application to which this entry is\napplicable.")
jnxSipCommonCfgTimerA = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerA.setDescription("This object reflects the initial value for the retransmit timer\nfor the INVITE method.  The retransmit timer doubles after each\nretransmission, ensuring an exponential backoff in network\ntraffic.  This object represents the initial time a SIP entity\nwill wait to receive a provisional response to an INVITE before\nresending the INVITE request.")
jnxSipCommonCfgTimerB = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerB.setDescription("This object reflects the maximum time a SIP entity will wait to\nreceive a final response to an INVITE.  The timer is started\nupon transmission of the initial INVITE request.")
jnxSipCommonCfgTimerC = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(180000, 300000)).clone(180000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerC.setDescription("This object reflects the maximum time a SIP Proxy Server will\nwait to receive a provisional response to an INVITE.  The Timer\nC MUST be set for each client transaction when an INVITE\nrequest is proxied.")
jnxSipCommonCfgTimerD = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 300000)).clone(32000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerD.setDescription("This object reflects the amount of time that the server\ntransaction can remain in the 'Completed' state when unreliable\ntransports are used.  The default value MUST be equal to or\ngreater than 32000 for UDP transport, and its value MUST be 0\nfor TCP/SCTP transport.")
jnxSipCommonCfgTimerE = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)).clone(500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerE.setDescription("This object reflects the initial value for the retransmit timer\nfor a non-INVITE method while in 'Trying' state.  The\nretransmit timer doubles after each retransmission until it\nreaches T2 to ensure an exponential backoff in network traffic.\nThis object represents the initial time a SIP entity will wait\nto receive a provisional response to the request before\nresending the non-INVITE request.")
jnxSipCommonCfgTimerF = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerF.setDescription("This object reflects the maximum time a SIP entity will wait to\nreceive a final response to a non-INVITE request.  The timer is\nstarted upon transmission of the initial request.")
jnxSipCommonCfgTimerG = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerG.setDescription("This object reflects the initial value for the retransmit timer\nfor final responses to INVITE requests.  If timer G fires, the\nresponse is passed to the transport layer again for\nretransmission, and timer G is set to fire in MIN(2*T1, T2)\nseconds.  From then on, when timer G fires, the response is\npassed to the transport again for transmission, and timer G is\nreset with a value that doubles, unless that value exceeds T2,\nin which case, it is reset with the value of T2.  The default\nvalue MUST be T1 for UDP transport, and its value MUST be 0 for\nreliable transport like TCP/SCTP.")
jnxSipCommonCfgTimerH = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerH.setDescription("This object reflects the maximum time a server will wait to\nreceive an ACK before it abandons retransmitting the response.\nThe timer is started upon entering the 'Completed' state.")
jnxSipCommonCfgTimerI = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)).clone(5000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerI.setDescription("This object reflects the maximum time a SIP entity will wait to\nreceive additional ACK message retransmissions.\nThe timer is started upon entering the 'Confirmed' state.  The\ndefault value MUST be T4 for UDP transport and its value MUST\nbe 0 for reliable transport like TCP/SCTP.")
jnxSipCommonCfgTimerJ = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(32000, 300000)).clone(32000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerJ.setDescription("This object reflects the maximum time a SIP server will wait to\nreceive retransmissions of non-INVITE requests.  The timer is\nstarted upon entering the 'Completed' state for non-INVITE\ntransactions.  When timer J fires, the server MUST transition to\nthe 'Terminated' state.")
jnxSipCommonCfgTimerK = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)).clone(5000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerK.setDescription("This object reflects the maximum time a SIP client will wait to\nreceive retransmissions of responses to non-INVITE requests.\nThe timer is started upon entering the 'Completed' state for\nnon-INVITE transactions.  When timer K fires, the server MUST\ntransition to the 'Terminated' state.  The default value MUST\nbe T4 for UDP transport, and its value MUST be 0 for reliable\ntransport like TCP/SCTP.")
jnxSipCommonCfgTimerT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(200, 10000)).clone(500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerT1.setDescription("This object reflects the T1 timer for a SIP entity.  T1 is an\nestimate of the round-trip time (RTT) between the client and\nserver transactions.")
jnxSipCommonCfgTimerT2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(200, 10000)).clone(4000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerT2.setDescription("This object reflects the T2 timer for a SIP entity.  T2 is the\nmaximum retransmit interval for non-INVITE requests and INVITE\nresponses.  It's used in various parts of the protocol to reset\nother Timer* objects to this value.")
jnxSipCommonCfgTimerT4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(200, 10000)).clone(5000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSipCommonCfgTimerT4.setDescription("This object reflects the T4 timer for a SIP entity.  T4 is the\nmaximum duration a message will remain in the network.  It\nrepresents the amount of time the network will take to clear\nmessages between client and server transactions.  It's used in\nvarious parts of the protocol to reset other Timer* objects to\nthis value.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-SIP-COMMON-MIB", PYSNMP_MODULE_ID=jnxSipCommonMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-SIP-COMMON-MIB", jnxSip=jnxSip, jnxSipCommonMIB=jnxSipCommonMIB, jnxSipCommonMIBObjects=jnxSipCommonMIBObjects, jnxSipCommonCfgTable=jnxSipCommonCfgTable, jnxSipCommonCfgEntry=jnxSipCommonCfgEntry, jnxSipCfgApplName=jnxSipCfgApplName, jnxSipCommonCfgProtocolVersion=jnxSipCommonCfgProtocolVersion, jnxSipCommonCfgServiceOperStatus=jnxSipCommonCfgServiceOperStatus, jnxSipCommonCfgServiceStartTime=jnxSipCommonCfgServiceStartTime, jnxSipCommonCfgServiceLastChange=jnxSipCommonCfgServiceLastChange, jnxSipCommonCfgOrganization=jnxSipCommonCfgOrganization, jnxSipCommonCfgMaxTransactions=jnxSipCommonCfgMaxTransactions, jnxSipCommonCfgEntityType=jnxSipCommonCfgEntityType, jnxSipCommonPortTable=jnxSipCommonPortTable, jnxSipCommonPortEntry=jnxSipCommonPortEntry, jnxSipPortApplName=jnxSipPortApplName, jnxSipCommonPort=jnxSipCommonPort, jnxSipCommonPortTransportRcv=jnxSipCommonPortTransportRcv, jnxSipCommonOptionTagTable=jnxSipCommonOptionTagTable, jnxSipCommonOptionTagEntry=jnxSipCommonOptionTagEntry, jnxSipOptionTagApplName=jnxSipOptionTagApplName, jnxSipCommonOptionTagIndex=jnxSipCommonOptionTagIndex, jnxSipCommonOptionTag=jnxSipCommonOptionTag, jnxSipCommonOptionTagHeaderField=jnxSipCommonOptionTagHeaderField, jnxSipCommonMethodSupportedTable=jnxSipCommonMethodSupportedTable, jnxSipCommonMethodSupportedEntry=jnxSipCommonMethodSupportedEntry, jnxSipMethodSupportedApplName=jnxSipMethodSupportedApplName, jnxSipCommonMethodSupportedIndex=jnxSipCommonMethodSupportedIndex, jnxSipCommonMethodSupportedName=jnxSipCommonMethodSupportedName, jnxSipCommonCfgTimerTable=jnxSipCommonCfgTimerTable, jnxSipCommonCfgTimerEntry=jnxSipCommonCfgTimerEntry, jnxSipCfgTimerApplName=jnxSipCfgTimerApplName, jnxSipCommonCfgTimerA=jnxSipCommonCfgTimerA, jnxSipCommonCfgTimerB=jnxSipCommonCfgTimerB, jnxSipCommonCfgTimerC=jnxSipCommonCfgTimerC, jnxSipCommonCfgTimerD=jnxSipCommonCfgTimerD, jnxSipCommonCfgTimerE=jnxSipCommonCfgTimerE, jnxSipCommonCfgTimerF=jnxSipCommonCfgTimerF, jnxSipCommonCfgTimerG=jnxSipCommonCfgTimerG, jnxSipCommonCfgTimerH=jnxSipCommonCfgTimerH, jnxSipCommonCfgTimerI=jnxSipCommonCfgTimerI, jnxSipCommonCfgTimerJ=jnxSipCommonCfgTimerJ, jnxSipCommonCfgTimerK=jnxSipCommonCfgTimerK, jnxSipCommonCfgTimerT1=jnxSipCommonCfgTimerT1, jnxSipCommonCfgTimerT2=jnxSipCommonCfgTimerT2, jnxSipCommonCfgTimerT4=jnxSipCommonCfgTimerT4)
