from amath import is_even

def main():
    data = [
        {"data" : 10, "exp_result" : True},
        {"data" : 15, "exp_result" : False},
        {"data" : 0, "exp_result" : False},
        {"data" : -0, "exp_result" : False},
        {"data" : -15, "exp_result" : False}
    ] 
    for a in data:
        rvalue = is_even(a["data"])
        if(rvalue != a["exp_result"]):
            print(f"For {a['data']} is_even retval :{rvalue} expected :{a['exp_result']}, FAIL")
        else:
            print(f"For {a['data']} is_even retval :{rvalue} expected :{a['exp_result']}, PASS")
if (__name__=="__main__"):
    main()
