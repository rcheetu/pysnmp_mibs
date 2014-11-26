# PySNMP SMI module. Autogenerated from smidump -f python ARUBA-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 08:59:06 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises", "snmpModules")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Objects

aruba = MibIdentifier((1, 3, 6, 1, 4, 1, 14823))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1))
switchProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1))
a5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 1))
a2400 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 2))
a800 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 3))
a6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 4))
a2400E = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 7))
a800E = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 8))
a804 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 9))
a200 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 10))
a2424 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 11))
a6000_SC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 12)).setLabel("a6000-SC3")
a3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 13))
a3200_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 14)).setLabel("a3200-8")
a3400 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 15))
a3400_32 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 16)).setLabel("a3400-32")
a3600 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 17))
a3600_64 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 18)).setLabel("a3600-64")
a650 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 19))
a651 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 20))
reserved1 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 21))
reserved2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 22))
a620 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 23))
s3500_24P = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 24)).setLabel("s3500-24P")
s3500_24T = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 25)).setLabel("s3500-24T")
s3500_48P = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 26)).setLabel("s3500-48P")
s3500_48T = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 27)).setLabel("s3500-48T")
s2500_24P = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 28)).setLabel("s2500-24P")
s2500_24T = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 29)).setLabel("s2500-24T")
s2500_48P = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 30)).setLabel("s2500-48P")
s2500_48T = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 31)).setLabel("s2500-48T")
a7210 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 32))
a7220 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 33))
a7240 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 34))
s3500_24F = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 35)).setLabel("s3500-24F")
s1500_48P = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 36)).setLabel("s1500-48P")
s1500_24P = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 37)).setLabel("s1500-24P")
s1500_12P = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 38)).setLabel("s1500-12P")
aUndefined = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 1, 9999))
apProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2))
a50 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 1))
a52 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 2))
ap60 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 3))
ap61 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 4))
ap70 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 5))
walljackAp61 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 6))
a2E = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 7))
ap1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 8))
ap80s = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 9))
ap80m = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 10))
wg102 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 11))
ap40 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 12))
ap41 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 13))
ap65 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 14))
apMw1700 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 15))
apDuowj = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 16))
apDuo = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 17))
ap80MB = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 18))
ap80SB = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 19))
ap85 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 20))
ap124 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 21))
ap125 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 22))
ap120 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 23))
ap121 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 24))
ap1250 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 25))
ap120abg = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 26))
ap121abg = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 27))
ap124abg = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 28))
ap125abg = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 29))
rap5wn = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 30))
rap5 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 31))
rap2wg = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 32))
reserved4 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 33))
ap105 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 34))
ap65wb = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 35))
ap651 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 36))
reserved6 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 37))
ap60p = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 38))
reserved7 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 39))
ap92 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 40))
ap93 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 41))
ap68 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 42))
ap68p = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 43))
ap175p = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 44))
ap175ac = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 45))
ap175dc = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 46))
ap134 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 47))
ap135 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 48))
reserved8 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 49))
ap93h = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 50))
rap3wn = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 51))
rap3wnp = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 52))
ap104 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 53))
rap155 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 54))
rap155p = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 55))
rap108 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 56))
rap109 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 57))
ap224 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 58))
ap225 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 59))
ap114 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 60))
ap115 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 61))
rap109L = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 62))
apUndefined = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 2, 9999))
emsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 3))
partnerProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 4))
ecsE50 = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 4, 1))
ecsE100C = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 4, 2))
ecsE100A = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 4, 3))
ecsENSM = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 4, 4))
amigopodProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 1, 5))
arubaEnterpriseMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1))
arubaMIBModules = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2))
wlsxEnterpriseMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1))
arubaAp = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 3))
wlsrEnterpriseMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 3, 1))
wlsrOutDoorApMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 3, 2))
aiEnterpriseMibModules = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 3, 3))
arubaEcs = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 4))
arubaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 3))

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("ARUBA-MIB", aruba=aruba, products=products, switchProducts=switchProducts, a5000=a5000, a2400=a2400, a800=a800, a6000=a6000, a2400E=a2400E, a800E=a800E, a804=a804, a200=a200, a2424=a2424, a6000_SC3=a6000_SC3, a3200=a3200, a3200_8=a3200_8, a3400=a3400, a3400_32=a3400_32, a3600=a3600, a3600_64=a3600_64, a650=a650, a651=a651, reserved1=reserved1, reserved2=reserved2, a620=a620, s3500_24P=s3500_24P, s3500_24T=s3500_24T, s3500_48P=s3500_48P, s3500_48T=s3500_48T, s2500_24P=s2500_24P, s2500_24T=s2500_24T, s2500_48P=s2500_48P, s2500_48T=s2500_48T, a7210=a7210, a7220=a7220, a7240=a7240, s3500_24F=s3500_24F, s1500_48P=s1500_48P, s1500_24P=s1500_24P, s1500_12P=s1500_12P, aUndefined=aUndefined, apProducts=apProducts, a50=a50, a52=a52, ap60=ap60, ap61=ap61, ap70=ap70, walljackAp61=walljackAp61, a2E=a2E, ap1200=ap1200, ap80s=ap80s, ap80m=ap80m, wg102=wg102, ap40=ap40, ap41=ap41, ap65=ap65, apMw1700=apMw1700, apDuowj=apDuowj, apDuo=apDuo, ap80MB=ap80MB, ap80SB=ap80SB, ap85=ap85, ap124=ap124, ap125=ap125, ap120=ap120, ap121=ap121, ap1250=ap1250, ap120abg=ap120abg, ap121abg=ap121abg, ap124abg=ap124abg, ap125abg=ap125abg, rap5wn=rap5wn, rap5=rap5, rap2wg=rap2wg, reserved4=reserved4, ap105=ap105, ap65wb=ap65wb, ap651=ap651, reserved6=reserved6, ap60p=ap60p, reserved7=reserved7, ap92=ap92, ap93=ap93, ap68=ap68, ap68p=ap68p, ap175p=ap175p, ap175ac=ap175ac, ap175dc=ap175dc, ap134=ap134, ap135=ap135, reserved8=reserved8, ap93h=ap93h, rap3wn=rap3wn, rap3wnp=rap3wnp, ap104=ap104, rap155=rap155, rap155p=rap155p, rap108=rap108, rap109=rap109, ap224=ap224, ap225=ap225, ap114=ap114, ap115=ap115, rap109L=rap109L, apUndefined=apUndefined, emsProducts=emsProducts, partnerProducts=partnerProducts, ecsE50=ecsE50, ecsE100C=ecsE100C, ecsE100A=ecsE100A, ecsENSM=ecsENSM, amigopodProducts=amigopodProducts, arubaEnterpriseMibModules=arubaEnterpriseMibModules, common=common, arubaMIBModules=arubaMIBModules, switch=switch, wlsxEnterpriseMibModules=wlsxEnterpriseMibModules, arubaAp=arubaAp, wlsrEnterpriseMibModules=wlsrEnterpriseMibModules, wlsrOutDoorApMibModules=wlsrOutDoorApMibModules, aiEnterpriseMibModules=aiEnterpriseMibModules, arubaEcs=arubaEcs, arubaMgmt=arubaMgmt)
