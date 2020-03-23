# Project-public-mask-API-
using Public Mask API

<h5>INPUT : 정보를 보고자 하는 장소의 주소(시군구)<br>
OUTPUT : 해당 주소(시군구)에 속하는 판매처의 주소/상호/재고량 등의 정보<br></h5>

<h4>주소(시군구)를 입력받으면, 해당 주소 내에 있는 판매처들 중에서<br>
마스크의 재고가 남아 있는 곳의 정보를 출력해줍니다.<br><br></h4>

출력 예시는 다음과 같습니다.<br>
{'addr': '판매처의 주소', 'code': '코드', 'created_at': '정보의 업데이트 시각', 'lat': '위도', 'lng': '경도', 'name': '판매처의 이름', 'remain_stat': '마스크의 재고량', 'stock_at': '마스크의 입고 시각', 'type': '타입'}
