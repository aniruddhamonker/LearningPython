#ip_range_list = [ f'150.81.4.{}']

vlan_ids = [100 + i for i in range(1,56)]
ip_range_list = []
count = 1
ip_range_list = list(map(lambda count: f'150.81.4.{count+4}', list(range(1,56))))

# for i in range(1,56):
#     #vlan_id.append(100 + i)
#     count = count + 4
#     ip_range_list.append(f'150.81.4.{count}')

for i in range(1,17):
    #print(f'set unit {155+i} vlan-id {155+i} family inet address 96.34.236.{count}/30\n')
    #print(f'set neighbor 96.34.236.{count} local-address 96.34.236.{count-1}')
    #print(f'set unit {196+i} vlan-id {196+i} family inet6 address 2602:104:2:801{str(hex(int(i))).strip("0x")}::11/64\n')
    print(f'set neighbor 2602:104:2:801{str(hex(int(i))).strip("0x")}::10 peer-as 20116')

