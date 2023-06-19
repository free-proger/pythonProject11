if __name__ == "__main__":
    a = int(input())
    t=0
    if a<=250:
       t=a*7
    if 250<a<=300:
        t=250*7+(a-250)*17
    if a>300:
        t=300*7+(a-300)*20
    print(t)
