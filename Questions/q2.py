org_len = 11
org_wid = 4

final_len = 5
final_wid = 1

folds = 0

#  Calc Len_ratio
if org_len % final_len == 0: 
    len_ratio = org_len//final_len
else :
    len_ratio = (org_len//final_len) + 1

#  Calc wid_ratio
if org_wid % final_wid == 0: 
    wid_ratio = org_wid//final_wid
else :
    wid_ratio = (org_wid//final_wid) + 1

print('lr : ',len_ratio)
print('wr : ', wid_ratio)

x,y = 1, 1
while not 2**x >= len_ratio:
    x += 1
while not 2**y >= wid_ratio:
    y+=1

print(x, y)
folds = x + y 
print(folds)