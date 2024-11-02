SELECT a.name, b.rentals_date
FROM customers a
INNER JOIN rentals b
ON a.id = b.id_customers
WHERE EXTRACT(YEAR FROM b.rentals_date) = 2016 AND
EXTRACT(MONTH FROM b.rentals_date) = 9;