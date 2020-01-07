from sklearn.linear_model import LinearRegression
f=[[0,10],[2,15],[5,20],[8,45],[10,100]]
l=[1,3,4.5,5.6,10]
clf=LinearRegression()
trained=clf.fit(f,l)
res = trained.predict([[0,15],[5,15],[1,10],[20,500]])
print(res)

