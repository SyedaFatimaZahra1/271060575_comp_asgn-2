import random  
class Movie:
    def __init__(self,movie_title):
        self.seat_array=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
        self.movie_list = ["shawshank redemption","the godfather","lord of the rings","angry men","pulp fiction","hotel transylvania","jojo rabbit","life is beautiful","star wars","up","hachi"]
        self.movie_title = movie_title
        self.seat_available = 20
    def manage_booking(self):
        print("welcome to the cinema ")
        print("the following movies are available :")
        print(f"{self.movie_list}")
        movie_decided = int(input("enter the number of movie which you would like to watch (e.g godfather = 2): "))
        self.movie_title = self.movie_list[movie_decided - 1]
        ticket = input(f"Would you like a movie ticket for movie {self.movie_title}? (yes/no): ")
        while ticket == "yes":
            print("Please select your seat from the following seats available:")
            print(f"{self.seat_array}")
            k = int(input("Enter seat number: "))
            self.seat_array[k-1] = " "
            self.seat_available = self.seat_available - 1
            print(f"You have booked a ticket for movie {self.movie_title}")
            print(f"Remaining tickets available for this movie are : {self.seat_available}")
            print(f"Remaining seats are : {self.seat_array}")
            ticket = input("Would you like to book another seat? (yes/no): ")
        else:
            print(f"You did not book a ticket for movie {self.movie_title}")
            print("the seats which you booked have been registered")
class Screen:
    def __init__(self, screen_num):
        self.screen_num = screen_num
        self.screen_list = []
        self.screen_timeslot = {}

    def screen_number_assign(self):
        k = int(input("enter the numbers of screen you want for this cinema : "))
        self.screen_num = k
        for i in range(1, self.screen_num + 1):
            screen_name = "screen number" + str(i)
            self.screen_list.append(screen_name)  
        return self.screen_list

    def assign_timeslot(self, timeslot_obj):
        for screen_name in self.screen_list:
            self.screen_timeslot[screen_name] = timeslot_obj
            print(f"Timeslots assigned to {screen_name}: ")
            timeslot_obj.display_timeslot()
 


class Timeslot:
    def __init__(self, start_time, stop_time):
        self.start_time = start_time
        self.stop_time = stop_time
        self.timeslot_list = []

    def add_timeslot(self):
        print("lets add timeslots for the screens seleccted")
        print("Adding a new timeslot")
        overlap_found = False
        for start, stop in self.timeslot_list:
            if self.start_time < stop and self.stop_time > start:
                overlap_found = True
                print(f"timeslot could not be added as it interferes with pre-existing timeslots")
                break

        if not overlap_found:
            self.timeslot_list.append((self.start_time, self.stop_time))
            print(f"New time slot has been added from {self.start_time} to {self.stop_time}")

    def remove_timeslot(self):
        print("Removing the timeslot")
        inp = input(f"Do you want to remove timeslot from {self.start_time} to {self.stop_time}? (yes/no): ")
        if inp == "yes":
            self.timeslot_list.remove((self.start_time, self.stop_time))
            print("Timeslot has been removed.")
        else:
            print("Timeslot has not been removed.")

    def display_timeslot(self):
        print("the following timeslots have been selected for the movie :")
        print("Timeslots:")
        for start, stop in self.timeslot_list:
            print(f"{start} to {stop}")

class Admin:
    def __init__(self,email,password,movie_title,screen_num,start_time,stop_time):
        self.timeslot_obj = Timeslot(start_time,stop_time)
        self.screen_obj = Screen(screen_num)
        self.movie_obj = Movie(movie_title)
        self.email = email
        self.password = password
        pass
    def login(self):
        while True:
            email_check = input("Enter your email to sign in: ")
            password_check = input("Enter your password: ")

            if email_check == self.email and password_check == self.password:
                print("You have successfully logged into your account ")
                break  
            else:
                print("Incorrect email or password. Please try again ")

    def movie_list_change(self):
        print("the list of movies is : ")
        print(f"{self.movie_obj.movie_list}")
        k = int(input("press 1 to append movie , press 2 to remove movie,press 3 for it remain same : "))
        if k == 1:
            appending_movie = input("enter the name of movie you want to append :")
            self.movie_obj.movie_list.append(appending_movie)
            print(f"movie has been appended . {self.movie_obj.movie_list}")
        elif k == 2:
            removing_movie = str(input("enter the name of movie which you want to remove :")) 
            self.movie_obj.movie_list.remove(removing_movie)    
            print("the movie has been removed . the remaining movies are: ")
            print(f"{self.movie_obj.movie_list}")
        else:
            print("nothing will happen")  
    def seating_change(self):
        print("the list of seat is : ")
        print(f"{self.movie_obj.seat_array}")
        j = int(input("press 1 to add seat , press 2 to remove seat , press 3 for it to remain same : "))
        if j == 1:
            print("appending a new seat")
            self.movie_obj.seat_array.append("new seat")
            print(f"seat has been added . {self.movie_obj.seat_array}")
        elif j == 2:
            print("removing seat")
            k = input(f"enter which seat will you like to remove from list : {self.movie_obj.seat_array} : ")
            self.movie_obj.seat_array.remove(k)
            print(f"the seat has been removed . remaining seats are {self.movie_obj.seat_array}")
        else:
            print("seating arrangements remains the same")  
    def screen_number_change(self):  
        print(f"{self.screen_obj.screen_number_assign()}")   
    def adjusting_timeslot(self):
        print(f"{self.timeslot_obj.add_timeslot()}")  
    def removing_new_timeslot(self):
        print(f"{self.timeslot_obj.remove_timeslot()}")  

       
        pass  



class booking_detail:
    def __init__(self, movie_title, screen_num,start_time,stop_time):
        self.movie_title = movie_title
        self.obj_movie = Movie(movie_title)
        self.screen_obj = Screen(screen_num)
        self.timeslot_obj = Timeslot(start_time,stop_time)

    def generate_id(self):
        print(f"Welcome user, your ID for your booking is:")
        i = random.randint(10000,99999)
        print(i)
        return i

    def seat_movie_select(self):
        print(f"The movie is are displayed : ") 
        return self.obj_movie.manage_booking()

    def seat_screen_select(self):
        self.screen_obj.screen_number_assign()
        print(f"The names of screens are: {self.screen_obj.screen_list}")
        timeslot_1_start = str(input("Enter starting time of first timeslot: "))
        timeslot_1_stop = str(input("Enter stopping time of first timeslot: "))
        timeslot_2_start = str(input("Enter starting time of second timeslot: "))
        timeslot_2_stop = str(input("Enter stopping time of second timeslot: "))
        timeslot_obj_1 = Timeslot(timeslot_1_start, timeslot_1_stop)
        timeslot_obj_2 = Timeslot(timeslot_2_start, timeslot_2_stop)

        self.screen_obj.assign_timeslot(timeslot_obj_1)
        self.screen_obj.assign_timeslot(timeslot_obj_2)

        self.timeslot_obj.display_timeslot()
    


class User:
    def __init__(self, email, password,movie_title, screen_num,start_time,stop_time):
        self.email = email
        self.password = password
        self.booking_obj = booking_detail(movie_title, screen_num,start_time,stop_time)

    def login(self):
        while True:
            email_check = input("Enter your email to sign in: ")
            password_check = input("Enter your password: ")

            if email_check == self.email and password_check == self.password:
                print("You have successfully logged into your account ")
                break  
            else:
                print("Incorrect email or password. Please try again ")

print("logging into admin account: ")
email_input_1 = input("enter email to make account :")
password_input_1 = input("enter password for this email : ")           

start_time_1 = int(input("enter starting time of first timeslot: "))  
stop_time_1 = int(input("enter stopping time of first timeslot : "))  
admin_obj = Admin(email_input_1,password_input_1,"kitkat",2,start_time_1,stop_time_1)  
admin_obj.login()
admin_obj.movie_list_change()
admin_obj.seating_change()
admin_obj.screen_number_change()
admin_obj.adjusting_timeslot()
admin_obj.removing_new_timeslot()

print("logging into admin account: ")
email_input_2 = input("enter email to make account :")
password_input_2 = input("enter password for this email : ")           

start_time_2 = int(input("enter starting time of second timeslot: "))  
stop_time_2 = int(input("enter stopping time of second timeslot : "))  
admin_obj_2 = Admin(email_input_2,password_input_2,"kitkat",2,start_time_2,stop_time_2)   
admin_obj_2.login()
admin_obj_2.movie_list_change()
admin_obj_2.seating_change()
admin_obj_2.screen_number_change()
admin_obj_2.adjusting_timeslot()
admin_obj_2.removing_new_timeslot()

print("now trying the user side: ")
email_input_1 = input("enter email to make account :")
password_input_1 = input("enter password for this email : ")           
user_obj_1 = User(email_input_1,password_input_1,"guardian of space", 3, 1,1 )
user_obj_1.login() 
user_obj_1.booking_obj.generate_id()
user_obj_1.booking_obj.seat_movie_select()
user_obj_1.booking_obj.seat_screen_select()

print("thanks for registering seats in the Cinema Booking System")

