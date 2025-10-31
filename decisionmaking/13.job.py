print("Job Eligibility Check")
print("----------------------")

age = int(input("Enter your age: "))
if age > 18:
    experience = input("Do you have experience? (yes/no): ").lower()
    if experience == "yes":
        print("You are eligible for the job.")
    else:
        print("You must have experience to be eligible.")
else:
    print("You must be above 18 to be eligible.")