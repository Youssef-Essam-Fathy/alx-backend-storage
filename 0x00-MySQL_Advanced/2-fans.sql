--SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Create a temporary table to aggregate number of fans per country origin
CREATE TEMPORARY TABLE IF NOT EXISTS tmp_fan_counts AS
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank origins by number of fans in descending order
SELECT origin, nb_fans
FROM tmp_fan_counts
ORDER BY nb_fans DESC;
