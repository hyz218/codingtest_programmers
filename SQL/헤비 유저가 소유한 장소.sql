SELECT ID, NAME, HOST_ID
FROM PLACES
where HOST_ID IN(
    SELECT HOST_ID from PLACES
    group by HOST_ID
    having count(*)>=2)