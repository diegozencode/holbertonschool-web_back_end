-- creates a view that list all students
CREATE OR REPLACE VIEW need_meeting
AS SELECT name FROM students
WHERE score < 80 and (last_meeting IS NULL or last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH ));
