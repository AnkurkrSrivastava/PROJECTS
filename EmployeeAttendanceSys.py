import time  #Time module for time based codes

# def DisplayTime():

#Creating a global dictionary. System saved employees
employee = {
        223456: "Ankur Srivastava",
        223457: "Veer pratap"
    }
#Cresting a temporary data storing for check Outs
Attendance_data_temp = {}

#Function for attandace marking
def Attendance(ID):

    if ID in Attendance_data_temp : # Checks for if ID already exists in temporary data dictionary...(Check Outs)
        if ID not in Attendance_data_temp: # Why nested if? Becoz using employee[ID] with (random) not system saved IDs will raise error. 
            print(f"{employee[ID]} checked out")
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("\rTime:", current_time, end="")
        else:
            print(f"Guest ID no.{ID} checked out")
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("\rTime:", current_time, end="")
    elif ID not in employee:
        print("Guest checked in")
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("\rTime:", current_time, end="")
        Attendance_data_temp[ID] = current_time
    else:
        print(f"{employee[ID]} checked in")
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("\rTime:", current_time, end="")
        Attendance_data_temp[ID] = current_time 


def main():
    while True: #Running a while loop for givng a realism as system is on it gives reports like check outs.
        emp = int(input("Enter your Employee ID : "))
        #if emp.isdigit():
        Attendance(emp)
        print("Enter valid ID in digits")

        off = int(input("\nEnter 0 to off the system other(1) to keep it on :"))

        if off == 0:
            break

main()