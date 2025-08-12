import os
import uvicorn
from . import api

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    # Use uvicorn to run the responder app
    uvicorn.run(
        "app:api",
        host=host,
        port=port,
        log_level="info",
        access_log=True
    )
