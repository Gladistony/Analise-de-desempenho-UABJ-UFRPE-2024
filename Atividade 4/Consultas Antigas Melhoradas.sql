-- Listar todos os livros com seus autores:
SELECT Autor.Nome, Livro.Titulo 
FROM Autor
JOIN Livro ON Autor.ID_Autor = Livro.ID_Autor;

-- Listar todos os empréstimos e os usuários correspondentes:
SELECT Emprestimo.ID_Emprestimo, Usuario.Nome 
FROM Emprestimo
Join Usuario ON Emprestimo.ID_Usuario = Usuario.ID_Usuario;

-- Listar todos os livros e suas categorias:
SELECT Livro.Titulo, Categoria.Nome 
FROM Livro
JOIN Livro_Categoria on Livro.ID_Livro = Livro_Categoria.ID_Livro
JOIN Categoria on Livro_Categoria.ID_Categoria = Categoria.ID_Categoria;

-- Listar todos os livros emprestados:
SELECT Livro.Titulo, Usuario.Nome 
FROM Livro 
JOIN Emprestimo on Livro.ID_Livro = Emprestimo.ID_Livro
JOIN Usuario on Emprestimo.ID_Usuario = Usuario.ID_Usuario;

-- Listar todos os autores e seus livros publicados:
SELECT Autor.Nome, Livro.Titulo 
FROM Autor
join Livro on Autor.ID_Autor = Livro.ID_Autor
