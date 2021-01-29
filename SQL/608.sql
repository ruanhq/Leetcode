#608. Tree Node:
SELECT id,
(
	CASE WHEN tree.p_id IS NULL THEN 'Root'
	     WHEN tree.id IN (SELECT p_id FROM tree) THEN 'Inner'
	     ELSE 'Leaf'
	END
) AS Type
FROM tree;