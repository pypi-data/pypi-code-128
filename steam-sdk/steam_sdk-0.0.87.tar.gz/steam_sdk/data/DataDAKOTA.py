from pydantic import BaseModel, PrivateAttr, Field
from typing import (Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union, Type, Literal)
import ruamel.yaml

### SUBLEVEL
class interface(BaseModel):
    analysis_drivers: str = ''
    interface_arguments: Dict = {}

class responses(BaseModel):
    response_functions: int = 0
    objective_functions: int = 0
    nonlinear_inequality_constraints: int = 0
    calibration_terms: int = 0
    type_gradients: str = ''
    numerical_gradients: Dict = {}
    analytical_gradients: Dict = {}
    no_gradients: bool = False
    no_hessians: bool = False

class variables(BaseModel):
    type_variable: str = ''
    variable_arguments: Dict = {}

class model(BaseModel):
    type_model: str = ''

class method(BaseModel):
    type_method: str = ''
    method_argument: Dict = {}

class environment(BaseModel):
    graphics: bool = False
    type_tabular_data: str = ''
    tabular_data_argument: Dict = {}

######### MAIN LEVEL #####
class DAKOTA_analysis(BaseModel):
    interface: interface = interface()
    responses: responses = responses()
    variables: variables = variables()
    method: method = method()
    model: model = model()
    environment: environment = environment()