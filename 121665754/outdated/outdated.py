
months={
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
    }

while True:
    date = input("Date: ").strip().rstrip()
    try:
        if date.find(",")!=-1:
            date=date.replace(",","")
            month,day,year=date.split(" ")
            month = months[month]
            if int(month)>=12 and int(day)>=31:
                continue
            else:
                print(f"{year}-{month}-{int(day):02}")
                break
        elif date.find("/")!=-1:
            month,day,year = date.split("/")
            if int(day)<=31 and int(month)<=12:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
            else:
                continue
        else:
            continue
    except ValueError:
        pass
    except KeyError:
        pass
