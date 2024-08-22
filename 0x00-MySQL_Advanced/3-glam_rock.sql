-- lists all bands with Glam rock as thier style ranked by longevity
SELECT band_name, (IFNULL(split, '2020')) - formed_ AS lifespan
	FROM metal_bands
	WHERE FIND_IN_SET('Glam rock', INFULL(style, "")) > 0
	ORDER BY lifespan DESC;
