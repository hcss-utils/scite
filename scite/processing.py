# -*- coding: utf-8 -*-
import pandas as pd

from .papers import get_papers_by_target
from .models import DOI, Reference


def generate_references(doi: DOI) -> Reference:
    """Get a detailed info on papers citing a given DOI.
    

    Examples
    --------
    >>> refs = generate_references("10.1017/cbo9780511628283.008")
    >>> refs.target_doi
    '10.1017/cbo9780511628283.008'
    """
    refs = get_papers_by_target(doi)
    if refs == {"detail": "Paper not found"}:
        raise ValueError("Paper not found in the database.")
    
    concise_refs = [*refs["papers"].keys()] 
    detailed_table = pd.DataFrame([*refs["papers"].values()])
    return Reference(
        target_doi=doi,
        concise_references=concise_refs,
        detailed_references=detailed_table
    )
