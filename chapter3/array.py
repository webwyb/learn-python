#3-1
names = ['tom', 'wuyanbin', 'robbin']
for name in names:
    print(name);
#3-2
for name in names:
    print(name + ', how are you ?')

#3-3
traffic_ways = ['bike', 'motorcycle', 'car']
for way in traffic_ways:
    print('i would like to own a', way)

#3-4
guest_lists = ['tom', 'bob', 'robbin']
for name in guest_lists:
    print('hello', name,', i would invited you come with me for dinner')
#3-5 修改嘉宾
no_have_time = 'tom'
for name in guest_lists:
    if name == 'tom':
        print('sorry', name, 'don\'t have time')
        guest_lists[0] = 'james' # 改变列表中的值
        new_guest_list = guest_lists
        print('最新名单', guest_lists)
        for newName in new_guest_list: 
            print('hello', newName,', i would invited you come with me for dinner')
#3-6
# 添加新人到名单开头
guest_lists.insert(0, 'lucy')
print(guest_lists)
# 添加新人到中间
list_middle = int(len(guest_lists)/2)
guest_lists.insert(list_middle, 'lucy')
print(guest_lists)
# 添加新人到末尾
guest_lists.append('eve')
print(guest_lists)

#3-7
print('当前所有人的列表', guest_lists)
refuse_invite_lists = [] # 无法邀请名单
 
while(len(guest_lists) >2):
    # print(guest_lists.pop())
    # refuse_invite_lists.append(guest_lists.pop())
    print('sorry', guest_lists.pop(), 'i can\'t invited you')
    # print(refuse_invite_lists)
print(guest_lists)
# del(guest_lists[0]) 
guest_lists.remove('lucy')
del(guest_lists[0])
print(guest_lists)

#3-8
address = ['nanjing', 'suzhou', 'dali', 'lijang']
# 暂时性排序
print(address)
print(sorted(address))
print(sorted(address, reverse=True))
print(address)

# 反转列表
address.reverse()
print(address)
address.reverse()
print(address)

# 排序列表
address.sort()
print(address)
address.sort(reverse = True)
print(address)

#3-9
print('长度是', len(address))