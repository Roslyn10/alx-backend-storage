-- a function that divides and returns the first by the second number
DELIMITER //

DROP FUNCTION IF EXSISTS SafeDiv;

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0 THEN
		RETURN NULL;
	ELSE
		RETURN a / b;
	END IF;
END //
DELIMITER ;
