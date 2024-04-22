use Omega;

CREATE TABLE typ_udalosti (
    id_typu int identity(1,1) primary key,
    typ_udalosti VARCHAR(50) NOT NULL
);

CREATE TABLE udalost (
    id_udalosti INT PRIMARY KEY IDENTITY(1,1),
    popis NVARCHAR(MAX) NOT NULL,
    datum_cas DATETIME NOT NULL,
    id_typu INT,
    FOREIGN KEY (id_typu) REFERENCES typ_udalosti(id_typu)
);

insert into typ_udalosti(typ_udalosti)
values ('ukol'),
('udalost');