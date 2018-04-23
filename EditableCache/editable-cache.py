from mitmproxy import http
from mitmproxy import ctx
import os

class EditableCache:
    url_filter = "www.only-redirect-requests-from-this-domain.com"
    path = "/Full/path/to/cache/folder"

    def response(self, flow: http.HTTPFlow) -> None:
        if (self.url_filter in flow.request.pretty_url):
            fullpath = self.path + "/" + self.clean_url(flow.request.url)
            if not os.path.isfile(fullpath):
                if not os.path.exists(os.path.dirname(fullpath)):
                    os.makedirs(os.path.dirname(fullpath))
                file = open(fullpath, "w")
                file.write(flow.response.text)
                file.close()

    def request(self, flow: http.HTTPFlow) -> None:
        if (self.url_filter in flow.request.pretty_url):
            fullpath = self.path + "/" + self.clean_url(flow.request.url)
            if os.path.isfile(fullpath):
                with open(fullpath, 'r') as cache_file:
                    cache_content = cache_file.read()
                flow.response = http.HTTPResponse.make(
                    200,
                    cache_content
                )

    def clean_url(self, url):
        filename = url
        filename = filename.replace("https://", "")
        filename = filename.replace("?", "_")
        filename = filename.replace(",", "-")
        return filename

addons = [EditableCache()]
