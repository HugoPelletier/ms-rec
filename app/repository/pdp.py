import time

from app.repository.BaseRepository import BaseRepository


class PdpRepository(BaseRepository):

    def __init__(self, pool):
        BaseRepository.__init__(self, pool)

    def get_by_category(self, cid, catid):
        start = time.time()
        print(['cid:%s' % cid, 'product:category:%s' % catid])
        data = self.get_redis().sinter(['cid:%s' % cid, 'product:category:%s' % catid])
        print("--- %s seconds ---" % (time.time() - start))
        return data


    def get_by_brand(self, cid, bid):
        start = time.time()
        print(['cid:%s' % cid, 'product:brand:%s' % bid])
        data = self.get_redis().sinter(['cid:%s' % cid, 'product:brand:%s' % bid])
        print("--- %s seconds ---" % (time.time() - start))
        return data
