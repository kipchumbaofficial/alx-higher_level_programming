-- List number of rows with the same score
-- Displays only score and number
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
