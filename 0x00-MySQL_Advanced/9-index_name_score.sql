-- creates an index on the table
-- order the names by first letter and score
CREATE INDEX idx_name_first_score
ON names (LEFT(name, 1), score);
