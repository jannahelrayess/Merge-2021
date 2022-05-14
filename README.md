# Remodeling-the-H-1B-Visa-Application-Process
Created from March 26-28 2021

Video description:
https://vimeo.com/529955156

The H-1B visa process is very biased and does not accurately reflect the needs of the 
USA or the applicant. This systematic approach should replace the current randomized 
lottery that chooses who receives a H-1B visa. 

Our approach works by taking into account an applicants highest degree level, income 
of the job they are applying for, and what job they will have. As explained in the 
video, stage 1 uses a weighted random for what applicants will be chosen based off of 
their degrees. The ratio for the degrees is based off of what an actual applicant pool 
looks like. The coefficients for the degrees are as follows:

Less than Bachelor’s degree has a coefficient of 1
Bachelor's degree has a coefficient of 30
Master's degree has a coefficient of 55
Doctorate degree has a coefficient of 10
Professional degree has a coefficient of 4

After stage 1 about 400 applicants are left (as the data used had only 500 applicants 
since this is run on a smaller scale). The next step was to sort the applicants through 
the income of the job they will be receiving. A threshold was made using the geometric 
mean of the applicants incomes. The reason why geometric mean was used apposed to 
arithmetic is because the arithmetic mean would have skewed the threshold towards the 
higher incomes too much. The program accepts 40% of people below the geometric mean and 
90% of people above and equal to the geometric mean are accepted, leaving around 250 
applicants left after this stage. The purpose of the final stage is to sort the remaining 
applicants based on the jobs they will be applying for. Considering the jobs needed by 
the USA changes constantly, this part of the code is meant to be edited as the needs 
change. At the moment, more medical health professionals are needed due to COVID-19, so 
the algorithm ensures a certain amount of medical professionals who are accepted. The 
percent of people given the visa is based on the cap amount as the H-1B visa does have a 
maximum acceptance number. Computer-Related Occupations make up 50% of cap amount, 
Occupations in Medicine and Health Occupations are 15% of cap amount (due to COVID-19), 
Occupations in Education are 10% of cap amount, and finally the rest of the cap amount 
(usually about 25% is left) is filled by all other Occupations, whose applicants are 
randomly chosen. The cap amount for our data set is 200 as we started with 500 applicants.
We modeled our dataset based on the available data on the breakdown of those who are 
given an H-1B visa.

Each stage of the algorithm uses a different method of sorting through the petitioners.
For example we use weighted randoms, then percentages against the threshold, and finally 
a specific number of petitioners based off of the cap number.

In the future, algorithms like these should be used to not only determine H-1B visas,
but also other kinds of visas with a cap. Of course the requirements and what would be 
taken into consideration changes from visa to visa. The goal is to move towards fully 
eliminating human biases in the US immigration system through systematic algorithms that
choose who gets a visa rather than humans.
