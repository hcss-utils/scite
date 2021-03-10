# -*- coding: utf-8 -*-
from .models import DOI, DOIs
from .http_utils import remote_call
from .logging_utils import set_logger

logger = set_logger("Tallies")


def get_tally(doi):
    """Get smart citation tally for given DOI.

    
    Examples
    --------
    >>> get_tally("10.1016/j.biopsych.2005.08.012")
    ... {
    ...    'doi': '10.1016/j.biopsych.2005.08.012', 
    ...    'total': 318, 
    ...    'supporting': 24, 
    ...    'contradicting': 4, 
    ...    'mentioning': 290, 
    ...    'unclassified': 0
    ...}
    
    Notes
    -----
    Docs: https://api.scite.ai/docs#operation/get_tally_tallies__doi__get
    """
    if not isinstance(doi, DOI):
        doi = DOI(id=doi).id
    logger.debug(f"Calling https://api.scite.ai/tallies/{doi}")
    return remote_call(endpoint=f"tallies/{doi}")


def get_tallies(dois):
    """Get multiple smart citation tallies
    Up to 500 papers can be requested at once by
    passing in a list of DOIs

    
    Examples
    --------
    >>> DOIs = ["10.1017/CBO9780511628283.008", "10.1093/oxfordhb/9780199646135.013.7"]
    >>> get_tallies(DOIs)
    
    Notes
    -----
    Docs: https://api.scite.ai/docs#operation/get_tallies_tallies_get
    """
    if not isinstance(dois, DOIs):
        items = DOIs(ids=[{"id": item} for item in dois])
        dois = {item.id for item in items.ids}
    logger.debug(f"Calling https://api.scite.ai/tallies with a payload of {len(dois)} papers")
    return remote_call(endpoint="tallies", payload=[*dois])
