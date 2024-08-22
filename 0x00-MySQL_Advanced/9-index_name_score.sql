-- creates an index idx_name_first_score
-- on the table, order the names by first letter and score
CREATE INDEX idx_name_first_score
ON names((name(1)), score);
