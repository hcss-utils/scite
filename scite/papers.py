# -*- coding: utf-8 -*-
from .models import DOI, DOIs, JSON 
from .http_utils import remote_call
from .logging_utils import set_logger

logger = set_logger("Papers")


def get_paper(doi: DOI) -> JSON:
    """Get paper metadata for DOI. 

    
    Examples
    --------
    >>> doi = "10.1017/cbo9780511628283.008"
    >>> get_paper(doi)

    Notes
    -----
    Docs: https://api.scite.ai/docs#operation/get_paper_papers__doi__get
    """
    logger.debug(f"Calling https://api.scite.ai/papers/{doi}")
    return remote_call(endpoint=f"papers/{doi}")


def get_papers_by_target(target_doi: DOI) -> JSON:
    """Get papers citing a given DOI.


    Examples
    --------
    >>> target_doi = "10.1017/cbo9780511628283.008"
    >>> get_papers_by_target(target_doi)

    Notes
    -----
    Docs: https://api.scite.ai/docs#operation/get_target_sources_papers_sources__target_doi__get
    """
    logger.debug(f"Calling https://api.scite.ai/papers/{target_doi}")
    return remote_call(endpoint=f"papers/sources/{target_doi}")


def get_papers(dois: DOIs) -> JSON:
    """Get multiple papers.
    Up to 500 papers can be requested at once by passing in a list of DOIs

    
    Examples
    --------
    >>> DOIS = [
    ...    "10.1017/CBO9780511628283.008",
    ...    "10.1093/oxfordhb/9780199646135.013.7"
    ... ]
    >>> get_papers(DOIs)

    Notes
    -----
    Docs: https://api.scite.ai/docs#operation/get_papers_papers_get
    """
    logger.debug(f"Calling https://api.scite.ai/papers with a payload of {len(dois)} papers")
    return remote_call(endpoint="papers", payload=dois)