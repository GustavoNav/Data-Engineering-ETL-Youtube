CREATE DATABASE IF NOT EXISTS pipeline_db;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`videos`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255),
title VARCHAR(255),
channel_link VARCHAR(255),
video_link VARCHAR(255),
views BIGINT,
video_time VARCHAR(255),
time_online VARCHAR(255),
extraction_date DATETIME NOT NULL,
primary key(id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`videos_detalhes`(
id BIGINT NOT NULL AUTO_INCREMENT,
video_id BIGINT,
channel VARCHAR(255),
likes VARCHAR(255),
total_comments VARCHAR(255),
tags TEXT,
extraction_date DATETIME NOT NULL,
primary key(id),
FOREIGN KEY (`video_id`) REFERENCES `pipeline_db`.`videos`(`id`)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`canais_sobre`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255) UNIQUE,
about TEXT,
creation_date DATETIME,
channel_location VARCHAR(255),
extraction_date DATETIME NOT NULL,
primary key(id)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`canais_metricas`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255),
subscriptions VARCHAR(255),
total_videos INTEGER,
total_views BIGINT,
extraction_date DATETIME NOT NULL,
primary key(id)
)ENGINE=INNODB;
