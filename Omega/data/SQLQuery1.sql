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

INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Sch�zka s klientem', '2024-04-22 09:00:00', 1);

-- P��klad 2: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Pracovn� setk�n�', '2024-04-23 14:30:00', 2);

-- P��klad 3: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Tr�nink', '2024-04-24 18:00:00', 1);


-- P��klad 4: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Sch�zka se zam�stnanci', '2024-04-24 10:00:00', 2);

-- P��klad 5: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Prezenta�n� workshop', '2024-04-25 13:00:00', 1);

-- P��klad 6: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Firemn� ve��rek', '2024-04-26 19:00:00', 2);

-- P��klad 7: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Pl�nov�n� strategie', '2024-04-27 15:30:00', 1);

-- P��klad 8: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Sch�zka s dodavatelem', '2024-04-28 11:00:00', 1);

-- P��klad 9: Dal�� ud�lost s jin�m popisem, datem a �asem a ID typu ud�losti
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Pravideln� t�mov� meeting', '2024-04-29 09:30:00', 1);

SELECT * FROM udalost WHERE CAST(datum_cas AS DATE) = '2024-04-24'  ORDER BY datum_cas;

SELECT udalost.*, typ_udalosti.typ_udalosti FROM udalost INNER JOIN typ_udalosti 
            ON udalost.id_typu = typ_udalosti.id_typu WHERE typ_udalosti.typ_udalosti = 'ukol' ORDER BY udalost.datum_cas;

INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Sch�zka s t�mem ohledn� nov�ho projektu', '2024-04-01 10:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Prezentace nov�ho produktu pro klienty', '2024-04-2 14:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Tr�nink zam�stnanc� na nov� software', '2024-04-03 09:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Setk�n� s vedouc�m na hodnocen� v�konu', '2024-04-04 11:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Team-buildingov� aktivita ve voln� p��rod�', '2024-04-05 12:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Firemn� ve��rek k oslav� �sp�ch�', '2024-04-30 18:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Testov�n� nov�ho prototypu produktu', '2024-04-06 10:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Workshop na t�ma kreativity a inovace', '2024-04-07 13:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Konference o budoucnosti pr�myslu', '2024-04-08 09:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Brainstorming nov�ch n�pad� na marketing', '2024-04-09 14:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('�kolen� nov�ch zam�stnanc�', '2024-04-08 10:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Audit bezpe�nosti informa�n�ho syst�mu', '2024-04-10 11:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Obchodn� jedn�n� s potenci�ln�m partnerem', '2024-04-11 15:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Marketingov� kampa� na soci�ln�ch s�t�ch', '2024-04-12 10:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Implementace nov�ho CRM syst�mu', '2024-04-13 09:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('�kolen� zam�stnanc� z oblasti komunikace', '2024-04-14 13:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Hodnocen� v�konu pracovn�k� za uplynul� obdob�', '2024-04-15 11:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Dobro�inn� akce ve prosp�ch m�stn� komunity', '2024-04-16 15:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Oslava dosa�en� obchodn�ho miln�ku', '2024-04-17 17:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('P�edn�ka o inovativn�ch technologi�ch', '2024-04-18 10:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Sch�zka s dodavatelem ohledn� dod�vky materi�lu', '2024-04-19 09:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Prezentace v�sledk� pr�zkumu trhu', '2024-04-20 14:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Tr�nink prodejn�ch dovednost�', '2024-04-21 11:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Setk�n� s investory ohledn� financov�n�', '2024-04-22 13:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Team-buildingov� akce ve venkovn�m centru', '2024-04-23 12:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Firemn� ve��rek k p��le�itosti v�ro�� spole�nosti', '2024-04-25 18:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Testov�n� beta verze softwaru', '2024-04-26 10:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Workshop na t�ma t�mov� spolupr�ce', '2024-04-27 14:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Konference o nov�ch trendech v odv�tv�', '2024-04-28 14:30:00', 1);