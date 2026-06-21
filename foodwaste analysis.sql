create database local_food_management
use local_food_management

-- Q1. Total Providers by City
SELECT city, COUNT(*) AS total_providers
FROM providers
GROUP BY city
ORDER BY total_providers DESC;


--Q2. Providers by Type
SELECT type, COUNT(*) AS total_providers
FROM providers
GROUP BY type;

--Q3. Top 10 Food Contributing Providers
SELECT top 10
       p.name,
       SUM(f.quantity) AS total_quantity
FROM providers p
JOIN food_listings f
ON p.provider_id = f.provider_id
GROUP BY p.name
ORDER BY total_quantity DESC;

--Q4. Provider Type Contributing Most Food
SELECT provider_type,
       SUM(quantity) AS total_food
FROM food_listings
GROUP BY provider_type
ORDER BY total_food DESC;

-- 2. Receiver Analysis
--Q5. Receivers by City

SELECT city,
       COUNT(*) AS total_receivers
FROM receivers
GROUP BY city;

--Q6. Receivers by Type
SELECT type,
       COUNT(*) AS total_receivers
FROM receivers
GROUP BY type;

-- Q7. Top 10 Receivers by Claims
SELECT r.name,
       COUNT(c.claim_id) AS total_claims
FROM receivers r
JOIN claims c
ON r.receiver_id = c.receiver_id
GROUP BY r.name
ORDER BY total_claims DESC;

--3. Food Availability Analysis
--Q8. Total Food Quantity Available
SELECT SUM(quantity) AS total_food_quantity
FROM food_listings;


--Q9. Food Listings by City
SELECT location,
       COUNT(*) AS total_listings
FROM food_listings
GROUP BY location
ORDER BY total_listings DESC;

--Q10. Food Quantity by City
SELECT location,
       SUM(quantity) AS total_food
FROM food_listings
GROUP BY location
ORDER BY total_food DESC;

--Q11. Food Type Distribution
SELECT food_type,
       COUNT(*) AS total
FROM food_listings
GROUP BY food_type;

-- Q12. Meal Type Distribution
SELECT meal_type,
       COUNT(*) AS total
FROM food_listings
GROUP BY meal_type;

-- 4. Claims Analysis
-- Q13. Claim Status Distribution
SELECT status,
       COUNT(*) AS total_claims
FROM claims
GROUP BY status;

-- Q14. Claim Status Percentage
SELECT status,
       ROUND(
       COUNT(*) * 100.0 /
       SUM(COUNT(*)) OVER(),2
       ) AS percentage
FROM claims
GROUP BY status;

-- Q15. Most Claimed Food Items
SELECT f.food_name,
       COUNT(c.claim_id) AS total_claims
FROM food_listings f
JOIN claims c
ON f.food_id = c.food_id
GROUP BY f.food_name
ORDER BY total_claims DESC;


-- 5. Advanced Business Insights
-- Q17. Food Type Most in Demand
SELECT f.food_type,
       COUNT(c.claim_id) AS total_claims
FROM food_listings f
JOIN claims c
ON f.food_id=c.food_id
GROUP BY f.food_type
ORDER BY total_claims DESC;

-- Q18. Meal Type Most in Demand
SELECT f.meal_type,
       COUNT(c.claim_id) AS total_claims
FROM food_listings f
JOIN claims c
ON f.food_id=c.food_id
GROUP BY f.meal_type
ORDER BY total_claims DESC;

-- Q19. City with Highest Food Demand
SELECT r.city,
       COUNT(c.claim_id) AS total_claims
FROM receivers r
JOIN claims c
ON r.receiver_id=c.receiver_id
GROUP BY r.city
ORDER BY total_claims DESC;

-- Q20. Donation Success Rate
SELECT
ROUND(
SUM(CASE WHEN status='Completed' THEN 1 ELSE 0 END)*100.0
/
COUNT(*),2
) AS success_rate
FROM claims;

SELECT TOP 5 * FROM claims;

SELECT TOP 5 * FROM receivers;

SELECT TOP 5 * FROM food_listings

SELECT TOP 5 *
FROM providers;

