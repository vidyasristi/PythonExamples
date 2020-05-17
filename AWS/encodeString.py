import io
import json
import base64
import gzip
import zlib

var1 = '''{
    "messageType": "DATA_MESSAGE",
    "owner": "464420198474",
    "logGroup": "dms-tasks-dms-fn2-snbxsf-01",
    "logStream": "dms-task-2a946c13825649dcb02b3dba65918507",
    "subscriptionFilters": [
        "mySAMstack-HelloWorldFunctionHelloWorld-1A8JCZHKAAU9O"
    ],
    "logEvents": [
        {
            "id": "35452582176479425658919633457661363434145338943644958722",
            "timestamp": 1589748766728,
            "message": "END RequestId: 03701e42-9181-4a9b-a515-6309668841df"
        }
    ]
}'''

def gzip_str(string_):
    out = io.BytesIO()

    with gzip.GzipFile(fileobj=out, mode='w') as fo:
        fo.write(bytes(string_, 'utf_8'))

    bytes_obj = out.getvalue()
    return base64.b64encode(bytes_obj)


gz = gzip_str(var1)
print(gz)

decodedEvent = zlib.decompress(base64.b64decode(gz), 16 + zlib.MAX_WBITS).decode("utf-8")
print('decodedEvent:v' + decodedEvent)
