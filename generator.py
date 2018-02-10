#!/usr/bin/python
import random
import redis
import sys

from app.configs.RedisPool import POOL
from var.brands import brands
from var.categories import categories
from var.products import products

redisClient = redis.Redis(connection_pool=POOL, decode_responses=True)
redisClient.flushdb()  # remove all data in the DB

# create 50k client
clients = [x * 13 for x in range(1, 10)]
print("\rGenerating data for %s clients" % len(clients))

# create random data recommendation for each client
for c in clients:
    pipe = redisClient.pipeline()
    pipe.multi()
    key = 'cid:%s' % c
    # choose random amount of products
    nb_product = random.randint(30, 3000)
    sys.stdout.write("\rClient %s will have %s products" % (key, nb_product))
    sys.stdout.flush()
    for r in range(1, random.randint(100, 20000)):
        product_id = random.choice(products)
        pipe.sadd(key, product_id)
    pipe.execute()

# add product to categories
print("\rGenerating categories set")
for c in categories[:10]:
    pipe = redisClient.pipeline()
    pipe.multi()
    key = 'product:category:%s' % c
    # choose random amount of products
    nb_product = random.randint(30, 3000)
    sys.stdout.write("\rCategory %s will have %s products" % (key, nb_product))
    sys.stdout.flush()
    for r in range(1, random.randint(100, 20000)):
        product_id = random.choice(products)
        pipe.sadd(key, product_id)
    pipe.execute()

# add product to brands
print("\rGenerating data for brands")
for b in brands[:10]:
    pipe = redisClient.pipeline()
    pipe.multi()
    key = 'product:brand:%s' % b
    # choose random amount of products
    nb_product = random.randint(30, 3000)
    sys.stdout.write("\rBrand %s will have %s products" % (key, nb_product))
    sys.stdout.flush()
    for r in range(1, random.randint(100, 20000)):
        product_id = random.choice(products)
        pipe.sadd(key, product_id)
    pipe.execute()

# generate URL for testing
urls = []
path = 'http://localhost:5000'
print("\rGenerating url for load test")
for c in categories[:10]:
    client = random.choice(clients)
    urls.append('%s/pdp/%s/category/%s' % (path, client, c))

for b in brands[:10]:
    client = random.choice(clients)
    urls.append('%s/pdp/%s/brand/%s' % (path, client, b))


with open('./tests/load/urls.txt', 'w') as f:
    for u in urls:
        f.write(u)
        f.write("\n")
