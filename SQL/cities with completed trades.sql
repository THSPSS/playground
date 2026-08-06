--We begin by joining the trades and users tables based on the related column user_id. This is because the 'Completed' order status is stored in the trades table, while the cities are stored in the users table.

--In the SELECT statement, we pull the city field from the users table and the order_id field from the trades table.

===============================================================================

SELECT us.city
     , count(order_id) as total_orders
  FROM trades tr
       INNER JOIN users us  ON tr.user_id = us.user_id
where status = 'Completed'
group by us.city
order by total_orders desc
limit 3;