SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A left join ANIMAL_OUTS B
on A.ANIMAL_ID = B.ANIMAL_ID
where A.DATETIME > B.DATETIME
order by A.DATETIME