from mitmproxy import http
from mitmproxy import ctx

class Redirect:
    redirect_rules = {
        "my-domain.com/images": "my-domain.com/images-new", # replace `my-domain.com/images` with `my-domain.com/images-new` in requests url
        "my-domain.com/api": "my-domain.com/api-new"
    }

    def load(self, loader):
        ctx.options.http2 = False # HTTP2 won't let you update the url

    def request(self, flow: http.HTTPFlow) -> None:
        for init_domain, new_domain in self.redirect_rules.items():
            if (init_domain in flow.request.pretty_url):
                flow.request.url = flow.request.pretty_url.replace(init_domain, new_domain)


addons = [Redirect()]
