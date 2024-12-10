-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        9.1.0 - MySQL Community Server - GPL
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- musicapp 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `musicapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `musicapp`;

-- 테이블 musicapp.administrator 구조 내보내기
CREATE TABLE IF NOT EXISTS `administrator` (
  `ID` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='관리자 테이블\r\n';

-- 테이블 데이터 musicapp.administrator:~1 rows (대략적) 내보내기
INSERT INTO `administrator` (`ID`, `name`, `sex`) VALUES
	(1, 'master', 'M');

-- 테이블 musicapp.favorite 구조 내보내기
CREATE TABLE IF NOT EXISTS `favorite` (
  `UID` int NOT NULL,
  `MID` int NOT NULL,
  PRIMARY KEY (`UID`,`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 musicapp.favorite:~3 rows (대략적) 내보내기
INSERT INTO `favorite` (`UID`, `MID`) VALUES
	(1, 2),
	(3, 1),
	(3, 3);

-- 테이블 musicapp.heard 구조 내보내기
CREATE TABLE IF NOT EXISTS `heard` (
  `UID` int NOT NULL,
  `MID` int NOT NULL,
  `heardNum` int NOT NULL,
  `heardDate` datetime DEFAULT NULL,
  PRIMARY KEY (`UID`,`MID`),
  KEY `MID` (`MID`),
  CONSTRAINT `heard_ibfk_1` FOREIGN KEY (`MID`) REFERENCES `music` (`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='''듣기'' 테이블 (music과 user의 relation ship table';

-- 테이블 데이터 musicapp.heard:~7 rows (대략적) 내보내기
INSERT INTO `heard` (`UID`, `MID`, `heardNum`, `heardDate`) VALUES
	(1, 1, 3, '2024-12-07 10:52:00'),
	(1, 2, 1, '2024-12-07 10:57:15'),
	(1, 3, 1, '2024-12-06 07:35:16'),
	(2, 1, 1, '2024-12-07 11:27:51'),
	(2, 2, 2, '2024-12-07 11:28:06'),
	(3, 1, 1, '2024-12-07 11:23:12'),
	(3, 2, 1, '2024-12-07 11:35:22');

-- 테이블 musicapp.including 구조 내보내기
CREATE TABLE IF NOT EXISTS `including` (
  `UID` int NOT NULL,
  `MID` int NOT NULL,
  `PID` int NOT NULL,
  PRIMARY KEY (`MID`,`PID`,`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='music과 playlist의 relationship table\r\n음악을 담고 있는 playlist';

-- 테이블 데이터 musicapp.including:~1 rows (대략적) 내보내기
INSERT INTO `including` (`UID`, `MID`, `PID`) VALUES
	(1, 2, 1);

-- 테이블 musicapp.membership 구조 내보내기
CREATE TABLE IF NOT EXISTS `membership` (
  `Mname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`Mname`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='구독권 테이블';

-- 테이블 데이터 musicapp.membership:~1 rows (대략적) 내보내기
INSERT INTO `membership` (`Mname`, `price`) VALUES
	('premium', 10000);

-- 테이블 musicapp.music 구조 내보내기
CREATE TABLE IF NOT EXISTS `music` (
  `adminID` int NOT NULL,
  `MID` int NOT NULL,
  `Mname` varchar(50) NOT NULL,
  `singer` varchar(50) NOT NULL,
  PRIMARY KEY (`MID`),
  KEY `adminID` (`adminID`),
  CONSTRAINT `music_ibfk_1` FOREIGN KEY (`adminID`) REFERENCES `administrator` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='음악 테이블';

-- 테이블 데이터 musicapp.music:~3 rows (대략적) 내보내기
INSERT INTO `music` (`adminID`, `MID`, `Mname`, `singer`) VALUES
	(1, 1, 'blue', 'bigbang'),
	(1, 2, 'apt', 'rose'),
	(1, 3, 'love dive', 'izone');

-- 테이블 musicapp.playlist 구조 내보내기
CREATE TABLE IF NOT EXISTS `playlist` (
  `Pname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `MgrID` int NOT NULL,
  `PID` int NOT NULL,
  PRIMARY KEY (`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='플레이리스트 테이블';

-- 테이블 데이터 musicapp.playlist:~6 rows (대략적) 내보내기
INSERT INTO `playlist` (`Pname`, `MgrID`, `PID`) VALUES
	('summer', 1, 1),
	('shower', 1, 2),
	('night', 1, 3),
	('summer', 2, 4),
	('sad', 2, 5),
	('fitness', 3, 6);

-- 테이블 musicapp.search 구조 내보내기
CREATE TABLE IF NOT EXISTS `search` (
  `UID` int NOT NULL,
  `MID` int NOT NULL,
  PRIMARY KEY (`UID`,`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 musicapp.search:~0 rows (대략적) 내보내기

-- 테이블 musicapp.user 구조 내보내기
CREATE TABLE IF NOT EXISTS `user` (
  `adminID` int DEFAULT NULL,
  `UID` int NOT NULL,
  `password` varchar(50) NOT NULL DEFAULT '',
  `name` varchar(50) NOT NULL,
  `sex` char(1) NOT NULL,
  `subStatus` char(1) NOT NULL DEFAULT 'N',
  `subName` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`UID`),
  KEY `adminID` (`adminID`),
  KEY `subName` (`subName`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`adminID`) REFERENCES `administrator` (`ID`),
  CONSTRAINT `user_ibfk_2` FOREIGN KEY (`subName`) REFERENCES `membership` (`Mname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='user 테이블';

-- 테이블 데이터 musicapp.user:~4 rows (대략적) 내보내기
INSERT INTO `user` (`adminID`, `UID`, `password`, `name`, `sex`, `subStatus`, `subName`) VALUES
	(1, 1, '1', 'john', 'm', 'Y', 'premium'),
	(1, 2, '2', 'bob', 'f', 'N', NULL),
	(1, 3, '3', 'ava', 'f', 'Y', 'premium'),
	(1, 4, '4', 'emily', 'f', 'N', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
