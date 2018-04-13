/*
 Navicat Premium Data Transfer

 Source Server         : 本地局域网
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : 127.0.0.1
 Source Database       : telegram_robot

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : utf-8

 Date: 04/13/2018 17:05:49 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `wallet`
-- ----------------------------
DROP TABLE IF EXISTS `wallet`;
CREATE TABLE `wallet` (
  `wallet` varchar(512) NOT NULL,
  `code` varchar(256) DEFAULT NULL,
  `user_id` int(15) DEFAULT NULL,
  `first_name` varchar(256) DEFAULT NULL,
  `last_name` varchar(256) DEFAULT NULL,
  `num` int(11) unsigned zerofill NOT NULL DEFAULT '00000000000',
  PRIMARY KEY (`wallet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
