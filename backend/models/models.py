#A Input the code and then check for the code activity store thr code from differernt sources and then compare it to get conflict and to generate an output
from pydantic import BaseModel
from typing import List, Optional
#BaseModel is a class from the Pydantic library that provides data validation and parsing capabilities. It allows you to define data models with type annotations, and it will automatically validate and parse the input data based on those annotations.
class MergeRequest(BaseModel):#Merge request all the three types
    base_code:str
    head_code:str
    incoming_code:str
class ConflictState(BaseModel):# all the states
    physical:bool
    semantic:bool
    compilable:bool
    resolved:bool
class MergeConflict(BaseModel):#Merge
    merged_code:str# output storage
    conflict_regions:List[str]# regions with conflicts
    state:ConflictState
    status:str
class MergeResult(BaseModel):#Merge result
    resolved_code:Optional[str]
    status:str
#flow is merge->conflict detection->conflict resolution->output generation(until here)