# Write your MySQL query statement below
select FirstName, LastName, City, State
from Person P left join Address A on P.PersonId = A.PersonId 