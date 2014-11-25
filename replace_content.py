from collections import namedtuple

Replacement = namedtuple('Replacement', ['active', 'pattern', 'filepath'])
REPLACEMENTS = map(Replacement._make, [
    (True, '~u mitmproxy', 'requirements.txt'),
])


def request(context, flow):
    flow.request.anticache()
    flow.request.anticomp()


def response(context, flow):
    for replacement in REPLACEMENTS:
        if replacement.active and flow.match(replacement.pattern):
            with open(replacement.filepath) as f:
                flow.response.content = f.read()
