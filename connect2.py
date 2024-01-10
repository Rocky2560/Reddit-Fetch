import requests
import json
import base64
from Crypto.Cipher import AES


# Remove padding at end of byte array
def unpad(byte_array):
    last_byte = byte_array[-1]
    return byte_array[0:-last_byte]


def decrypt(key, message):
    """
    Input encrypted bytes, return decrypted bytes, using iv and key
    """

    byte_array = base64.b64decode(message)

    iv = byte_array[0:16]   # extract the 16-byte initialization vector

    message_bytes = byte_array[16:]  # encrypted message is the bit after the iv

    cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv)

    decrypted_padded = cipher.decrypt(message_bytes)

    decrypted = unpad(decrypted_padded)

    return decrypted.decode("UTF-8")


database_url = 'https://casservice.ekbana.net/select'

#query = """select * from v_sale where billyear = '2020' and billdate >='2020-05-05' and billdate < '2020-05-06'"""

#query = """select * from ip_detail where latitude=27.4284 and longitude=85.0322 limit 1"""

query = """select * from reddit_post limit 1"""


offset_key = ""
session_id = ""
status = ""

try:
    while status != 'done':
        json_format = \
            {
                "dbms": "cassandra",
                "query": query,
                "username": "cassandra",
                "password": "cassandra",
                "offset_key": offset_key,
                "session_id": session_id
            }

        request = requests.post(database_url, data=json.dumps(json_format),
                                headers={"Content-Type": "application/json"})
        json_result = request.json()
        status_code = json_result['status_code']
        print(status_code)
        if status_code == 200:
            session_id = json_result['session_id']
            status = json_result['status']
            offset_key = json_result['offset_key']
            result = json_result['result']
            print(decrypt("9uMs6PFC9aQ8ztEhG63rApu6pTZRBRmk", result))
        else:
            print("status_code: %d" % status_code)
            print("error_msg: %s" % json_result['msg'])
            print("Error while fetching data")
            break
except Exception as e:
    print(e)


