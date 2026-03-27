import matplotlib.pyplot as plt

# Sample Data
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'Amdocs']
recruitments = [120, 100, 150, 80, 90, 110, 70]

# a) Bar Chart
plt.figure()
plt.bar(companies, recruitments)
plt.title("Company Recruitment")
plt.xlabel("Company")
plt.ylabel("Number of Students")
plt.show()

# b) Pie Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.figure()
explode = [0.1 if c == 'Amazon' else 0 for c in companies]
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', explode=explode)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# e) Comparison (IBM vs Amdocs)
plt.figure()
plt.bar(['IBM', 'Amdocs'], [80, 70])
plt.title("IBM vs Amdocs Recruitment")
plt.show()