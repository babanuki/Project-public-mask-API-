# Project-public-mask-API-
using Public Mask API

<h5>INPUT : 정보를 보고자 하는 장소의 주소(시군구)   (혹시 도로명이나 동 정보도 희망하는 경우, 이후에 입력받음)<br>
OUTPUT : 해당 주소(시군구)에 속하는 판매처의 주소/상호/재고량 등의 정보<br></h5>

<h4>주소를 입력받으면, 해당 주소 내에 있는 판매처들 중에서<br>
마스크의 재고가 남아 있는 곳의 정보를 출력해줍니다.<br><br></h4>

출력 형식 다음과 같습니다.<br><br>
<h5>n)</h5>     <------- n번째 정보를 나타냄<br>
<h5>'addr': '판매처의 주소'<br>
'code': '코드'<br>
'created_at': '정보의 업데이트 시각'<br>
'lat': '위도'<br>
'lng': '경도'<br>
'name': '판매처의 이름'<br>
'remain_stat': '마스크의 재고량'<br>
'stock_at': '마스크의 입고 시각'<br>
'type': '타입'
</h5>
