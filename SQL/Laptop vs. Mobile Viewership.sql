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


cte_mobile_view AS (
  SELECT 1 as num,
  COUNT(*) AS mobile_reviews
  FROM viewership
  WHERE device_type IN ("tablet", "phone"))

cte_laptop_view AS (
  SELECT 2 as num,COUNT(*) AS laptop_reviews
  FROM viewership
  WHERE device_type = "laptop";
);


SELECT COUNT(*) FROM viewership
WHERE DEVICE_TYPE IN ("tablet", "phone");


WITH cte_table AS ( SELECT CASE WHEN device_type = "laptop" THEN 1 ELSE 0 END AS laptop_views,
       CASE WHEN device_type IN ("tablet", "phone") THEN 1 ELSE 0 END AS mobile_views
FROM viewership)

SELECT SUM(laptop_views) AS laptop_views,
       SUM(mobile_views) AS mobile_vews
  FROM cte_table;
