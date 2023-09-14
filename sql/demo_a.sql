-- MariaDB dump 10.19  Distrib 10.7.3-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: qryhqkim
-- ------------------------------------------------------
-- Server version	10.7.3-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activityData`
--

DROP TABLE IF EXISTS `activityData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activityData` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schoolID` int(5) NOT NULL COMMENT '学校id',
  `uuid` int(11) NOT NULL COMMENT '活动id',
  `activitytime` char(30) NOT NULL COMMENT '活动时间',
  `boutique` int(20) NOT NULL,
  `boutiqueStr` char(20) NOT NULL,
  `catalog2name` char(20) NOT NULL COMMENT '活动类型',
  `imageUrl` text NOT NULL COMMENT '活动图片地址',
  `name` char(50) NOT NULL COMMENT '活动名称',
  `status` int(11) NOT NULL,
  `statusText` char(10) NOT NULL COMMENT '活动状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `id_2` (`id`),
  KEY `uuid` (`uuid`),
  KEY `schoolID` (`schoolID`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activityData`
--

LOCK TABLES `activityData` WRITE;
/*!40000 ALTER TABLE `activityData` DISABLE KEYS */;
INSERT INTO `activityData` VALUES
(3,10001,8437050,'2023.08.22 至 2023.08.24',0,'','思想成长','http://image.5idream.net/45386726/1691893776816_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','不“七”而遇 满心欢“夕”',6,'已结束'),
(4,10001,8436142,'2023.08.09 至 2023.08.10',0,'','文艺体育','http://image.5idream.net/45384346/1691457622374_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','二十四节气之立秋',6,'已结束'),
(5,10001,8435428,'2023.08.06 至 2023.08.11',0,'','技能特长','http://image.5idream.net/45385259/1691052587405_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','“易”起去旅行',6,'已结束'),
(6,10001,8434837,'2023.08.01 至 2023.08.02',0,'','思想成长','http://image.5idream.net/45387693/1690808513151_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','建军节',6,'已结束'),
(7,10001,8432574,'2023.07.27 至 2023.07.30',0,'','技能特长','http://image.5idream.net/45384985/1690024067152_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','暑期指南，我为你录',6,'已结束'),
(8,10001,8426330,'2023.07.15 至 2023.07.22',0,'','技能特长','http://image.5idream.net/45384985/1689143523717_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','舌尖上的家乡菜',6,'已结束'),
(9,10001,8418521,'2023.07.07 至 2023.07.08',0,'','技能特长','http://image.5idream.net/45387693/1688625564245_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','二十四节气之一，小暑',6,'已结束'),
(10,10001,8417340,'2023.07.08 至 2023.07.11',0,'','技能特长','http://image.5idream.net/45385107/1688558307815_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','风尘仆仆，终有归途',6,'已结束'),
(11,10001,8416783,'2023.07.05 至 2023.07.05',0,'','实践实习','http://image.5idream.net/45384995/1688543295604_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募志愿者',6,'已结束'),
(12,10001,8413615,'2023.07.04 至 2023.07.04',0,'','技能特长','http://image.5idream.net/40975129/1688390692117_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','“三下乡”启动仪式志愿者招募',6,'已结束'),
(13,10001,8413539,'2023.07.04 至 2023.07.04',0,'','实践实习','http://image.5idream.net/45387862/1688388981124_3?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募志愿者',6,'已结束'),
(14,10001,8413453,'2023.07.04 至 2023.07.04',0,'','实践实习','http://image.5idream.net/45386375/1688387099318_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募志愿者',6,'已结束'),
(15,10001,8413375,'2023.07.04 至 2023.07.04',0,'','实践实习','http://image.5idream.net/45383273/1688357430284_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','7.4志愿者招募',6,'已结束'),
(16,10001,8413288,'2023.07.04 至 2023.07.04',0,'','实践实习','http://image.5idream.net/45384346/1688383895506_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','“三下乡”出征仪式',6,'已结束'),
(17,10001,8412171,'2023.07.03 至 2023.07.03',0,'','实践实习','http://image.5idream.net/45383273/1688357430284_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','7.3互联网+项目志愿者招募',6,'已结束'),
(18,10001,8411712,'2023.07.03 至 2023.07.03',0,'','技能特长','http://image.5idream.net/45386410/1688343796990_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','行政楼202志愿者',6,'已结束'),
(19,10001,8411640,'2023.07.03 至 2023.07.03',0,'','实践实习','http://image.5idream.net/45386410/1688316463797_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','行政楼202志愿者',6,'已结束'),
(20,10001,8411500,'2023.07.03 至 2023.07.03',0,'','技能特长','http://image.5idream.net/AF7993D1-57CA-4AB8-B0D8-65E7B9DB7701?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募志愿者',6,'已结束'),
(21,10001,8408151,'2023.07.02 至 2023.07.02',0,'','实践实习','http://image.5idream.net/45384891/1688184297298_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','活动招募志愿者',6,'已结束'),
(22,10001,8403957,'2023.06.30 至 2023.06.30',0,'','创新创业','http://image.5idream.net/45387545/1688031149930_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','《中国创业者》线上观影',6,'已结束'),
(23,10001,8403062,'2023.06.30 至 2023.07.22',0,'','文艺体育','http://image.5idream.net/41426384/1688014634458_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','资助网络竞赛答题活动',6,'已结束'),
(24,10001,8400401,'2023.06.29 至 2023.06.29',0,'','实践实习','http://image.5idream.net/72F0F547-BE0F-42CC-BB8F-55D695608A4F?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','物资搬运志愿者招募',6,'已结束'),
(25,10001,8399375,'2023.06.29 至 2023.06.30',0,'','创新创业','http://image.5idream.net/45383078/1687931271564_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','给第九届“互联网＋”大赛送祝福',6,'已结束'),
(26,10001,8399308,'2023.06.28 至 2023.06.28',0,'','实践实习','http://image.5idream.net/41426384/1687930720230_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','6.28毕业生档案志愿者招募活动',6,'已结束'),
(27,10001,8394937,'2023.06.29 至 2023.06.30',0,'','思想成长','http://image.5idream.net/41151473/1687841631809_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','信息素养教育与文献资源利用培训讲座',6,'已结束'),
(28,10001,8391956,'2023.06.27 至 2023.06.30',0,'','实践实习','http://image.5idream.net/45385673/1687775653810_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','和展板合影签字活动',6,'已结束'),
(29,10001,8391267,'2023.06.27 至 2023.06.27',0,'','实践实习','http://image.5idream.net/45387693/1687769582931_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','“心理问题的识别与预防”讲座',6,'已结束'),
(30,10001,8389853,'2023.06.27 至 2023.06.27',0,'','实践实习','http://image.5idream.net/45383480/1687756864873_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募志愿者',6,'已结束'),
(31,10001,8389055,'2023.06.26 至 2023.06.26',2,'校级精品','创新创业','http://image.5idream.net/45385916/1687751029993_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','行政楼205志愿者',6,'已结束'),
(32,10001,8389021,'2023.06.26 至 2023.06.26',2,'校级精品','创新创业','http://image.5idream.net/45385916/1687750705585_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','行政楼205志愿者',6,'已结束'),
(33,10001,8387765,'2023.06.28 至 2023.06.28',0,'','实践实习','http://image.5idream.net/45383473/1687706562112_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','定格夏天，幸福醉心',6,'已结束'),
(34,10001,8386825,'2023.06.26 至 2023.06.26',0,'','实践实习','http://image.5idream.net/45386343/1687692054243_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','BIM协会6.25志愿者',6,'已结束'),
(35,10001,8384649,'2023.06.29 至 2023.06.30',0,'','实践实习','http://image.5idream.net/41151473/1687663831260_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','“笔墨传香 书写经典”线下抄书活动',6,'已结束'),
(36,10001,8384619,'2023.07.01 至 2023.07.02',0,'','实践实习','http://image.5idream.net/41151473/1687663020033_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','“笔墨传香 书写经典”抄书活动',6,'已结束'),
(37,10001,8383194,'2023.06.25 至 2023.06.25',0,'','实践实习','http://image.5idream.net/45387699/1687612631674_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','班长联盟最强大脑颁奖仪式',6,'已结束'),
(38,10001,8382114,'2023.06.25 至 2023.06.25',0,'','创新创业','http://image.5idream.net/45387920/1687587594029_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','搬运物资志愿者',6,'已结束'),
(39,10001,8381754,'2023.06.24 至 2023.06.25',0,'','创新创业','http://image.5idream.net/45383833/1687575763855_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','创新大发明',6,'已结束'),
(40,10001,8380933,'2023.06.25 至 2023.06.28',0,'','实践实习','http://image.5idream.net/45387602/1687514716604_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','花开满盛夏 毕业致青春',6,'已结束'),
(44,10001,8415562,'2023.07.07 至 2023.09.01',0,'','实践实习','http://image.5idream.net/45385402/1688477350096_6?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','我为暑假借本书',5,'进行中'),
(45,10001,8443472,'2023.08.30 至 2023.08.31',0,'','思想成长','http://image.5idream.net/45384513/1693276271446_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','中元节',5,'进行中'),
(47,10001,8453909,'2023.09.03 至 2023.09.03',0,'','实践实习','http://image.5idream.net/5C60AA1E-59FF-4874-A501-85B169889F04?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者活动',2,'规划中'),
(48,10001,8455780,'2023.09.04 至 2023.09.04',0,'','实践实习','http://image.5idream.net/45385339/1693756082662_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(53,10001,8452374,'2023.09.07 至 2023.09.28',0,'','文艺体育','http://image.5idream.net/45383273/1693652238482_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','电气系2023迎新晚会',3,'报名中'),
(54,10001,8460444,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45386375/1693889163815_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','冶金系迎新生活动',2,'规划中'),
(55,10001,8460557,'2023.09.08 至 2023.09.28',0,'','文艺体育','http://image.5idream.net/45387699/1693891051785_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','计算机应用系2023迎新晚会招募',2,'规划中'),
(56,10001,8461348,'2023.09.05 至 2023.09.05',0,'','实践实习','http://image.5idream.net/45385125/1693904842563_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(57,10001,8461054,'2023.09.07 至 2023.09.07',0,'','实践实习','http://image.5idream.net/1231693912264547?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','9.7上午法治主题宣讲活动志愿者（仅招募男生）',2,'规划中'),
(58,10001,8460982,'2023.09.07 至 2023.09.07',0,'','实践实习','http://image.5idream.net/45387977/1693898886877_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','9.7上午法治主题宣讲活动志愿者（仅招募女生）',2,'规划中'),
(59,10001,8462189,'2023.09.06 至 2023.09.08',0,'','文艺体育','http://image.5idream.net/45383428/1693919027441_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','电气系手绘海报',2,'规划中'),
(60,10001,8463175,'2023.09.06 至 2023.09.07',0,'','思想成长','http://image.5idream.net/41181980/1693964694319_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募志愿者',2,'规划中'),
(61,10001,8463680,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384891/1693974083163_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募23级迎新活动志愿者',2,'规划中'),
(62,10001,8463793,'2023.09.06 至 2023.09.06',0,'','实践实习','http://image.5idream.net/45385125/1693975585493_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(63,10001,8464124,'2023.09.06 至 2023.09.06',0,'','创新创业','http://image.5idream.net/45385125/1693982227945_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',3,'报名中'),
(64,10001,8465062,'2023.09.07 至 2023.09.07',0,'','创新创业','http://image.5idream.net/45385125/1694000077295_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','9月7日  8：30-12：30图书整理志愿者',2,'规划中'),
(65,10001,8465160,'2023.09.07 至 2023.09.07',0,'','创新创业','http://image.5idream.net/45385125/1694002135804_5?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','9月7日  18：00-22：00图书整理志愿者',2,'规划中'),
(66,10001,8465135,'2023.09.07 至 2023.09.07',0,'','创新创业','http://image.5idream.net/45385125/1694001542041_3?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','9月7日  14：30-17：30图书整理志愿者',2,'规划中'),
(67,10001,8465418,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384262/1694006340066_12?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','2023迎新志愿者7',2,'规划中'),
(68,10001,8465407,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384262/1694006153131_11?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','2023迎新志愿者6',2,'规划中'),
(69,10001,8465402,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384262/1694005979071_8?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','2023迎新志愿者5',2,'规划中'),
(70,10001,8465394,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384262/1694005807872_6?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','2023迎新志愿者4',2,'规划中'),
(71,10001,8465385,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384262/1694005620928_4?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','2023迎新志愿者3',2,'规划中'),
(72,10001,8465374,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384262/1694005398836_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','2023迎新志愿者2',2,'规划中'),
(73,10001,8465352,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45384262/1694004933426_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','2023迎新志愿者',2,'规划中'),
(74,10001,8466438,'2023.09.07 至 2023.09.07',0,'','技能特长','http://image.5idream.net/C0938DF1-1D67-4751-8441-316E482592A0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(75,10001,8467034,'2023.09.07 至 2023.09.07',0,'','创新创业','http://image.5idream.net/45385125/1694064362908_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','9月7日14：30图书整理',2,'规划中'),
(76,10001,8468007,'2023.09.08 至 2023.09.08',0,'','创新创业','http://image.5idream.net/4339DA50-3436-43CA-BA90-BBB8FB3BCD1F?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(77,10001,8468919,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/40975129/1694099367287_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','土木系2023迎新志愿者招募',2,'规划中'),
(78,10001,8469790,'2023.09.08 至 2023.09.08',0,'','创新创业','http://image.5idream.net/B45E5D5B-B29C-48CA-92FC-2CCC4ED33388?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(79,10001,8470239,'2023.09.08 至 2023.09.08',0,'','技能特长','http://image.5idream.net/8EC48922-D55C-494D-9D71-381802A26E45?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','搬运凳子',2,'规划中'),
(80,10001,8471112,'2023.09.09 至 2023.09.09',0,'','实践实习','http://image.5idream.net/40975129/1694172197932_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','搬运桌子志愿者',2,'规划中'),
(81,10001,8472222,'2023.09.10 至 2023.09.11',0,'','技能特长','http://image.5idream.net/45383099/1694231803561_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','永怀感恩心，喜迎教师节',2,'规划中'),
(82,10001,8472734,'2023.09.11 至 2023.09.16',0,'','思想成长','http://image.5idream.net/45386695/1694247438796_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','师泽如山，感念有你',2,'规划中'),
(83,10001,8472849,'2023.09.12 至 2023.09.12',0,'','实践实习','http://image.5idream.net/45386695/1694248673298_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(84,10001,8472670,'2023.09.10 至 2023.09.13',0,'','思想成长','http://image.5idream.net/1231694251616403?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','桃李不言下自成蹊',2,'规划中'),
(85,10001,8473741,'2023.09.10 至 2023.09.10',0,'','实践实习','http://image.5idream.net/45385339/1694279670768_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','师情难忘，观“张桂梅”纪录片',2,'规划中'),
(86,10001,8474533,'2023.09.10 至 2023.09.10',0,'','创新创业','http://image.5idream.net/455E005F-644C-46DF-B899-5BD78D360A17?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(87,10001,8473744,'2023.09.12 至 2023.09.12',0,'','思想成长','http://image.5idream.net/45385189/1694279060560_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','尊师爱生风尚美',2,'规划中'),
(88,10001,8475168,'2023.09.10 至 2023.09.10',0,'','创新创业','http://image.5idream.net/61E03AF8-7369-47FA-8001-F4B59B05C046?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(89,10001,8475217,'2023.09.10 至 2023.09.10',0,'','技能特长','http://image.5idream.net/E5DC5AD3-7D63-46F8-963E-FB97803F676E?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','搬运易拉宝',2,'规划中'),
(90,10001,8475212,'2023.09.10 至 2023.09.10',0,'','创新创业','http://image.5idream.net/AAF8037E-B0E2-4A81-95E6-1A49894807E4?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(91,10001,8476462,'2023.09.11 至 2023.09.11',0,'','技能特长','http://image.5idream.net/39C3459B-3BB8-4C56-8EF5-C317853909EE?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','体育馆二楼整理场地',2,'规划中'),
(92,10001,8478157,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/40F5A18E-FAFF-4379-B95E-5FC2474DC37F?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(93,10001,8478286,'2023.09.13 至 2023.09.13',0,'','创新创业','http://image.5idream.net/7E7B2122-40D1-4224-A4A3-97A76BF9417B?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(94,10001,8480869,'2023.09.11 至 2023.09.11',0,'','实践实习','http://image.5idream.net/45383228/1694436955631_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','体育馆收场志愿者',2,'规划中'),
(95,10001,8481000,'2023.09.12 至 2023.09.12',0,'','实践实习','http://image.5idream.net/45383228/1694438090319_1?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','体育馆志愿者',2,'规划中'),
(96,10001,8481459,'2023.09.12 至 2023.09.12',0,'','创新创业','http://image.5idream.net/45387920/1694444159201_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','9.12整理会场志愿者',3,'报名中'),
(97,10001,8481757,'2023.09.12 至 2023.09.12',0,'','思想成长','http://image.5idream.net/45386695/1694450013235_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','体育馆二楼整理场地',2,'规划中'),
(98,10001,8481859,'2023.09.12 至 2023.09.12',0,'','创新创业','http://image.5idream.net/45383237/1694476615019_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','招募志愿者',2,'规划中'),
(99,10001,8482582,'2023.09.12 至 2023.09.12',0,'','实践实习','http://image.5idream.net/8704C672-1DF2-4BFF-A81D-AE90DBF05EB6?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','志愿者招募',2,'规划中'),
(100,10001,8483910,'2023.09.13 至 2023.09.13',0,'','实践实习','http://image.5idream.net/45386343/1694500758667_2?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','大学生社团管理中心9.13志愿者',2,'规划中'),
(101,10001,8483878,'2023.09.12 至 2023.09.12',0,'','实践实习','http://image.5idream.net/45386343/1694500423661_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','大学生社团管理中心9.12志愿者',2,'规划中'),
(102,10001,8487444,'2023.09.15 至 2023.09.27',0,'','技能特长','http://image.5idream.net/40975129/1694566648579_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','迎新晚会舞蹈志愿者招募',2,'规划中'),
(103,10001,8489746,'2023.09.14 至 2023.09.20',0,'','思想成长','http://image.5idream.net/45384262/1694595630530_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','学习二十大、永远跟党走、奋进新征程',2,'规划中'),
(104,10001,8491850,'2023.10.10 至 2023.10.15',0,'','文艺体育','http://image.5idream.net/45385402/1694619653308_0?x-oss-process=image/resize,w_375,h_0/quality,Q_100/format,jpg','我为新生荐本书',3,'报名中');
/*!40000 ALTER TABLE `activityData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schoolData`
--

DROP TABLE IF EXISTS `schoolData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schoolData` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` int(10) NOT NULL,
  `name` char(20) NOT NULL COMMENT '学校名称',
  `qq` char(20) NOT NULL COMMENT 'qq',
  `qqGroup` text NOT NULL COMMENT 'QQ群',
  `ban` tinyint(1) NOT NULL COMMENT '出错状态',
  `open` tinyint(1) NOT NULL COMMENT '是否启用',
  `errorMsg` char(30) NOT NULL COMMENT '错误信息',
  `d` text NOT NULL COMMENT '到梦空间d参数',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `id_2` (`id`),
  KEY `uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schoolData`
--

LOCK TABLES `schoolData` WRITE;
/*!40000 ALTER TABLE `schoolData` DISABLE KEYS */;
INSERT INTO `schoolData` VALUES
(1,10001,'桂林理工大学','1533115017','760861972,754079071,392838485',0,0,'d参数失效，请重新上传','****');
/*!40000 ALTER TABLE `schoolData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'qryhqkim'
--

--
-- Dumping routines for database 'qryhqkim'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-14 14:13:26
