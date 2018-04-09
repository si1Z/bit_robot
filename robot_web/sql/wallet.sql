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

 Date: 04/08/2018 19:10:41 PM
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
  PRIMARY KEY (`wallet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
