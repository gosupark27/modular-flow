#!/bin/bash
# Run FastAPI app with hot-reload
uvicorn app.main:app --reload --port 8000
