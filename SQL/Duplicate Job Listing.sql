This is the same question as problem #8 in the SQL Chapter of Ace the Data Science Interview!

Assume you're given a table containing job postings from various companies on the LinkedIn platform. Write a query to retrieve the count of companies that have posted duplicate job listings.

Definition:

Duplicate job listings are defined as two job listings within the same company that share identical titles and descriptions.

=========================

with cte_company_duplicates as(
select company_id, count(company_id) , count(title), count(description)
from job_listings
group by company_id ,title, description
having count(title) = 2 and count(description) = 2
)

select count(*)
from cte_company_duplicates;
