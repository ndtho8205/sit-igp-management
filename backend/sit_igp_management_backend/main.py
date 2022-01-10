from fastapi import FastAPI

from sit_igp_management_backend.api.professors import professors_router


app = FastAPI()

app.include_router(professors_router.router)


@app.get("/")
def read_root():
    return {"message": "API is up and running."}
