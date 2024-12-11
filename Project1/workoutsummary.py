'''Objective 1: Create an interactive prompt in a function that builds out a workout plan. Your prompt should ask for the workout name,
muscle concentration (i.e. chest, shoulders, biceps, triceps, etc.), number of sets, number of reps, note/description.  Take
all the responses to build a dictionary and return results to the function call. 
'''

def workout_prompt():
    workout_plan = {}
    # plan_details = ["Workout Name", "Muscle Focus", "Number of Sets", "Number of Reps", "Notes/Description"]
    workout_plan["Workout Name"] = input('What is the name of your workout?\n')
    workout_plan["Muscle Concentration"] = input('What is the muscle focus of this plan?\n')
    workout_plan["Number of sets"] = int(input('How many sets are in this workout?\n'))
    workout_plan["Number of reps"] = int(input('How many reps are in this workout?\n'))
    workout_plan["Description"] = input('Provide a brief description of this workout\n')

    print(workout_plan)
    return workout_plan


workout_prompt()