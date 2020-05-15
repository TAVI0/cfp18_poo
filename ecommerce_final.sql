CREATE DATABASE  IF NOT EXISTS `ecommerce_final`;
USE `ecommerce_final`;



DROP TABLE IF EXISTS `paises`;
CREATE TABLE `paises` (
  `pais_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`pais_id`)
);

INSERT INTO `paises` VALUES (1,'Argentina'),(2,'Uruguay'),(3,'Chile'),(4,'Paraguay'),(5,'Bolivia');



DROP TABLE IF EXISTS `provincias`;
CREATE TABLE `provincias` (
  `provincia_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `pais_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`provincia_id`),
  FOREIGN KEY (`pais_id`) REFERENCES `paises` (`pais_id`)
);

INSERT INTO `provincias` VALUES (1,'Ciudad Autónoma de Buenos Aires',1),(2,'Gran Buenos Aires',1),(3,'Buenos Aires',1),(4,'Santa Fe',1),(5,'Córdoba',1);



DROP TABLE IF EXISTS `ciudades`;
CREATE TABLE `ciudades` (
  `ciudad_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `provincia_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ciudad_id`),
  FOREIGN KEY (`provincia_id`) REFERENCES `provincias` (`provincia_id`)
) ;

INSERT INTO `ciudades` VALUES (1,'Ciudad Autonoma de Buenos Aires',1),(2,'Mar del Plata',3),(3,'Bahia Blanca',3),(4,'Necochea',3),(5,'San Isidro',2),(6,'Vicente Lopez',2),(7,'San Fernando',2);



DROP TABLE IF EXISTS `direcciones`;
CREATE TABLE `direcciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calle` varchar(50) NOT NULL,
  `altura` smallint(5) NOT NULL,
  `codigo_postal` smallint(4) DEFAULT NULL,
  `ciudad_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`ciudad_id`) REFERENCES `ciudades` (`ciudad_id`)
);

INSERT INTO `direcciones` VALUES (1,'Malaver',876,4713,3),(2,'General Pueyrredon',1564,3421,2),(3,'Emilio Mitre',4222,1213,7),(4,'Cuyo',366,1313,6),(5,'Santa Cruz',2020,1354,5),(6,'Misiones',876,4713,3),(7,'Chacabuco',1564,3421,2),(8,'Juan Domingo Peron',4222,1213,7),(9,'Santa Fe',366,1313,6),(10,'Aconcagua',2020,1354,5);



DROP TABLE IF EXISTS `marcas`;
CREATE TABLE `marcas` (
  `marca_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`marca_id`)
);

INSERT INTO `marcas` VALUES (1,'Adidas'),(2,'Nike'),(3,'Reebok'),(4,'Topper'),(5,'Puma'),(6,'Converse'),(7,'Crocs'),(8,'DC'),(9,'Vans'),(10,'Le coq sportif');



DROP TABLE IF EXISTS `categorias`;
CREATE TABLE `categorias` (
  `categoria_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`categoria_id`)
) ;

INSERT INTO `categorias` VALUES (1,'Calzado y zapatillas'),(2,'Remeras'),(3,'Pantalones'),(4,'Buzos y camperas'),(5,'Pelotas'),(6,'Trajes de baño'),(7,'Ropa interior'),(8,'Otros');



DROP TABLE IF EXISTS `productos`;
CREATE TABLE `productos` (
  `producto_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `precio` float NOT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `marca_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`producto_id`),
  FOREIGN KEY (`categoria_id`) REFERENCES `categorias` (`categoria_id`),
  FOREIGN KEY (`marca_id`) REFERENCES `marcas` (`marca_id`)
);

INSERT INTO `productos` VALUES (1,'Zapatillas runner',NULL,5500,1,1),(2,'Zapatillas tennis',NULL,3600,1,1),(3,'Camiseta Boca Juniors',NULL,1100,2,2),(4,'Camiseta River Plate',NULL,1100,2,1),(5,'Zapatillas skateboard',NULL,3000,1,8),(6,'Pelota de fútbol',NULL,1200,8,4),(7,'Guantes de boxeo',NULL,1600,8,1),(8,'Short deportivo',NULL,1100,3,2),(9,'Campera Boca Junios',NULL,2200,4,2),(10,'Campera Seleccion Argentina',NULL,2500,4,2);



DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `clave` char(150) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` char(20) NOT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`usuario_id`),
  FOREIGN KEY (`direccion_id`) REFERENCES `direcciones` (`id`)
);

INSERT INTO `usuarios` VALUES (1,39100420,'Martina','Gutierrez','gatonegro','martg@gmail.com','1554584969',NULL),(2,23049956,'Federico','Gomez','picapiedra','fedgom@hotmail.com','1569599739',NULL),(3,38858949,'Ximena','Podesta','elefante9','ximepo@gmail.com','1566442235',NULL),(4,11331122,'Roberto','Mena','martina95','martg@hotmail.com','114794632',NULL),(5,42111124,'Rodrigo','Castillo','gnr2013','rod_gnr@gmail.com','1534226422',NULL),(6,32211112,'Clara','Coppola','gatonegro','claracop@gmail.com','211242234',NULL),(7,23122334,'Francisca','Gomez','picapiedra','frang@hotmail.com','232444221',NULL),(8,38123443,'Javier','Martin','elefante9','javi94@gmail.com','2334221332',NULL),(9,11554223,'Analía','Mena','juisgi','anime01@hotmail.com','244884663',NULL),(10,42154468,'Sebastian','Castillo','gnr2013','sebcasti@hotmail.com','322455646',NULL);



DROP TABLE IF EXISTS `compras`;
CREATE TABLE `compras` (
  `compra_id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) DEFAULT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  `producto_id` int(11) DEFAULT NULL,
  `cantidad` smallint(4) NOT NULL,
  `precio_total` float NOT NULL,
  PRIMARY KEY (`compra_id`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`),
  FOREIGN KEY (`direccion_id`) REFERENCES `direcciones` (`id`),
  FOREIGN KEY (`producto_id`) REFERENCES `productos` (`producto_id`)
);

INSERT INTO `compras` VALUES (1,1,1,1,1,5500),(2,3,2,1,1,5500),(3,4,3,2,1,3600),(4,5,4,2,1,3600),(5,3,2,3,1,1100),(6,4,3,3,1,1100),(7,2,7,1,1,5500),(8,1,1,1,1,5500),(9,6,8,2,1,3600),(10,7,9,2,1,3600);

