from jar import Jar

def test_init():
    jar=Jar()
    try:
        jar.__init__(-3)
    except ValueError:
        pass


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(4)
    assert jar.size==4
    jar.deposit(2)
    assert jar.size==6


def test_withdraw():
    jar=Jar()
    jar.deposit(12)
    jar.withdraw(4)
    assert jar.size==8
    jar.withdraw(2)
    assert jar.size==6
