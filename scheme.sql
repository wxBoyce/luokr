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


--Table: post_terms
CREATE TABLE post_terms(
    `post_id` INT,
    `term_id` INT
)DEFAULT CHARSET = UTF8;

--Table: posts
CREATE TABLE posts(
     `post_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
     `user_id` INT DEFAULT 0,
     `post_title` VARCHAR(128),
     `post_descp` VARCHAR(256),
     `post_author` VARCHAR(128),
     `post_source` VARCHAR(1024),
     `post_summary` TEXT,
     `post_content` TEXT,
     `post_type` INT(10) DEFAULT 0,
     `post_ctms` INT(10) NOT NULL,
     `post_utms` INT(10) NOT NULL,
     `post_ptms` INT(10) NOT NULL,
     `post_refc` INT(10) DEFAULT 0,
     `post_rank` INT(10) DEFAULT 99,
     `post_plus` INT(10) DEFAULT 0,
     `post_mins` INT(10) DEFAULT 0,
     `post_stat` INT(3) NOT NULL DEFAULT 0
)DEFAULT CHARSET = UTF8;

--Index: idx_postId_termId
CREATE UNIQUE INDEX idx_postId_termId ON post_terms(
    `post_id`,
    `term_id`
);

-- Index: idx_userId_postPtms_postStat
CREATE INDEX idx_userId_postPtms_postStat ON posts (
    `user_id`,
    `post_ptms`,
    `post_stat`
);


-- Index: idx_postId_postPtms_postStat
CREATE INDEX idx_postId_postPtms_postStat ON posts (
    `post_id`,
    `post_ptms`,
    `post_stat`
);


-- Index: idx_postPtms_postStat
CREATE INDEX idx_postPtms_postStat ON posts (
    `post_ptms`,
    `post_stat`
);


-- Index: idx_postPtms_postStat_postRank
CREATE INDEX idx_postPtms_postStat_postRank ON posts (
    `post_ptms`,
    `post_stat`,
    `post_rank`
);


-- Index: idx_postPtms_postStat_postRefc
CREATE INDEX idx_postPtms_postStat_postRefc ON posts (
    `post_ptms`,
    `post_stat`,
    `post_refc`
);

--Table: talks
CREATE TABLE talks(
     `talk_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
     `post_id` INT,
     `user_id` INT NOT NULL,
     `user_ip` VARCHAR(39),
     `talk_ptid` INT NOT NULL DEFAULT 0,
     `user_name` VARCHAR(64),
     `user_mail` VARCHAR(64),
     `talk_text` TEXT,
     `talk_rank` INT(10) NOT NULL DEFAULT 100,
     `talk_plus` INT(10) NOT NULL DEFAULT 0,
     `talk_mins` INT(10) NOT NULL DEFAULT 0,
     `talk_ctms` INT(10) NOT NULL,
     `talk_utms` INT(10) NOT NULL
)DEFAULT CHARSET = UTF8;

-- Index: idx_talkRank_talkId
CREATE INDEX idx_talkRank_talkId ON talks (
    `talk_rank`,
    `talk_id`
);

-- Index: idx_postId_talkRank_talkId
CREATE INDEX idx_postId_talkRank_talkId ON talks (
    `post_id`,
    `talk_rank`,
    `talk_id`
);


--Table: mails
CREATE TABLE mails(
     `mail_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
     `user_ip` VARCHAR(39),

     `user_name` VARCHAR(64),
     `user_mail` VARCHAR(64) NOT NULL,
     `mail_text` TEXT,

     `mail_stat` INT(1) DEFAULT 0,
     `mail_ctms` INT(10) NOT NULL,
     `mail_utms` INT(10) NOT NULL
)DEFAULT CHARSET = UTF8;

-- Index: idx_mailStat_mailId
CREATE INDEX idx_mailStat_mailId ON mails (
    `mail_stat`,
    `mail_id`
);


-- Table: alogs
CREATE TABLE alogs(
     `alog_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
     `user_id` INT DEFAULT 0,

     `user_ip` VARCHAR(39),
     `user_name` VARCHAR(64),
     `alog_text` TEXT,

     `alog_data` TEXT,
     `alog_ctms` INT(10) NOT NULL
)DEFAULT CHARSET = UTF8;


--Table: confs
CREATE TABLE confs(
     `conf_name` VARCHAR(32) NOT NULL UNIQUE,
     `conf_vals` TEXT,
     `conf_ctms` INT(10)
)DEFAULT CHARSET = UTF8;