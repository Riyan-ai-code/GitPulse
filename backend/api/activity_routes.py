from fastapi import APIRouter, HTTPException

from models.models import MergeRequest
from services.ingestion.activity_service import ingest_activity
router= APIRouter()
@router.post("/ingest_activity")