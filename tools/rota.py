#!/usr/bin/python3
import json
import datetime
import re
from collections import defaultdict
from tabulate import tabulate

 
                    
rotadef = defaultdict
rotadef = {}
rotadef = {'oncall': {'actorlist':      ['alan','luke','ian','joe','nick','noel','peter','tom'],
                      'shiftlist':      ['mon','tue','wed','thu','fri','sat','sun'],
                      'journaldate':    "2020-8-02",
                      'actorcredit' :    {'peter' :  {'mon': 6, 'tue': 0, 'wed': 0, 'thu': 0, 'fri': 0, 'sat': 0, 'sun': 0},
                                          'warren':  {'mon': 0, 'tue': 0, 'wed': 0, 'thu': 0, 'fri': 0, 'sat': 0, 'sun': 0}},
                      'actoravailable' : {'peter' :  {'mon': 0, 'tue': 0, 'wed': 0, 'thu': 0, 'fri': 0, 'sat': 0, 'sun': 0},
                                          'warren':  {'mon': 0, 'tue': 0, 'wed': 0, 'thu': 0, 'fri': 0, 'sat': 0, 'sun': 0}},                                          
                      'journal':        {'2020-06-29' : {'actor':   'peter',    'shift':    'mon',  'available':['peter','warren','darren'] },
                                         '2020-06-30' : {'actor':   'peter',    'shift':    'tue',  'available':['peter','warren','darren'] },
                                         '2020-07-01' : {'actor':   'peter',    'shift':    'wed',  'available':['peter','warren','darren'] },
                                         '2020-07-02' : {'actor':   'peter',    'shift':    'thu',  'available':['peter','warren','darren'] },
                                         '2020-07-03' : {'actor':   'peter',    'shift':    'fri',  'available':['peter','warren','darren'] },
                                         '2020-07-04' : {'actor':   'peter',    'shift':    'sat',  'available':['peter','warren','darren'] },
                                         '2020-07-05' : {'actor':   'peter',    'shift':    'sun',  'available':['peter','warren','darren'] },
                                         '2020-07-06' : {'actor':   'warren',   'shift':    'mon',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-07' : {'actor':   'warren',   'shift':    'tue',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-08' : {'actor':   'warren',   'shift':    'wed',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-09' : {'actor':   'warren',   'shift':    'thu',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-10' : {'actor':   'warren',   'shift':    'fri',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-11' : {'actor':   'warren',   'shift':    'sat',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-12' : {'actor':   'warren',   'shift':    'sun',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-13' : {'actor':   'peter',    'shift':    'mon',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-14' : {'actor':   'peter',    'shift':    'tue',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-15' : {'actor':   'peter',    'shift':    'wed',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-16' : {'actor':   'darren',   'shift':    'thu',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-17' : {'actor':   'darren',   'shift':    'fri',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-18' : {'actor':   'darren',   'shift':    'sat',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-19' : {'actor':   'darren',   'shift':    'sun',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-20' : {'actor':   'joe',      'shift':    'mon',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-21' : {'actor':   'joe',      'shift':    'tue',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-22' : {'actor':   'joe',      'shift':    'wed',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-23' : {'actor':   'joe',      'shift':    'thu',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-24' : {'actor':   'joe',      'shift':    'fri',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-25' : {'actor':   'joe',      'shift':    'sat',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-26' : {'actor':   'joe',      'shift':    'sun',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-27' : {'actor':   'peter',    'shift':    'mon',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-28' : {'actor':   'peter',    'shift':    'tue',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-29' : {'actor':   'peter',    'shift':    'wed',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-30' : {'actor':   'peter',    'shift':    'thu',  'available':['peter','warren','darren','joe'] },
                                         '2020-07-31' : {'actor':   'peter',    'shift':    'fri',  'available':['peter','warren','darren','joe'] },
                                         '2020-08-01' : {'actor':   'peter',    'shift':    'sat',  'available':['peter','warren','darren','joe'] },
                                         '2020-08-02' : {'actor':   'peter',    'shift':    'sun',  'available':['peter','warren','darren','joe'] }}
                      }
            }



def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
def writejson(filename,dictionary):
    json_object = json.dumps(dictionary,indent=4)
    with open(filename,"w") as outfile:
        outfile.write(json_object)
    return
def readjson(filename):
    with open(filename, 'r') as openfile:  
        json_object = json.load(openfile) 
    return(json_object)

def debug(*arg):                                                                # *arg
    if DEBUG:
        for Arg in arg:
            print ('P: >'+str(namestr(Arg,globals()))+"< >"+str(type(Arg))+'< >'+str(Arg)+'<')
    return

def printif(PrintFlag,*arg):
    if PrintFlag:
        for Arg in arg:
            print(Arg)
    return


def conv_datestring_from_date(DateTime):                                        # DateTime                            -> DateString
    DateString=DateTime.strftime("%Y-%m-%d")
    return DateString
def conv_date_from_datestring(DateString):                                      # DateString                          -> DateTime
    DateTime = datetime.datetime.strptime(DateString,'%Y-%m-%d').date()
    return DateTime



# Date Functions
def get_dayname_from_date(Date):                                                # Date                                -> DayName   
    if isinstance(Date,str):
        DateTime = conv_date_from_datestring(Date)
    else :
        DateTime = Date
    DayName = DateTime.strftime("%a").lower()
    return DayName
def get_next_date(DateTime,DayCount=1):                                         # DateTime,[DayCount]                 -> DateTime
    NewDateTime = DateTime + datetime.timedelta(days=DayCount)
    return NewDateTime
def get_next_datestring(DateString,DayCount=1):                                 # DateString,[DayCount]               -> DateString
    DateTime      = conv_date_from_datestring(DateString)
    NewDateTime   = get_next_date(DateTime,DayCount)
    NewDateString = conv_datestring_from_date(NewDateTime)
    return          NewDateString


# Year-Week Functions
def get_weekstring_from_weeknumber(WeekNumber):
    (Year,Week) = WeekNumber
    WeekString  = Year + '-' + Week
    return
def get_weeknumber_from_weekstring(WeekString):
    SplitList = WeekString.split('-')
    Year      = int(SplitList[0])
    Week      = int(SplitList[1])
    return (Year,Week)
def get_weeknumber_from_datestring(DateString):
    if isinstance(DateString,str):
        DateTime    = conv_date_from_datestring(DateString)
    else :
        DateTime    = DateString
    (Year,Week,Day) = DateTime.isocalendar()
    return            (Year,Week)    
    
    return (Year,Week)
def get_dayone_from_weekarg(WeekArg):
    # WeekNumber          = tuple  : Year,Week
    # WeekString          = string : "Year-Week"
    # WeekArg             =
    if isinstance(WeekArg, str):
        WeekArg = get_weeknumber_from_weekstring(WeekArg)
    YearNumber,WeekNumber = WeekArg
    WeekNumberString      = str(YearNumber) + '-' + str(WeekNumber)
    DateTime              = datetime.datetime.strptime(WeekNumberString + '-1', "%G-%V-%u")
    DateString            = conv_datestring_from_date(DateTime)
    return DateString



def get_rota_firstvacant(RotaName):
    MostRecent = '0000-00-00'
    for DateString in rotadef[RotaName]['journal'].keys():
        if rotadef[RotaName]['journal'][DateString]['actor']:
            if DateString > MostRecent:
                MostRecent = DateString
    FirstVacant = get_next_datestring(MostRecent)
    return FirstVacant
    



def validate_actorcredit(RotaName,Actor,ShiftType):                               # RotaName,DateString                 -> void
    # check dict datastructure exists for synchronise_actorcredits
    # actorcredit
    if Actor not in rotadef[RotaName]['actorcredit'].keys():
        rotadef[RotaName]['actorcredit'][Actor] = {}
    if ShiftType not in rotadef[RotaName]['actorcredit'][Actor].keys():
        rotadef[RotaName]['actorcredit'][Actor][ShiftType] = 0
    return
def validate_actoravailable(RotaName,Actor,ShiftType):                            # RotaName,Actor,ShiftType            -> void
    # check dict datastructure exists.
    # actoravailable
    if Actor not in rotadef[RotaName]['actoravailable'].keys():
        rotadef[RotaName]['actoravailable'][Actor] = {}
    if ShiftType not in rotadef[RotaName]['actoravailable'][Actor].keys():
        rotadef[RotaName]['actoravailable'][Actor][ShiftType] = 0
    return
def validate_actordata(RotaName,Actor,ShiftType):                               # RotaName,Actor,ShiftType            -> void
    validate_actorcredit(RotaName,Actor,ShiftType)
    validate_actoravailable(RotaName,Actor,ShiftType)
    return
def validate_journal(RotaName,DateString):                                        # RotaName,DateString                 -> void
    # check dict datastructure exists for journal
    # journal
    if DateString not in rotadef[RotaName]['journal'].keys():
        rotadef[RotaName]['journal'][DateString]              = {}
    if 'actor' not in rotadef[RotaName]['journal'][DateString].keys():
        rotadef[RotaName]['journal'][DateString]['actor']     = ''
    if 'shift' not in rotadef[RotaName]['journal'][DateString].keys():
        rotadef[RotaName]['journal'][DateString]['shift']     = ''
    if 'available' not in rotadef[RotaName]['journal'][DateString].keys():
        rotadef[RotaName]['journal'][DateString]['available'] = []
        
        
    return


def wipe_actorcredits(RotaName):                                                # RotaName                            -> void
    ActorList = rotadef[RotaName]['actorlist']
    ShiftTypeList = rotadef[RotaName]['shiftlist']
    for Actor in ActorList:
        if Actor not in rotadef[RotaName]['actorcredit'].keys():
            rotadef[RotaName]['actorcredit'][Actor] = {}
        for shift in ShiftTypeList:
            rotadef[RotaName]['actorcredit'][Actor][shift] = 0            
    return
def wipe_actoravailable(RotaName):                                              # RotaName                            -> void
    ActorList = rotadef[RotaName]['actorlist']
    ShiftTypeList = rotadef[RotaName]['shiftlist']
    for Actor in ActorList:
        if Actor not in rotadef[RotaName]['actoravailable'].keys():
            rotadef[RotaName]['actoravailable'][Actor] = {}
        for shift in ShiftTypeList:
            rotadef[RotaName]['actoravailable'][Actor][shift] = 0            
    return
def wipe_actordata(RotaName):
    wipe_actorcredits(RotaName)
    wipe_actoravailable(RotaName)
    return
def wipe_journal(RotaName):
    for DateString in rotadef[RotaName]['journal'].keys():
        rotadef[RotaName]['journal'][DateString]['actor']     = ''
        rotadef[RotaName]['journal'][DateString]['shift']     = ''
        rotadef[RotaName]['journal'][DateString]['available'] = []
    return
        





def synchronise_actorcredits(RotaName):                                         # RotaName                            -> void 
    wipe_actorcredits(RotaName)
    DateList      = list(rotadef[RotaName]['journal'].keys())
    ActorList     = rotadef[RotaName]['actorlist']
    ShiftTypeList = rotadef[RotaName]['shiftlist']
    for DateString in DateList:
        Actor     = rotadef[RotaName]['journal'][DateString]['actor']
        ShiftType = rotadef[RotaName]['journal'][DateString]['shift']
        validate_actordata(RotaName,Actor,ShiftType)
        if (Actor and ShiftType): rotadef[RotaName]['actorcredit'][Actor][ShiftType] += 1
    return
def synchronise_actoravailable(RotaName):                                       # RotaName                            -> void
    wipe_actoravailable(RotaName)
    DateList      = list(rotadef[RotaName]['journal'].keys())
    ActorList     = rotadef[RotaName]['actorlist']
    ShiftTypeList = rotadef[RotaName]['shiftlist']
    for DateString in DateList:
        ShiftType          = rotadef[RotaName]['journal'][DateString]['shift']
        AvailableActorList = rotadef[RotaName]['journal'][DateString]['available']
        for Actor in AvailableActorList:
            validate_actordata(RotaName,Actor,ShiftType)
            rotadef[RotaName]['actoravailable'][Actor][ShiftType] += 1
    return    
def synchronise_actordata(RotaName):                                            # RotaName                            -> void
    synchronise_actorcredits(RotaName)
    synchronise_actoravailable(RotaName)
    return


def get_shiftrota(RotaName,DateString):                                         # RotaName,DateString                 -> Actor,ShiftType
    validate_journal(RotaName,DateString)
    Actor     = rotadef[RotaName]['journal'][DateString]['actor']
    ShiftType = rotadef[RotaName]['journal'][DateString]['shift']
    return Actor,ShiftType
def set_shiftrota(RotaName,DateString,*args):
    Actor              = ''
    ShiftType          = ''
    Repeat             = 1
    AvailableList      = []
    AvailableResetFlag = False
    for Arg in args:
        [Key,KeyValue] = Arg.split('=')
        if Key == 'Repeat':
            Repeat      = int(KeyValue)
        if Key == 'Actor':
            Actor       = KeyValue
        if Key == 'ShiftType':
            ShiftType   = KeyValue    
        if Key == 'Available':
            for tmp in KeyValue.split(','):
                AvailableList.append(tmp)

    for Count in range(Repeat):
        DateStringCount = get_next_datestring(DateString,Count)
        validate_journal(RotaName,DateStringCount)

        if ShiftType:
            if ShiftType == 'Default': ShiftTypeCount = get_dayname_from_date(DateStringCount)
            rotadef[RotaName]['journal'][DateStringCount]['shift'] = ShiftTypeCount
        if not rotadef[RotaName]['journal'][DateStringCount]['shift']:
            rotadef[RotaName]['journal'][DateStringCount]['shift'] = get_dayname_from_date(DateStringCount)

        if Actor:
            rotadef[RotaName]['journal'][DateStringCount]['actor'] = Actor

        if AvailableList:
            if  ( AvailableList[0][:1] == '+' or AvailableList[0][:1] == '-' ):
                NewAvailableList = rotadef[RotaName]['journal'][DateStringCount]['available']
            else:
                NewAvailableList = []
            for tmpActor in AvailableList:
                ActionFlag = 'Add'
                if tmpActor[:1] == '+' :
                    tmpActor    =  tmpActor[1:]
                    ActionFlag  =  'Add'
                if tmpActor[:1] == '-' :
                    tmpActor    =  tmpActor[1:]
                    ActionFlag  =  'Remove'
                if ActionFlag == 'Add':
                    if tmpActor == 'Default':
                        for tmpDefaultActor in rotadef[RotaName]['actorlist']:
                            if tmpDefaultActor not in NewAvailableList:
                                NewAvailableList.append(tmpDefaultActor)
                    else:
                        if tmpActor not in NewAvailableList:
                            NewAvailableList.append(tmpActor)
                if ActionFlag == 'Remove':
                    if tmpActor == 'Default':
                        for tmpDefaultActor in rotadef[RotaName]['actorlist']:
                            if tmpActor in NewAvailableList:
                                NewAvailableList.remove(tmpDefaultActor)
                    else:
                        if tmpActor in NewAvailableList:
                            NewAvailableList.remove(tmpActor)
            rotadef[RotaName]['journal'][DateStringCount]['available'] = NewAvailableList

    return


def update_actorcredit(RotaName,Actor,ShiftType,Increment):                     # RotaName,Actor,ShiftType,Increment  -> void
    validate_actorcredit(RotaName,Actor,ShiftType)
    rotadef[RotaName]['actorcredit'][Actor][ShiftType] += Increment  
    return
def update_actoravailable(RotaName,ActorList,ShiftType,Increment):              # RotaName,ActorList,ShiftType,Increment  -> void
    for Actor in ActorList:
        validate_actoravailable(RotaName,Actor,ShiftType)
        rotadef[RotaName]['actoravailable'][Actor][ShiftType] += Increment
    return
def update_shiftrota(RotaName,DateString,Actor,ShiftType=None):                 # RotaName,DateString,Actor,[ShiftType]   -> void
    Existing_Actor,Existing_Shift = get_shiftrota(RotaName,DateString)
    if ShiftType is None:                                                           # Set ShiftType from current journal
        ShiftType = Existing_Shift
    if not ShiftType:                                                               # Set ShiftType from date
        ShiftType = get_dayname_from_date(DateString)
    if Existing_Actor and Existing_Shift:                                       # Remove credit
        update_actorcredit(RotaName,Existing_Actor,Existing_Shift,-1)
    update_actorcredit(RotaName,Actor,ShiftType,1)                                      # Add credit 
    set_shiftrota(RotaName,DateString,Actor,ShiftType)                                        # Update rota journal  
    return


def print_rota(RotaName,DateString,DayCount=1):
    RotaTable = []    
    for Count in range(DayCount):
        validate_journal(RotaName,DateString)
        Actor                = rotadef[RotaName]['journal'][DateString]['actor']
        ShiftType            = rotadef[RotaName]['journal'][DateString]['shift']
        AvailableActorList   = rotadef[RotaName]['journal'][DateString]['available']
        AvailableActorString = ' '.join(AvailableActorList)
        WeekNumber           = get_weeknumber_from_datestring(DateString)
        #Day                 = get_dayname_from_date(DateString)
        DateList             = [DateString,WeekNumber,ShiftType,Actor,AvailableActorString]
        DateString           = get_next_datestring(DateString)
        RotaTable.append(DateList)
    print(tabulate(RotaTable,headers=['Date','Week Number','Shift Type','Actor','Availability'],tablefmt='github'))
    return



def print_actordata(RotaName,PickRuleDefinition=None):
    synchronise_actordata(RotaName)
    if PickRuleDefinition is not None:
        PickRuleDefinition          = re.sub(re.compile(r'\s+'),'',PickRuleDefinition)                         # remove whitespace from pick rule definition
        PickRuleList                = PickRuleDefinition.split('+')                                            # split definition into individual rules
        PickRuleDict                = {}
        for PickRule in PickRuleList:
            if '*' in PickRule:
                tmp                 = PickRule.split('*')
                ShiftMultiplier     = int(tmp[1])
                ShiftType           = tmp[0]
            else:
                ShiftMultiplier     = 1
                ShiftType           = PickRule
            PickRuleDict[ShiftType] = ShiftMultiplier
    else:
        PickRuleDict                = {}     # to avoid failures when no pickdefinition exists.
    
    ActorList      = rotadef[RotaName]['actorlist']
    ShiftTypeList  = rotadef[RotaName]['shiftlist']
    ActorPickScore = {}
    ActorData      = {}
    ActorTable     = []
    HeaderList     = []
    if PickRuleDefinition is not None: HeaderList = ShiftTypeList + ['PickScore']
    else:                              HeaderList = ShiftTypeList
    
    for Actor in ActorList:
        ActorData[Actor]                   = {}
        ActorRow                           = ['Actor\nShiftType\nCredit\nAvailable\nRatio']
        ActorPickScore[Actor]              = {}
        ActorPickScore[Actor]['credit']    = 0
        ActorPickScore[Actor]['available'] = 0
        for ShiftType in ShiftTypeList:

            ActorData[Actor]['credit']     = rotadef[RotaName]['actorcredit'][Actor][ShiftType]
            ActorData[Actor]['available']  = rotadef[RotaName]['actoravailable'][Actor][ShiftType]
            ActorData[Actor]['ratio']      = ActorData[Actor]['credit'] / ActorData[Actor]['available']    if ActorData[Actor]['available'] != 0 else 0
            tmp                            = float("{:.2f}".format(ActorData[Actor]['ratio']))
            ActorCell                      = Actor+'\n'+ShiftType+'\n'+str(ActorData[Actor]['credit'])+'\n'+str(ActorData[Actor]['available'])+'\n'+str(tmp)
            
            if ShiftType in PickRuleDict:
                ActorPickScore[Actor]['credit']    += ActorData[Actor]['credit']    * PickRuleDict[ShiftType]
                ActorPickScore[Actor]['available'] += ActorData[Actor]['available'] * PickRuleDict[ShiftType] 
            ActorRow.append(ActorCell)

        if PickRuleDefinition is not None:
            ActorPickScore[Actor]['ratio']       = ActorPickScore[Actor]['credit'] / ActorPickScore[Actor]['available']    if ActorPickScore[Actor]['available'] != 0 else 0
            ActorPickScore[Actor]['ratiostring'] = str(float("{:.4f}".format(ActorPickScore[Actor]['ratio'])))
            ActorRow.append(ActorPickScore[Actor]['ratiostring'])
        ActorTable.append(ActorRow)

    print(tabulate(ActorTable,headers=HeaderList,tablefmt='fancy_grid'))
    return
def get_rota_pickscore(RotaName,PickRuleDefinition):    
    PickRuleDefinition          = re.sub(re.compile(r'\s+'),'',PickRuleDefinition)                         # remove whitespace from pick rule definition
    PickRuleList                = PickRuleDefinition.split('+')                                            # split definition into individual rules
    PickRuleDict                = {}
    for PickRule in PickRuleList:
        if '*' in PickRule:
            tmp                 = PickRule.split('*')
            ShiftMultiplier     = int(tmp[1])
            ShiftType           = tmp[0]
        else:
            ShiftMultiplier     = 1
            ShiftType           = PickRule
        PickRuleDict[ShiftType] = ShiftMultiplier
    debug
    
    ActorList      = rotadef[RotaName]['actorlist']
    ShiftTypeList  = rotadef[RotaName]['shiftlist']
    ActorPickScore = {}
    ActorPickRatio = {}
    ActorData      = {}
    for Actor in ActorList:
        ActorData[Actor]                   = {}
        ActorRow                           = ['Actor\nShiftType\nCredit\nAvailable\nRatio']
        ActorPickScore[Actor]              = {}
        ActorPickScore[Actor]['credit']    = 0
        ActorPickScore[Actor]['available'] = 0
        for ShiftType in ShiftTypeList:
            ActorData[Actor]['credit']     = rotadef[RotaName]['actorcredit'][Actor][ShiftType]
            #debug(Actor,RotaName,ShiftType)
            ActorData[Actor]['available']  = rotadef[RotaName]['actoravailable'][Actor][ShiftType]
            ActorData[Actor]['ratio']      = ActorData[Actor]['credit'] / ActorData[Actor]['available']    if ActorData[Actor]['available'] != 0 else 0
            
            if ShiftType in PickRuleDict:
                ActorPickScore[Actor]['credit']    += ActorData[Actor]['credit']    * PickRuleDict[ShiftType]
                ActorPickScore[Actor]['available'] += ActorData[Actor]['available'] * PickRuleDict[ShiftType] 

        ActorPickScore[Actor]['ratio']       = ActorPickScore[Actor]['credit'] / ActorPickScore[Actor]['available']    if ActorPickScore[Actor]['available'] != 0 else 0
        ActorPickScore[Actor]['ratiostring'] = str(float("{:.4f}".format(ActorPickScore[Actor]['ratio'])))
        ActorPickRatio[Actor]                = ActorPickScore[Actor]['ratio']      # simpler key-val dictionary for later sorting

    SortedActorPickRatio = sorted(ActorPickRatio.items(), key=lambda x: x[1], reverse=False)    
    SortedActorPickList  = []
    for SortedActor in SortedActorPickRatio:
        tmpActor,tmpPickScore = SortedActor
        SortedActorPickList.append(tmpActor)
        
    return SortedActorPickList
def print_rotaweek(RotaName,WeekArg,WeekCount=1):
    DateString = get_dayone_from_weekarg(WeekArg)
    DayCount = WeekCount * 7
    print_rota(RotaName,DateString,DayCount)
def print_rota_prettyweek(RotaName,DateArg,WeekCount=1):
    if isinstance(DateArg,str):
        DateArg = get_weeknumber_from_datestring(DateArg)
    DateStringDayOne = get_dayone_from_weekarg(DateArg)
    DateString = ""
    DateString = DateStringDayOne
    RotaTable = []
    for WeekCount in range(WeekCount):
        WeekTable = []
        for DayCount in range(7):
            validate_journal(RotaName,DateString)
            DayName = get_dayname_from_date(DateString)
            ShiftName = rotadef[RotaName]['journal'][DateString]['shift']
            ActorName = rotadef[RotaName]['journal'][DateString]['actor']
            
            if not ShiftName: ShiftName = '...'
            if not ActorName: ActorName = '...'
            
            ShiftCell = DateString + '\n' + ShiftName + '\n' + ActorName
            #ShiftCell = [DateString,DayName,ShiftName,ActorName]
            
            WeekTable.append(ShiftCell)
            DateString = get_next_datestring(DateString,1)
        RotaTable.append(WeekTable)
    print(tabulate(RotaTable,tablefmt='fancy_grid'))
    return
def update_rota_firstvacant(RotaName,DayCount,PickRuleDefinition):
    synchronise_actordata(RotaName)
    FirstVacant     = get_rota_firstvacant(RotaName)
    NextActor       = get_rota_pickscore(RotaName,PickRuleDefinition)[0]
    NextActorString = 'Actor=' + NextActor
    RepeatString    = 'Repeat=' + str(DayCount)
    set_shiftrota(RotaName,FirstVacant,NextActorString,RepeatString,'Available=Default')
    return
    
    
    


RotaName           = 'oncall'
DateString         = '2020-06-28'
Duration           = 42
PickRuleDefinition = 'mon+tue+wed+thu+fri*2+sat*3+sun*3'

def example1():
    synchronise_actordata(RotaName)
    #wipe_actordata('oncall')
    #print_rota('oncall','2020-06-01',70)
    print_actordata('oncall','mon+tue+wed+thu+fri*2+sat*4+sun*6')
    ActorList = get_rota_pickscore('oncall','mon+tue+wed+thu+fri*2+sat*4+sun*6')
    print("ActorList>",ActorList)
    return
#example1()
def example2():
    print_rotaweek('oncall','2020-26',8)
    print('\n'*0)
    #print_rota('oncall','2020-08-03',7)
    return
#example2()
def example3():
    synchronise_actordata(RotaName)
    print_rota(RotaName,DateString,Duration)
    print('\n'*0)

    set_shiftrota(RotaName,'2020-08-03','joe','mon')
    set_shiftrota(RotaName,'2020-08-07','joe')

    synchronise_actordata(RotaName)
    print_rota(RotaName,DateString,Duration)
    print('\n'*0)
    print('\n'*1)

    update_shiftrota('oncall','2020-07-30','joe')
    print_rota(RotaName,DateString,Duration)
    print('\n'*0)

    print('\n'*1)
    print_actordata('oncall','mon+tue+wed+thu+fri*2+sat*4+sun*6')
    #ActorList = get_rota_pickscore('oncall','mon+tue+wed+thu+fri*2+sat*4+sun*6')
    return
#example3()
def example4():
    wipe_journal(RotaName)
    
    set_shiftrota(RotaName,'2020-06-29','Actor=peter' ,'Repeat=7','Available=Default')
    set_shiftrota(RotaName,'2020-07-06','Actor=warren','Repeat=7','Available=Default')
    set_shiftrota(RotaName,'2020-07-13','Actor=darren','Repeat=7','Available=Default')
    set_shiftrota(RotaName,'2020-07-20','Actor=joe'   ,'Repeat=7','Available=Default')
    set_shiftrota(RotaName,'2020-07-27','Actor=peter' ,'Repeat=7','Available=Default')
    

    
    return
#example4()
def example5():
    print_rotaweek(RotaName,'2020-26',7)
    
    synchronise_actordata(RotaName)
    print_actordata(RotaName,PickRuleDefinition)
    return
#example5()
def example6():
    wipe_journal(RotaName)
    
    set_shiftrota(RotaName,'2020-01-01','Actor=peter' ,'Repeat=3','Available=Default')
#    print_rotaweek(RotaName,'2020-01',12)
    
    for i in range(84):
        update_rota_firstvacant(RotaName,3,PickRuleDefinition)
    
    print_rotaweek(RotaName,'2020-01',13)
    
    print_actordata(RotaName,PickRuleDefinition)
    
    return
#example6()
def example7():
    #print_rota_prettyweek(RotaName,(2020,15),1)
    print_rota_prettyweek(RotaName,"2020-06-01",12)
    return
#example7()

def example8():
    wipe_actordata('oncall')
    wipe_journal('oncall')
    #print_actordata('oncall')
    set_shiftrota('oncall','2020-01-06','Actor=peter','Repeat=7','Available=Default')
    print_rota('oncall','2020-01-06',7)
    
    #print_rota_prettyweek('oncall','2020-01-06',7)
    set_shiftrota('oncall','2020-01-13','Actor=alan','Repeat=7','Available=Default')
    print_rota_prettyweek('oncall','2020-01-06',2)
    
    set_shiftrota('oncall','2020-01-17','Actor=luke')
    set_shiftrota('oncall','2020-01-18','Actor=noel')
    set_shiftrota('oncall','2020-01-19','Actor=joe')


    
    set_shiftrota('oncall','2020-01-20','Actor=luke' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-01-27','Actor=ian'  ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-02-03','Actor=joe'  ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-02-10','Actor=nick' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-02-17','Actor=noel' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-02-24','Actor=tom'  ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-03-02','Actor=peter','Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-03-09','Actor=alan' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-03-16','Actor=luke' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-03-23','Actor=ian'  ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-03-30','Actor=joe'  ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-04-06','Actor=nick' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-04-13','Actor=noel' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-04-20','Actor=tom'  ,'Repeat=7','Available=Default')

    print_rota_prettyweek('oncall','2020-01-06',8)


    set_shiftrota('oncall','2020-02-24','Actor=nick' ,'Repeat=7','Available=Default')
    set_shiftrota('oncall','2020-04-20','Actor=joe'  ,'Repeat=7','Available=Default')
    rotadef['oncall']['actorlist'] = ['alan','luke','ian','joe','nick','noel','peter']
    set_shiftrota('oncall','2020-03-23','Actor=nick' ,'Repeat=7','Available=Default')
    rotadef['oncall']['actorlist'] = ['alan','luke','joe','nick','noel','peter']
    set_shiftrota('oncall','2020-04-03','Actor=alan' ,'Repeat=3','Available=Default')
    set_shiftrota('oncall','2020-03-14','Actor=joe'  ,'Repeat=3','Available=Default')


    print_rota_prettyweek('oncall','2020-01-06',16)
    print_actordata('oncall')
    print_rota('oncall','2019-12-01',260)
    #print_rota('oncall','2020-01-06',112)
    
    print(get_rota_pickscore('oncall','mon+tue+wed+thu+fri*2+sat*3+sun*3'))
    
    for i in range(8):
        update_rota_firstvacant('oncall',7,'mon+tue+wed+thu+fri*2+sat*3+sun*3')
    print_rota_prettyweek('oncall','2020-04-27',8)
    

    return
example8()




#
##
