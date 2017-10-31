/*
*                 CityPal Database
*        Code Written By Tim, Tom and Steven
*          Code Commented By Will and Jacob
*                Group number: 73
*/

-- Creates the CityPal database.
CREATE DATABASE CityPal;

-- Creates and sets up table for registered users, including
-- the salt and hash for secure passwords. Primary key is
-- username.
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_type` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `username` varchar(45) NOT NULL DEFAULT,
  `email` varchar(45) NOT NULL DEFAULT,
  `salt` varchar(512) DEFAULT NULL,
  `hash` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`username`)
); ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Creates table for items which professional users can
-- search through. Primary key is item_id.
DROP TABLE IF EXISTS `items_professionals`;
CREATE TABLE `items_professionals` (
  `item_id` int(11) NOT NULL,
  `type` text,
  `name` text,
  `street` text,
  `suburb` text,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`item_ID`)
); ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Creates table for items which student users can
-- search through. Primary key is item_id.
DROP TABLE IF EXISTS `items_students`;
CREATE TABLE items_students (
  `item_id` int(11) NOT NULL,
  `type` text,
  `name` text,
  `street` text,
  `suburb` text,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`item_ID`)
); ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Creates table for items which tourist users can
-- search through. Primary key is item_id.
DROP TABLE IF EXISTS `items_tourists`;
CREATE TABLE items_tourists (
  `item_id` int(11),
  `type` text,
  `name` text,
  `street` text,
  `suburb` text,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`item_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Creates table for reviews left by professional users
-- on items. Primary key is review_id and it auto-increments
-- for every review added.
DROP TABLE IF EXISTS `reviews_professionals`;
CREATE TABLE `reviews_professionals` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `review` text,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- Creates table for reviews left by student users
-- on items. Primary key is review_id and it auto-increments
-- for every review added.
DROP TABLE IF EXISTS `reviews_students`;
CREATE TABLE `reviews_students` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `review` text,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- Creates table for reviews left by tourist users
-- on items. Primary key is review_id and it auto-increments
-- for every review added.
DROP TABLE IF EXISTS `reviews_tourists`;
CREATE TABLE `reviews_tourists` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `review` text,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
