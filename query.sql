WITH f1 AS(
SELECT name, high, low, ts, SUBSTRING(ts,12,2) AS hour 
FROM "AwsDataCatalog"."finance-db"."12"),
f2 AS(
SELECT name,SUBSTRING(ts,12,2) as hour, max(high) AS high, min(low) AS low
FROM "AwsDataCatalog"."finance-db"."12"
GROUP BY name, SUBSTRING(ts,12,2))

SELECT f1.name, f1.hour, f2.high, f2.low, f1.ts
FROM f1 JOIN f2 ON f1.name = f2.name AND f1.high = f2.high AND f1.hour = f2.hour
ORDER BY f1.name, f1.hour;
 