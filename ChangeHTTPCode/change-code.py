from mitmproxy import http
from mitmproxy import ctx

class ChangeHTTPCode:
    http_code_rules = {
        "my-domain/images": 404 # if request url contains `my-domain/images` then returned HTTP code is 404
    }

    def response(self, flow: http.HTTPFlow) -> None:
        for keyword, http_code in self.http_code_rules.items():
            if (keyword in flow.request.pretty_url):
                flow.response.status_code = http_code

addons = [ChangeHTTPCode()]
