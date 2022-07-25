from __future__ import annotations
from typing import (Optional, List, Any, Tuple, Callable)
from ...fable_library.array import (try_find_index, choose, map, map_indexed, try_find, filter, exists as exists_1)
from ...fable_library.option import (to_array, default_arg, value as value_2, bind, map as map_1)
from ...fable_library.reflection import (TypeInfo, int32_type, bool_type, record_type)
from ...fable_library.seq import (exists, iterate)
from ...fable_library.types import Record
from ...fable_library.util import equals
from ...fs_hafas_python.context import (Context, Platform, CommonData, Profile__get_parseWhen, ParsedWhen, Profile__get_parsePlatform, Profile__get_parsePolyline, Profile__get_parseStopovers)
from ...fs_hafas_python.lib.transformations import (U2StationStop_FromSomeU3StationStopLocation, Default_Leg, Default_Location, Default_Alternative)
from ...fs_hafas_python.types_hafas_client import (StopOver, Leg, Line, FeatureCollection, Location, Cycle, Alternative)
from ...fs_hafas_python.types_raw_hafas_client import (RawMsg, RawSec, RawPltf, RawGis, RawJny, RawPoly, RawPolyG, RawCrd, RawFreq, RawStop)
from .common import (get_element_at_some, get_element_at, msg_lto_remarks)

def parse_platform(ctx: Context, platf_s: Optional[str]=None, platf_r: Optional[str]=None, cncl: Optional[bool]=None) -> Platform:
    planned : Optional[str] = platf_s
    prognosed : Optional[str] = platf_r
    def predicate(x: bool, ctx: Context=ctx, platf_s: Optional[str]=platf_s, platf_r: Optional[str]=platf_r, cncl: Optional[bool]=cncl) -> bool:
        return x
    
    if exists(predicate, to_array(cncl)):
        return Platform(None, planned, prognosed)
    
    else: 
        return Platform(default_arg(prognosed, planned), planned, None)
    


def expr_446() -> TypeInfo:
    return record_type("FsHafas.Parser.JourneyLeg.RemarkRange", [], RemarkRange, lambda: [("rem_x", int32_type), ("whole_leg", bool_type), ("from_index", int32_type), ("to_index", int32_type)])


class RemarkRange(Record):
    def __init__(self, rem_x: int, whole_leg: bool, from_index: int, to_index: int) -> None:
        super().__init__()
        self.rem_x = rem_x or 0
        self.whole_leg = whole_leg
        self.from_index = from_index or 0
        self.to_index = to_index or 0
    

RemarkRange_reflection = expr_446

def get_remark_range(msg: RawMsg, common: CommonData, stopovers: List[StopOver]) -> Optional[RemarkRange]:
    from_loc : Optional[Any] = U2StationStop_FromSomeU3StationStopLocation(get_element_at_some(msg.f_loc_x, common.locations))
    to_loc : Optional[Any] = U2StationStop_FromSomeU3StationStopLocation(get_element_at_some(msg.t_loc_x, common.locations))
    def predicate(s: StopOver, msg: RawMsg=msg, common: CommonData=common, stopovers: List[StopOver]=stopovers) -> bool:
        return equals(s.stop, from_loc)
    
    def predicate_1(s_1: StopOver, msg: RawMsg=msg, common: CommonData=common, stopovers: List[StopOver]=stopovers) -> bool:
        return equals(s_1.stop, to_loc)
    
    match_value : Tuple[Optional[int], Optional[int], Optional[int]] = (msg.rem_x, try_find_index(predicate, stopovers), try_find_index(predicate_1, stopovers))
    (pattern_matching_result, from_index_1, rem_x, to_index_1) = (None, None, None, None)
    if match_value[0] is not None:
        if match_value[1] is not None:
            if match_value[2] is not None:
                pattern_matching_result = 0
                from_index_1 = match_value[1]
                rem_x = match_value[0]
                to_index_1 = match_value[2]
            
            else: 
                pattern_matching_result = 1
            
        
        else: 
            pattern_matching_result = 1
        
    
    else: 
        pattern_matching_result = 1
    
    if pattern_matching_result == 0:
        return RemarkRange(rem_x, (to_index_1 == (len(stopovers) - 1)) if (from_index_1 == 0) else False, from_index_1, to_index_1)
    
    elif pattern_matching_result == 1:
        return None
    


def get_remark_ranges(msg_l: List[RawMsg], common_data: CommonData, stopovers: List[StopOver]) -> List[RemarkRange]:
    def chooser(x: Optional[RemarkRange]=None, msg_l: List[RawMsg]=msg_l, common_data: CommonData=common_data, stopovers: List[StopOver]=stopovers) -> Optional[RemarkRange]:
        return x
    
    def mapping(msg: RawMsg, msg_l: List[RawMsg]=msg_l, common_data: CommonData=common_data, stopovers: List[StopOver]=stopovers) -> Optional[RemarkRange]:
        return get_remark_range(msg, common_data, stopovers)
    
    return choose(chooser, map(mapping, msg_l, None), None)


def apply_remark_range(remark_range: RemarkRange, common_data: CommonData, stopover: StopOver) -> StopOver:
    def arrow_447(remark_range: RemarkRange=remark_range, common_data: CommonData=common_data, stopover: StopOver=stopover) -> List[Any]:
        match_value : Tuple[Optional[List[Any]], Optional[Optional[Any]]] = (stopover.remarks, get_element_at(remark_range.rem_x, common_data.hints))
        (pattern_matching_result, hint_2, remarks, hint_3) = (None, None, None, None)
        if match_value[0] is None:
            if match_value[1] is not None:
                if value_2(match_value[1]) is not None:
                    pattern_matching_result = 1
                    hint_3 = value_2(match_value[1])
                
                else: 
                    pattern_matching_result = 2
                
            
            else: 
                pattern_matching_result = 2
            
        
        elif match_value[1] is not None:
            pattern_matching_result = 0
            hint_2 = value_2(match_value[1])
            remarks = match_value[0]
        
        else: 
            pattern_matching_result = 2
        
        if pattern_matching_result == 0:
            return remarks
        
        elif pattern_matching_result == 1:
            return [value_2(hint_3)]
        
        elif pattern_matching_result == 2:
            return []
        
    
    return StopOver(stopover.stop, stopover.departure, stopover.departure_delay, stopover.prognosed_departure, stopover.planned_departure, stopover.departure_platform, stopover.prognosed_departure_platform, stopover.planned_departure_platform, stopover.arrival, stopover.arrival_delay, stopover.prognosed_arrival, stopover.planned_arrival, stopover.arrival_platform, stopover.prognosed_arrival_platform, stopover.planned_arrival_platform, arrow_447(), stopover.pass_by, stopover.cancelled)


def apply_remark_ranges(common_data: CommonData, stopovers: List[StopOver], remark_ranges: List[RemarkRange]) -> List[StopOver]:
    def mapping(i: int, s: StopOver, common_data: CommonData=common_data, stopovers: List[StopOver]=stopovers, remark_ranges: List[RemarkRange]=remark_ranges) -> StopOver:
        def predicate(r: RemarkRange, i: int=i, s: StopOver=s) -> bool:
            if (r.from_index <= i) if (not r.whole_leg) else False:
                return r.to_index >= i
            
            else: 
                return False
            
        
        match_value : Optional[RemarkRange] = try_find(predicate, remark_ranges)
        if match_value is None:
            return s
        
        else: 
            return apply_remark_range(match_value, common_data, s)
        
    
    return map_indexed(mapping, stopovers, None)


def parse_journey_leg(ctx: Context, pt: RawSec, date: str) -> Leg:
    leg : Leg = Default_Leg
    origin : Optional[Any] = get_element_at_some(pt.dep.loc_x, ctx.common.locations)
    destination : Optional[Any] = get_element_at_some(pt.arr.loc_x, ctx.common.locations)
    dep : ParsedWhen = Profile__get_parseWhen(ctx.profile)(ctx)(date)(pt.dep.d_time_s)(pt.dep.d_time_r)(pt.dep.d_tzoffset)(pt.dep.d_cncl)
    arr : ParsedWhen = Profile__get_parseWhen(ctx.profile)(ctx)(date)(pt.arr.a_time_s)(pt.arr.a_time_r)(pt.arr.a_tzoffset)(pt.arr.a_cncl)
    def match_platf_s(a_platf_s: Optional[str]=None, a_pltf_s: Optional[RawPltf]=None, ctx: Context=ctx, pt: RawSec=pt, date: str=date) -> Optional[str]:
        if a_platf_s is None:
            if a_pltf_s is not None:
                return a_pltf_s.txt
            
            else: 
                return None
            
        
        else: 
            return a_platf_s
        
    
    d_platf_s : Optional[str] = match_platf_s(pt.dep.d_platf_s, pt.dep.d_pltf_s)
    d_platf_r : Optional[str] = match_platf_s(pt.dep.d_platf_r, pt.dep.d_pltf_r)
    dep_pl : Platform = Profile__get_parsePlatform(ctx.profile)(ctx)(d_platf_s)(d_platf_r)(pt.dep.d_cncl)
    a_platf_s_1 : Optional[str] = match_platf_s(pt.arr.a_platf_s, pt.arr.a_pltf_s)
    a_platf_r : Optional[str] = match_platf_s(pt.arr.a_platf_r, pt.arr.a_pltf_r)
    arr_pl : Platform = Profile__get_parsePlatform(ctx.profile)(ctx)(a_platf_s_1)(a_platf_r)(pt.arr.a_cncl)
    if True if (True if (pt.type == "WALK") else (pt.type == "TRSF")) else (pt.type == "DEVI"):
        def arrow_448(ctx: Context=ctx, pt: RawSec=pt, date: str=date) -> Leg:
            distance : Optional[int]
            match_value : Optional[RawGis] = pt.gis
            distance = None if (match_value is None) else match_value.dist
            transfer : Optional[bool] = True if (pt.type == "TRSF") else (pt.type == "DEVI")
            return Leg(leg.trip_id, leg.origin, leg.destination, leg.departure, leg.planned_departure, leg.prognosed_arrival, leg.departure_delay, leg.departure_platform, leg.prognosed_departure_platform, leg.planned_departure_platform, leg.arrival, leg.planned_arrival, leg.prognosed_departure, leg.arrival_delay, leg.arrival_platform, leg.prognosed_arrival_platform, leg.planned_arrival_platform, leg.stopovers, leg.schedule, leg.price, leg.operator, leg.direction, leg.line, leg.reachable, leg.cancelled, True, leg.load_factor, distance, True, transfer, leg.cycle, leg.alternatives, leg.polyline, leg.remarks, leg.current_location)
        
        leg = arrow_448()
    
    if pt.type == "JNY":
        def action(jny: RawJny, ctx: Context=ctx, pt: RawSec=pt, date: str=date) -> None:
            nonlocal leg
            line : Optional[Line] = get_element_at(jny.prod_x, ctx.common.lines)
            polyline : Optional[FeatureCollection]
            match_value_1 : Optional[RawPoly] = jny.poly
            if match_value_1 is None:
                match_value_2 : Optional[RawPolyG] = jny.poly_g
                if match_value_2 is None:
                    polyline = None
                
                else: 
                    poly_g : RawPolyG = match_value_2
                    idx : int = poly_g.poly_xl[0] or 0
                    polyline = ctx.common.polylines[idx] if (idx < len(ctx.common.polylines)) else None
                
            
            else: 
                value : RawPoly = match_value_1
                polyline = Profile__get_parsePolyline(ctx.profile)(ctx)(value)
            
            stopovers : Optional[List[StopOver]] = Profile__get_parseStopovers(ctx.profile)(ctx)(jny.stop_l)(date) if ctx.opt.stopovers else None
            remark_ranges : List[RemarkRange]
            match_value_4 : Tuple[Optional[List[RawMsg]], Optional[List[StopOver]]] = (jny.msg_l, stopovers)
            (pattern_matching_result, msg_l, stopovers_1) = (None, None, None)
            if match_value_4[0] is not None:
                if match_value_4[1] is not None:
                    pattern_matching_result = 0
                    msg_l = match_value_4[0]
                    stopovers_1 = match_value_4[1]
                
                else: 
                    pattern_matching_result = 1
                
            
            else: 
                pattern_matching_result = 1
            
            if pattern_matching_result == 0:
                remark_ranges = get_remark_ranges(msg_l, ctx.common, stopovers_1)
            
            elif pattern_matching_result == 1:
                remark_ranges = []
            
            stopovers_with_remarks : Optional[List[StopOver]] = apply_remark_ranges(ctx.common, stopovers, remark_ranges) if (stopovers is not None) else None
            msg_l_2 : Optional[List[RawMsg]]
            match_value_5 : Optional[List[RawMsg]] = jny.msg_l
            def predicate_1(msg: RawMsg, jny: RawJny=jny) -> bool:
                def predicate(r: RemarkRange, msg: RawMsg=msg) -> bool:
                    if equals(r.rem_x, msg.rem_x):
                        return not r.whole_leg
                    
                    else: 
                        return False
                    
                
                return not exists_1(predicate, remark_ranges)
            
            msg_l_2 = None if (match_value_5 is None) else filter(predicate_1, match_value_5)
            current_location : Optional[Location]
            match_value_6 : Optional[RawCrd] = jny.pos
            if match_value_6 is None:
                current_location = None
            
            else: 
                pos : RawCrd = match_value_6
                current_location = Location(Default_Location.type, Default_Location.id, Default_Location.name, Default_Location.poi, Default_Location.address, pos.x / 1000000, pos.y / 1000000, Default_Location.altitude, Default_Location.distance)
            
            remarks : Optional[List[Any]] = msg_lto_remarks(ctx, msg_l_2) if ctx.opt.remarks else None
            cycle : Optional[Cycle]
            match_value_7 : Optional[RawFreq] = jny.freq
            if match_value_7 is None:
                cycle = None
            
            else: 
                freq : RawFreq = match_value_7
                match_value_8 : Tuple[Optional[int], Optional[int]] = (freq.min_c, freq.max_c)
                def arrow_449(jny: RawJny=jny) -> Optional[Cycle]:
                    max_c : int = match_value_8[1] or 0
                    min_c : int = match_value_8[0] or 0
                    return Cycle(min_c * 60, max_c * 60, freq.num_c)
                
                def arrow_450(jny: RawJny=jny) -> Optional[Cycle]:
                    min_c_1 : int = match_value_8[0] or 0
                    return Cycle(min_c_1 * 60, None, None)
                
                cycle = (arrow_449() if (match_value_8[1] is not None) else arrow_450()) if (match_value_8[0] is not None) else None
            
            def binder_4(freq_1: RawFreq, jny: RawJny=jny) -> Optional[List[Alternative]]:
                def mapping(array_2: List[RawJny], freq_1: RawFreq=freq_1) -> List[Alternative]:
                    def parse_alternative(a: RawJny, array_2: List[RawJny]=array_2) -> Alternative:
                        line_1 : Optional[Line] = get_element_at(a.prod_x, ctx.common.lines)
                        parsed_when : Optional[ParsedWhen]
                        match_value_9 : Optional[List[RawStop]] = a.stop_l
                        (pattern_matching_result_1, stop_l_1) = (None, None)
                        if match_value_9 is not None:
                            if len(match_value_9) > 0:
                                pattern_matching_result_1 = 0
                                stop_l_1 = match_value_9
                            
                            else: 
                                pattern_matching_result_1 = 1
                            
                        
                        else: 
                            pattern_matching_result_1 = 1
                        
                        if pattern_matching_result_1 == 0:
                            st0 : RawStop = stop_l_1[0]
                            parsed_when = Profile__get_parseWhen(ctx.profile)(ctx)(date)(st0.d_time_s)(st0.d_time_r)(st0.d_tzoffset)(st0.d_cncl)
                        
                        elif pattern_matching_result_1 == 1:
                            parsed_when = None
                        
                        def binder(v: ParsedWhen, a: RawJny=a) -> Optional[str]:
                            return v.when
                        
                        def binder_1(v_1: ParsedWhen, a: RawJny=a) -> Optional[str]:
                            return v_1.planned_when
                        
                        def binder_2(v_2: ParsedWhen, a: RawJny=a) -> Optional[str]:
                            return v_2.prognosed_when
                        
                        def binder_3(v_3: ParsedWhen, a: RawJny=a) -> Optional[int]:
                            return v_3.delay
                        
                        return Alternative(a.jid, a.dir_txt, Default_Alternative.location, line_1, Default_Alternative.stop, bind(binder, parsed_when), bind(binder_1, parsed_when), bind(binder_2, parsed_when), bind(binder_3, parsed_when), Default_Alternative.platform, Default_Alternative.planned_platform, Default_Alternative.prognosed_platform, Default_Alternative.remarks, Default_Alternative.cancelled, Default_Alternative.load_factor, Default_Alternative.provenance, Default_Alternative.previous_stopovers, Default_Alternative.next_stopovers, Default_Alternative.frames, Default_Alternative.polyline, Default_Alternative.current_trip_position, Default_Alternative.origin, Default_Alternative.destination)
                    
                    return map(parse_alternative, array_2, None)
                
                return map_1(mapping, freq_1.jny_l)
            
            alternatives : Optional[List[Alternative]] = bind(binder_4, jny.freq)
            leg = Leg(jny.jid, leg.origin, leg.destination, leg.departure, leg.planned_departure, leg.prognosed_arrival, leg.departure_delay, leg.departure_platform, leg.prognosed_departure_platform, leg.planned_departure_platform, leg.arrival, leg.planned_arrival, leg.prognosed_departure, leg.arrival_delay, leg.arrival_platform, leg.prognosed_arrival_platform, leg.planned_arrival_platform, stopovers_with_remarks, leg.schedule, leg.price, leg.operator, jny.dir_txt, line, jny.is_rchbl, leg.cancelled, leg.walking, leg.load_factor, leg.distance, leg.public, leg.transfer, cycle, alternatives, polyline, remarks, current_location)
        
        iterate(action, to_array(pt.jny))
    
    cancelled : Optional[bool] = default_arg(pt.dep.d_cncl, pt.arr.a_cncl)
    return Leg(leg.trip_id, origin, destination, dep.when, dep.planned_when, arr.prognosed_when, dep.delay, dep_pl.platform, dep_pl.prognosed_platform, dep_pl.planned_platform, arr.when, arr.planned_when, dep.prognosed_when, arr.delay, arr_pl.platform, arr_pl.prognosed_platform, arr_pl.planned_platform, leg.stopovers, leg.schedule, leg.price, leg.operator, leg.direction, leg.line, leg.reachable, cancelled, leg.walking, leg.load_factor, leg.distance, leg.public, leg.transfer, leg.cycle, leg.alternatives, leg.polyline, leg.remarks, leg.current_location)


