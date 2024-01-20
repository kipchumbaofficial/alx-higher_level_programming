-- List all records from second table
-- Rows without name not displayed
SELECT score, name FROM second_table
WHERE name != NULL
ORDER BY score DESC;
