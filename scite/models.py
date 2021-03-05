# -*- coding: utf-8 -*-
from typing import Any, AnyStr, Dict, List, NamedTuple
import pandas as pd


DOI = AnyStr
DOIs = List[DOI]
JSON = Dict[str, Any]
Reference = NamedTuple(
    "References", [
        ("target_doi", DOI), 
        ("concise_references", list),
        ("detailed_references", pd.DataFrame)
    ]
)