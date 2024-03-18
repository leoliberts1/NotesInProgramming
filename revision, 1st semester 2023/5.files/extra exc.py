
"""
Additional Exercise on Files (1)
You are given a txt file with data about vehicles passing on a motorway.
 Use this data to determine the vehicles, that violate the safety distance rules
  to the vehicle in front of them.

Here is a summary of the rule: If you fail to keep a sufficient distance,
 and if you are caught very close to the car in front (defined as a gap of between 0.2 and 0.4 seconds, which equates to a distance between 7 m and 14 m at 130 km/h)
 , you are liable to receive an recordable offence on your licence under the Demerit Point System,
  in addition to a fine. If the distance is less than 0.2 seconds (under 7 m at 130 km/h)
  you will be fined and your licence will be revoked for a minimum of six months.
data-autobahn-sample.txt"""



def finenumbers(textfile):
    import re
    with open(textfile) as f:
        data = f.readlines()
    #print(data)
    lane1 = []
    lane2 = []
    lane3 = []
    #I define the lanes in which the cars will be driving in
    #
    for car in data:
        if "lane=1" in car:
            lane1.append(car)
        if "lane=2" in car :
            lane2.append(car)
        if "lane=3" in car:
            lane3.append(car)
    #print(lane1)
    def istooclose(lane):

        from datetime import datetime
        fines = 0
        licenserevokes = 0
        index = 0
        for car in lane:
            if index == 0 :
                index+=1
                continue
            carinfrontSPEED = re.findall(r'speed=\w+',lane[index-1])
            carinfrontTIME = re.findall(r'\d\d\d\d-\d\d-\d\d\s\d\d:\d\d:\d+\.\d+',lane[index-1])
            if carinfrontTIME == []:
                carinfrontTIME = re.findall(r'\d\d\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d', lane[index - 1])
                carinfrontTIME = carinfrontTIME[0]+".000000"
                k = "".join(carinfrontTIME)
                carinfrontTIME = [k]

            carinfrontSPEED = re.findall(r'\d+',carinfrontSPEED[0])
            #print(carinfrontSPEED)
            date_format = "%Y-%m-%d %H:%M:%S"
            carinfrontTIMEsinmili = datetime.strptime(carinfrontTIME[0][0:19],date_format)


            #print(carinfrontTIMEsinmili)
            carinfrontmili = int(carinfrontTIME[0][-6:])
            carinfrontTIME = carinfrontTIMEsinmili.replace(microsecond=carinfrontmili)
            #print(carinfrontmili)
            #print(carinfrontTIME)
            carTIME = re.findall(r'\d\d\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d\.\d+',car)
            if carTIME == []:
                carTIME = re.findall(r'\d\d\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d',car)
                carTIME = carTIME[0]+".000000"
                k = "".join(carTIME)
                carTIME = [k]
            #print(carTIME)

            carTIMEsinmili = datetime.strptime(carTIME[0][0:19],date_format)
            carMILI = int(carTIME[0][-6:])
            carTIME = carTIMEsinmili.replace(microsecond=carMILI)
            carSPEED = re.findall(r'speed=\w+',lane[index])
            carSPEED = re.findall(r'\d+',carSPEED[0])
            #print(carSPEED)
            difference = carTIME-carinfrontTIME

            JustFine = (datetime(2020,1,1,0,0,0,400000)-datetime(2020,1,1,0,0,0,0))
            FineAndLicense = (datetime(2020,1,1,0,0,0,200000)-datetime(2020,1,1,0,0,0,0))
            #print(JustFine)
            #print(FineAndLicense)
            #print(carinfrontTIME)
            #print(carTIME)
            #print(difference)
            #print(car)
            index+=1
            if difference <= FineAndLicense :#or int(difference)*carSPEED[0]*1000/3600<0.2:
                licenserevokes+=1
                #print(f'lose license{car}')
                continue
            elif difference <= JustFine:
                fines +=1
                #print(f'get fined{car} and diff-{difference}')
                continue
        return(print(fines,licenserevokes))
            #Calculate the distance between the cars
            #calculate the time passed since first car times speed of first car - the distance
            #'''
    istooclose(lane1)
    istooclose(lane2)
    istooclose(lane3)


finenumbers("data-autobahn-sample.txt")
#finenumbers("smallData.txt")




