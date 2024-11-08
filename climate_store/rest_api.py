from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .gee_interface import fetch_era5_data


def get_app():
    app = FastAPI(root_path="/v1")
    origins = [
        "*",  # Allow all origins
        "http://localhost:3000",
        "localhost:3000",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = get_app()

climate_data = app.get("/climate_data")(fetch_era5_data)


def main_backend():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
