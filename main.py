from fastapi import FastAPI, APIRouter
from app.handlers import quiz_router


app = FastAPI(title="Questions for quiz")
main_router = APIRouter()

main_router.include_router(quiz_router)
app.include_router(main_router)
