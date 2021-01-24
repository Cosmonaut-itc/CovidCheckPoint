# CovidCheckPoint
 This project was done in the Intern Hackathon 2021.

Welcome to CovidCheckPoint, the main purpose of this game is to
evaluate different data about employees in a company. This game is
inspired in an existing game called "PapersPlease" but in this one
you also need to evaluate if employees have COVID-19 meassures achived.

The game works in this way: 

- You have 3 lives to reach as much score as you can doing no errors while
you accept or not employees. (Every day that passes is an extra live).

- If you give access to a person who does not have authorization, you are going to
loose a live, same way if you dont give access to people that have everything in
order.

- If you have no mistakes while playing you can get streaks, this will boost your
points

Here you have some constraints to see if a person have authorization to enter
to the company or not

Employee has successfull access if:
- his/her credential is a worker credential
- his/her clearance level is up to 0
- Has mask on
- last check status is minor than 15 days

Employee has denied access if:
- His/her credential is a fired worker
- cleareance level is equal to 0
- Does not have a mask
- Last check status is greater than 15 days (if you get unlucky, maybe a person who has more than 15 days could enter also, because there is a percentage that is calculated about the extra days he hasnt checked and if the dice gets less or equal for the percentage, that person could have entered and you loose a life, its about luck sometimes)



Resources 
  - python3
  - import names
  - pip installer
