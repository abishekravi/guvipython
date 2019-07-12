shen,vig=map(str,input().split())
if(len(shen)!=len(vig)):
 print("no")
else:
 s2=[shen.count(i) for i in shen]
 s3=[vig.count(i) for i in vig]
if(s2==s3):
 print("yes")
else:
 print("no")
 #a
