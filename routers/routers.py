from fastapi import APIRouter, Depends, HTTPException

from schemas.schemas import ResponseSchema

router = APIRouter()


@router.post('/tokenize', tags=['NTKL-Endpoints'])
def tokenize(data: ResponseSchema = None):
    pass

@router.post('/pos_tag', tags=['NTKL-Endpoints'])
def pos_tag(data: ResponseSchema = None):
    pass

@router.post('/ner', tags=['NTKL-Endpoints'])
def ner(data: ResponseSchema = None):
    pass

