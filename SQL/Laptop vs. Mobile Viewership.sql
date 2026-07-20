--This is the same question as problem #3 in the SQL Chapter of Ace the Data Science Interview!

--Assume you're given the table on user viewership categorised by device type where the three types are laptop, tablet, and phone.

--Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. Output the total viewership for laptops as laptop_reviews and the total viewership for mobile devices as mobile_views.

--Effective 15 April 2023, the solution has been updated with a more concise and easy-to-understand approach.

=========================

cte_mobile_view AS (
  SELECT COUNT(*) AS mobile_reviews
  FROM viewership
  WHERE device_type IN ("tablet", "phone"))

UNION ALL
cte_laptop_view AS (
  SELECT COUNT(*) AS laptop_reviews
  FROM viewership
  WHERE device_type = "laptop";
);

SELECT COUNT(*) FROM viewership
WHERE DEVICE_TYPE IN ("tablet", "phone");

