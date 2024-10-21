SELECT a.id, a.name FROM customers a
LEFT JOIN locations b
ON a.id = b.id_customers
WHERE b.id_customers IS NULL
ORDER BY a.id;