from fastapi import FastAPI, APIRouter
from app.handlers import router


application = FastAPI(title="Questions for quiz")
main_router = APIRouter()

main_router.include_router(router)
application.include_router(main_router)
