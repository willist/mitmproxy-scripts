def response(context, flow):
    flow.response.headers['X-Silly'] = ['This is a very silly header']
