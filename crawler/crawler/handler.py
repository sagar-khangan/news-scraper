import pymongo
import re
import json
from bson.json_util import dumps
from crawler import settings
from scrapy.log import logger

client = pymongo.MongoClient(settings.MONGO_URI,ssl=True)
db = client[settings.MONGO_DATABASE]
collection = db[settings.MONGO_COLLECTION]


def get_data(args):
    """

    :param args:
    :return: query response
    """
    try:
        if not args:
            # Without any query params
            logger.info("Request for all data...")
            return dumps(collection.find())
        else:
            # with query params
            _args = dict(args)
            if [i for i in filter(lambda x: x not in settings.ALLOWED_ARGS,_args.keys())]:
                return '{"msg":"incorrect arguments"}'
            else:
                # generating query with params
                query = dict()
                for k, v in _args.items():
                    if k != 'limit':
                        query[k] = re.compile(".*"+v+".*", re.IGNORECASE)
                logger.info("Request for data with query %s..." % json.dumps(query))
                if 'limit' in _args.keys():
                    return dumps(collection.find(query).limit(int(_args.get('limit',1))))
                else:
                    return dumps(collection.find(query))
    except Exception as e:
        logger.exception("Exception occured %s" %str(e))
        return '{"msg":"something went wrong"}'
