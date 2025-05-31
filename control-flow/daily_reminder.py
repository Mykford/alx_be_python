task = input("What is your task for today? ")
priority = input("What is the priority of this task? (high/medium/low) ")
time_bound = input("Is this task time-bound? (yes/no) ")
priority = priority.lower()
time_bound = time_bound.lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today! ")
        else:
            print(f"")