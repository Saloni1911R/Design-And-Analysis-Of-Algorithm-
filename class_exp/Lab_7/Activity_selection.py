def activity_selection(start, finish):
    n = len(start)
    activities = sorted(zip(start, finish, range(n)),key= lambda x:x[1])
    finish_time = -1
    selected_activites = []
    for s,f,id in activities:
        if s>= finish_time:
            finish_time = f
            selected_activites.append(id)
    print("Selected activites: ", selected_activites)


start = [1,3,5,2,7,6]
finish = [5,6,8,4,9,8]
activity_selection(start, finish)