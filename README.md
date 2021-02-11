# 주제 선정

![56b9ccfcff272c492df213f11e902580](https://user-images.githubusercontent.com/69154643/107541383-6a127780-6c0a-11eb-901a-29c7cd32909f.jpg)
### 독서실까지 가는 길에는 수많은 유혹들이 있다.

나는 고등학교 시절, 독서실을 등록하고 오히려 공부 시간이 줄었다.  
게임을 너무 좋아했던 나는 독서실을 가던 도중 친구와 pc방을 가거나, 금방 독서실에서 나와 주변 pc방을 가곤 했다.  
집에서는 공부에 집중이 안되고, 독서실을 가다가 pc방을 지나치지 못해서 결국 자괴감과 스트레스를 받는 것을 반복했다.  
이것은 나뿐만의 문제가 아니라, 게임을 좋아하는 많은 학생들이 겪는 딜레마이다.  

하지만 나같은 학생들을 붙잡아줄 독서실이 어딘가에는 있지 않을까? 

## 데이터 수집

### 카카오 지도 API
https://apis.map.kakao.com/

![readme12](https://user-images.githubusercontent.com/69154643/107637985-515d9c80-6cb2-11eb-9d60-2af001a5059c.JPG)

API를 Json을 이용한 파싱을 통해 다음과 같은 데이터를 수집했다.

## 데이터 시각화



### 광진구 지역
![readme1](https://user-images.githubusercontent.com/69154643/107546584-de9be500-6c0f-11eb-871f-0182cfb12ff7.JPG)

- folium 라이브러리를 사용하여 내가 살고있는 광진구 지역을 시각화했다.
- 빨강 : 학교
- 하늘 : 독서실
- 회색 : pc방

### 내가 다녔던 독서실
![readme2](https://user-images.githubusercontent.com/69154643/107547945-67ffe700-6c11-11eb-9bdf-4dd454487b5b.JPG)

- 내가 다녔던 독서실 '아카데미 라운지'와 주변 pc방이 보인다.
- 집에서 가까워서 선택했었지만 이렇게 지도상으로 보아도 좋지 않은 환경이었다.

### 대원고
![readme3](https://user-images.githubusercontent.com/69154643/107630409-d347c880-6ca6-11eb-9bac-59a02a4a0850.JPG)

- 대원중, 대원고, 대원여고, 대원국제고의 경우 가장 독서실을 무사히 갈 수 있는 이상적인 형태를 갖고 있었다.
- 어째서 독서실만 있고, 피시방은 떨어져있는지 알아본 결과, 그 이유를 알 수 있었다.

- 교육환경법 제8조, 9조에 따르면 pc방은 학습과 교육환경에 나쁜 영향을 주는 유해시설로 간주되어 학교로부터 200미터 범위 안에 설립될 수 없다.
- 덕분에 뒤로는 아차산을 끼고, 앞에는 독서실을 바로 두고 있는 이상적인 형태가 될 수 있었다.

### 최악의 독서실
![readme5](https://user-images.githubusercontent.com/69154643/107632857-69c9b900-6caa-11eb-99d8-a73cb28a6b3a.JPG)

- 건대입구 주변 유일한 독서실로, 주변에 가까운 중,고등학교도 없어 접근성이 좋지 않다.
- 또한 pc방만 봐도 이렇게 많은데, 주변 술집, 게임장들을 고려하면 무사히 독서실까지 가는 것은 상당한 의지가 필요할 것이다.

### 광양고
![readme6](https://user-images.githubusercontent.com/69154643/107633476-6daa0b00-6cab-11eb-8d13-fcbeac0213ce.JPG)

- 광양고의 경우 대원고와 유사하게 이상적인 형태를 갖고 있었다.
- 뒤로는 한강을 끼고 있으며, 가까운 독서실이 있는 반면 pc방은 떨어져있다.

### 광진구 정리
![readme8](https://user-images.githubusercontent.com/69154643/107634363-c037f700-6cac-11eb-9d4e-e2c043e19ca4.JPG)

- pc방은 학교와 무조건 일정 거리 떨어져있으며, 시내 중심에 밀집되어 있는 경우가 많다.
- 독서실은 학교와 가깝게 지어지는 경우가 많다.
- 학교가 주변에 산이나 강과 같은 지형지물을 끼고 있는 경우 독서실이 집중될 확률이 높다.  
-> 지형적으로 시내에서 떨어져있기 때문에 pc방이 멀리 있어 독서실의 비율이 훨씬 높아진다.


### 강남구 지역
![readme9](https://user-images.githubusercontent.com/69154643/107634999-c8446680-6cad-11eb-820e-170ef3abec65.JPG)

- 광진구와 동일한 특징을 갖고 있는지 검증하기 위해 강남구 지역도 시각화해보았다.

### 한강 주변
![readme10](https://user-images.githubusercontent.com/69154643/107635524-a3042800-6cae-11eb-83f6-43d4e596998a.JPG)

- 강남구 지역 또한 강을 낀 지역은 pc방보다 독서실이 더 많이 분포되어 있다.
- 하지만 우측의 청담고의 경우 가까운 독서실이 없어 독서실에 가기 위해서는 pc방을 꼭 지나쳐야만 한다.
- 청담고 주변에 독서실을 설치하면 성공할 수 있을 것 같다.

### 시내 지역
![readme11](https://user-images.githubusercontent.com/69154643/107636796-82d56880-6cb0-11eb-9172-81df656bb798.JPG)

- 전체적으로 pc방과 독서실이 고르게 분포되어 있는데, 가운데 지역인 도곡동에는 유독 독서실이 집중되어 있다.
- 그 가운데의 한 pc방은 주변 네 곳의 학교의 거리에서 200미터를 준수하면서 경쟁 pc방도 없이,  
독서실을 주변에 끼고 있어 수많은 학생들을 유혹하고 있는 최고의 pc방이다.

# 결론

- pc방은 법에 따라 학교와 무조건 일정 거리 떨어져있어야 하며, 시내 중심에 밀집되어 있는 경우가 많다.  
-> 주 고객층이 학생이 아니기 때문
- 독서실은 학교와 가깝게 지어지는 경우가 많다.  
-> 주 고객층이 학생이기 때문
- 학교가 주변에 산이나 강과 같은 지형지물을 끼고 있는 경우 독서실이 집중될 확률이 높다.
- 집 또는 학원을 들리기 위하여 일단 시내로 나가게 되면 pc방을 지나치지 않고 독서실을 가는 것은 거의 불가능해진다.
- 독서실을 가장 안전하게 갈 수 있는 방법은 학교를 마친 후 곧장 가장 가까운 독서실로 직행하는 것이다.
