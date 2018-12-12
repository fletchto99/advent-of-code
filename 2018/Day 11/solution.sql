--DROP TABLE IF EXITS Input;
--CREATE TABLE input (val TEXT);
--.import input.txt Input

DROP TABLE IF EXISTS Areas;
CREATE TABLE Areas (
  X INTEGER NOT NULL,
  Y INTEGER NOT NULL,
  Size INTEGER NOT NULL,
  Area INTEGER NOT NULL,
  PRIMARY KEY(X, Y, Size)
);
CREATE INDEX Areas_Index ON Areas (Area DESC);

DROP TABLE IF EXISTS Grid;
CREATE TABLE Grid (
  X INTEGER NOT NULL,
  Y INTEGER NOT NULL,
  Score INTEGER NOT NULL,
  PRIMARY KEY(X, Y)
);
CREATE INDEX XY_Index ON Grid (X ASC, Y ASC);

INSERT INTO grid(X, Y, Score)
WITH RECURSIVE coords(coord) AS (SELECT 1 UNION ALL SELECT coord+1 FROM coords LIMIT 300)
SELECT x.coord, y.coord, (((((((x.coord + 10) * y.coord) + (select CAST(val as Unsigned) from Input)) * (x.coord + 10))/100)%10) - 5)
FROM coords AS x, coords AS y;

INSERT INTO Areas(X, Y ,Size, Area)
WITH RECURSIVE size(len) AS (SELECT 1 UNION ALL SELECT len+1 FROM size LIMIT 300)
SELECT
  x.len,
  y.len,
  s.len,
  (
    SELECT SUM(g.Score)
    FROM Grid g
    WHERE
      (g.x between x.len AND x.len+s.len-1) AND
      (g.y between y.len AND y.len+s.len-1)
  )
FROM size AS x, size AS y, size as s
WHERE s.len < 5 and x.len + s.len - 1 <= 300 AND y.len + s.len - 1 <= 300;

SELECT X, Y, Size, Area
FROM Areas
WHERE Size=3
ORDER BY Area DESC
LIMIT 1;

SELECT X, Y, Size, Area
FROM Areas
ORDER BY Area DESC
LIMIT 1;
