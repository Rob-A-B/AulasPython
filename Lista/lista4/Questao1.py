R=10
farenheit=[]
celsius=[]
for i in range(R):
    print("Digite a temperatura ",i,"\n")
    farenheit.append(int(input()))
    celsius.append((5/9)*(farenheit[i]-32))
print(celsius)