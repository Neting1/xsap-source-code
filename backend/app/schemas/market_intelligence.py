from pydantic import BaseModel
from typing import Dict, List


class SectorPerformanceResponse(
    BaseModel
):

    sector: str
    average_return: float
    trend: str


class SectorExposureResponse(
    BaseModel
):

    sector_exposure: Dict[
        str,
        float
    ]


class BestSectorResponse(
    BaseModel
):

    best_sector: str
    expected_growth: float


class RotationOpportunityResponse(
    BaseModel
):

    from_sector: str
    to_sector: str
    reason: str