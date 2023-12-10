roadLog = [
    [300, 25], #0
    [540, 35], #1
    [380, 30], #2
    [400, 20], #3
    [350, 20], #4
    [200, 13], #5
    [400, 35], #6
    [520, 40], #7
    [430, 30], #8
    [500, 28], #9
    [500, 32], #10
    [480, 30], #11
    [300, 20], #12
    [500, 25]  #13
]             #len() 14


def get_total_fuel_usage(RoadLog):
    return sum([interval[1] for interval in RoadLog])

def get_total_distance_travelled(RoadLog):
    return sum([interval[0] for interval in RoadLog])

def get_average_fuel_usage(RoadLog):
    return get_total_fuel_usage(RoadLog) / get_total_distance_travelled(RoadLog) * 100

def get_most_fuel_used(RoadLog):
    fuelLog = [interval[1] for interval in RoadLog]
    return fuelLog.index(max(fuelLog))

def get_least_fuel_used(RoadLog):
    fuelLog = [interval[0] for interval in RoadLog]
    return fuelLog.index(min(fuelLog))

def append_log(RoadLog, NewInterval):
    RoadLog.append(NewInterval)
    return RoadLog

def insert_log_at_index(RoadLog, NewInterval, NewIndex):
    RoadLog.insert(NewIndex, NewInterval)
    return RoadLog

def get_usage_per_interval(RoadLog): #pre kontrolu remove_interval_over_limit()
    return [interval[1] / interval[0] * 100 for interval in RoadLog]

def remove_interval_over_limit(RoadLog, UsageLimit):
    tempUsage = 0
    trashList = []

    for interval in RoadLog:
        tempUsage = interval[1] / interval[0] * 100
        if tempUsage > UsageLimit:
            trashList.append(interval)
    
    for interval in trashList:
        RoadLog.remove(interval)
        
    return RoadLog


print(f"celkova_spotreba(): {get_total_fuel_usage(roadLog)} l\nprejdena_vzdialenost(): {get_total_distance_travelled(roadLog)} km\npriemerna_spotreba(): {get_average_fuel_usage(roadLog)} l/100km")
print(f"najvyššia_spotreba(): index {get_most_fuel_used(roadLog)}\nnajnižšia_spotreba(): index {get_least_fuel_used(roadLog)}")
#pre pridaj_zaznam_na_koniec() (append_log()) a pridaj_zaznam_na_index() (insert_log_at_index())zadajte NewInterval ako novy zaznam
#a NewIndex ako index na ktory checete vlozit novy interval
NewInterval = [350, 30] #napr
NewIndex = 3
print(f"pridaj_zaznam_na_koniec(): {append_log(roadLog, NewInterval)}\npridaj_zaznam_na_index() (na index {NewIndex}: {insert_log_at_index(roadLog, NewInterval, NewIndex)}")
print(f"Usage log: {get_usage_per_interval(roadLog)}\nUpdated log with removed excess intervals: {remove_interval_over_limit(roadLog, 3.00)}")

'''
celkova_spotreba() - vypočíta celkové množstvo paliva, ktoré sme použili,      get_total_fuel_usage(RoadLog)
prejdena_vzdialenost() - vypočíta celkovú prejdenú vzdialenosť,     get_total_distance_travelled(RoadLog)
priemerna_spotreba() - vypočíta doterajšiu priemernú spotrebu (l/100km),    get_average_fuel_usage(RoadLog)
najvyššia_spotreba() - vráti index toho tankovania, v ktorom sme zaznamenali najvyššiu spotrebu,    get_most_fuel_used(RoadLog)
najnižšia_spotreba() - vráti index toho tankovania, v ktorom sme zaznamenali najnižšiu spotrebu,    get_least_fuel_used(RoadLog)
pridaj_zaznam_na_koniec() - pridá záznam tankovania na koniec,      append_log(RoadLog, NewInterval)
pridaj_zaznam_na_index() - pridá záznam tankovania na určený index,     insert_log_at_index(RoadLog, NewInterval, NewIndex)
zmaz_zaznamy_nad_spotrebou() - vymaže tie záznamy, v ktorých je spotreba vyššia ako zadaná spotreba (l/100km)   remove_interval_over_limit(RoadLog, UsageLimit)
'''