from um import count

def main():
    test_um()
def test_um():
    assert count("um")==1
    assert count("um?")==1
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...")==2

if __name__=="__main__":
    main
