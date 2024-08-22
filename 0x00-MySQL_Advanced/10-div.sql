-- a function that divides and returns the first by the second number
DROP FUNCTION IF EXISTS
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURN FLOAT
AS
BEGIN
	IF b = 0;
		RETURN NULL;
	RETURN number / number;
END;
