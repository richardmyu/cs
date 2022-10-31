SELECT
  DISTINCT emp
FROM
  EmpSkills AS ES1
WHERE
  NOT EXISTS (
    SELECT
      skill
    FROM
      Skills
    WHERE
      skill NOT IN (
        SELECT
          skill
        FROM
          EmpSkills AS ES2
        WHERE
          ES1.emp = ES2.emp
      )
  );
