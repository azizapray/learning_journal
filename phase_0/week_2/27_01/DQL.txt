-- Mengambil semua data
SELECT * FROM teachers;

-- Mengambil kolom first_name, school, salary
SELECT first_name, school, salary
FROM teachers;

-- Mengambil data dimana school=MIT/Standford University
SELECT *
FROM teachers
WHERE school='MIT' or school='Standford University';
	-- atau
SELECT *
FROM teachers
WHERE school in ('mit', 'Standford University');

-- Mengambil data dengan query data yang lebih spesifik
SELECT *
FROM teachers
WHERE BINARY school in ('mit', 'Standford University');

-- Mencari jumlah guru dimana school=MIT/Standford University
SELECT COUNT(*)
FROM teachers
WHERE school in ('mit', 'standford university');
	-- atau
SELECT COUNT(*) AS "Jumlah Guru"
FROM teachers
WHERE school in ('mit', 'standford university');

-- Mengambil data dimana school=MIT/Standford University dan diurutkan berdasarkan gaji
SELECT *
FROM teachers
WHERE school in ('MIT', 'Standford University')
ORDER by salary DESC;	-- DESC atau ASC

-- Mencari tahu berapa banyak sekolah di database
SELECT DISTINCT school
FROM teachers;

SELECT COUNT(DISTINCT school)
FROM teachers;