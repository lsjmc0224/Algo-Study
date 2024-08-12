def read(text):
    ridename, restrictions = text.split(":")
    ridename = ridename.strip()
    restrictions = restrictions.strip()

    cmmin = cmmax = None #초기 설정 해주는 것

    if "~" in restrictions:
        parts = restrictions.split("~")
        cmmin = int(parts[0].strip().replace("cm", "").strip())
        cmmax = int(parts[1].strip().replace("cm", "").strip())

    elif "이상" in restrictions and "이하" in restrictions:
        pass
    else:
        if "이상" in restrictions:
            cmmin = int(restrictions.split("cm")[0].strip())
        elif "이하" in restrictions:
            cmmax = int(restrictions.split("cm")[0].strip())

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)

