SELECT MCDP_CD AS '진료과 코드', COUNT(MCDP_CD) AS '5월예약건수'
FROM APPOINTMENT
WHERE SUBSTR(APNT_YMD, 6, 2) = 05
GROUP BY MCDP_CD 
ORDER BY 2 ASC, 1 ASC;