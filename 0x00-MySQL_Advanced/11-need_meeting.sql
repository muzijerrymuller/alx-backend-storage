-- Creates a view need_meeting that lists all students with a score below 80
-- and either no last_meeting or a last_meeting date older than one month.
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
    SELECT name
        FROM students
        WHERE score < 80 AND
            (
                last_meeting IS NULL
                OR last_meeting < SUBDATE(CURRENT_DATE(), INTERVAL 1 MONTH)
            )
;
