# Directory Database
# Directory, Data, Class.
# Directory: 데이터를 담고 있는 트리 구조를 의미함.
# Data: 의미를 담고 있는 데이터를 의미함. NoSQL에서 도큐멘트와 같음.
# Class: 데이터의 구조를 담음. Class는 NULL일 수 있음.(NoSQL처럼 작동함), 또는 Data 또는 Directory가 Class를 상속받을 경우, 데이터는 그 형식을 지켜야함. 클래스는 클래스를 상속받을수도 있음. 클래스 제약이 걸려있는 상위 디렉토리 아래에 다른 클래스를 상속받은 디렉토리가 있는 경우, Overwrite함. 