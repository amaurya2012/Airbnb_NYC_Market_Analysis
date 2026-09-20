-- Airbnb NYC SQL Analysis
-- The Python notebook/script can load AB_NYC_2019.csv into a SQLite table named airbnb.
-- Run these queries after creating the table.

-- 1. Number of listings by borough
SELECT neighbourhood_group, COUNT(*) AS listings
FROM airbnb
GROUP BY neighbourhood_group
ORDER BY listings DESC;

-- 2. Average price by borough
SELECT neighbourhood_group,
       ROUND(AVG(price), 2) AS avg_price
FROM airbnb
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;

-- 3. Median is not built into standard SQLite.
-- Use Python/Pandas for median calculations.

-- 4. Average price by room type
SELECT room_type,
       ROUND(AVG(price), 2) AS avg_price,
       COUNT(*) AS listings
FROM airbnb
GROUP BY room_type
ORDER BY avg_price DESC;

-- 5. Borough + room type
SELECT neighbourhood_group,
       room_type,
       COUNT(*) AS listings,
       ROUND(AVG(price), 2) AS avg_price
FROM airbnb
GROUP BY neighbourhood_group, room_type
ORDER BY neighbourhood_group, avg_price DESC;

-- 6. Top neighborhoods by listing count
SELECT neighbourhood,
       COUNT(*) AS listings
FROM airbnb
GROUP BY neighbourhood
ORDER BY listings DESC
LIMIT 15;

-- 7. Hosts with the most listings
SELECT host_id,
       COUNT(*) AS listings
FROM airbnb
GROUP BY host_id
ORDER BY listings DESC
LIMIT 15;

-- 8. Most reviewed listings
SELECT id, name, neighbourhood_group, room_type,
       price, number_of_reviews
FROM airbnb
ORDER BY number_of_reviews DESC
LIMIT 15;

-- 9. Price bands
SELECT
    CASE
        WHEN price <= 50 THEN '$0-50'
        WHEN price <= 100 THEN '$51-100'
        WHEN price <= 200 THEN '$101-200'
        WHEN price <= 500 THEN '$201-500'
        ELSE '$500+'
    END AS price_band,
    COUNT(*) AS listings
FROM airbnb
GROUP BY price_band
ORDER BY listings DESC;

-- 10. Average availability by room type
SELECT room_type,
       ROUND(AVG(availability_365), 2) AS avg_available_days
FROM airbnb
GROUP BY room_type
ORDER BY avg_available_days DESC;