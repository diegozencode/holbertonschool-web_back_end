-- stored procedure overall weighted score for all
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
   UPDATE users
   SET average_score = (
       SELECT SUM(score * projects.weight) / SUM(projects.weight)
       FROM corrections
       INNER JOIN projects
       ON projects.id = corrections.project_id
       WHERE corrections.user_id = users.id
   );
END$$

DELIMITER ;
