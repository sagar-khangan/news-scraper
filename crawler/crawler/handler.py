import pymongo
import re
from bson.json_util import dumps
from crawler import settings
from scrapy.log import logger

client = pymongo.MongoClient(settings.MONGO_URI,ssl=True)
db = client[settings.MONGO_DATABASE]
collection = db[settings.MONGO_COLLECTION]


def get_data(args):
    try:
        if not args:
            return dumps(collection.find())
        else:
            _args = dict(args)
            if [i for i in filter(lambda x: x not in settings.ALLOWED_ARGS,_args.keys())]:
                return '{"msg":"incorrect arguments"}'
            else:
                query = dict()
                for k, v in _args.items():
                    query[k] = re.compile(".*"+v+".*", re.IGNORECASE)
                if 'limit' in _args.keys():
                    return dumps(collection.find(query).limit(_args.get('limit',1)))
                else:
                    return dumps(collection.find(query))
    except Exception as e:
        logger.exception("Exception occured %s" %str(e))
        return '{"msg":"something went wrong"}'
