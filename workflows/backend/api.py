import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import router

app = FastAPI(title='Workflow Execution Service')


def _get_cors_origins() -> list[str]:
	raw = os.getenv('WORKFLOW_USE_CORS_ORIGINS', 'http://localhost:5173,http://127.0.0.1:5173')
	origins = [origin.strip() for origin in raw.split(',') if origin.strip()]
	return origins or ['http://localhost:5173']


cors_origins = _get_cors_origins()
allow_all = '*' in cors_origins

# Add CORS middleware
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'] if allow_all else cors_origins,
	allow_credentials=not allow_all,
	allow_methods=['*'],
	allow_headers=['*'],
)

# Include routers
app.include_router(router)


# Optional standalone runner
if __name__ == '__main__':
	uvicorn.run('api:app', host='127.0.0.1', port=8000, log_level='info')
