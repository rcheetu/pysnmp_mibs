# PySNMP SMI module. Autogenerated from smidump -f python SNMPv2-TC
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:14 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, MibIdentifier, TimeTicks, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks", "TimeTicks")

# Types

class AutonomousType(ObjectIdentifier):
    pass

class DateAndTime(TextualConvention, OctetString):
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(11,11),)
    
class DisplayString(TextualConvention, OctetString):
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    
class InstancePointer(ObjectIdentifier):
    pass

class MacAddress(TextualConvention, OctetString):
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(6,6)
    fixedLength = 6
    
class PhysAddress(TextualConvention, OctetString):
    displayHint = "1x:"
    
class RowPointer(ObjectIdentifier):
    pass

class RowStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(3,4,1,6,5,2,)
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6), )
    
class StorageType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(4,3,1,2,5,)
    namedValues = NamedValues(("other", 1), ("volatile", 2), ("nonVolatile", 3), ("permanent", 4), ("readOnly", 5), )
    
class TAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)
    
class TDomain(ObjectIdentifier):
    pass

class TestAndIncr(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class TruthValue(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,1,)
    namedValues = NamedValues(("true", 1), ("false", 2), )
    
class VariablePointer(ObjectIdentifier):
    pass

class TimeStamp(TimeTicks):
    pass


# Exports

# Types
mibBuilder.exportSymbols("SNMPv2-TC", AutonomousType=AutonomousType, DateAndTime=DateAndTime, DisplayString=DisplayString, InstancePointer=InstancePointer, MacAddress=MacAddress, PhysAddress=PhysAddress, RowPointer=RowPointer, RowStatus=RowStatus, StorageType=StorageType, TAddress=TAddress, TDomain=TDomain, TestAndIncr=TestAndIncr, TimeInterval=TimeInterval, TruthValue=TruthValue, VariablePointer=VariablePointer, TimeStamp=TimeStamp)

