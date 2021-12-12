# 아스키 코드를 떠올렸지만 어떻게 사용할지 고민했다.
string = input()
alpha = list(range(97,123))#알파벳 범위를 list로 변환

for i in alpha:
  print(string.find(chr(i)),end=' ')#char : 아스키 -> 문자, find() : 문자열에서 문자가 포함되지 않는 경우 -1출력, end=' ': 형식맞추기
  
#(ps. index()함수도 문자열, list, tuple에서 찾는 기능은 같지만 포함되지 않은 경우 AttributeError가 발생한다고 한다.)
