--Write a query to identify the top 2 Power Users who sent the highest number of messages
--on Microsoft Teams in August 2022. Display the IDs of these 2 users along with
--the total number of messages they sent. Output the results in descending order based on the count of the messages.

===========================================================

SELECT sender_id, count(*) FROM messages
where sent_date between '2022-08-01' and '2022-08-30'
group by sender_id
order by count(*) desc
limit 2;