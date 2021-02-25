from datetime import datetime
odds =  [1,3,5,7,9,11,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
if datetime.today().minute in odds:
    print("Odds")
else:
    print("No odds")
