-- Adding Citties

SELECT id,name FROM states WHERE state_id IN (SELECT id FROM states WHERE name = "California") ORDER BY cities.id ASC;