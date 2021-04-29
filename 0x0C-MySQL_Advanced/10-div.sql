-- safe divide
DELIMITER $$

DROP FUNCTION IF EXISTS SafeDiv $$

CREATE FUNCTION SafeDiv(
    a int,
    b int
)
RETURNS float
BEGIN
    IF b = 0 THEN
        RETURN (0);
    ELSE
        RETURN (a / b);
    END IF;
END$$

DELIMITER ;
