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

        assert rvalue == a["exp_result"], f"For {a['data']} is_even retval :{rvalue} expected :{a['exp_result']}"

if (__name__=="__main__"):
    main()
