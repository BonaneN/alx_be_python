task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        priority_message = "is a high priority task"
    case "medium":
        priority_message = "is a medium priority task"
    case "low":
        priority_message = "is a low priority task"
    case _:
        priority_message = "has an undefined priority level"
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."
print(f"Reminder: {task} {priority_message}. {time_message}")