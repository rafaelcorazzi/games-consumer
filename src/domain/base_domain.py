import json
import datetime
import decimal


class BaseDomain(object):

    @staticmethod
    def default(o):
        if type(o) is BaseDomain:
            return o.toJSON()
        if type(o) is datetime.date or type(o) is datetime.datetime:
            return o.isoformat()
        if type(o) is decimal.Decimal:
            return float(o)
        if type(o) is bytes:
            return o.decode('utf-8')

        return o.__dict__

    def to_json(self):
        return json.loads(json.dumps(self, default=BaseDomain.default, ensure_ascii=False).encode('utf8'))
