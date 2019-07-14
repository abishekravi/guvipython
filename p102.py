#a
try:
	num=int(input())
	li=list(map(int,input().split()))
	li.sort()
	print(2*(li[-1]+li[-2]))
except ValueError:
	print("invalid")
