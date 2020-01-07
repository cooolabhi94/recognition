import matplotlib.pyplot as plt
x=[1,3,6,9]
y=[2,6,8,23]
p=[1,9,2,8]
q=[9,3,7,23]
f=[0,2,5,8]
l=[1,3,7,8]
plt.subplot(3,2,1)
plt.bar(f,l)
plt.subplot(3,2,5)
plt.plot(x,y,'--r',p,q,x,y,'^g')
plt.title('important graph')
plt.xlabel('time')
plt.ylabel('velocity')
plt.show()



