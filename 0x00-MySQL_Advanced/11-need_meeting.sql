-- creates a view that lists all student that have a score under 80
CREATE VIEW need_meeting AS
SELECT name, score
FROM students
WHERE score < 80 AND 
(
	last_meeting IS NULL
	OR last_meeting < SUBDATE(CURRENT_DATE, INTERVAL 1 MONTH)
);
