-- Listar todos os livros com seus autores:
SELECT Autor.Nome, Livro.Titulo 
FROM Autor, Livro 
WHERE Autor.ID_Autor = Livro.ID_Autor;

-- Listar todos os empréstimos e os usuários correspondentes:
SELECT Emprestimo.ID_Emprestimo, Usuario.Nome 
FROM Emprestimo, Usuario 
WHERE Emprestimo.ID_Usuario = Usuario.ID_Usuario;

-- Listar todos os livros e suas categorias:
SELECT Livro.Titulo, Categoria.Nome 
FROM Livro, Livro_Categoria, Categoria 
WHERE Livro.ID_Livro = Livro_Categoria.ID_Livro 
AND Livro_Categoria.ID_Categoria = Categoria.ID_Categoria;

-- Listar todos os livros emprestados:
SELECT Livro.Titulo, Usuario.Nome 
FROM Livro, Emprestimo, Usuario 
WHERE Livro.ID_Livro = Emprestimo.ID_Livro 
AND Emprestimo.ID_Usuario = Usuario.ID_Usuario;

-- Listar todos os autores e seus livros publicados:
SELECT Autor.Nome, Livro.Titulo 
FROM Autor, Livro 
WHERE Autor.ID_Autor = Livro.ID_Autor;
