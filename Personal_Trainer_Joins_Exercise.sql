-- Joins queries for personalTrainer db
use personaltrainer;

-- Activity 1: Select all columns from ExerciseCategory and Exercise.
-- The tables should be joined on ExerciseCategoryId.
-- This query returns all Exercises and their associated ExerciseCategory.
-- 64 rows
select e.*, ec.* from exercise e
left join exercisecategory ec 
on e.exerciseCategoryId = ec.exerciseCategoryId;

-- Activity 2: Select ExerciseCategory.Name and Exercise.Name where the ExerciseCategory does not have a ParentCategoryId (it is null).
-- Again, join the tables on their shared key (ExerciseCategoryId).
-- 9 rows
select ec.Name, e.Name from exercise e
left join exerciseCategory ec 
on ec.exerciseCategoryId = e.exerciseCategoryId
where ec.parentCategoryId is null;

-- Activity 3: The query above is a little confusing. At first glance, it's hard to tell which Name belongs to ExerciseCategory and which belongs to Exercise.
-- Rewrite the query using aliases:
-- Alias ExerciseCategory.Name as 'CategoryName'.
-- Alias Exercise.Name as 'ExerciseName'.
-- 9 rows
select ec.Name as CategoryName, e.Name as ExerciseName from exercise e
left join exerciseCategory ec 
on ec.exerciseCategoryId = e.exerciseCategoryId
where ec.parentCategoryId is null;

-- Activity 4: Select FirstName, LastName, and BirthDate from Client and EmailAddress from Login where Client.BirthDate is in the 1990s.
-- Join the tables by their key relationship.
-- What is the primary-foreign key relationship?
-- 35 rows
select c.firstname, c.lastname, c.birthdate, l.emailAddress from client c
join login l
on c.clientId = l.clientId
where c.birthdate like "199%";


-- Activity 5: Select Workout.Name, Client.FirstName, and Client.LastName for Clients with LastNames starting with 'C'?
-- How are Clients and Workouts related?
-- 25 rows
select w.name, c.firstname, c.lastname from client c, clientWorkout cw, workout w
where c.clientId = cw.clientId and w.workoutId = cw.workoutId and c.lastname like "C%";

select w.name, c.firstname, c.lastname from client c
inner join clientworkout cw on c.clientId = cw.clientId
inner join workout w on w.workoutId = cw.workoutId
where c.lastname like "C%";

-- Activity 6: Select Names from Workouts and their Goals.
-- This is a many-to-many relationship with a bridge table.
-- Use aliases appropriately to avoid ambiguous columns in the result.
select w.name as WorkoutName, g.name as GoalName from workout w
inner join workoutGoal wg on w.workoutId = wg.workoutId
inner join goal g on g.goalId = wg.goalId;

-- Activity 7: Select FirstName and LastName from Client.
-- Select ClientId and EmailAddress from Login.
-- Join the tables, but make Login optional.
-- 500 rows
select c.firstname, c.lastname, l.clientId, l.emailAddress from client c
left outer join login l
on c.clientId = l.clientId;

-- Using the query above as a foundation, select Clients who do not have a Login.
-- 200 rows
select c.firstname, c.lastname, l.clientId, l.emailAddress from client c
left outer join login l
on c.clientId = l.clientId
where l.clientId is null;

-- Activity 8
-- Does the Client, Romeo Seaward, have a Login?
-- Decide using a single query.
-- 0 rows
select c.firstname, c.lastname from client c
inner join login l on c.clientId = l.clientId
where c.firstname = "Romeo" and c.lastname = "Seaward";

-- Activity 9: Select ExerciseCategory.Name and its parent ExerciseCategory's Name.
-- This requires a self-join.
-- 12 rows
select ec.name as Category, e.name as ParentCategory from exerciseCategory ec, exerciseCategory e
where ec.exerciseCategoryId = e.ParentCategoryId;

select ec.name as Category, e.name as ParentCategory from exerciseCategory ec
inner join exerciseCategory e
on ec.exerciseCategoryId = e.ParentCategoryId;

-- Activity 10: Rewrite the query above so that every ExerciseCategory.Name is included, even if it doesn't have a parent.
-- 16 rows
select ec.name as Category, e.name as ParentCategory from exerciseCategory ec
left join exerciseCategory e
on ec.exerciseCategoryId = e.ParentCategoryId;  -- case 1 (wrong)

select ec.name as Category, e.name as ParentCategory from exerciseCategory ec
left join exerciseCategory e
on ec.ParentCategoryId = e.exerciseCategoryId;   -- case 2 (correct)

-- Activity 11
-- Are there Clients who are not signed up for a Workout?
-- 50 rows
select c.clientId as Client, cw.clientId as ClientWorkout from client c
left join clientworkout cw on c.clientId = cw.clientId
where cw.clientId is null;

-- Activity 12
-- Which Beginner-Level Workouts satisfy at least one of Shell Creane's Goals?
-- Goals are associated to Clients through ClientGoal.
-- Goals are associated to Workouts through WorkoutGoal.
-- 6 rows, 4 unique rows

-- our solution (with subquery)
select distinct w.name as WorkoutName, w.levelId from workout w
inner join workoutGoal wg on w.workoutId = wg.workoutId
inner join goal g on g.goalId = wg.goalId
where w.levelId = 1 and g.name in (select g.name as GoalName from goal g
inner join clientGoal cg on g.goalId = cg.goalId
inner join client c on c.clientId = cg.clientId
where c.firstname = "Shell" and c.lastname = "Creane");

-- actual solution (with 3 inner joins)
SELECT distinct w.name as WorkoutName, w.levelId FROM Client c
INNER JOIN ClientGoal cg ON c.ClientId = cg.ClientId
INNER JOIN WorkoutGoal wg ON cg.GoalId = wg.GoalId
INNER JOIN Workout w ON wg.WorkoutId = w.WorkoutId
WHERE c.FirstName = 'Shell' AND c.LastName = 'Creane' AND w.LevelId = 1;

-- Activity 13: Select all Workouts.
-- Join to the Goal, 'Core Strength', but make it optional.
-- You may have to look up the GoalId before writing the main query.
-- If you filter on Goal.Name in a WHERE clause, Workouts will be excluded. Why?
-- 26 Workouts, 3 Goals
select w.name Workout, g.name Goal
from workout w left join workoutgoal wg 
on w.workoutId = wg.workoutId and wg.goalId = 10
left join goal g 
on wg.goalId = g.goalId;

-- Activity 14
-- The relationship between Workouts and Exercises is... complicated:
-- Workout links to WorkoutDay (one day in a Workout routine) 
-- which links to WorkoutDayExerciseInstance (Exercises can be repeated in a day so a bridge table is required) 
-- which links to ExerciseInstance (Exercises can be done with different weights, repetitions, laps, etc...) 
-- which finally links to Exercise.
-- Select Workout.Name and Exercise.Name for related Workouts and Exercises.
select w.name Workout, e.name Exercise from workout w
join workoutDay wd on w.workoutId = wd.workoutId
join workoutDayExerciseInstance wdei on wd.workoutDayId = wdei.workoutDayId
join exerciseInstance ei on wdei.exerciseInstanceId = ei.exerciseInstanceId
join exercise e on ei.exerciseId = e.exerciseId;


-- Activity 15
-- An ExerciseInstance is configured with ExerciseInstanceUnitValue.
-- It contains a Value and UnitId that links to Unit.
-- Example Unit/Value combos include 10 laps, 15 minutes, 200 pounds.
-- Select Exercise.Name, ExerciseInstanceUnitValue.Value, and Unit.Name for the 'Plank' exercise.
-- How many Planks are configured, which Units apply, and what are the configured Values?
-- 4 rows, 1 Unit, and 4 distinct Values
select e.name Exercise, eiuv.value Value, u.name Unit from exercise e
join exerciseInstance ei on e.exerciseId = ei.exerciseId and e.name = "Plank"
left join exerciseInstanceUnitValue eiuv on ei.exerciseInstanceId = eiuv.exerciseInstanceId
left join unit u on eiuv.unitId = u.unitId;


