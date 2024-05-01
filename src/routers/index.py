import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

index_router = APIRouter()

templates = Jinja2Templates(
    directory="src/public/templates",
)


@index_router.get(
    path="/",
    response_class=HTMLResponse,
)
async def index(
    request: Request,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="/index/index.html",
        context={}
    )