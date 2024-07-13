from  datetime import datetime
def message(date, current, fill):
    dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    data = dt.date().isoformat()

    message = (f"\n"
               f"VREMENSKA PROGNOZA\b\n"
               f"Vremenska prognoza za {data},\n"
               f"Trenutna temperatura je {current}\n"
               f"Osecaj je napolju je {fill}\n")

    return message
