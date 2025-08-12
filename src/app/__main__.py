import os
from . import api

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    api.run(address="0.0.0.0", port=port, debug=False)
