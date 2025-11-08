CREATE TABLE vaccine_schedules (		
species_id	VARCHAR (255)	,
vaccine_name	VARCHAR (255)	,
vaccine_category	VARCHAR (255)	,
vaccination_stage	VARCHAR (255)	,
administration_route	VARCHAR (255)	,
age_min_weeks	INTEGER	,
age_max_weeks	INTEGER	,
doses	INTEGER	,
dose_interval_min_weeks	INTEGER	,
dose_interval_max_weeks	INTEGER	,
dose_interval_years	INTEGER	,
recommended_frequency	VARCHAR (255)	,
disease_targeted	VARCHAR (255)	,
source	VARCHAR (255)	,
updated_on	TIMESTAMP DEFAULT CURRENT_TIMESTAMP	
);		