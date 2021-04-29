-- stored procedure that computes overall weighted score
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id int
)
BEGIN
   UPDATE users
   SET average_score = (
       SELECT SUM(score * projects.weight) / SUM(projects.weight)
       FROM corrections
       INNER JOIN projects
       ON projects.id = project_id
       WHERE corrections.user_id = user_id
   )
   WHERE id = user_id;
END$$

DELIMITER ;
