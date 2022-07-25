from __future__ import annotations
from typing import (Optional, Tuple, List, Callable, Any)
from ...fable_library.array import (map, filter, try_find as try_find_1, map_indexed)
from ...fable_library.int32 import try_parse
from ...fable_library.option import (map as map_1, bind)
from ...fable_library.reflection import (TypeInfo, string_type, option_type, int32_type, record_type)
from ...fable_library.reg_exp import replace
from ...fable_library.string import substring
from ...fable_library.types import (Record, FSharpRef)
from ...fable_library.util import equals
from ...fs_hafas_python.context import (Context, Profile__get_parseBitmask)
from ...fs_hafas_python.extra_types import IndexMap_2
from ...fs_hafas_python.lib.transformations import (Coordinate_toFloat, Default_Location, Default_Stop, Default_Station)
from ...fs_hafas_python.types_hafas_client import (Location, Line, Stop, Station)
from ...fs_hafas_python.types_raw_hafas_client import (RawLoc, RawCrd, RawCommon)
from .common import (to_option, map_index_array)

def expr_428() -> TypeInfo:
    return record_type("FsHafas.Parser.Location.Lid", [], Lid, lambda: [("L", option_type(string_type)), ("O", option_type(string_type)), ("X", option_type(int32_type)), ("Y", option_type(int32_type))])


class Lid(Record):
    def __init__(self, L: Optional[str], O: Optional[str], X: Optional[int], Y: Optional[int]) -> None:
        super().__init__()
        self.L = L
        self.O = O
        self.X = X
        self.Y = Y
    

Lid_reflection = expr_428

def parse_lid(lid: Optional[str]=None) -> Lid:
    if lid is None:
        return Lid(None, None, None, None)
    
    else: 
        lid_1 : str = lid
        def mapping(s_1: str, lid: Optional[str]=lid) -> Tuple[str, str]:
            return (s_1[0], substring(s_1, 2))
        
        def predicate(s: str, lid: Optional[str]=lid) -> bool:
            return len(s) > 3
        
        tuples : List[Tuple[str, str]] = map(mapping, filter(predicate, lid_1.split("@")), None)
        def try_find(c: str, lid: Optional[str]=lid) -> Optional[str]:
            def mapping_1(tupled_arg_1: Tuple[str, str], c: str=c) -> str:
                return tupled_arg_1[1]
            
            def predicate_1(tupled_arg: Tuple[str, str], c: str=c) -> bool:
                return tupled_arg[0] == c
            
            return map_1(mapping_1, try_find_1(predicate_1, tuples))
        
        try_find : Callable[[str], Optional[str]] = try_find
        def try_parse_int(s_2: str, lid: Optional[str]=lid) -> Optional[int]:
            match_value : Tuple[bool, int]
            out_arg : int = 0
            def arrow_429(s_2: str=s_2) -> int:
                return out_arg
            
            def arrow_430(v_2: int, s_2: str=s_2) -> None:
                nonlocal out_arg
                out_arg = v_2 or 0
            
            match_value = (try_parse(s_2, 511, False, 32, FSharpRef(arrow_429, arrow_430)), out_arg)
            if match_value[0]:
                return match_value[1]
            
            else: 
                return None
            
        
        try_parse_int : Callable[[str], Optional[int]] = try_parse_int
        return Lid(try_find("L"), try_find("O"), bind(try_parse_int, try_find("X")), bind(try_parse_int, try_find("Y")))
    


def remove_leading_zeros(s: str) -> str:
    return replace(s, "^0+", "")


def parse_location_phase1(ctx: Context, i: int, locl: List[RawLoc]) -> Tuple[RawLoc, Any]:
    l : RawLoc = locl[i]
    lid : Lid = parse_lid(l.lid)
    def arrow_431(s: str, ctx: Context=ctx, i: int=i, locl: List[RawLoc]=locl) -> str:
        return remove_leading_zeros(s)
    
    def arrow_432(ctx: Context=ctx, i: int=i, locl: List[RawLoc]=locl) -> Optional[str]:
        match_value : Tuple[Optional[str], Optional[str]] = (l.ext_id, lid.L)
        return match_value[0] if (match_value[0] is not None) else (match_value[1] if (match_value[1] is not None) else None)
    
    id : Optional[str] = map_1(arrow_431, arrow_432())
    pattern_input : Tuple[Optional[float], Optional[float]]
    match_value_1 : Optional[RawCrd] = l.crd
    (pattern_matching_result, crd_1) = (None, None)
    if match_value_1 is not None:
        def arrow_433(ctx: Context=ctx, i: int=i, locl: List[RawLoc]=locl) -> bool:
            crd : RawCrd = match_value_1
            return (crd.y > 0) if (crd.x > 0) else False
        
        if arrow_433():
            pattern_matching_result = 0
            crd_1 = match_value_1
        
        else: 
            pattern_matching_result = 1
        
    
    else: 
        pattern_matching_result = 1
    
    if pattern_matching_result == 0:
        pattern_input = (Coordinate_toFloat(crd_1.x), Coordinate_toFloat(crd_1.y))
    
    elif pattern_matching_result == 1:
        match_value_2 : Tuple[Optional[int], Optional[int]] = (lid.X, lid.Y)
        (pattern_matching_result_1, X, Y) = (None, None, None)
        if match_value_2[0] is not None:
            if match_value_2[1] is not None:
                pattern_matching_result_1 = 0
                X = match_value_2[0]
                Y = match_value_2[1]
            
            else: 
                pattern_matching_result_1 = 1
            
        
        else: 
            pattern_matching_result_1 = 1
        
        if pattern_matching_result_1 == 0:
            pattern_input = (Coordinate_toFloat(X), Coordinate_toFloat(Y))
        
        elif pattern_matching_result_1 == 1:
            pattern_input = (None, None)
        
    
    lon : Optional[float] = pattern_input[0]
    lat : Optional[float] = pattern_input[1]
    def binder(d: int, ctx: Context=ctx, i: int=i, locl: List[RawLoc]=locl) -> Optional[int]:
        if d > 0:
            return d
        
        else: 
            return None
        
    
    distance : Optional[int] = bind(binder, l.dist)
    match_value_3 : Optional[str] = l.type
    if match_value_3 is None:
        return (l, Location(Default_Location.type, id, l.name, Default_Location.poi, Default_Location.address, lon, lat, Default_Location.altitude, distance))
    
    else: 
        type : str = match_value_3
        if type == "S":
            def mapping(_arg1: float, ctx: Context=ctx, i: int=i, locl: List[RawLoc]=locl) -> Location:
                return Location(Default_Location.type, id, Default_Location.name, Default_Location.poi, Default_Location.address, lon, lat, Default_Location.altitude, Default_Location.distance)
            
            def mapping_1(p_cls: int, ctx: Context=ctx, i: int=i, locl: List[RawLoc]=locl) -> IndexMap_2[str, bool]:
                return Profile__get_parseBitmask(ctx.profile)(ctx)(p_cls)
            
            def get_target_array(_arg2: RawCommon, ctx: Context=ctx, i: int=i, locl: List[RawLoc]=locl) -> Optional[List[Line]]:
                return ctx.common.lines
            
            return (l, Stop(Default_Stop.type, id, l.name, map_1(mapping, lon), Default_Stop.station, map_1(mapping_1, l.p_cls), to_option(map_index_array(ctx.res.common, get_target_array, l.p_ref_l)) if ctx.opt.lines_of_stops else None, Default_Stop.is_meta, Default_Stop.reisezentrum_opening_hours, Default_Stop.ids, Default_Stop.load_factor, Default_Stop.entrances, Default_Stop.transit_authority, distance))
        
        else: 
            return (l, Location(Default_Location.type, id, l.name if (type != "A") else None, Default_Location.poi, l.name if (type == "A") else None, lon, lat, Default_Location.altitude, distance))
        
    


def parse_location_phase2(i: int, l: RawLoc, locations: List[Tuple[RawLoc, Any]], common_locations: List[Any]) -> Stop:
    station : Optional[Station]
    match_value : Optional[int] = l.m_mast_loc_x
    (pattern_matching_result, m_mast_loc_x_1) = (None, None)
    if match_value is not None:
        if match_value < len(locations):
            pattern_matching_result = 0
            m_mast_loc_x_1 = match_value
        
        else: 
            pattern_matching_result = 1
        
    
    else: 
        pattern_matching_result = 1
    
    if pattern_matching_result == 0:
        match_value_1 : Tuple[RawLoc, Any] = locations[m_mast_loc_x_1]
        if isinstance(match_value_1[1], Stop):
            stop : Stop = match_value_1[1]
            station = Station(Default_Station.type, stop.id, stop.name, Default_Station.station, stop.location, stop.products, stop.lines, Default_Station.is_meta, Default_Station.regions, Default_Station.facilities, Default_Station.reisezentrum_opening_hours, Default_Station.stops, Default_Station.entrances, Default_Station.transit_authority, Default_Station.distance)
        
        else: 
            station = None
        
    
    elif pattern_matching_result == 1:
        (pattern_matching_result_1, m_mast_loc_x_3) = (None, None)
        if match_value is not None:
            if match_value < len(common_locations):
                pattern_matching_result_1 = 0
                m_mast_loc_x_3 = match_value
            
            else: 
                pattern_matching_result_1 = 1
            
        
        else: 
            pattern_matching_result_1 = 1
        
        if pattern_matching_result_1 == 0:
            match_value_2 : Any = common_locations[m_mast_loc_x_3]
            if isinstance(match_value_2, Stop):
                stop_1 : Stop = match_value_2
                station = Station(Default_Station.type, stop_1.id, stop_1.name, Default_Station.station, stop_1.location, stop_1.products, stop_1.lines, Default_Station.is_meta, Default_Station.regions, Default_Station.facilities, Default_Station.reisezentrum_opening_hours, Default_Station.stops, Default_Station.entrances, Default_Station.transit_authority, Default_Station.distance)
            
            else: 
                station = None
            
        
        elif pattern_matching_result_1 == 1:
            station = None
        
    
    match_value_3 : Tuple[RawLoc, Any] = locations[i]
    if isinstance(match_value_3[1], Stop):
        stop_2 : Stop = match_value_3[1]
        return Stop(stop_2.type, stop_2.id, stop_2.name, stop_2.location, station, stop_2.products, stop_2.lines, stop_2.is_meta, stop_2.reisezentrum_opening_hours, stop_2.ids, stop_2.load_factor, stop_2.entrances, stop_2.transit_authority, stop_2.distance)
    
    else: 
        return match_value_3[1]
    


def parse_locations(ctx: Context, loc_l: List[RawLoc]) -> List[Any]:
    def mapping(i: int, _arg1: RawLoc, ctx: Context=ctx, loc_l: List[RawLoc]=loc_l) -> Tuple[RawLoc, Any]:
        return parse_location_phase1(ctx, i, loc_l)
    
    locations : List[Tuple[RawLoc, Any]] = map_indexed(mapping, loc_l, None)
    def predicate(u3: Any=None, ctx: Context=ctx, loc_l: List[RawLoc]=loc_l) -> bool:
        (pattern_matching_result,) = (None,)
        if isinstance(u3, Location):
            def arrow_434(u3: Any=u3) -> bool:
                l_1 : Location = u3
                return True if equals(l_1.latitude, None) else equals(l_1.longitude, None)
            
            if arrow_434():
                pattern_matching_result = 0
            
            else: 
                pattern_matching_result = 1
            
        
        else: 
            pattern_matching_result = 1
        
        if pattern_matching_result == 0:
            return False
        
        elif pattern_matching_result == 1:
            return True
        
    
    def mapping_1(i_1: int, tupled_arg: Tuple[RawLoc, Any], ctx: Context=ctx, loc_l: List[RawLoc]=loc_l) -> Any:
        return parse_location_phase2(i_1, tupled_arg[0], locations, ctx.common.locations)
    
    return filter(predicate, map_indexed(mapping_1, locations, None))


