import json


def request(context, flow):
    flow.request.anticache()
    flow.request.anticomp()


def response(context, flow):
    if flow.match("~u forecast.io/forecast"):
        with open("barrow.json") as f:
            barrow_current = json.load(f)
            data = json.loads(flow.response.content)

            data["currently"] = barrow_current
            flow.response.content = json.dumps(data)
