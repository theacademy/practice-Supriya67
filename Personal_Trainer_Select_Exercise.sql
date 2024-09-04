-- SELECT Questions
use personaltrainer;

-- Activity 1: Select all rows and columns from the Exercise table (64 rows)
select * from exercise;

-- Activity 2: Select all rows and columns from the Client table. (500 rows)
select * from client;

-- Activity 3: Select all columns from Client where the City is Metairie. (29 rows)
select * from client
where city = 'Metairie';

select count(*) from client
where city = 'Metairie';

-- Activity 4: Is there a Client with the ClientId '818u7faf-7b4b-48a2-bf12-7a26c92de20c'? (0 rows)
select clientId from client
where clientId = '818u7faf-7b4b-48a2-bf12-7a26c92de20c';

-- Activity 5: How many rows are in the Goal table? (17 rows)
select count(*) from goal;

-- Activity 6: Select Name and LevelId from the Workout table. (26 rows)
select name, levelId from workout;

-- Activity 7: Select Name, LevelId, and Notes from Workout where LevelId is 2. (11 rows)
select name, levelId, notes from workout
where levelId = 2;

-- Activity 8: Select FirstName, LastName, and City from Client where City is Metairie, Kenner, or Gretna. (77 rows)
select firstname, lastname, city from client
where city = 'Metairie' or city = 'Kenner' or city = 'Gretna';

-- Activity 9: Select FirstName, LastName, and BirthDate from Client for Clients born in the 1980s. (72 rows)
select firstname, lastname, birthdate from client
where birthdate like '198%';

select count(*) from client
where birthdate like '198%';

-- Activity 10: Write the query above in a different way.
select firstname, lastname, birthdate from client
where birthdate between '1980-01-01' and '1989-12-31';

-- Activity 11: How many rows in the Login table have a .gov EmailAddress? (17 rows)
select count(*) from login
where emailaddress like '%.gov';

-- Activity 12: How many Logins do NOT have a .com EmailAddress? (122 rows)
select count(*) from login
where emailaddress not like '%.com';

-- Activity 13: Select first and last name of Clients without a BirthDate. (37 rows)
select firstname, lastname from client
where birthdate is null;

-- Activity 14: Select the Name of each ExerciseCategory that has a parent (ParentCategoryId value is not null). (12 rows)
select name from exercisecategory
where parentcategoryid is not null;

-- Activity 15: Select Name and Notes of each level 3 Workout that contains the word 'you' in its Notes. (4 rows)
select name, notes from workout
where levelid = 3 and notes like '%you%';

-- Activity 16: Select FirstName, LastName, City from Clients whose LastName starts with L,M, or N and who live in LaPlace. (5 rows)
select firstname, lastname, city from client
where (lastname like 'L%' or lastname like 'M%' or lastname like 'N%') and city = 'LaPlace';

-- Activity 17: Select InvoiceId, Description, Price, Quantity, and ServiceDate from InvoiceLineItem.
-- Add an additional field that uses Price and Quantity to calculate the line item total.
-- Display records where the line item total is between 15 and 25 dollars. (667 rows)
select invoiceid, description, price, quantity, servicedate, (price * quantity) as itemTotal from invoicelineitem
where (price * quantity) between 15 and 25;

-- Activity 18: Does the Client, Estrella Bazely, have a Login? If so, what is her email address?
-- This requires two queries:
-- Select a Client record for Estrella Bazely. Does it exist?
-- If it does, select a Login record that matches its ClientId.
select count(*) from client
where firstname = 'Estrella' and lastname = 'Bazely';

select a.*, b.emailaddress from client a, login b 
where a.firstname = 'Estrella' and a.lastname = 'Bazely'
and a.clientid = b.clientid;

-- Activity 19: What are the Goals of the Workout with the Name 'This Is Parkour'?
-- Select the WorkoutId from Workout where Name equals 'This Is Parkour'. (1 row)
select workoutid from workout
where name = 'This is Parkour';
-- outputs 12
-- Select GoalId from WorkoutGoal where the WorkoutId matches the WorkoutId from your first query. (3 rows)
select goalid from workoutgoal
where workoutid = 12;
-- outputs 3, 8, 15
-- Select everything from Goal where the GoalId is one of the GoalIds from your second query. (3 rows)
select * from goal
where goalId in (3, 8, 15);

select * from goal
where goalId in (
select goalid from workoutgoal
where workoutid = (select workoutid from workout
where name = 'This is Parkour')
);



