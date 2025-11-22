-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2025 at 06:52 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lnb`
--

-- --------------------------------------------------------

--
-- Table structure for table `administradores`
--

CREATE TABLE `administradores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `apellido` varchar(30) DEFAULT NULL,
  `id_usuario` varchar(30) DEFAULT NULL,
  `pass` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `administradores`
--

INSERT INTO `administradores` (`id`, `nombre`, `apellido`, `id_usuario`, `pass`) VALUES
(1, 'Andrés', 'Fernandez', 'andres.fernandez', 'dqguhv.dgplq'),
(3, 'Gamaliel', 'Quiroz', 'el.profe', 'ho.surih'),
(4, 'Kobe', 'Bryant', 'mamba24', 'eurrnobq'),
(5, 'Lio', 'Messi', 'pulga', 'dqwr');

-- --------------------------------------------------------

--
-- Table structure for table `aficionados`
--

CREATE TABLE `aficionados` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `apellido` varchar(30) DEFAULT NULL,
  `id_usuario` varchar(30) DEFAULT NULL,
  `pass` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `d_of_birth` date DEFAULT NULL,
  `equipo_favorito` int(11) DEFAULT NULL,
  `jugador_favorito` int(11) DEFAULT NULL,
  `puntos` int(11) DEFAULT 0,
  `foto_perfil` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aficionados`
--

INSERT INTO `aficionados` (`id`, `nombre`, `apellido`, `id_usuario`, `pass`, `email`, `d_of_birth`, `equipo_favorito`, `jugador_favorito`, `puntos`, `foto_perfil`) VALUES
(1, 'Andrés', 'Fernandez', 'andres.user', 'xvhu.sdvv', 'andy@java.com', '2002-09-26', 1, 2, 20, ''),
(2, 'Andrés', 'Fernandez', 'prueba.1', 'suxhed.1', 'prueba@1.com', '2000-02-20', NULL, NULL, NULL, ''),
(3, 'juancito', 'juanes', 'juancho', 'mxdqflwr', 'juancito@juan.com', '2000-02-06', NULL, NULL, NULL, ''),
(5, 'Pepe', 'Ordovás', 'franquista01', '12345678', 'pepe@ae.com', '1917-01-01', NULL, NULL, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `aficionado_jugador`
--

CREATE TABLE `aficionado_jugador` (
  `id` int(11) NOT NULL,
  `id_aficionado` int(11) DEFAULT NULL,
  `id_jugador` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aficionado_jugador`
--

INSERT INTO `aficionado_jugador` (`id`, `id_aficionado`, `id_jugador`) VALUES
(16, 1, 9),
(17, 1, 18),
(18, 1, 2),
(19, 1, 1),
(20, 1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `articulos`
--

CREATE TABLE `articulos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(150) DEFAULT NULL,
  `descripcion` varchar(3000) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `portada` blob DEFAULT NULL,
  `foto_1` blob DEFAULT NULL,
  `foto_2` blob DEFAULT NULL,
  `foto_3` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `articulos`
--

INSERT INTO `articulos` (`id`, `titulo`, `descripcion`, `fecha`, `portada`, `foto_1`, `foto_2`, `foto_3`) VALUES
(2, 'Titulazo', 'sklanvlñasnvlñas ñlanvlñnaslñvnasñ vn alñvnñlkavnñl nañlskvnñasln', '2025-06-26', NULL, NULL, NULL, NULL),
(6, 'dddddddd', 'selftest\nesfsfasdlkfasdlvnas\nasldvnasñlvnpanvlñsadnvalñsjva lsv\nasdvlñajvad\nvajsjvaskvlñajvlasnv aalñsjv sahv ksajv ksahasv \nadk aklva av lñajsñv a', '2025-06-26', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dts`
--

CREATE TABLE `dts` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `apellido` varchar(30) DEFAULT NULL,
  `d_of_birth` date DEFAULT NULL,
  `nacionalidad` varchar(30) DEFAULT NULL,
  `ciudad` varchar(50) DEFAULT NULL,
  `equipo` int(11) DEFAULT NULL,
  `temporadas_en_liga` int(11) DEFAULT NULL,
  `foto` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dts`
--

INSERT INTO `dts` (`id`, `nombre`, `apellido`, `d_of_birth`, `nacionalidad`, `ciudad`, `equipo`, `temporadas_en_liga`, `foto`) VALUES
(1, 'Federico', 'Fernandez', '1985-05-17', 'Argentino', 'Bragado, Buenos Aires', 1, 5, NULL),
(2, 'Lucas', 'Victoriano', '1977-11-05', 'Argentino', 'San Miguel de Tucumán', 5, 6, NULL),
(3, 'Leandro', 'Ramella', '1974-12-12', 'Argentino', 'Mar del Plata', 6, 10, NULL),
(4, 'Manuel', 'Anglese', '1985-11-23', 'Argentino', 'Ciudad de Buenos Aires', 8, 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `equipos`
--

CREATE TABLE `equipos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `ciudad` varchar(50) DEFAULT NULL,
  `estadio` varchar(50) DEFAULT NULL,
  `fecha_de_fundacion` date DEFAULT NULL,
  `temporadas_en_liga` int(11) DEFAULT NULL,
  `campeonatos` int(11) DEFAULT NULL,
  `escudo` blob DEFAULT NULL,
  `foto_estadio` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `equipos`
--

INSERT INTO `equipos` (`id`, `nombre`, `ciudad`, `estadio`, `fecha_de_fundacion`, `temporadas_en_liga`, `campeonatos`, `escudo`, `foto_estadio`) VALUES
(1, 'Ferro Carril Oeste', 'Ciudad de Buenos Aires', 'Héctor Etchart', '1904-07-28', 29, 3, NULL, NULL),
(2, 'Boca Juniors', 'Ciudad de Buenos Aires', 'Luis Conde \'La Bombonerita\'', '1905-04-03', 35, 4, NULL, NULL),
(3, 'Atenas', 'Córdoba', 'Atenas Estadio', '1938-04-17', 39, 9, NULL, NULL),
(4, 'Peñarol', 'Mar del Plata', 'Polideportivo Islas Malvinas', '1922-11-07', 37, 5, NULL, NULL),
(5, 'Instituto', 'Córdoba', 'Ángel Sandrín', '1918-08-08', 11, 1, NULL, NULL),
(6, 'Quimsa', 'Santiago del Estero', 'Estadio Ciudad Quimsa', '1989-08-13', 17, 2, NULL, NULL),
(7, 'Gimnasia y Esgrima', 'Comodoro Rivadavia', 'Socios Fundadores', '1919-02-13', 35, 1, NULL, NULL),
(8, 'Zárate Basket', 'Zárate', 'Diego Armando Maradona', '2017-05-11', 1, 0, NULL, NULL),
(9, 'Obras Basket', 'Ciudad de Buenos Aires', 'Estadio Obras Sanitarias', '1917-03-27', 27, 0, NULL, NULL),
(10, 'San Lorenzo', 'Ciudad de Buenos Aires', 'Roberto Pando', '1908-04-01', 10, 5, NULL, NULL),
(11, 'Platense', 'Vicente López', 'Estadio Ciudad de Vicente López', '1905-05-25', 5, 0, NULL, NULL),
(12, 'Ciclista Olímpico', 'La Banda', 'Vicente Rosales', '1921-12-09', 19, 0, NULL, NULL),
(14, 'Argentino', 'Junín', 'El Fortín de las Morochas', '1935-10-01', 16, 0, NULL, NULL),
(15, 'Independiente', 'Oliva', 'El Gigante', '1921-04-14', 2, 0, NULL, NULL),
(16, 'La Unión', 'Formosa', 'Cincuentenario', '2004-08-05', 16, 0, NULL, NULL),
(17, 'Oberá Tenis Club', 'Oberá', 'Estadio Oberá Tenis Club', '1940-01-17', 4, 0, NULL, NULL),
(18, 'Regatas', 'Corrientes', 'José Jorge Contte', '1923-09-27', 20, 1, NULL, NULL),
(19, 'Riachuelo', 'La Rioja', 'Superdomo', '2016-07-23', 3, 0, NULL, NULL),
(20, 'San Martín', 'Corrientes', 'El Fortín Rojinegro', '1932-01-24', 11, 0, NULL, NULL),
(21, 'Unión', 'Santa Fé', 'Ángel Malvicino', '1907-04-15', 6, 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `eventos`
--

CREATE TABLE `eventos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(150) DEFAULT NULL,
  `descripcion` varchar(3000) DEFAULT NULL,
  `fecha_y_hora` datetime DEFAULT NULL,
  `cap_max` int(11) DEFAULT NULL,
  `portada` blob DEFAULT NULL,
  `foto_1` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `eventos`
--

INSERT INTO `eventos` (`id`, `titulo`, `descripcion`, `fecha_y_hora`, `cap_max`, `portada`, `foto_1`) VALUES
(1, 'Traino con Lezcano', 'Veni a entrenar con el Tucu en el Hector Etchart', '2025-07-15 15:30:00', 50, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `evento_aficionado`
--

CREATE TABLE `evento_aficionado` (
  `id` int(11) NOT NULL,
  `id_evento` int(11) DEFAULT NULL,
  `id_aficionado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `jugadores`
--

CREATE TABLE `jugadores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `apellido` varchar(30) DEFAULT NULL,
  `camiseta` int(11) DEFAULT NULL,
  `media` int(11) DEFAULT NULL,
  `posicion` varchar(15) DEFAULT NULL,
  `nacionalidad` varchar(30) DEFAULT NULL,
  `equipo` int(11) DEFAULT NULL,
  `tiro` int(11) DEFAULT NULL,
  `dribling` int(11) DEFAULT NULL,
  `velocidad` int(11) DEFAULT NULL,
  `pase` int(11) DEFAULT NULL,
  `defensa` int(11) DEFAULT NULL,
  `salto` int(11) DEFAULT NULL,
  `d_of_birth` date DEFAULT NULL,
  `ciudad` varchar(50) DEFAULT NULL,
  `altura` float DEFAULT NULL,
  `mano_habil` varchar(10) DEFAULT NULL,
  `especialidad` varchar(30) DEFAULT NULL,
  `jugada` varchar(30) DEFAULT NULL,
  `aficionado_id` int(11) DEFAULT NULL,
  `foto_carnet` blob DEFAULT NULL,
  `media_day` blob DEFAULT NULL,
  `foto_juego` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jugadores`
--

INSERT INTO `jugadores` (`id`, `nombre`, `apellido`, `camiseta`, `media`, `posicion`, `nacionalidad`, `equipo`, `tiro`, `dribling`, `velocidad`, `pase`, `defensa`, `salto`, `d_of_birth`, `ciudad`, `altura`, `mano_habil`, `especialidad`, `jugada`, `aficionado_id`, `foto_carnet`, `media_day`, `foto_juego`) VALUES
(1, 'Alejo', 'Maggi', 13, 99, 'Ala-Pivot', 'Argentino', 8, 99, 99, 99, 99, 99, 99, '2002-04-07', 'Ciudad de Buenos Aires', 2.01, 'Derecha', 'Tapas', 'Volcada en contrataque', NULL, NULL, NULL, NULL),
(2, 'Felipe', 'Rodríguez', 9, 82, 'Escolta/Alero', 'Argentino', 1, 91, 80, 83, 68, 85, 89, '2003-03-12', 'Ramos Mejía', 1.98, 'Derecha', 'Tiro', 'Salida de tirador', NULL, NULL, NULL, NULL),
(3, 'Andrés', 'Fernandez', 5, 65, 'Alero', 'Argentino', NULL, 67, 62, 64, 62, 62, 64, '2002-09-26', 'Ciudad de Buenos Aires', 1.98, 'Derecha', 'Tiro', 'Triple', 5, NULL, NULL, NULL),
(4, 'Andrés', 'Fernandez', 5, 65, 'Alero', 'Argentino', NULL, 68, 62, 62, 64, 62, 64, '2002-09-26', 'Ciudad de Buenos Aires', 1.98, 'Derecha', 'Tiro', 'Triple', 1, NULL, NULL, NULL),
(5, 'Pedro', 'Barral', 13, 89, 'Base', 'Argentino', 9, 89, 91, 84, 93, 74, 72, '1994-10-20', 'Morón', 1.86, 'Derecha', 'Asistencias', 'Pick and Roll', NULL, NULL, NULL, NULL),
(6, 'Leonel', 'Schattmann', 20, 86, 'Escolta', 'Argentino', 9, 92, 88, 80, 80, 72, 69, '1985-05-14', 'Viedma, Río Negro', 1.94, 'Derecha', 'Tiro', 'Salida de tirador', NULL, NULL, NULL, NULL),
(7, 'Tomás', 'Chapero', 30, 84, 'Pivot', 'Argentino', 9, 64, 62, 72, 65, 89, 85, '2001-06-10', 'Vera, Santa Fé', 2.08, 'Derecha', 'Volcadas', 'Alley-oop', NULL, NULL, NULL, NULL),
(8, 'Selem', 'Safar', 15, 88, 'Escolta', 'Argentino', 10, 90, 85, 79, 75, 79, 75, '1987-05-06', 'Mar del Plata', 1.92, 'Izquierda', 'Tiro', 'Salida de tirador', NULL, NULL, NULL, NULL),
(9, 'José', 'Vildoza', 11, 97, 'Base', 'Argentino', 2, 98, 97, 94, 93, 88, 88, '1996-01-15', 'Córdoba, Córdoba', 1.91, 'Izquierda', 'Tiro', 'Pick and Roll', NULL, NULL, NULL, NULL),
(10, 'Marcos', 'Delía', 12, 88, 'Pivot', 'Argentino', 2, 65, 70, 74, 75, 92, 93, '1992-04-08', 'Saladillo, Buenos Aires', 2.08, 'Derecha', 'Volcadas', 'Volcada en contrataque', NULL, NULL, NULL, NULL),
(11, 'Sebastián', 'Vega', 17, 85, 'Alero/Ala-Pivot', 'Argentino', 2, 88, 84, 88, 83, 88, 82, '1988-07-09', 'Gualeguaychú, Entre Ríos', 2, 'Derecha', 'Tiro', 'Triple', NULL, NULL, NULL, NULL),
(12, 'Tomás', 'Spano', 21, 87, 'Base/Escolta', 'Argentino', 1, 91, 91, 90, 84, 86, 82, '1998-05-05', 'Civilcoy, Buenos Aires', 1.85, 'Derecha', 'Uno contra uno', 'Flotadora', NULL, NULL, NULL, NULL),
(17, 'Facundo', 'Vázquez', 22, 85, 'Base', 'Argentino', 11, 85, 93, 90, 90, 84, 79, '1998-04-23', 'Vicente López', 1.85, 'Derecha', 'Asistencias', 'Pick and roll', NULL, NULL, NULL, NULL),
(18, 'Emiliano', 'Lezcano', 4, 87, 'Base/Escolta', 'Argentino', 1, 85, 82, 96, 84, 92, 89, '2001-03-02', 'Tafí del Valle, Tucumán', 1.87, 'Derecha', 'Uno contra uno', 'Tiro de media distancia', NULL, NULL, NULL, NULL),
(19, 'Ignacio', 'Laterza', 8, 88, 'Base', 'Argentino', 17, 86, 88, 91, 93, 80, 72, '1997-05-07', 'Necochea, Buenos Aires', 1.85, 'Derecha', 'Asistencias', 'Pick and roll', NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aficionados`
--
ALTER TABLE `aficionados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `equipo_favorito` (`equipo_favorito`),
  ADD KEY `jugador_favorito` (`jugador_favorito`);

--
-- Indexes for table `aficionado_jugador`
--
ALTER TABLE `aficionado_jugador`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_aficionado` (`id_aficionado`),
  ADD KEY `id_jugador` (`id_jugador`);

--
-- Indexes for table `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `titulo` (`titulo`);

--
-- Indexes for table `dts`
--
ALTER TABLE `dts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_dt_equipo` (`equipo`);

--
-- Indexes for table `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indexes for table `eventos`
--
ALTER TABLE `eventos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `titulo` (`titulo`);

--
-- Indexes for table `evento_aficionado`
--
ALTER TABLE `evento_aficionado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_evento_aficionado` (`id_evento`,`id_aficionado`),
  ADD KEY `id_aficionado` (`id_aficionado`),
  ADD KEY `id_evento` (`id_evento`);

--
-- Indexes for table `jugadores`
--
ALTER TABLE `jugadores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `aficionado` (`aficionado_id`),
  ADD UNIQUE KEY `aficionado_id` (`aficionado_id`),
  ADD KEY `equipo` (`equipo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `administradores`
--
ALTER TABLE `administradores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `aficionados`
--
ALTER TABLE `aficionados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `aficionado_jugador`
--
ALTER TABLE `aficionado_jugador`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `articulos`
--
ALTER TABLE `articulos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `dts`
--
ALTER TABLE `dts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `equipos`
--
ALTER TABLE `equipos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `eventos`
--
ALTER TABLE `eventos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `evento_aficionado`
--
ALTER TABLE `evento_aficionado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `jugadores`
--
ALTER TABLE `jugadores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `aficionados`
--
ALTER TABLE `aficionados`
  ADD CONSTRAINT `aficionados_ibfk_1` FOREIGN KEY (`equipo_favorito`) REFERENCES `equipos` (`id`),
  ADD CONSTRAINT `aficionados_ibfk_2` FOREIGN KEY (`jugador_favorito`) REFERENCES `jugadores` (`id`);

--
-- Constraints for table `aficionado_jugador`
--
ALTER TABLE `aficionado_jugador`
  ADD CONSTRAINT `aficionado_jugador_ibfk_1` FOREIGN KEY (`id_aficionado`) REFERENCES `aficionados` (`id`),
  ADD CONSTRAINT `aficionado_jugador_ibfk_2` FOREIGN KEY (`id_jugador`) REFERENCES `jugadores` (`id`);

--
-- Constraints for table `dts`
--
ALTER TABLE `dts`
  ADD CONSTRAINT `fk_dt_equipo` FOREIGN KEY (`equipo`) REFERENCES `equipos` (`id`);

--
-- Constraints for table `evento_aficionado`
--
ALTER TABLE `evento_aficionado`
  ADD CONSTRAINT `evento_aficionado_ibfk_1` FOREIGN KEY (`id_aficionado`) REFERENCES `aficionados` (`id`),
  ADD CONSTRAINT `evento_aficionado_ibfk_2` FOREIGN KEY (`id_evento`) REFERENCES `eventos` (`id`);

--
-- Constraints for table `jugadores`
--
ALTER TABLE `jugadores`
  ADD CONSTRAINT `jugadores_ibfk_1` FOREIGN KEY (`equipo`) REFERENCES `equipos` (`id`),
  ADD CONSTRAINT `jugadores_ibfk_2` FOREIGN KEY (`aficionado_id`) REFERENCES `aficionados` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
