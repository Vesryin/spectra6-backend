import os
import uvicorn
from .factory import create_app

if __name__ == "__main__":
    api = create_app()
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    uvicorn.run(
        api,
        host=host,
        port=port,
        log_level="info"
    )
