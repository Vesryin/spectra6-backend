import responder

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "Hello, world!"

if __name__ == "__main__":
    api.run()
