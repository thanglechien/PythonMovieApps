-- create database
CREATE DATABASE MovieData;

-- use the database
USE MovieData;

-- create Genres table
CREATE TABLE Genres (
    GenreID INT PRIMARY KEY IDENTITY(1,1),
    GenreName VARCHAR(50) NOT NULL
);

-- Create Movies Table
CREATE TABLE Movies (
    MovieID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(255) NOT NULL,
    Director NVARCHAR(255),
    YearReleased INT,
    Description NVARCHAR(MAX) NOT NULL,
    GenreID INT NOT NULL,
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

-- Populate the Genres table
INSERT INTO Genres (GenreName) VALUES 
('Horror'),
('Fantasy'),
('Action'),
('Drama'),
('Science Fiction'),
('Comedy'),
('Thriller'),
('Adventure'),
('Romance'),
('Crime');

-- Populate the Movies table

INSERT INTO Movies (Title, Director, YearReleased, Description, GenreID)
VALUES 
('The Conjuring', 'James Wan', 2013, 'Paranormal investigators help a family terrorized by a dark presence.', 1),
('Harry Potter and the Sorcerer''s Stone', 'Chris Columbus', 2001, 'A boy learns he is a wizard and attends a magical school.', 2),
('Mad Max: Fury Road', 'George Miller', 2015, 'A post-apocalyptic chase through the desert.', 3),
('The Shawshank Redemption', 'Frank Darabont', 1994, 'A man wrongly imprisoned finds hope and friendship.', 4),
('Inception', 'Christopher Nolan', 2010, 'A thief enters dreams to steal secrets.', 5),
('The Hangover', 'Todd Phillips', 2009, 'A bachelor party in Vegas goes terribly wrong.', 6),
('Se7en', 'David Fincher', 1995, 'Two detectives hunt a killer who uses the seven deadly sins.', 7),
('Indiana Jones and the Last Crusade', 'Steven Spielberg', 1989, 'An archaeologist searches for the Holy Grail.', 8),
('The Notebook', 'Nick Cassavetes', 2004, 'A love story told through a lifetime.', 9),
('The Godfather', 'Francis Ford Coppola', 1972, 'The rise of a crime family in America.', 10);