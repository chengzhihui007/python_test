#tool.oschina.net/uploads/apidocs/jquery/regexp.html
import re
# m=re.search('\d','asf923asdf345')
# print(m.group(0))
#贪婪模式，从开头匹配到结尾
one = 'msn123123n'
#非贪婪
two = 'a\d'
pattern = re.compile('m(.*)n')
pattern2 = re.compile(r'a\\b')
result = pattern.findall(one)
result2 = pattern2.findall(two)
print(result2)