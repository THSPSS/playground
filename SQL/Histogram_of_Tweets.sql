WITH cte_tweet AS (
  SELECT user_id
       , count(tweet_id) as tweet_num
  FROM tweets
 WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP by user_id
)

  SELECT tweet_num AS twee_bucket
       , count(user_id) AS users_num
    FROM cte_tweet
GROUP BY tweet_num;