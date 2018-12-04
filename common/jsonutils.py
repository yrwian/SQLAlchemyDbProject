import json

from model.user import User


class JsonUtils:

    def json2obj(self, jsonObj, obj):
        keys = jsonObj.keys()
        for key in keys:
            if hasattr(obj, key):
                setattr(obj, key, jsonObj[key])
        return obj

    def jsonStr2obj(self, jsonstr, obj):
        objdict = json.loads(jsonstr)
        return self.json2obj(objdict, obj)

    def jsonobj2Str(self, jsonobj):
        jsonstr = json.dumps(jsonobj, ensure_ascii=False)
        return jsonstr

    def obj2json(self, city):
        dict = city.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def obj2jsonStr(self, city):
        obj_json = self.obj2json(city)
        jsonstr = json.dumps(obj_json, ensure_ascii=False)
        return jsonstr

    def __test__(self):
        cityjson = {
            "city_name": "%s你好",
            "id": "1212",
        }
        utils = JsonUtils()
        obj = utils.json2obj(cityjson, User())
        print(utils.obj2jsonStr(obj))


if __name__ == '__main__':
    JsonUtils().__test__()
