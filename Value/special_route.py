import json

with open('train_value.json','r',encoding='utf-8') as f:
	data = json.load(f)
	total = len(data)
	
matchroadid = ['66000m3JE02']

time  = [list(data[i].keys()) for i in matchroadid]
value = [list(data[i].values()) for i in matchroadid]

#print('len1:',len(time[0]))   # 51
#print('len2:',len(value[0]))  # 51
# 51 / 6573

pair = []                                # merge to time - value
for i in range(len(time[0])):
	pair.append([time[0][i],value[0][i]])
	#print(pair[i][0],end=' ')
	#print(pair[i][1])

	
with open("./time.json",'r') as f:
		content = json.load(f)
		#print(content)
		print(len(content)) # 6573

# supplement data # i:第幾個時間(段) 
all = []
for i in range(len(content)):
	all.append([])
	for j in range(len(time[0])): 
		if content[i] == pair[j][0]:
			all[i] = pair[j][1]
			#print(i,all[i])

# ex			
#print(len(all[0]))
#if len(all[0]) == 0:
#	all[0].append(100)
#print(all[0])
#print(len(all[0]))
#print(all[0][0])	
for i in range(len(content)):
	#print(all[i])
	if len(all[i]) == 0:
		#print(all[i]) # value
		flag = 0       # 找不到 
		for j in range(i+1,len(content)): #往後找
			if len(all[j])!=0:
				#print('>>>',all[j])
				all[i] = all[j]
				flag = 1                  #有補上
				break
		if flag == 0:		
			for k in range(i-1,-1,-1):
				if len(all[k])!=0:
					all[i] = all[k]
					flag = 1
					break
		if flag == 0:
			print('amazing')
			all[i].append(100)
#print(all)				
#print(all[900])

#for i in range(2,10):
#	print(i) # 2 3 4 5 6 7 8 9

with open('66000m3JE02.json','w') as f:
	json.dump(all,f)
	
			
