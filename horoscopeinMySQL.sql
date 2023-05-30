/*1) We can use Inner join*/
/*If our table exists we delete*/
drop table if exists `horoscope`;

/*Create new table with id,sign,date_start,date_end cloumns*/
CREATE TABLE IF NOT EXISTS sys.`horoscope` (
    `id` INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `sign` VARCHAR(255) NOT NULL UNIQUE,
    `date_start` VARCHAR(5),
    `date_end` VARCHAR(5)
);
CREATE INDEX `horoscope_idx_1` ON `horoscope`(`date_start`, `date_end`);

/*Add values for columns*/
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Aries', '03-21', '04-20');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Taurus', '04-21', '05-20');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Gemini', '05-22', '06-21');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Cancer', '06-22', '07-22');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Leo', '07-23', '08-23');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Virgin', '08-24', '09-22');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Libra', '08-23', '10-22');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Scorpio', '10-23', '11-21');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Sagittarius', '11-22', '12-21');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Capricorn', '12-22', '01-20');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Aquarius', '01-21', '02-19');
INSERT INTO `horoscope` (`sign`, `date_start`, `date_end`) VALUES ('Pisces', '02-20', '03-20');

/*Start use inner join for joining our tables "nefer" and "horoscope"*/
select *
from horoscope where date_start > date_end
;

select lastname,firstname,birthdate,sign
from nefer n
inner join horoscope h
where (h.date_start > h.date_end 
       and n.birthdate between str_to_date(concat(year(birthdate)-1, h.date_start),'%Y%m-%d') and str_to_date(concat(year(birthdate), h.date_end),'%Y%m-%d')
      )
or (h.date_start < h.date_end 
    and n.birthdate between str_to_date(concat(year(birthdate), h.date_start),'%Y%m-%d') and str_to_date(concat(year(birthdate), h.date_end),'%Y%m-%d')
   );
 /*Select just showing only lastname,fistname,birthdate and sign columns our table*/  
   
   
   /*2)This is general way for using case in our 'nefer' table */
   SELECT 
    CASE 
        WHEN (MONTH(birthdate) = 1 AND DAY(birthdate) <= 19) OR (MONTH(birthdate) = 12 AND DAY(birthdate) >= 22) THEN 'Capricorn'
        WHEN (MONTH(birthdate) = 1 AND DAY(birthdate) >= 20) OR (MONTH(birthdate) = 2 AND DAY(birthdate) <= 18) THEN 'Aquarius'
        WHEN (MONTH(birthdate) = 2 AND DAY(birthdate) >= 19) OR (MONTH(birthdate) = 3 AND DAY(birthdate) <= 20) THEN 'Pisces'
        WHEN (MONTH(birthdate) = 3 AND DAY(birthdate) >= 21) OR (MONTH(birthdate) = 4 AND DAY(birthdate) <= 19) THEN 'Aries'
        WHEN (MONTH(birthdate) = 4 AND DAY(birthdate) >= 20) OR (MONTH(birthdate) = 5 AND DAY(birthdate) <= 20) THEN 'Taurus'
        WHEN (MONTH(birthdate) = 5 AND DAY(birthdate) >= 21) OR (MONTH(birthdate) = 6 AND DAY(birthdate) <= 20) THEN 'Gemini'
        WHEN (MONTH(birthdate) = 6 AND DAY(birthdate) >= 21) OR (MONTH(birthdate) = 7 AND DAY(birthdate) <= 22) THEN 'Cancer'
        WHEN (MONTH(birthdate) = 7 AND DAY(birthdate) >= 23) OR (MONTH(birthdate) = 8 AND DAY(birthdate) <= 22) THEN 'Leo'
        WHEN (MONTH(birthdate) = 8 AND DAY(birthdate) >= 23) OR (MONTH(birthdate) = 9 AND DAY(birthdate) <= 22) THEN 'Virgo'
        WHEN (MONTH(birthdate) = 9 AND DAY(birthdate) >= 23) OR (MONTH(birthdate) = 10 AND DAY(birthdate) <= 22) THEN 'Libra'
        WHEN (MONTH(birthdate) = 10 AND DAY(birthdate) >= 23) OR (MONTH(birthdate) = 11 AND DAY(birthdate) <= 21) THEN 'Scorpio'
        WHEN (MONTH(birthdate) = 11 AND DAY(birthdate) >= 22) OR (MONTH(birthdate) = 12 AND DAY(birthdate) <= 21) THEN 'Sagittarius'
     END AS horoscope_sign, firstname,lastname
FROM 
   sys.`nefer`;
   /*We see only fistname,lastname and horoscope_sign columns our table*
