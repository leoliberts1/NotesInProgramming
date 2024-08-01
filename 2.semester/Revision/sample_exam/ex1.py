from datetime import datetime, timedelta
import heapq

# Print current date for reference
print(datetime.now().strftime('%B %d, %Y'))


# Function to compare dates, ensuring the year is adjusted appropriately
def datecomparer(d1):
    return datetime(2024, d1.month, d1.day)


# List of friends with their names and dates of birth
friendsList = [
    {"name": "Fab Sales", "dob": datetime(1999, 2, 8)},
    {"name": "Arat Smulos", "dob": datetime(2001, 4, 3)},
    {"name": "Fex Soles", "dob": datetime(1998, 2, 12)},
    {"name": "Denis Sreles", "dob": datetime(2001, 12, 9)},
    {"name": "Nouel Samules", "dob": datetime(2002, 11, 11)},
    {"name": "Fink Sremules", "dob": datetime(2000, 2, 12)},
    {"name": "James Sales", "dob": datetime(1999, 1, 30)},
]

# Print statement for clarity
print("Next birthdays are:")


def BirthdayCycle(friends_list, nr_of_bdays):
    # Helper function to calculate the next birthday from today
    def next_birthday(dob, today):
        this_year_birthday = datetime(today.year, dob.month, dob.day)
        if this_year_birthday < today:
            this_year_birthday = datetime(today.year + 1, dob.month, dob.day)
        return this_year_birthday

    # Get today's date
    today = datetime.now()

    # Initialize a min-heap with the next birthday for each friend
    heap = []
    for friend in friends_list:
        next_bd = next_birthday(friend['dob'], today)
        heapq.heappush(heap, (next_bd, friend))

    # Generate the next nr_of_bdays birthdays
    for _ in range(nr_of_bdays):
        next_bd, friend = heapq.heappop(heap)
        yield f"{friend['name']}, on {next_bd.strftime('%B %d, %Y')}"
        # Calculate the friend's birthday for the next year and push it back into the heap
        next_year_bd = datetime(next_bd.year + 1, next_bd.month, next_bd.day)
        heapq.heappush(heap, (next_year_bd, friend))


# Test code to display the next 10 birthdays
for party_day in BirthdayCycle(friendsList, 10):
    print(party_day)
