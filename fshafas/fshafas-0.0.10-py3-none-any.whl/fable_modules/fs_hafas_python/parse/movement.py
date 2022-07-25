from __future__ import annotations
from typing import (Optional, Any, Tuple, List)
from ...fable_library.array import (choose, map_indexed)
from ...fable_library.option import value as value_1
from ...fs_hafas_python.context import (Context, Profile__get_parseStopovers, Profile__get_parsePolyline)
from ...fs_hafas_python.lib.transformations import (Default_Location, Coordinate_toFloat, U2StopLocation_FromSomeU3StationStopLocation)
from ...fs_hafas_python.types_hafas_client import (Location, Frame, FeatureCollection, Movement)
from ...fs_hafas_python.types_raw_hafas_client import (RawJny, RawCrd, RawAni, RawPoly, PolyG)
from .common import get_element_at

def parse_movement(ctx: Context, m: RawJny) -> Movement:
    def arrow_425(ctx: Context=ctx, m: RawJny=m) -> Optional[Location]:
        match_value : Optional[RawCrd] = m.pos
        if match_value is None:
            return None
        
        else: 
            pos : RawCrd = match_value
            return Location(Default_Location.type, Default_Location.id, Default_Location.name, Default_Location.poi, Default_Location.address, Coordinate_toFloat(pos.x), Coordinate_toFloat(pos.y), Default_Location.altitude, Default_Location.distance)
        
    
    def arrow_426(ctx: Context=ctx, m: RawJny=m) -> Optional[List[Frame]]:
        match_value_1 : Optional[RawAni] = m.ani
        if match_value_1 is None:
            return None
        
        else: 
            ani : RawAni = match_value_1
            def chooser(x: Optional[Frame]=None) -> Optional[Frame]:
                return x
            
            def mapping(i: int, ms: int) -> Optional[Frame]:
                match_value_2 : Tuple[Optional[Any], Optional[Any]] = (U2StopLocation_FromSomeU3StationStopLocation(get_element_at(ani.f_loc_x[i], ctx.common.locations)), U2StopLocation_FromSomeU3StationStopLocation(get_element_at(ani.t_loc_x[i], ctx.common.locations)))
                (pattern_matching_result, destination_1, origin_1) = (None, None, None)
                if match_value_2[0] is not None:
                    if match_value_2[1] is not None:
                        pattern_matching_result = 0
                        destination_1 = value_1(match_value_2[1])
                        origin_1 = value_1(match_value_2[0])
                    
                    else: 
                        pattern_matching_result = 1
                    
                
                else: 
                    pattern_matching_result = 1
                
                if pattern_matching_result == 0:
                    return Frame(origin_1, destination_1, ms)
                
                elif pattern_matching_result == 1:
                    return None
                
            
            return choose(chooser, map_indexed(mapping, ani.m_sec, None), None)
        
    
    def arrow_427(ctx: Context=ctx, m: RawJny=m) -> Optional[FeatureCollection]:
        match_value_3 : Optional[RawAni] = m.ani
        if match_value_3 is None:
            return None
        
        else: 
            ani_1 : RawAni = match_value_3
            match_value_4 : Optional[RawPoly] = ani_1.poly
            if match_value_4 is None:
                match_value_5 : Optional[PolyG] = ani_1.poly_g
                if match_value_5 is None:
                    return None
                
                else: 
                    poly_g : PolyG = match_value_5
                    idx : int = poly_g.poly_xl[0] or 0
                    return ctx.common.polylines[idx] if (idx < len(ctx.common.polylines)) else None
                
            
            else: 
                value : RawPoly = match_value_4
                return Profile__get_parsePolyline(ctx.profile)(ctx)(value)
            
        
    
    return Movement(m.dir_txt, m.jid, get_element_at(m.prod_x, ctx.common.lines), arrow_425(), Profile__get_parseStopovers(ctx.profile)(ctx)(m.stop_l)(value_1(m.date)), arrow_426(), arrow_427())


