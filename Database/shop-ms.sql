-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2017 at 06:14 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shop-ms`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `CategoryID` int(11) NOT NULL,
  `CategoryName` varchar(25) DEFAULT NULL,
  `DateAdd` datetime NOT NULL,
  `ActiveCategory` tinyint(1) NOT NULL DEFAULT '1',
  `SectionID` int(11) DEFAULT NULL,
  `UserID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`CategoryID`, `CategoryName`, `DateAdd`, `ActiveCategory`, `SectionID`, `UserID`) VALUES
(3, 'معلبات', '2017-04-19 21:31:52', 1, 17, 1),
(4, 'شكلاته', '2017-04-19 21:32:15', 1, 17, 1),
(5, 'صابون', '2017-04-19 21:43:02', 1, 9, 2),
(6, 'فلاش', '2017-04-19 21:43:09', 1, 9, 2);

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `CustomersID` int(11) NOT NULL,
  `CustomersName` varchar(50) NOT NULL,
  `CustomersPhone` varchar(20) NOT NULL,
  `CustomersEmail` varchar(50) NOT NULL,
  `CustomerImage` varchar(100) NOT NULL,
  `CustomersDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `CustomersAddress` varchar(255) NOT NULL,
  `CustomersSex` varchar(10) NOT NULL,
  `UserID` int(11) NOT NULL,
  `CustomersActive` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`CustomersID`, `CustomersName`, `CustomersPhone`, `CustomersEmail`, `CustomerImage`, `CustomersDate`, `CustomersAddress`, `CustomersSex`, `UserID`, `CustomersActive`) VALUES
(1, 'ali', '077677777', 'ali_dd@gmail.com', 'OCbddg80qs2X56596a855Ze6e.jpg', '2017-04-19 21:22:17', 'test', 'ذكر', 2, 1),
(2, 'احمد', '077677777', 'ali_d05d@gmail.com', '42Fb1kX7809bfP036ba10ne6u.jpg', '2017-04-19 21:22:38', 'test', 'ذكر', 2, 1),
(3, 'احمد', '077678525', 'd05d@hotamil.com', '8614z0DE38ccEf94HS274d992.jpg', '2017-04-19 21:22:54', 'test', 'ذكر', 2, 1),
(4, 'احمد علي', '077678525', 'd05d@hotamil.com', 'k116dab851d16ajJ6awLCc7y2.jpg', '2017-04-19 21:23:12', 'test', 'ذكر', 2, 1),
(5, 'نور علي', '077678525', 'lfjbo5d@yahoo.com', 'J5aId28aX5592Dde3k3fYafbe.jpg', '2017-04-19 21:23:43', 'test', 'ذكر', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `employes`
--

CREATE TABLE `employes` (
  `EmployeName` varchar(50) DEFAULT NULL,
  `NumberID` varchar(20) NOT NULL,
  `NumberPhone` varchar(20) NOT NULL,
  `DateOfEmployment` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `emploActive` tinyint(1) NOT NULL DEFAULT '1',
  `image` varchar(100) NOT NULL,
  `Salary` varchar(10) NOT NULL,
  `Age` int(3) DEFAULT NULL,
  `Sex` varchar(10) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `SectionID` int(11) DEFAULT NULL,
  `UserID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `employes`
--

INSERT INTO `employes` (`EmployeName`, `NumberID`, `NumberPhone`, `DateOfEmployment`, `emploActive`, `image`, `Salary`, `Age`, `Sex`, `Address`, `SectionID`, `UserID`) VALUES
('محمد', '2313', '05648345', '2017-04-19 19:01:49', 1, 'ehc1z6fyEeeEb52cbd7a6acLb.jpg', '200', 50, 'ذكر', 'jsdouvijsd oisjdvsasiovjisdo', 13, 1),
('احمد', '9985151', '021564168', '2017-04-19 19:01:08', 1, 'a975410Ef111nEi0Ubb24de2e.jpg', '300', 20, 'ذكر', 'iosjd sjdvoisdj sodvjsdio', 12, 1);

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `ItemID` int(11) NOT NULL,
  `ItemName` varchar(25) DEFAULT NULL,
  `Price` varchar(25) DEFAULT NULL,
  `Quentity` int(11) DEFAULT NULL,
  `Image` varchar(100) DEFAULT NULL,
  `DateOfProduction` date DEFAULT NULL,
  `CompletionDate` date DEFAULT NULL,
  `DateAdd` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UserID` int(11) DEFAULT NULL,
  `CategoryID` int(11) DEFAULT NULL,
  `StoreID` int(11) DEFAULT NULL,
  `ActiveItem` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`ItemID`, `ItemName`, `Price`, `Quentity`, `Image`, `DateOfProduction`, `CompletionDate`, `DateAdd`, `UserID`, `CategoryID`, `StoreID`, `ActiveItem`) VALUES
(1, 'فول', '50', 89, '63ae2gc1Y3d60ok26C3S6f095.jpg', '2020-02-20', '2020-02-20', '2017-04-19 21:33:41', 1, 3, 2, 1),
(4, 'medames', '20', 70, 'erC8n3aaG828Nb394i4aFe0ae.png', '2020-05-02', '2020-05-05', '2017-04-19 21:45:19', 2, 3, 2, 1),
(5, 'qugu', '100', 3597, 'k67q98866WlS1E4M03a21Jfde.png', '2020-08-08', '2020-04-04', '2017-04-19 21:46:06', 2, 3, 3, 1),
(6, 'امريكانيا', '5', 97, '7614aca0y9OcJei0Dd6d9nfa7.jpg', '2020-08-08', '2014-08-08', '2017-04-19 21:47:04', 2, 3, 4, 1),
(7, 'ACV', '510', 619, 'm1e38aMO3V2e7863KgR635E0f.jpg', '2020-05-05', '2020-05-05', '2017-04-19 21:50:51', 2, 5, 2, 1),
(8, 'MATI', '6', 188, 'c07a5ua60elGdbx43c7d119eS.jpg', '2020-05-05', '2020-05-05', '2017-04-19 21:51:18', 2, 5, 3, 1),
(9, 'KI', '20', 1, 'd727X5T6b0fd9Dc6d962crZJ2.jpg', '2030-08-08', '2020-08-08', '2017-04-19 21:51:53', 2, 5, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `section`
--

CREATE TABLE `section` (
  `SectionID` int(11) NOT NULL,
  `SectionName` varchar(25) DEFAULT NULL,
  `DateAdd` datetime NOT NULL,
  `ActiveSection` tinyint(1) NOT NULL DEFAULT '1',
  `UserID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `section`
--

INSERT INTO `section` (`SectionID`, `SectionName`, `DateAdd`, `ActiveSection`, `UserID`) VALUES
(9, 'المنظفات', '2017-04-17 15:54:57', 1, 1),
(12, 'الالكترونيات', '2017-04-17 15:56:18', 1, 1),
(13, 'الالعاب', '2017-04-17 15:56:45', 1, 1),
(17, 'الاطعمه', '2017-04-19 21:30:55', 1, 1),
(18, 'hussam', '2017-04-20 12:22:22', 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `StoreID` int(11) NOT NULL,
  `StoreName` varchar(25) DEFAULT NULL,
  `ActiveStore` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `store`
--

INSERT INTO `store` (`StoreID`, `StoreName`, `ActiveStore`) VALUES
(2, 'EF_168', 1),
(3, 'EF_167', 1),
(4, 'EF_166', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserID` int(11) NOT NULL,
  `FullName` varchar(50) DEFAULT NULL,
  `Username` varchar(25) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `PhoneNumber` varchar(20) DEFAULT NULL,
  `NumberID` varchar(25) DEFAULT NULL,
  `permission` varchar(255) DEFAULT NULL,
  `DataRegister` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Active` tinyint(1) DEFAULT '0',
  `img` varchar(255) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `CodeResetPassword` varchar(255) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserID`, `FullName`, `Username`, `Password`, `Email`, `PhoneNumber`, `NumberID`, `permission`, `DataRegister`, `Active`, `img`, `sex`, `CodeResetPassword`) VALUES
(1, 'ايمن محمود عليوة', 'admin', '827ccb0eea8a706c4c34a16891f84e7b', 'progaymanalaiwah95@gmail.com', '0778480862', '9951044136', '1,2,3,11,12,201,21,22,23,203,31,204,41,205,51,52,206', '2017-01-25 17:45:47', 0, '7529btbEeJ902baZd7s195bH7.jpg', 'ذكر', '0'),
(2, 'ayman  mahmoud mohammed alaiwah', 'root', '63a9f0ea7bb98050796b649e85481845', 'prog.aymanmahmoud@gmail.com', '0778480862', '9951044136', '1,2,3,11,12,201,21,22,23,203,31,204,41,205,51,52,206', '2017-04-15 15:36:39', 0, '7529btbEeJ902baZd7s195bH7.jpg', 'ذكر', '0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`CategoryID`),
  ADD UNIQUE KEY `CategoryName` (`CategoryName`),
  ADD KEY `AddCategory` (`UserID`),
  ADD KEY `SectionFollow` (`SectionID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CustomersID`),
  ADD KEY `customers` (`UserID`);

--
-- Indexes for table `employes`
--
ALTER TABLE `employes`
  ADD PRIMARY KEY (`NumberID`),
  ADD KEY `AddEmployes` (`UserID`),
  ADD KEY `SectionFollw` (`SectionID`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`ItemID`),
  ADD KEY `AddItem` (`UserID`),
  ADD KEY `CategoryFollow` (`CategoryID`),
  ADD KEY `StoreID` (`StoreID`);

--
-- Indexes for table `section`
--
ALTER TABLE `section`
  ADD PRIMARY KEY (`SectionID`),
  ADD KEY `AddSection` (`UserID`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`StoreID`),
  ADD UNIQUE KEY `StorName` (`StoreName`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `CategoryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `CustomersID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
  MODIFY `ItemID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `section`
--
ALTER TABLE `section`
  MODIFY `SectionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `StoreID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `category`
--
ALTER TABLE `category`
  ADD CONSTRAINT `AddCategory` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `SectionFollow` FOREIGN KEY (`SectionID`) REFERENCES `section` (`SectionID`) ON UPDATE CASCADE;

--
-- Constraints for table `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `customers` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`);

--
-- Constraints for table `employes`
--
ALTER TABLE `employes`
  ADD CONSTRAINT `AddEmployes` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `SectionFollw` FOREIGN KEY (`SectionID`) REFERENCES `section` (`SectionID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `item`
--
ALTER TABLE `item`
  ADD CONSTRAINT `AddItem` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `CategoryFollow` FOREIGN KEY (`CategoryID`) REFERENCES `category` (`CategoryID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `StoreID` FOREIGN KEY (`StoreID`) REFERENCES `store` (`StoreID`);

--
-- Constraints for table `section`
--
ALTER TABLE `section`
  ADD CONSTRAINT `AddSection` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
