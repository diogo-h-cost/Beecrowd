SELECT a.name, b.name, c.name
FROM products a
INNER JOIN providers b ON a.id_providers = b.id
INNER JOIN categories c ON a.id_categories = c.id
WHERE b.name = 'Sansul SA' AND c.name = 'Imported';