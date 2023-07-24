import random
video_list =  [
                "/neck1.mov",
                "/neck2.mov",
                "/neck3.mov",
                "/neck4.mov",
                "/shoulder.mov",
                "/back1.mov",
                "/neko.mov",
              ]
              #首,肩,背中,猫背,手首.
def dec_stretch(concern, estimate, suggested_list, setcount):
    #一回目の推薦
    if sum(suggested_list) == 0: 
        if estimate == 1:
            return 6
        elif estimate == 2:
            return 4

    if sum(suggested_list) > 6:
        index = 0
        if(concern[0] == 1): #首
            while(index < 4):
                if(suggested_list[index] == 0):
                    return index
                index += 1
        if(concern[1] == 1): #肩
            if(suggested_list[4] == 0):
                return 4
            index += 1
        if(concern[2] == 1): #背中
            if(suggested_list[5] == 0):
                return 5
            index += 1
        if(concern[3] == 1): #猫背
            if(suggested_list[6] == 0):
                return 6
    return random.randint(0,6)

            
