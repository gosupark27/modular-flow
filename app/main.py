from fastapi import FastAPI
from app.routes import mirror_log

app = FastAPI()

app.include_router(mirror_log.router, prefix="/mirror-log")
