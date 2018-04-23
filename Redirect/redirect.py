from mitmproxy import http
from mitmproxy import ctx

class Redirect:
    host_filter = "www.only-redirect-requests-from-this-domain.com"

    redirect_rules = {
        "api": "www.new-host.com", # if request url contains `api` then redirect host to `www.new-host.com`
        "images": "cdn.new-host.com" # if request url contains `images` then redirect host to `cdn.new-host.com`
    }

    def request(self, flow: http.HTTPFlow) -> None:
        if (self.url_filter in flow.request.pretty_url):
            for keyword, redirection in self.redirect_rules.items():
                if (flow.request.pretty_host == self.host_filter) and (rule in flow.request.pretty_url):
                    flow.request.host = redirection

addons = [Redirect()]
