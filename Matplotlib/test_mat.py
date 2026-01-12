import matplotlib.pyplot as plt

subject=['Maths','science','English','Computer']
Marks=[78,85,88,92]

print("Draw a Bar chart")
plt.bar(subject,Marks,)

print("addtitle,xlable,ylable")
plt.title("student_mark")
plt.ylabel("marks")
plt.xlabel("subject")
print("Change the marker style")
plt.scatter(subject,Marks)
print("display the graph")
plt.show()