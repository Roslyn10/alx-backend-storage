-- a function that divides and returns the first by the second number
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0;
		RETURN NULL;
	RETURN number / number;
END //
DELIMITER;
