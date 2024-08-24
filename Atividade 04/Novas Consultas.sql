-- Listar todos os autores e seus livros publicados:
SELECT Autor.Nome, Livro.Titulo 
FROM Autor
join Livro on Autor.ID_Autor = Livro.ID_Autor;

-- Nova consulta 1: Listar todos os livros publicados após o ano 2000:
SELECT Titulo, Ano_Publicacao 
FROM Livro 
WHERE Ano_Publicacao > 1990;

-- Nova consulta 2: Lista todas as categorias e quantidades de livros em cada categoria:
SELECT Categoria.Nome, COUNT(Livro_Categoria.ID_Livro) AS Numero_Livros
FROM Categoria
LEFT JOIN Livro_Categoria ON Categoria.ID_Categoria = Livro_Categoria.ID_Categoria
GROUP BY Categoria.Nome;

-- Nova consulta 3: Lista todos os livros ainda não emprestados:
SELECT Livro.Titulo
FROM Livro
LEFT JOIN Emprestimo on Livro.ID_Livro = Emprestimo.ID_Livro
WHERE Emprestimo.ID_Livro is NULL;