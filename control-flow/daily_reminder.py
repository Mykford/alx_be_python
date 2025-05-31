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
            print(f"Note: {task} is a high priority task that should be completed today. ")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon. ")
        else:
            print(f"Note: {task} is a medium priority task that can be completed later this week. ")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be completed at your convenience. ")
        else:
            print(f"Note:{task} is a low priority task that can be completed whenever you have free time. ")        