import falcon

from app.configs.RedisPool import POOL
from app.controllers.DefaultController import DefaultController
from app.controllers.PdpBrandController import PdpBrandController
from app.controllers.PdpCategoryController import PdpCategoryController

app = falcon.API()

app.add_route('/pdp/{cid}/category/{catid}', PdpCategoryController(POOL))
app.add_route('/pdp/{cid}/brand/{bid}', PdpBrandController(POOL))
app.add_route('/', DefaultController())
