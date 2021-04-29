-- creates a stored procedure AddBonus that adds a new correction

DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id int,
    IN project_name varchar(255),
    IN score int
)
BEGIN
    INSERT INTO projects (name)
    SELECT * FROM (SELECT project_name) AS tmp
    WHERE NOT EXISTS (
        SELECT name FROM projects WHERE name = project_name
    ) LIMIT 1;
    INSERT INTO corrections (
        user_id, project_id, score
    )
    VALUES (
        user_id,
        (SELECT id FROM projects WHERE name = project_name),
        score
    );
END$$

DELIMITER ;
