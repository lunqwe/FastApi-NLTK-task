from fastapi import APIRouter, Depends, HTTPException

from schemas.schemas import RequestSchema
from services.services import NTKLService

router = APIRouter()
ntkl_service = NTKLService()

@router.post('/tokenize', tags=['NTKL-Endpoints'])
async def tokenize(request: RequestSchema):
    try:
        tokens = await ntkl_service.tokenize_text(request.text)
        return {"tokens": tokens}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/pos_tag', tags=['NTKL-Endpoints'])
async def pos_tag(request: RequestSchema):
    try:
        pos_tags = await ntkl_service.pos_tag_text(request.text)
        return {"pos_tags": pos_tags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/ner', tags=['NTKL-Endpoints'])
async def ner(request: RequestSchema):
    try:
        named_entities = await ntkl_service.ner_text(request.text)
        # result to a readable format
        entities = []
        for tree in named_entities:
            if hasattr(tree, 'label'):
                entity_name = ' '.join([child[0] for child in tree])
                entity_type = tree.label()
                entities.append({"entity": entity_name, "type": entity_type})
        return {"named_entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
