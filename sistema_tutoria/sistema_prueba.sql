-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.9.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para sistemas_prueba
CREATE DATABASE IF NOT EXISTS `sistemas_prueba` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `sistemas_prueba`;

-- Volcando estructura para tabla sistemas_prueba.dato_tutorados
CREATE TABLE IF NOT EXISTS `dato_tutorados` (
  `id` char(6) NOT NULL,
  `nombres` varchar(45) NOT NULL DEFAULT '0',
  `apellidos` varchar(45) NOT NULL,
  `ciclo` varchar(2) NOT NULL,
  `tipo_beca` varchar(45) DEFAULT NULL,
  `fk_dato_tutor` varchar(20) DEFAULT NULL,
  `fk_ranking` int(11) DEFAULT NULL,
  `fk_usuario` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_dato_tutorados_dato_tutores` (`fk_dato_tutor`),
  KEY `FK_dato_tutorados_ranking` (`fk_ranking`),
  KEY `FK_dato_tutorados_dato_usuarios` (`fk_usuario`),
  CONSTRAINT `FK_dato_tutorados_dato_tutores` FOREIGN KEY (`fk_dato_tutor`) REFERENCES `dato_tutores` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_dato_tutorados_dato_usuarios` FOREIGN KEY (`fk_usuario`) REFERENCES `dato_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_dato_tutorados_ranking` FOREIGN KEY (`fk_ranking`) REFERENCES `ranking` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.dato_tutores
CREATE TABLE IF NOT EXISTS `dato_tutores` (
  `id` varchar(20) NOT NULL DEFAULT '',
  `grado` varchar(10) DEFAULT '',
  `nombres` varchar(45) DEFAULT '',
  `apellidos` varchar(45) DEFAULT '',
  `nro_tutorados` int(11) DEFAULT NULL,
  `ses_individuales` int(11) DEFAULT NULL,
  `ses_grupales` int(11) DEFAULT NULL,
  `referidos` int(11) DEFAULT NULL,
  `atendidos` int(11) DEFAULT NULL,
  `criterio` int(11) NOT NULL,
  `fk_ranking` int(11) DEFAULT NULL,
  `fk_usuario` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_dato_tutores_ranking` (`fk_ranking`),
  KEY `FK_dato_tutores_dato_usuarios` (`fk_usuario`),
  CONSTRAINT `FK_dato_tutores_dato_usuarios` FOREIGN KEY (`fk_usuario`) REFERENCES `dato_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_dato_tutores_ranking` FOREIGN KEY (`fk_ranking`) REFERENCES `ranking` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.dato_usuarios
CREATE TABLE IF NOT EXISTS `dato_usuarios` (
  `id` varchar(20) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  `contrasenia` varchar(100) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `correo` varchar(50) DEFAULT NULL,
  `fk_documento` int(11) DEFAULT 0,
  `fk_rol` int(11) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `FK_dato_usuarios_documentos` (`fk_documento`),
  KEY `FK_dato_usuarios_rol_usuarios` (`fk_rol`),
  CONSTRAINT `FK_dato_usuarios_documentos` FOREIGN KEY (`fk_documento`) REFERENCES `documentos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_dato_usuarios_rol_usuarios` FOREIGN KEY (`fk_rol`) REFERENCES `rol_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.documentos
CREATE TABLE IF NOT EXISTS `documentos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_doc` varchar(45) NOT NULL DEFAULT '0',
  `archivo` blob NOT NULL,
  `tipo` varchar(15) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.documento_generados
CREATE TABLE IF NOT EXISTS `documento_generados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `doc_generado` blob NOT NULL,
  `fk_usuario` varchar(20) DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `FK__dato_usuarios` (`fk_usuario`),
  CONSTRAINT `FK__dato_usuarios` FOREIGN KEY (`fk_usuario`) REFERENCES `dato_usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.modalidad
CREATE TABLE IF NOT EXISTS `modalidad` (
  `id` int(11) NOT NULL,
  `nombre_modalidad` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.ranking
CREATE TABLE IF NOT EXISTS `ranking` (
  `id` int(11) NOT NULL DEFAULT 0,
  `ranking` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.rol_usuarios
CREATE TABLE IF NOT EXISTS `rol_usuarios` (
  `id` int(11) NOT NULL,
  `nombre_rol` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla sistemas_prueba.tutorados_modalidad
CREATE TABLE IF NOT EXISTS `tutorados_modalidad` (
  `fk_dato_tutorado` char(6) DEFAULT NULL,
  `fk_modalidad` int(11) DEFAULT 0,
  KEY `FK__dato_tutorados` (`fk_dato_tutorado`),
  KEY `FK__modalidad` (`fk_modalidad`),
  CONSTRAINT `FK__dato_tutorados` FOREIGN KEY (`fk_dato_tutorado`) REFERENCES `dato_tutorados` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK__modalidad` FOREIGN KEY (`fk_modalidad`) REFERENCES `modalidad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
