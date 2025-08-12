import os
import responder
from dotenv import load_dotenv
from .engine.emotional_state import EmotionalState, Emotion
from .engine.semantic_memory import SemanticMemory

load_dotenv()

api = responder.API()
emotional_engine = EmotionalState()
db_conn_string = os.getenv("DATABASE_URL")
if db_conn_string:
    memory_engine = SemanticMemory(db_conn_string)
else:
    memory_engine = None

@api.route("/")
def hello_world(req, resp):
    resp.text = "Hello, world!"

@api.route("/chat")
async def chat(req, resp):
    """
    Endpoint for real-time conversations.
    """
    if req.method == "post":
        data = await req.media()
        message = data.get("message")
        # TODO: Process message and get response from AI model
        resp.media = {"response": f"You said: {message}"}
    else:
        resp.status_code = 405
        resp.text = "Method Not Allowed"

@api.route("/emotion")
async def emotion(req, resp):
    """
    Endpoint to retrieve and update emotional states.
    """
    if req.method == "get":
        current_emotion = emotional_engine.get_state()
        resp.media = {"emotion": current_emotion.value}
    elif req.method == "post":
        data = await req.media()
        new_emotion_str = data.get("emotion")
        if new_emotion_str:
            try:
                new_emotion = Emotion(new_emotion_str.lower())
                emotional_engine.update_state(new_emotion)
                resp.media = {"status": f"Emotion updated to {new_emotion.value}"}
            except ValueError:
                resp.status_code = 400
                valid_emotions = [e.value for e in Emotion]
                resp.media = {
                    "error": f"Invalid emotion '{new_emotion_str}'. Valid emotions are: {valid_emotions}"
                }
        else:
            resp.status_code = 400
            resp.media = {"error": "Emotion not provided in request body."}
    else:
        resp.status_code = 405
        resp.text = "Method Not Allowed"

@api.route("/memory")
async def memory(req, resp):
    """
    Endpoint to manage and query memory.
    """
    if not memory_engine:
        resp.status_code = 503
        resp.media = {"error": "Memory engine not available. Check DATABASE_URL."}
        return

    if req.method == "get":
        query = req.params.get("q")
        if query:
            results = memory_engine.search_memory(query)
            resp.media = {"results": results}
        else:
            resp.status_code = 400
            resp.media = {"error": "Query parameter 'q' is required."}
    elif req.method == "post":
        data = await req.media()
        memory_to_add = data.get("memory")
        if memory_to_add:
            memory_engine.add_memory(memory_to_add)
            resp.media = {"status": f"Memory added: {memory_to_add}"}
        else:
            resp.status_code = 400
            resp.media = {"error": "Memory not provided in request body."}
    else:
        resp.status_code = 405
        resp.text = "Method Not Allowed"
