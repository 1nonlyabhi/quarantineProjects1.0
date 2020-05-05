-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2020 at 08:03 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cleanpost`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'First_Post', 'firstpost@gmail.com', '1234567890', 'This is my First Post...', '2020-04-25 23:46:33'),
(2, 'Second Test', 'bipow60238@mailboxt.com', '1239874560', 'AB ho jaa bhai', '2020-04-26 03:08:17');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(25) NOT NULL,
  `writer` text NOT NULL DEFAULT 'Admin',
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `writer`, `date`) VALUES
(1, 'A Man Called Ove', 'Gonna be first romantic book for me', 'firstbook', 'A Man Called Ove (original title in Swedish: En man som heter Ove) is a 2012 novel by Fredrik Backman, a Swedish columnist, blogger and writer. It was published in English in 2013. The English version reached the New York Times Best Seller list 18 months after it was published and stayed on the list for 42 weeks. (Reference : Wikipedia)', 'a-man-called-ove.jpg', 'Zughead', '2020-05-05 22:48:47'),
(2, 'Looking For Alaska', 'Something romantic by John Green', 'secondbook', 'Looking for Alaska is John Green\'s first novel, published in March 2005 by Dutton Juvenile. Based on his time at Indian Springs School, Green wrote the novel as a result of his desire to create meaningful young adult fiction. The characters and events of the plot are grounded in Green\'s life, while the story itself is fictional.\r\n\r\n(Reference : Wikipedia)', 'lookingforalaska.jpg', 'Zughead', '2020-05-05 20:54:08'),
(3, 'Five Feet Apart', 'A Heart-breaking Story', 'thirdbook', 'Five Feet Apart is a 2019 American romantic drama film directed by Justin Baldoni (in his directorial debut) and written by Mikki Daughtry and Tobias Iaconis. The film was inspired by Claire Wineland, who suffered from cystic fibrosis. Haley Lu Richardson and Cole Sprouse play two young patients with cystic fibrosis, who try to have a relationship despite always being forced to stay a certain distance (6 ft) away from each other. It was released in the United States on March 15, 2019 by CBS Films via Lionsgate. The film received mixed reviews from critics and has grossed over $91 million worldwide.\r\n\r\n(Reference : Wikipedia)', 'five-feet-apart.jpg', 'Zughead', '2020-05-05 21:46:04');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
