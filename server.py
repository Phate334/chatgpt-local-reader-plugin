from http.server import test, SimpleHTTPRequestHandler


class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "https://chat.openai.com")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header(
            "Access-Control-Allow-Headers",
            "content-type, openai-conversation-id, openai-ephemeral-user-id",
        )
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        return super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()


if __name__ == "__main__":
    test(HandlerClass=CORSHTTPRequestHandler)
