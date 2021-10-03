SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS
where ANIMAL_TYPE='Dog' and lower(NAME) like '%el%'
order by NAME