-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2022 at 04:48 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scrapy`
--

-- --------------------------------------------------------

--
-- Table structure for table `olxproperty`
--

CREATE TABLE `olxproperty` (
  `id` int(11) NOT NULL,
  `property_id` int(9) NOT NULL,
  `category_id` varchar(4) NOT NULL,
  `category` varchar(27) NOT NULL,
  `types` varchar(12) DEFAULT NULL,
  `province_code` varchar(7) NOT NULL,
  `province` varchar(64) NOT NULL,
  `regency_code` varchar(7) NOT NULL,
  `regency` varchar(64) NOT NULL,
  `subdistrict_code` varchar(7) NOT NULL,
  `subdistrict` varchar(64) NOT NULL,
  `latitude` float DEFAULT NULL,
  `longtitude` float DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_at_first` datetime DEFAULT NULL,
  `title` varchar(150) NOT NULL,
  `main_info` varchar(72) DEFAULT NULL,
  `price` bigint(20) NOT NULL,
  `sqr_building` bigint(20) DEFAULT NULL,
  `sqr_land` bigint(20) DEFAULT NULL,
  `bedroom` int(11) DEFAULT NULL,
  `bathroom` int(11) DEFAULT NULL,
  `floor` int(11) DEFAULT NULL,
  `certificate` varchar(24) DEFAULT NULL,
  `facility` varchar(200) DEFAULT NULL,
  `user_id` varchar(9) DEFAULT NULL,
  `user_type` varchar(16) DEFAULT NULL,
  `crawl_time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `olxproperty`
--
ALTER TABLE `olxproperty`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `olxproperty`
--
ALTER TABLE `olxproperty`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
