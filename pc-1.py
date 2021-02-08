import json
import requests
import sys
 
url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
apikey = "ccf9c4dda0eed674c075b234b8d3d390"
query = "광장동 피시방"

for i in range(1,2):
    r = requests.get( url, params = {'page':str(i), 'query':query}, headers={'Authorization' : 'KakaoAK ' + apikey } ).text
    r = json.loads(str(r))
    match_first = r['documents']
    #print(match_first)
    #print(r['documents'])
    #print(len(match_first))
    for j in match_first :
        print(j['place_name']) # 피시방 이름 출력
        print(j['address_name']) # 피시방 주소 출력
        print(j['x']) # 위도 출력
        print(j['y']) # 경도 출력
        print(j['phone']) # 전화번호 출력
        
#print(match_first[0].keys()) # key 확인
#print(match_first[0])
        
#js = json.JSONEncoder().encode(r.json())
#print(r.json())
"""
def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK ccf9c4dda0eed674c075b234b8d3d390"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    print(result)
    match_first = result['documents'][0]['address']
    return float(match_first['y']), float(match_first['x'])
print(getLatLng('강원 속초시 미시령로2983번길 88'))
"""