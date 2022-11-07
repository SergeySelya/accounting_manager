-- 1. Напишите запрос, который подсчитает какое количество ноутбуков представлено в каждом бренде.
--    Отсортируйте данные по убыванию.

SELECT notebooks_brand.*, COUNT(notebooks_notebook.id) AS "Number"
FROM notebooks_brand
JOIN notebooks_notebook ON notebooks_notebook.brand_id = notebooks_brand.id
GROUP BY notebooks_brand.id
ORDER BY "Number" DESC;


-- 2. Вам необходимо выделить группы ноутбуков по размерам.
--    Для этого размеры предварительно нужно округлить в большую сторону до ближайшего
--	  0 или 5 и затем сгруппировать по одинаковым размерам, подсчитав количество ноутбуков в каждой группе.
-- 	  Отсортируйте данные по размерам.

SELECT diagonal, COUNT(diagonal) AS "кол-во"
	FROM (SELECT ROUND(diagonal) AS "diagonal"
	  	  FROM notebooks_notebook
		 ) AS D
	GROUP BY diagonal
	ORDER BY diagonal DESC;


