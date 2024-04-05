CREATE DATABASE IF NOT EXISTS pipeline_db;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`videos`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255),
title VARCHAR(255),
link VARCHAR(255),
views INTEGER,
video_time VARCHAR(255),
time_online VARCHAR(255),
extraction_date DATETIME NOT NULL,
primary key(id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`canais`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255) UNIQUE,
about VARCHAR(255) UNIQUE,
subscriptions INTEGER,
total_videos INTEGER,
total_views INTEGER,
creation_date DATETIME,
channel_location VARCHAR(255)
primary key(id)
)ENGINE=INNODB;