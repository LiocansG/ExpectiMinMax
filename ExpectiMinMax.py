
MAX = {"P": 0.1, "F":0.9}
MIN = {"P":0.5, "F":0.5}

def solving(data, isMin):
    a = list()
    b = list()
    new_data = list()
    turn = 0
    m = MIN if isMin else MAX
    if(len(data) > 1):
        for i in range(0, len(data), 2):
            if(turn == 0):
                a.append(round((data[i]*m.get("P")) + (data[i+1]*m.get("F")), 2))
                turn = 1
            else:
                b.append(round((data[i]*m.get("P")) + (data[i+1]*m.get("F")), 2))
                turn = 0
        
        for i in range(len(a)):
            if(isMin):
                new_data.append(min(a[i], b[i]))
            else:
                new_data.append(max(a[i], b[i]))
                
        solving(new_data, not isMin)
    print(data)
    
        

if __name__ == "__main__":
    data = [12, 6, 14 , 2, 4, 18, 4, 12, 2, 18, 8, 2, 4, 14, 14, 4]
    solving(data, True)