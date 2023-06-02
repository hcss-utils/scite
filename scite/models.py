# -*- coding: utf-8 -*-
from typing import Any, List

from pydantic import BaseModel, Field, validator


class DOI(BaseModel):
    id: str = Field(regex=r"^10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+$")


class DOIs(BaseModel):
    ids: List[DOI]

    @validator("ids")
    def check_size(cls, v: List[Any]):
        size = len(v)
        if size < 1 or size > 500:
            raise ValueError("API takes up to 500 DOIs per request.")
        return v
