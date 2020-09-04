-- ranks country origins of bands
SELECT origin, fans as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
