from sklearn.naive_bayes import GaussianNB
f=[[0,100],[0,120],[1,150],[1,180]]
l=['orange','orange','apple','apple']
clf=GaussianNB()
trained=clf.fit(f,l)
res=trained.predict([[0,100],[0,140],[0,180],[1,150],[1,100]])
