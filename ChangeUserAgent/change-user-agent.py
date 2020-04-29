from mitmproxy import http
from mitmproxy import ctx

class ChangeUserAgent:
    user_agent = "my-custom-user-agent"

    def request(self, flow: http.HTTPFlow) -> None:
        flow.request.headers["user-agent"] = self.user_agent

addons = [ChangeUserAgent()]
