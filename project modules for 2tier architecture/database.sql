-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 09, 2020 at 03:44 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_shopping`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `password`) VALUES
('siva', 'siva1234'),
('gokul', 'gokul1234');

-- --------------------------------------------------------

--
-- Table structure for table `buyed_product`
--

CREATE TABLE `buyed_product` (
  `cus_id` varchar(5) NOT NULL,
  `item_id` varchar(5) NOT NULL,
  `quantity` int(5) NOT NULL,
  `address` text NOT NULL,
  `ordered_date` date NOT NULL,
  `delivery_date` date NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buyed_product`
--

INSERT INTO `buyed_product` (`cus_id`, `item_id`, `quantity`, `address`, `ordered_date`, `delivery_date`, `status`) VALUES
('c101', 'i101', 1, '123,rani street,trichy', '2020-06-16', '2020-06-23', 'Not delivered'),
('c101', 'i101', 2, '123,rani street,trichy', '2020-06-30', '2020-07-07', 'Not delivered'),
('c101', 'i101', 2, '123,rani street,trichy', '2020-06-30', '2020-07-07', 'Not delivered'),
('c101', 'i101', 2, '123,rani street,trichy', '2020-07-04', '2020-07-11', 'Not delivered'),
('c101', 'i104', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Delivered'),
('c101', 'i104', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Delivered'),
('c101', 'i102', 2, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i102', 2, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i102', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i102', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i102', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i102', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i102', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i101', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i101', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i104', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Delivered'),
('c101', 'i102', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i101', 1, '123,rani street,trichy', '2020-07-05', '2020-07-12', 'Not delivered'),
('c101', 'i102', 2, '123,rani street,trichy', '2020-07-07', '2020-07-14', 'Not delivered'),
('c101', 'i104', 1, '123,rani street,trichy', '2020-07-09', '2020-07-16', 'Delivered'),
('c101', 'i102', 2, '123,rani street,trichy', '2020-07-09', '2020-07-16', 'Not delivered'),
('c101', 'i101', 2, '123,rani street,trichy', '2020-07-09', '2020-07-16', 'Not delivered');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cus_id` varchar(5) NOT NULL,
  `item_id` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cus_id`, `item_id`) VALUES
('c101', 'i104'),
('c101', 'i101'),
('c101', 'i101'),
('c101', 'i102'),
('c101', 'i101'),
('c101', 'i101'),
('c101', 'i103');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cus_id` varchar(4) NOT NULL,
  `name` char(15) NOT NULL,
  `phone_no` int(11) NOT NULL,
  `password` varchar(15) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cus_id`, `name`, `phone_no`, `password`, `address`) VALUES
('1000', 'siva', 987654321, 'siva1234', 'sunnambu kara street'),
('c101', 'sk', 987654321, 'sk12', '123,rani street,trichy'),
('i105', 'sksk', 1234568, 'sksk1212', 'trichy'),
('c102', 'gokul', 5433435, 'gokul12', 'santhukadai,trichy'),
('c103', 'gk', 73246872, 'gk12', 'xyz street'),
('c104', 'vijay', 87654321, 'vj12', 'xyz street'),
('c105', 'ajith', 5678987, 'aj12', 'abcd street');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `item_id` varchar(4) NOT NULL,
  `item_name` varchar(20) NOT NULL,
  `price` int(10) NOT NULL,
  `specification` text NOT NULL,
  `quantity` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`item_id`, `item_name`, `price`, `specification`, `quantity`) VALUES
('i101', 'Redmi Note 8 Pro', 9999, '6 GB RAM | 64 GB ROM | Expandable Upto 512 GB\r\n16.59 cm (6.53 inch) Full HD+ Display\r\n64MP + 8MP + 2MP + 2MP | 20MP Front Camera\r\n4500 mAh Li-polymer Battery\r\nMediaTek Helio G90T Processor', 4),
('i102', 'Lenovo K10 Plus', 8999, '4 GB RAM | 64 GB ROM | Expandable Upto 2 TB\r\n15.8 cm (6.22 inch) HD+ Display\r\n13MP + 5MP + 8MP | 16MP Front Camera\r\n4050 mAh Battery\r\nQualcomm SDM632 Processor', 6),
('i103', 'Realme C3', 99993, '3GB RAM 32GB ROM |256Expandable memory |8mp and 13+2+2mp', 10),
('i104', 'Realme Narzo 10A', 9999, '4GB RAM |64 ROM |256Expandable memory |13MP and 13+2+2MP camera', 12),
('i105', 'Motorola One Fusion+', 17499, '6 GB RAM | 128 GB ROM | Expandable Upto 1 TB\r\n16.51 cm (6.5 inch) Full HD+ Display\r\n64MP + 8MP + 5MP + 2MP | 16MP Front Camera\r\n5000 mAh Lithium Polymer Battery\r\nQualcomm Snapdragon 730G Processor', 10),
('i106', 'Vivo U10 (Electric B', 10990, '3 GB RAM | 32 GB ROM | Expandable Upto 256 GB\r\n16.13 cm (6.35 inch) HD+ Display\r\n13MP + 8MP + 2MP | 8MP Front Camera\r\n5000 mAh Li-ion Battery\r\nQualcomm Snapdragon 665 AIE Processor\r\n18 W Fast Charging', 8),
('i107', 'Infinix Hot 9 (Ocean', 8999, '4 GB RAM | 64 GB ROM | Expandable Upto 256 GB\r\n16.76 cm (6.6 inch) HD+ Display\r\n13 MP + 2 MP + 2 MP + Low Light Sensor | 8MP Front Camera\r\n5000 mAh Li-ion Polymer Battery\r\nMediaTek Helio P22 (64 bit) Processor\r\n', 8),
('i108', 'oPPO A9 2020 (Vanill', 14000, '4 GB RAM | 128 GB ROM\r\n16.56 cm (6.52 inch) HD Display\r\n48MP + 8MP + 2MP + 2MP | 16MP Front Camera\r\n5000 mAh Battery\r\nQualcomm SM6125 Processor', 5),
('i109', 'OPPO A31 (Fantasy Wh', 12500, '4 GB RAM | 64 GB ROM | Expandable Upto 256 GB\r\n16.51 cm (6.5 inch) HD+ Display\r\n12MP + 2MP + 2MP | 8MP Front Camera\r\n4230 mAh Battery\r\nMediaTek Helio P35 ((MT6765V/CB) (4 x Cortex-A53L + 4 x Cortex-A53LL) 12 nm 64-bit Processor', 7),
('i110', 'Vivo Z1x (Phantom)', 16900, '6 GB RAM | 64 GB ROM\r\n16.21 cm (6.38 inch) Full HD+ Display\r\n48MP + 8MP + 2MP | 32MP Front Camera\r\n4500 mAh Li-ion Battery\r\nQualcomm Snapdragon 712 AIE Processor\r\n22.5 W Vivo Flash Charge', 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`item_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
