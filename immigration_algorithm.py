'''
immigration_algorithm.py
Jannah El-Rayess
2021-3-26

An algorithm that more fairly chooses who gets a H-1B visa and compares the result
statistics with those of how the outcome of H-1B visa is already chosen. The current
method is a random lottery while this algorithm uses thresholds based on the data of 
those who apply for an H-1B visa as well as the visa's purpose. Moreover, this program 
takes into account the current needs in the United States, and therefore needs to be 
updated and modernized on a regular basis to ensure it reflects our Country's necessities.
'''

# Imports
import random
import math

# make_list: -> lst
# Takes the immigration algorithm data and stores it into a list  
def make_list():
    data_lst = []
    data_file = open('immigration_algorithm_data.txt', 'r')
    
    for line in data_file:
        data_lst.append(line.strip().split(','))
    
    return data_lst
    
    data_file.close()

# highest_degree: -> lst
# Reduces the applicants for the visa by their highest degree
def highest_degree():
    degree_options = ["Less than Bachelor’s", "Bachelor's degree", "Master's degree", "Doctorate degree", "Professional degree"]
    degree_lst = random.choices(degree_options, weights=(1, 30, 55, 10, 4), k=400)
    data_lst = make_list()
    data_stage_one = []
    x = 0
    found = False

    while len(degree_lst) != 0:
        if found == False:
            if degree_lst[0] == data_lst[x][1]:
                data_stage_one.append(data_lst[x])
                data_lst[x] = ["0","Some Degree","0","Occupation"]
                found = True
            
            else:
                x += 1
        
        if found == True:
            x += 1
            degree_lst = degree_lst[1:]
            found = False
        
        if x > 498:
            x = 0

    return data_stage_one

# income: -> lst
# Reduces the applicants for the visa by their incomes for the jobs they are applying for
def income():
    data_lst = highest_degree()
    income_lst = []
    below_mean_lst = []
    above_mean_lst = []
    data_stage_two = []

    for i in range(len(data_lst)):
        income_lst.append(int(data_lst[i][2]))

    geomean = math.exp(math.fsum(math.log(num) for num in income_lst) / len(income_lst))

    for j in range(len(data_lst)):
        if int(data_lst[j][2]) < geomean:
            below_mean_lst.append(data_lst[j])
        
        else:
            above_mean_lst.append(data_lst[j])
    
    twenty_percent_below_lst = below_mean_lst[: int(len(below_mean_lst) * .4)]
    eighty_percent_above_lst = above_mean_lst[: int(len(above_mean_lst) * .9)]
    
    data_stage_two.extend(twenty_percent_below_lst)
    data_stage_two.extend(eighty_percent_above_lst)

    return [data_stage_two, geomean]

# job_category: -> lst
# Reduces the applicants for the visa by the jobs they are applying for
def job_category():
    all_data_lst = income()
    data_lst = all_data_lst[0]
    geomean = all_data_lst[1]
    cap_amount = 200
    computer_lst = []
    medical_lst = []
    education_lst = []
    other_lst = []
    data_stage_three = []
    j = 0

    for i in range(len(data_lst)):
        if data_lst[i][3] == 'Computer-Related':
            computer_lst.append(data_lst[i])
        
        elif data_lst[i][3] == 'Medicine and Health':
            medical_lst.append(data_lst[i])
        
        elif data_lst[i][3] == 'Education':
            education_lst.append(data_lst[i])
        
        else:
            other_lst.append(data_lst[i])
    
    cap_computer_lst = computer_lst[: int(cap_amount * .5)]
    cap_medical_lst = medical_lst[: int(cap_amount * .15)]
    cap_education_lst = education_lst[: int(cap_amount * .1)]

    data_stage_three.extend(cap_computer_lst)
    data_stage_three.extend(cap_medical_lst)
    data_stage_three.extend(cap_education_lst)

    while len(data_stage_three) < 200:
        data_stage_three.append(other_lst[j])
        j += 1
    
    return [data_stage_three, geomean]

# lottery: -> lst
# Chooses 200 applicants randomly
def lottery():
    random_numbers_chosen = random.sample(range(1, 501), 200)
    data_lst = make_list()
    random_people_chosen = []
    income_lst = []

    for i in range(len(data_lst)):
        if int(data_lst[i][0]) in random_numbers_chosen:
            random_people_chosen.append(data_lst[i])
    
    for j in range(len(random_people_chosen)):
        income_lst.append(int(data_lst[i][2]))

    geomean = math.exp(math.fsum(math.log(num) for num in income_lst) / len(income_lst))
    
    return [random_people_chosen, geomean]

# statistics: lst int str str -> 
# As a side effect, prints out the degree, income, and job statistics of all the 
# People in the given list as well as those who received the H-1B visa
def statistics(lst, mean, out_file, which):
    output_file = open(out_file, 'w')
    total_people = len(lst)

    for person in lst:
        print(person, file = output_file, end = '\n')
    
    lesser_degree = []
    bach_degree = []
    master_degree = []
    doc_degree = []
    prof_degree = []

    lower_income = []
    higher_income = []

    comp_job = []
    med_job = []
    edu_job = []
    other_job = []

    India_lst = []
    China_lst = []
    Canada_lst = []
    Mexico_lst = []
    UK_lst = []
    other_country_lst = []

    for i in range(len(lst)):
        if lst[i][1] == "Less than Bachelor’s":
            lesser_degree.append(lst[i])
        
        if lst[i][1] == "Bachelor's degree":
            bach_degree.append(lst[i])
        
        if lst[i][1] == "Master's degree":
            master_degree.append(lst[i])
        
        if lst[i][1] == "Doctorate degree":
            doc_degree.append(lst[i])
        
        if lst[i][1] == "Professional degree":
            prof_degree.append(lst[i])
        
        if int(lst[i][2]) < mean:
            lower_income.append(lst[i])
        
        if int(lst[i][2]) >= mean:
            higher_income.append(lst[i])
        
        if lst[i][3] == 'Computer-Related':
            comp_job.append(lst[i])
        
        if lst[i][3] == 'Medicine and Health':
            med_job.append(lst[i])
        
        if lst[i][3] == 'Education':
            edu_job.append(lst[i])
        
        if (lst[i][3] != 'Computer-Related') and (lst[i][3] != 'Medicine and Health') and (lst[i][3] != 'Education'):
            other_job.append(lst[i])
        
        if lst[i][4] == 'India':
            India_lst.append(lst[i])
        
        if lst[i][4] == 'China':
            China_lst.append(lst[i])
        
        if lst[i][4] == 'Canada':
            Canada_lst.append(lst[i])
        
        if lst[i][4] == 'Mexico':
            Mexico_lst.append(lst[i])
        
        if lst[i][4] == 'United Kingdom':
            UK_lst.append(lst[i])
        
        if (lst[i][4] != 'India') and (lst[i][4] != 'China') and (lst[i][4] != 'Canada') and (lst[i][4] != 'Mexico') and (lst[i][4] != 'United Kingdom'):
            other_country_lst.append(lst[i])

    percent_lesser_degree = (len(lesser_degree) / total_people) * 100
    percent_bach_degree = (len(bach_degree) / total_people) * 100
    percent_master_degree = (len(master_degree) / total_people) * 100
    percent_doc_degree = (len(doc_degree) / total_people) * 100
    percent_prof_degree = (len(prof_degree) / total_people) * 100

    percent_lower_income = (len(lower_income) / total_people) * 100
    percent_higher_income = (len(higher_income) / total_people) * 100

    percent_comp_job = (len(comp_job) / total_people) * 100
    percent_med_job = (len(med_job) / total_people) * 100
    percent_edu_job = (len(edu_job) / total_people) * 100
    percent_other_job = (len(other_job) / total_people) * 100

    percent_india = (len(India_lst) / total_people) * 100
    percent_china = (len(China_lst) / total_people) * 100
    percent_canada = (len(Canada_lst) / total_people) * 100
    percent_mexico = (len(Mexico_lst) / total_people) * 100
    percent_uk = (len(UK_lst) / total_people) * 100
    percent_other_country = (len(other_country_lst) / total_people) * 100

    print("\nHere are the statistics " + which + " the algorithm:\n" \
          "\nPercent of people who have less than a Bachelor’s degree: " + str(percent_lesser_degree) + "%\n" \
          "Percent of people who have a Bachelor’s degree: " + str(percent_bach_degree) + "%\n" \
          "Percent of people who have a Master's degree: " + str(percent_master_degree) + "%\n" \
          "Percent of people who have a Doctorate degree: " + str(percent_doc_degree) + "%\n" \
          "Percent of people who have a Professional degree: " + str(percent_prof_degree) + "%\n" \
          "\nPercent of people who have an income below the geometric mean income: " + str(percent_lower_income) + "%\n" \
          "Percent of people who have an income above the geometric mean income: " + str(percent_higher_income) + "%\n" \
          "\nPercent of people who have a Computer-Related Occupation: " + str(percent_comp_job) + "%\n" \
          "Percent of people who have a Medicine and Health Occupation: " + str(percent_med_job) + "%\n" \
          "Percent of people who have an Education Occupation: " + str(percent_edu_job) + "%\n" \
          "Percent of people who have neither a Computer-Related, Medicine and Health, nor an Education Occupation: " + str(percent_other_job) + "%" \
          "\nPercent of people who are from India: " + str(percent_india) + "%\n" \
          "Percent of people who are from China: " + str(percent_china) + "%\n" \
          "Percent of people who are from Canada: " + str(percent_canada) + "%\n" \
          "Percent of people who are from Mexico: " + str(percent_mexico) + "%\n" \
          "Percent of people who are from UK: " + str(percent_uk) + "%\n" \
          "Percent of people who are neither from India, China, Canada, Mexico, nor UK: " + str(percent_other_country) + "%\n" \
          , file = output_file, end = '')
    
    output_file.close()

# main: -> 
# Runs both the randomly chosen 200 people as will as the algorithmically chosen 200 people
# Through the statistics function and respectively prints the output into separate files
def main():
    # Algorithm data
    all_data_lst = job_category()
    data_lst = all_data_lst[0]
    geomean = all_data_lst[1]

    output_file = open('immigration_algorithm_result.txt', 'w')

    statistics(data_lst, geomean, 'immigration_algorithm_result.txt', 'using')
    
    output_file.close()

    # Lottery data
    random_chosen_people = lottery()
    lot_data_lst = random_chosen_people[0]
    lot_geomean = random_chosen_people[1]

    output_file_lot = open('immigration_algorithm_result_lottery.txt', 'w')
    
    statistics(lot_data_lst, lot_geomean, 'immigration_algorithm_result_lottery.txt', 'not using')

    output_file_lot.close()

main()
