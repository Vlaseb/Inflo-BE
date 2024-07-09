from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints.auth import auth_router


router = FastAPI()

origins = ["http://localhost:3000"]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router.include_router(auth_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=8000)
