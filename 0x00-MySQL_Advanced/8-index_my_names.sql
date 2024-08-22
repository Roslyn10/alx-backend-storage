-- creates an index and returns the first letter of name
CREATE INDEX idx_name_first_score
ON names (LEFT(name, 1));
