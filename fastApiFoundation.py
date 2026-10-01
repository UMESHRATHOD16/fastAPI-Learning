from fastapi import FastAPI
from fastapi import Request

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

@app.get("/orders")
def list_orders():
    """List recent Orders"""
    return{
        "orders":[
            {"id": 1, "item":"Butter Chicken", "status":"Delivered"},
            {"id": 2, "item":"Masala Dosa", "status":"preparing"},
            {"id": 3, "item":"Paneer Tikka", "status":"Delivered"}
        ]
    }

@app.get("/orders/status")
def order_status():
    """Get order status"""
    return{
        "total_today":2_340_45,
        "top_location":"Hyderabad"
    }

@app.get("/debug/request-info")
async def get_info(request:Request):
    """Inspect the raw request object"""
    return {
        "method":request.method,
        "url":str(request.url),
        "headers":dict(request.headers),
        "path_params": request.path_params,
        "query_params":dict(request.query_params),
    }
