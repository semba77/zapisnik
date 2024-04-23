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
VALUES ('Schùzka s klientem', '2024-04-22 09:00:00', 1);

-- Pøíklad 2: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Pracovní setkání', '2024-04-23 14:30:00', 2);

-- Pøíklad 3: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Trénink', '2024-04-24 18:00:00', 1);


-- Pøíklad 4: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Schùzka se zamìstnanci', '2024-04-24 10:00:00', 2);

-- Pøíklad 5: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Prezentaèní workshop', '2024-04-25 13:00:00', 1);

-- Pøíklad 6: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Firemní veèírek', '2024-04-26 19:00:00', 2);

-- Pøíklad 7: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Plánování strategie', '2024-04-27 15:30:00', 1);

-- Pøíklad 8: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Schùzka s dodavatelem', '2024-04-28 11:00:00', 1);

-- Pøíklad 9: Další událost s jiným popisem, datem a èasem a ID typu události
INSERT INTO udalost (popis, datum_cas, id_typu)
VALUES ('Pravidelný týmový meeting', '2024-04-29 09:30:00', 1);

SELECT * FROM udalost WHERE CAST(datum_cas AS DATE) = '2024-04-24'  ORDER BY datum_cas;

SELECT udalost.*, typ_udalosti.typ_udalosti FROM udalost INNER JOIN typ_udalosti 
            ON udalost.id_typu = typ_udalosti.id_typu WHERE typ_udalosti.typ_udalosti = 'ukol' ORDER BY udalost.datum_cas;

INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Schùzka s týmem ohlednì nového projektu', '2024-04-01 10:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Prezentace nového produktu pro klienty', '2024-04-2 14:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Trénink zamìstnancù na nový software', '2024-04-03 09:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Setkání s vedoucím na hodnocení výkonu', '2024-04-04 11:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Team-buildingová aktivita ve volné pøírodì', '2024-04-05 12:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Firemní veèírek k oslavì úspìchù', '2024-04-30 18:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Testování nového prototypu produktu', '2024-04-06 10:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Workshop na téma kreativity a inovace', '2024-04-07 13:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Konference o budoucnosti prùmyslu', '2024-04-08 09:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Brainstorming nových nápadù na marketing', '2024-04-09 14:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Školení nových zamìstnancù', '2024-04-08 10:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Audit bezpeènosti informaèního systému', '2024-04-10 11:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Obchodní jednání s potenciálním partnerem', '2024-04-11 15:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Marketingová kampaò na sociálních sítích', '2024-04-12 10:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Implementace nového CRM systému', '2024-04-13 09:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Školení zamìstnancù z oblasti komunikace', '2024-04-14 13:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Hodnocení výkonu pracovníkù za uplynulé období', '2024-04-15 11:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Dobroèinná akce ve prospìch místní komunity', '2024-04-16 15:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Oslava dosažení obchodního milníku', '2024-04-17 17:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Pøednáška o inovativních technologiích', '2024-04-18 10:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Schùzka s dodavatelem ohlednì dodávky materiálu', '2024-04-19 09:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Prezentace výsledkù prùzkumu trhu', '2024-04-20 14:00:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Trénink prodejních dovedností', '2024-04-21 11:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Setkání s investory ohlednì financování', '2024-04-22 13:00:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Team-buildingová akce ve venkovním centru', '2024-04-23 12:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Firemní veèírek k pøíležitosti výroèí spoleènosti', '2024-04-25 18:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Testování beta verze softwaru', '2024-04-26 10:30:00', 2);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Workshop na téma týmové spolupráce', '2024-04-27 14:30:00', 1);
INSERT INTO udalost(popis, datum_cas, id_typu) VALUES ('Konference o nových trendech v odvìtví', '2024-04-28 14:30:00', 1);