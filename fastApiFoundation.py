from fastapi import FastAPI

app = FastAPI(
    title="Swiggy order service",
    description=(
        "Internal API for managing orders"
        "Handle creation, tracking of delivery system"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """root end point - Health Check"""
    #  Fast API automatically converts this dictonary into JSON
    return{
        "message":"welcome to swiggy order service",
        "status":"Healthy"
    }

@app.get("/about")
def about():
    """returns API data"""
    return {
        "Service":"Order Service",
        "team":"Backend platform",
        "region":"tg-south-2",
        "version":"1.2.2"
    }