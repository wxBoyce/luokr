DROP DATABASE IF EXISTS `lk`;
CREATE DATABASE `lk` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `lk`;
SET NAMES utf8;
SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

-- Table: users
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`(
    `user_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_auid` VARCHAR(64) NOT NULL DEFAULT '',
	`user_name` VARCHAR(64) NOT NULL,
    `user_salt` CHAR(8) NOT NULL,
    `user_pswd` CHAR(32) NOT NULL,
    `user_perm` INT(10) NOT NULL DEFAULT 0,
    `user_mail` VARCHAR(128) NOT NULL,
	`user_sign` VARCHAR(256) NOT NULL DEFAULT '',
    `user_logo` VARCHAR(512) NOT NULL DEFAULT '',
    `user_meta` TEXT NOT NULL,
    `user_ctms` INT(10) NOT NULL,
    `user_utms` INT(10) NOT NULL,
    `user_atms` INT(10) NOT NULL,
    UNIQUE (`user_name` ASC),
    UNIQUE (`user_mail` ASC)
)DEFAULT CHARSET = UTF8;

INSERT INTO users(user_id, user_name, user_salt, user_pswd, user_perm, user_mail, user_meta, user_ctms, user_utms, user_atms)
values(1, 'admin', 'asdflkjh', 'b6ce17f5578131e2997ccfb99dcc3500', 2147483647, '', '', 1374486661, 1374786660, 1374765138);


--Table: files
DROP TABLE IF EXISTS `files`;
CREATE TABLE `files`(
    `file_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `file_hash` CHAR(32),
	  `file_base` VARCHAR(128),
    `file_path` VARCHAR(512),
    `file_type` VARCHAR(128),
    `file_memo` VARCHAR(512),
    `file_ctms` INT(10) NOT NULL
)DEFAULT CHARSET = UTF8;