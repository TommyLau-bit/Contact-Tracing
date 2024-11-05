#student number: 21041765

#!/usr/bin/env python3
"""Analyse a given dataset of sick people and their contacts. Identify
characteristics related to disease spreading as set out in the coursework
brief.
"""

import sys
import os.path
from format_list import format_list

# Function for section 2
def file_exists(file_name):
    """Verify that the file exists.

    Args:
        file_name (str): name of the file

    Returns:
        boolean: returns True if the file exists and False otherwise.
    """
    # Remove pass and fill in your code here
    #rerturn result of checking if file exists
    return os.path.exists(file_name)
        
# Function for section 3
def parse_file(file_name):
    """Read the input file, parse the contents and return a dictionary
    containing sick people and their contacts.

    Args:
        file_name (str): Contains the name of the file.

    Returns:
        dict: Contains contact tracing information. The keys are the sick
        people. The corresponding values are stored in a list that contains
        the names of all the people that the sick person has had contact with.
    """
    # Remove pass and fill in your code here
    dict = {} #initialise dictionary
    f = open(file_name,'r') #open file iin read mode
    while True:
        try:
            record = f.readline() #read new line from file
            if not record: #check if line exists
                break #stop loop if end of file
            else:
                name_list = record.rstrip().split(",") #remove any white space or new line at the end and parse using ','
                dict[name_list[0]] = name_list[1:] #make first name key and value is rest of names as a list 
        except ValueError:
            print("Error found in file, continuing.")
    f.close()
    return dict

# Function for section 5
def find_patients_zero(contacts_dic):
    """Return list of people who do not appear in any sick person's contact
    list. 

    Args:
        contacts_dic (dic): each entry is a sick person's name (key) and their
        list of contacts.

    Returns:
        list: names of people who do not appear in any sick person's contact
        list.
    """
    # Remove pass and fill in your code here
    patient_zeros = list(contacts_dic.keys()) #iinitialise patient zeros as all sick ppl
    for p in contacts_dic.keys():
        for c in contacts_dic[p]:
            if c in patient_zeros:
                patient_zeros.remove(c) #if any confirmed cases is a contact remove as patient zero
    return patient_zeros

# Function for section 6
def find_potential_zombies(contacts_dic):
    """Return list of people who do not appear to be sick yet. They appear in
    the contact lists but do not have their own contacts entry.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.

    Returns:
        list: names of people who are not listed as sick.
    """
    # Remove pass and fill in your code here
    patients = list(contacts_dic.keys())
    zombies = []
    for p in patients:
        for c in contacts_dic[p]:
            if not c in patients and not c in zombies:
                zombies.append(c) #add contact to list of zombie if they are not confimred as sick
    return zombies

# Function for section 7
def find_not_zombie_nor_zero(contacts_dic, patients_zero_list, zombie_list):
    """Return names of those people who are neither a zombie nor a patient
    zero.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.
        patients_zero_list (list): sick people identified as patient zero(es).
        zombie_list (list): contacts who are not a sick person (don't have
        their own contact list).

    Returns:
        list: people who are neither a zombie nor a patient zero.
    """
    # Remove pass and fill in your code here
    not_zombie_nor_zero = []
    for p in contacts_dic.keys():
        for c in contacts_dic[p]:
            if not c in patients_zero_list and not c in zombie_list and not c in not_zombie_nor_zero:
                not_zombie_nor_zero.append(c) #add any contact that is not a patient zero and not a zombie
    return not_zombie_nor_zero

# Function for section 8
def find_most_viral(contacts_dic):
    """Return the most viral contacts: those sick people with the largest
    contact list

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.

    Returns:
        list: contains the names of sick people who have the largest contact
        lists
    """
    # Remove pass and fill in your code here
    max_infected = 0
    most_viral_people = []
    for p in contacts_dic.keys(): #loop through all sick people
        if len(contacts_dic[p])>max_infected: #if number of contacts greater than prrevious max
            max_infected = len(contacts_dic[p]) #update max number of contacts
            most_viral_people = [p] #reassign most viral people as list containing only this sick person
        elif len(contacts_dic[p])==max_infected:
            most_viral_people.append(p) #if this sick person has same number as max_innfected append it to list
    return most_viral_people
    
# Function for section 9
def find_most_contacted(contacts_dic):
    """Return the contact or contacts who appear in the most sick persons'
    contact list.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.

    Returns:
        list: contains the names of contacts who appear in the most sick
        persons' contact list.
    """
    # Remove pass and fill in your code here
    contact_num = {}
    max_contacted = 0
    most_contacted = []
    #loop through all contacts
    for p in contacts_dic.keys():
        for c in contacts_dic[p]:
            if c in contact_num.keys():
                contact_num[c] += 1 #if contact is already a key increment contact count
            else:
                contact_num[c] = 1 #else initialise count to one
            if contact_num[c] > max_contacted: #if count for contact exceeds max
                #update max and most_contacted
                max_contacted = contact_num[c]
                most_contacted = [c]
            elif contact_num[c] == max_contacted: #if count same as max append contact to list
                most_contacted.append(c)
    return most_contacted
    
# Function for section 10
def find_maximum_distance_from_zombie(contacts_dic, zombie_list):
    """Return the maximum distance from a zombie for everyone in the dataset.
    The maximum distance from a potential zombie is the longest contact
    tracing path downwards in the dataset from a sick person to a potential
    zombie.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their
        list of contacts.
        zombie_list (list): all zombies

    Returns:
        dic: contains heights (maximum distance) of person from a zombie
    """
    # Remove pass and fill in your code here
    max_dist = {}
    for p in contacts_dic.keys(): max_dist[p] = 0
    for p in zombie_list: max_dist[p] = 0
    changed = True
    while changed:
        changed = False
        for p1 in contacts_dic.keys():
            for p2 in contacts_dic[p1]:
                if max_dist[p1] <= max_dist[p2]:
                    max_dist[p1] = max_dist[p2] + 1 
                    changed = True
    return max_dist

# "Additional Credit" Functions here

def find_spreader_zombies(contacts_dic, zombie_list):
    """Return sick people that has only been in conact with potential zombies

    Args:
        contacts_dic (dic): each entry is a sick person's name and their
        list of contacts.
        zombie_list (list): all zombies

    Returns:
        list: Contains the names of sick people who are spreader zombies
    """
    # Remove pass and fill in your code here
    spreader_zombies = []
    for p in contacts_dic.keys():
        spreader_zombie = True #initialise spreader zombie flag to True
        for c in contacts_dic[p]:
            if not c in zombie_list: #if a contact is not a potential zombie make flag False
                spreader_zombie = False
        if spreader_zombie: spreader_zombies.append(p)
    return spreader_zombies



def find_regular_zombies(contacts_dic, zombie_list):
    """Return sick people who have been in contact with both potential zombies
    and other sick people

    Args:
        contacts_dic (dic): each entry is a sick person's name and their
        list of contacts.
        zombie_list (list): all zombies
    
    Returns:
        list: Contains the names of sick people who are regular zombies
    """
    # Remove pass and fill in your code here
    regular_zombies = []
    for p in contacts_dic.keys():
        #initialise zombie and sick flag to False these mark if a perrson has been in contact with either
        zombie = False
        sick = False
        for c in contacts_dic[p]:
            if c in zombie_list:
                zombie = True #if a contact is a potential zombie make zombie flag true
            if c in list(contacts_dic.keys()):
                sick = True #if a contact is a sick person make sick flag true
        if sick and zombie: regular_zombies.append(p) #append name if both flags true
    return regular_zombies

def find_predator_zombies(contacts_dic, zombie_list):
    """Returns people that has had contact with only sick people

    Args:
        contacts_dic (dic): each entry is a sick person's name and their
        list of contacts.
        zombie_list (list): all zombies
    
    Returns:
        list: Contains the names of people who are predator zombies
    """
    # Remove pass and fill in your code here
    zombie_predators = []
    for p in contacts_dic.keys():
        zombie_predator = True #initialise zombie prerdator flag to true
        for c in contacts_dic[p]:
            if c in zombie_list or not c in list(contacts_dic.keys()):
                zombie_predator = False #if a contact is a zombie or is not a sick person then make flag false
        if zombie_predator: zombie_predators.append(p)
    return zombie_predators

def find_cycles_in_data(contacts_dic):
    """Returns whether a contact dictionary contains cycles or not

    Args:
        contacts_dic (dic): each entry is a sick person's name and their
        list of contacts.
    
    Returns:
        boolean: Indicates whether the dictionary contains at least one cycle or not
    """
    # Replace this return statement with your cycle detector when ready
    for p in contacts_dic.keys():
        for c in contacts_dic[p]: #for each contact of each sick person
            if c in contacts_dic.keys(): #check if the contact is a sick person
                if p in contacts_dic[c]: #if so check if the current sick person is a conatct of the contact
                    return True #if they are then a cycle exists return true
    return False

# Pretty printing functions. You have one function per section that
# must output a string as specified by contact_tracing.pdf 

def pretty_print_section_3():
    pass

def pretty_print_section_4(contact_dictionary):
    print("Contact Records:")
    patient_names = list(contact_dictionary.keys())
    patient_names.sort()
    for name in patient_names:
        contact_names = contact_dictionary[name]
        contact_names.sort()
        print("  " + name + " had contact with " + format_list(contact_names))

def pretty_print_section_5(patient_zero_list):
    patient_zero_list.sort()
    print()
    print("Patient Zero(s): " + format_list(patient_zero_list))

def pretty_print_section_6(potential_zombies_list):
    potential_zombies_list.sort()
    print("Potential Zombies: " + format_list(potential_zombies_list))

def pretty_print_section_7(not_zombie_or_patient_zero_list):
    not_zombie_or_patient_zero_list.sort()
    print("Neither Patient Zero or Potential Zombie: " + format_list(not_zombie_or_patient_zero_list))

def pretty_print_section_8(most_viral_list):
    most_viral_list.sort()
    print("Most Viral People: " + format_list(most_viral_list))

def pretty_print_section_9(most_contacted_list):
    most_contacted_list.sort()
    print("Most contacted: " + format_list(most_contacted_list))
    print()

def pretty_print_section_10(heights_dictionary):
    people = sorted(heights_dictionary.items(),key=lambda x:(-x[1],x[0]))
    print("Heights:")
    for p in people:
        print("  "+p[0]+": "+ str(p[1]))

# Additional credit printing functions

def pretty_print_section_11(spreader_zombie_list):
    spreader_zombie_list.sort()
    if len(spreader_zombie_list) != 0:
        print("  Spreader Zombies: " + format_list(spreader_zombie_list))
    else:
        print("  Spreader Zombies: (None)")

def pretty_print_section_12(regular_zombie_list):
    regular_zombie_list.sort()
    if len(regular_zombie_list) != 0:
        print("  Regular Zombies: " + format_list(regular_zombie_list))
    else:
        print("  Regular Zombies: (None)")

def pretty_print_section_13(zombie_predator_list):
    zombie_predator_list.sort()
    if len(zombie_predator_list) != 0:
        print("  Zombie Predators: " + format_list(zombie_predator_list))
    else:
        print("  Zombie Predators: (None)")

def pretty_print_section_14(cycles_state):
    pass
    
# =======================================================
# =======================================================
# Attention Student. Please do not modify any code below
# here. Doing so may result in lost marks.
# =======================================================
# =======================================================
def main():
    """
    Main logic for the program.
    DO NOT MODIFY THIS FUNCTION. THIS MAY RESULT IN LOST MARKS!
    """
    filename = ""
    args = sys.argv[1:]
    if len(args) == 0:
        filename = input("Please enter the name of the file: ")
    elif len(args) == 1:
        filename = args[0]
    else:
        print("""\n\nUsage\n\tTo run the program type:
        \tpython contact.py infile
        where infile is the name of the file containing the data.\n""")
        sys.exit()

    # Section 2. 
    if not file_exists(filename):
        print("File does not exist, ending program.")
        sys.exit()

    # Section 3.
    contacts_dic = parse_file(filename)

    # Section 4. 
    pretty_print_section_4(contacts_dic)

    # Section 5. 
    patients_zero_list = find_patients_zero(contacts_dic)
    pretty_print_section_5(patients_zero_list)

    # Section 6. 
    zombie_list = find_potential_zombies(contacts_dic)
    pretty_print_section_6(zombie_list)

    # Section 7.
    not_zombie_nor_zero = find_not_zombie_nor_zero(contacts_dic,
                                    patients_zero_list, zombie_list)
    pretty_print_section_7(not_zombie_nor_zero)

    # Section 8. 
    most_viral_list = find_most_viral(contacts_dic)
    pretty_print_section_8(most_viral_list)

    # Section 9. 
    most_contacted = find_most_contacted(contacts_dic)
    pretty_print_section_9(most_contacted)

    # Section 14.
    cycles = find_cycles_in_data(contacts_dic)
    pretty_print_section_14(cycles)

    if cycles:  # This evaluates to false if cycles = None
        print("Cycles detected")
    else:       
        # Section 10. 
        heights_dic = find_maximum_distance_from_zombie(contacts_dic, zombie_list)
        pretty_print_section_10(heights_dic)

    print("\nFor additional credit:")

    # Section 11.
    spreader = find_spreader_zombies(contacts_dic, zombie_list)
    pretty_print_section_11(spreader)

    # Section 12.
    regular = find_regular_zombies(contacts_dic, zombie_list)
    pretty_print_section_12(regular)

    # Section 13.
    predator = find_predator_zombies(contacts_dic, zombie_list)
    pretty_print_section_13(predator)

if __name__ == "__main__":
    main()
