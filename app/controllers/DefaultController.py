import falcon


class DefaultController:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nhello world\n\n')

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_404
        resp.body = ('\nNot supported\n\n')

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_404
        resp.body = ('\nNot supported\n\n')