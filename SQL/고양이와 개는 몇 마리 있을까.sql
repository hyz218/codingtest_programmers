SELECT ANIMAL_TYPE,count(*) from animal_ins
group by ANIMAL_TYPE
having ANIMAL_TYPE="cat" or ANIMAL_TYPE="dog"
order by ANIMAL_TYPE