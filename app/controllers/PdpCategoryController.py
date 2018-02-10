import json

from app.repository.pdp import PdpRepository


class PdpCategoryController:

    def __init__(self, pool):
        self.repository = PdpRepository(pool)

    def on_get(self, req, resp, cid, catid):
        resp.body = json.dumps(list(self.repository.get_by_category(cid, catid)))

    def on_put(self):
        pass

    def on_post(self):
        pass