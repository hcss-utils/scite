# -*- coding: utf-8 -*-
from .http_utils import remote_call
from .logging_utils import set_logger
from .models import DOI, DOIs

logger = set_logger("Papers")


def get_paper(doi: DOI):
    """Get paper metadata for DOI.


    Examples
    --------
    >>> doi = "10.1017/cbo9780511628283.008"
    >>> get_paper(doi)

    Notes
    -----
    Docs: https://api.scite.ai/docs#operation/get_paper_papers__doi__get
    """
    if not isinstance(doi, DOI):
        doi = DOI(id=doi).id
    logger.debug(f"Calling https://api.scite.ai/papers/{doi}")
    return remote_call(endpoint=f"papers/{doi}")


def get_papers_by_target(target_doi: DOI):
    """Get papers citing a given DOI.


    Examples
    --------
    >>> target_doi = "10.1017/cbo9780511628283.008"
    >>> get_papers_by_target(target_doi)

    Notes
    -----
    Docs: https://api.scite.ai/docs#operation/get_target_sources_papers_sources__target_doi__get
    """  # noqa
    if not isinstance(target_doi, DOI):
        target_doi = DOI(id=target_doi).id
    logger.debug(f"Calling https://api.scite.ai/papers/{target_doi}")
    return remote_call(endpoint=f"papers/sources/{target_doi}")


def get_papers(dois: DOIs):
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
    if not isinstance(dois, DOIs):
        items = DOIs(ids=[{"id": item} for item in dois])
        dois = {item.id for item in items.ids}
    logger.debug(
        f"Calling https://api.scite.ai/papers with a payload of {len(dois)} papers"
    )
    response = remote_call(endpoint="papers", payload=[*dois])
    return response.json()
