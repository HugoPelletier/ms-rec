import json

from app.repository.pdp import PdpRepository


class PdpBrandController:

    def __init__(self, pool):
        self.repository = PdpRepository(pool)

    def on_get(self, req, resp, cid, bid):
        resp.body = json.dumps(list(self.repository.get_by_brand(cid, bid)))

    def on_put(self):
        pass

    def on_post(self):
        pass
