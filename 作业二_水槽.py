#暂时不太会输入，请见谅
h=[1,8,6,2,5,4,8,3,7]
# inmax=0
# for i in range(0,len(h)):
#     if inmax<h[i]*(i+1):
#         inmax=h[i]*(i+1)
#以为y轴也能算作边界了
#==========================================
max=0
for j in range(0,len(h)):
    for k in range(j+1,len(h)):
        if max<(k-j)*min(h[j],h[k]) :
            max=(k-j)*min(h[j],h[k])
print(max)
