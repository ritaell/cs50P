from datetime import date,datetime
import inflect,re,sys,operator

class Date:
    def __init__(self,birth):
        self.birth=birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,birth):
        if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])",birth):
            sys.exit("Invalid date")

    def find_dif(self,birth):
        ty,tm,td=birth.split("-")
        birthday=datetime(int(ty),int(tm),int(td))

        now=str(date.today())
        ny,nm,nd=now.split("-")
        today=datetime(int(ny),int(nm),int(nd))

        dif=operator.sub(today,birthday)

        days,_,_=str(dif).split(" ")
        mins=int(days)*24*60
        words = inflect.engine().number_to_words(mins, andword="")



        return words.capitalize() + " minutes"







def main():
    birth=input("Date of Birth: ")
    date=Date(birth)
    print(date.find_dif(birth))


if __name__ == "__main__":
    main()
