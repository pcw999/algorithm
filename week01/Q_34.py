from wsgiref.simple_server import software_version


n = int(input())
input_list = list(map(int, input().split()))
s_sum = []

input_list.sort()

for i in range(n) :
    