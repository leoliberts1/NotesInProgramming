from datetime import datetime
print (datetime.now().strftime('%B %d, %Y'))
friendsList = [
{"name": "Fab Sales", "dob": datetime (1999, 2, 8)},
{"name": "Arat Smulos", "dob": datetime (2001, 4, 3)},
{"name": "Fex Soles", "dob": datetime (1998, 2, 12)},
{"name": "Denis Sreles", "dob": datetime (2001, 12, 9)},
{"name": "Nouel Samules", "dob": datetime (2002, 11, 11)},
{"name": "Fink Sremules", "dob": datetime (2000, 2, 12)},
{"name": "James Sales", "dob": datetime (1999, 1, 30)},]
def BirthdayCycle(ListOfFriends,HowManyYields_left):
    unordered = []
    #I need to sort the people by when their birthday is in the year
    while len(ListOfFriends) > 0:
        def finding_lowest(friends_list,):
            current_lowest = None
            current_lowest_date = None
            for friend in friends_list:
                #print(friend)
                if current_lowest == None:
                    current_lowest = friend
                    current_lowest_date = current_lowest.get("dob").date()
                #print(current_lowest_date)
                current_date = friend.get("dob").date()
                if current_date.month < current_lowest_date.month:
                    current_lowest = friend
                    current_lowest_date = current_lowest.get("dob").date()
                if current_date.month == current_lowest_date.month:
                    if current_date.day < current_lowest_date.day:
                        current_lowest = friend
                        current_lowest_date = current_lowest.get("dob").date()
            return current_lowest
        to_be_removed = finding_lowest(ListOfFriends)
        unordered.append(to_be_removed)
        ListOfFriends.pop(ListOfFriends.index(to_be_removed))
    print(unordered)
    #print(finished)
    start = datetime.now().date()
    index = 0
    while unordered[index].get("dob").month < start.month or unordered[index].get("dob").month == start.month and unordered[index].get("dob").day < start.day:
        index+=1

    #find the index at which to start
    finished = []
    while len(finished) < HowManyYields_left:
        finished.append(unordered[index])
        index+=1
        if index == len(unordered):
            index = 0
    print(f'this is finished{finished}')
    for person in finished:
        yield f'{person.get("name")} on {person.get("dob").month} {person.get("dob").day}'



    #print("this is the unordered list ^")
'''
friendsList = [
{"name": "Fab Sales", "dob": datetime (1999, 2, 8)},
{"name": "Arat Smulos", "dob": datetime (2001, 4, 3)},
{"name": "Fex Soles", "dob": datetime (1998, 2, 12)},
{"name": "Denis Sreles", "dob": datetime (2001, 12, 9)},
{"name": "Nouel Samules", "dob": datetime (2002, 11, 11)},
{"name": "Fink Sremules", "dob": datetime (2000, 2, 12)},
{"name": "James Sales", "dob": datetime (1999, 1, 30)},]
print ("Next birthdays are:")
for party_day in BirthdayCycle(friendsList, 10):
print (party_day)
'''
#expected output
'''
Next birthdays are:
Nouel Samules, on November 11, 2022
Denis Sreles, on December 09, 2022
James Sales, on January 30, 2023
Fab Sales, on February 08, 2023
Fex Soles, on February 12, 2023
Fink Sremules, on February 12, 2023
Arat Smulos, on April 03, 2023
Nouel Samules, on November 11, 2023
Denis Sreles, on December 09, 2023
James Sales, on January 30, 2024
'''
print ("Next birthdays are:")
for party_day in BirthdayCycle(friendsList, 10):
    print (party_day)