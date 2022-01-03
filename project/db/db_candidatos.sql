-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-12-2021 a las 19:34:50
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_candidatos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comment`
--

CREATE TABLE `comment` (
  `id` int NOT NULL,
<<<<<<< HEAD
  `comment_id` varchar(20) NOT NULL,
=======
  `comment_id` varchar(20) NOT NULL UNIQUE,
>>>>>>> main
  `profile_id` bigint(20) DEFAULT NULL,
  `from_name` varchar(500) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `created_time` time DEFAULT NULL,
  `reactions` int(11) DEFAULT NULL,
  `post_id` int NOT NULL,
  `feeling` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `page`
--

CREATE TABLE `page` (
  `id` int NOT NULL,
  `page_id` varchar(20) NOT NULL UNIQUE,
  `page_name` varchar(50) DEFAULT NULL,
  `page_name_id` varchar(50) DEFAULT NULL,
  `political_party` varchar(50) DEFAULT NULL,
  `kind` varchar(30) DEFAULT NULL,
  `region` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `post`
--

CREATE TABLE `post` (
  `id` int NOT NULL,
  `post_id` varchar(20) NOT NULL UNIQUE,
  `created_date` date DEFAULT NULL,
  `created_time` time DEFAULT NULL,
  `message` text DEFAULT NULL,
  `react_angry` int(11) DEFAULT NULL,
  `react_haha` int(11) DEFAULT NULL,
  `react_like` int(11) DEFAULT NULL,
  `react_love` int(11) DEFAULT NULL,
  `react_sad` int(11) DEFAULT NULL,
  `react_wow` int(11) DEFAULT NULL,
  `react_care` int(11) DEFAULT NULL,
  `share` int(11) DEFAULT NULL,
  `page_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `post_id` (`post_id`);

--
-- Indices de la tabla `page`
--
ALTER TABLE `page`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `page_id` (`page_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

-- AUTO_INCREMENT de la tabla `page`
--
ALTER TABLE `page`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
-- AUTO_INCREMENT de la tabla `post`
--
ALTER TABLE `post`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
  
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `fk_post` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `fk_page` FOREIGN KEY (`page_id`) REFERENCES `page` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
