-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Scripts: databasv2
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping Data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (1,'SEJ123','BMW','1 Series','Red',1),(2,'NOK456','AUDI','Q3','Yellow',2),(3,'DEK789','VOLKSWAGEN','Bora','Blue',3),(4,'FEN258','SAAB','9-3','White',4),(5,'DPG369','VOLVO','V60','Black',5);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `carsparepart`
--

LOCK TABLES `carssparepart` WRITE;
/*!40000 ALTER TABLE `carssparepart` DISABLE KEYS */;
INSERT INTO `carssparepart` VALUES (1,17),(4,17),(5,18),(2,19),(3,20);
/*!40000 ALTER TABLE `carssparepart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `customers`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'McDonole','Amazonevägen 3 418 78 Göteborg  Västra Götalands län','077789789','MacDonale@gmail.com',1),(2,'SMPP Holding AB','Bersjörnvägen 3 829 91 Ilssbo Gävleborgs län','063998564','SMPP@Holding.com',1),(3,'Valutec Group AB','Lasarettvägen 35 931 41 Skellefteå','079563124','Valutec@Group.com',1),(4,'Geely Sweden Holdings AB','Linnholmsallen 8B 417 55 Göteborg Västra Götalands län','065852369','Geely@Sweden.com',1),(5,'Alicia Bernhaldsson','Ekängsgatan 6  416 47 Göteborg  Västra Götalands län','0737583261','a.bernhaldsson@gmail.com',2),(6,'Patrik Sävdalen','Alégatan 32  425 89  Stockholm','0706778812','sävdalenpatrik@outlook.com',2),(7,'Walter Brown ','Berzeligatan 5  123 56 Olso Norway ','0701905462','walterbrown50@yahoo.com',2),(8,'Magdalena Maggan','Magdalená Nolhagagatan 3  852 69','0707202044 ','magdalena.m.magdalená@msn.com',2);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `customertypes`
--

LOCK TABLES `customertype` WRITE;
/*!40000 ALTER TABLE `customertype` DISABLE KEYS */;
INSERT INTO `customertype` VALUES (1,'Company'),(2,'Private');
/*!40000 ALTER TABLE `customertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `inventories`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,1,'Building 8',100,50,50,'15 days',18),(2,1,'Building 7',150,50,50,'20 days',20),(3,1,'Building 11',200,100,100,'15 days',17),(4,1,'Building 9',180,100,100,'20 days',19);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `manufacturers`
--

LOCK TABLES `manufactor` WRITE;
/*!40000 ALTER TABLE `manufactor` DISABLE KEYS */;
INSERT INTO `manufactor` VALUES (1,'Vehicle Sweden','Saabvägen 5, 461 38 Trollhättan','722654789',2);
/*!40000 ALTER TABLE `manufactor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2020-10-25','10:30:00',1,1),(2,'2020-10-28','12:10:00',3,2),(3,'2020-10-30','13:10:00',4,3),(4,'2020-11-25','14:45:00',1,4),(5,'2020-11-05','15:30:00',2,5);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `orderspareparts`
--

LOCK TABLES `orderssparepart` WRITE;
/*!40000 ALTER TABLE `orderssparepart` DISABLE KEYS */;
/*!40000 ALTER TABLE `orderssparepart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `personaldata`
--

LOCK TABLES `personaldata` WRITE;
/*!40000 ALTER TABLE `personaldata` DISABLE KEYS */;
INSERT INTO `personaldata` VALUES (1,'Aloyna Kanabova','078456258','Aloyna.Kanabova@gmail.com'),(2,'Anna Johansson','078569814','Anna.Johansson@gmail.com'),(3,'Sven Svensson','036456789','Sven.Svensson@gmail.com'),(4,'Johan Annasson','065785125','Johan.Annasson@gmail.com'),(5,'Karl Josefsson','025789523','Karl.Josefsson@gmail.com');
/*!40000 ALTER TABLE `personaldata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `spareparts`
--

LOCK TABLES `sparepart` WRITE;
/*!40000 ALTER TABLE `sparepart` DISABLE KEYS */;
INSERT INTO `sparepart` VALUES (17,'Oil Filter ',1,1,'Oil filter is necessary for internal combustion engine to guarantee quality of oil. The engine needs oil for oiling, but sometimes oil becomes dirty when it is used. Because of soot or wear of metal, foreign particles get into the oil. In addition, oil may become dirty directly before using. As any dirtying damages the engine, an oil filter is installed to remove all foreign substances from the oil. Due to this service life is prolonged.\n\nUsually it is used one oil filter but in some cars there is also lubricating oil fine filter. In this case you may evade necessary changing of oil. Still many car owners must regularly change the oil filter and oil. And you must pay attention to the manufacturer\'s instruction. You must change it after 20.000-30.000 km haul. Oil filter must be changed together with oil. If there remained oil, you can change the filter without any problems. Old filter must be removed by means of a special spanner.\n\nWe recommend you to pay attention to the manufacturer\'s instruction. If oil filter is used for a long period of time, its effect reduces. Moreover, if you repair it by yourself, there may appear problems with car insurance. In isolated cases this may lead to big expenses. You can easily avoid this if you follow the terms of check up. If you need conditioner pipe, receiver-dryer, lamps’ selector relay, air filter, window raiser, flange, fuel tank or another spare part for your car, then our online shop is the very thing you need. In our Internet store you will find all spare parts for the car.'),(18,'Windshield Wipers ',1,1,'Wiper blade is a part of windscreen wiper. Together with wiper, wiper motor and windscreen wiper, wiper blade helps to clean the windscreen and rear window. Wiper blades fit the window glass and function properly if there is enough water. Washing of dry glass can cause damage and accelerate the wear of the blade. Therefore, the blades should be used only with window washer that will moisten the dry surface of the glass. We also recommend using window washer in case of severe contamination. \n\nIn majority of cases blade defect leads to whistling noise or uneven cleaning of the glass. In order that new wiper blade to fit the windscreen wiper, it is necessary to buy original spare car part. Different makers offer blade Models that fit different cars. Buyers must purchase a high quality product, because service life is more important than price of the blade. Car owner can replace the strip without any assistance. You will need maintenance manual and a little patience. \n\nTo replace the blade lift up the windscreen wiper. This will simplify the work. After this you need carefully to put the blade on the glass. For trial testing activate the windscreen wipers or moist the glass with water. You can find other spare car parts in our Internet store. In our online store you can order shock mount, throttle valve sensor, muffler, bellows, radiator, horn, poly-V belt or box body.'),(19,'Shock Absorber',1,1,'Shock absorbers are used not only for comfort. Mostly they serve for safety. Shock absorbers provide between wheel and road and stabilize the car. It is very important when you change direction (turn, for example). Shock absorbers’ functioning is based on transformation of kinetic energy into heat. In modern cars mostly are installed hydraulic shock absorbers in which oil and gas are used. So, there are oil and gas-filled shock absorbers.\n\nIf the steering wheel vibrates when cornering, this is the sign that the shock absorber failed. Another sign that the shock absorber is faulty is worsening of running characteristics. If the car shakes for a long time after the load is removed from it, this also indicates the failure of the shock absorber. One more sign of failure is oil leak. Shock absorber should be replaced after 100 000 km. If it fails before this run, it is necessary to replace it.\n\nIt is necessary to replace both shock absorbers on the same axle. If on the one side there is a new absorber, but on the other an old one, this will worsen running characteristics of the vehicle. Replacement should be done in service centre as it requires special equipment. In our online store there are many inexpensive car parts of high quality. Here you will find damper struts, window lifters, brake disks, brake shoes, turn indicators and taillights. It is worth to compare our prices with those in service centres.'),(20,'Wheel Bearing',1,1,'Wheel Bearing serve to rotate the wheel on the hub with less resistance. They transmit the force applied to rotate the wheel on the axle. On the rear axle bearing modules are often used. When replacing the part, the module is entirely replaced. On the front axle there are installed angular contacts, conical roller, or radial bearings. It depends on the car model. To install and dismantle the wheel bearing a special tool is required. Therefore, it will be necessary to go to the car repair shop if the bearing is faulty.\n\nIn course of time wheel bearings wear out. As the bearing wears out, the noise level increases. Especially loud noise is when cornering. Increased noise level when cornering to the left indicates a faulty on the right side. Sometimes a play can appear because of wear. This problem can be diagnosed. When you turn the wheel press once on the brake and once turn the wheels without brake. If the play occurs in the last case, the problem is with the bearing.\n\nIf there is a faulty, you need to replace the bearing. To repair it you need a special press to press a new bearing in. Do not try to replace the bearing by yourself using a sledgehammer. A defective bearing must be timely replaced as it is dangerous to drive with a faulty bearing. In our Internet shop you will find any spare parts you need for your car: wheel brake cylinder, master cylinder, steering knuckles, brake shoes, window lifters, headlights, air dryer, fuel and oil filters.');
/*!40000 ALTER TABLE `sparepart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `stores`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES (1,'Group8cars Göteborg','Kobbarnas väg 1 Olskroken göteborg','063258789','Group8cars.Goteborg@gmail.com'),(2,'Group8cars Stockholm','Lignagatan 1, 117 34 Stockholm','045123789','Group8cars.Stockholm@gmail.com'),(3,'Group8cars Malmö','Jägersrovägen 100, 200 39 Malmö','069789521','Group8cars.Malmo@gmail.com'),(4,'Group8cars Borås','Skaraborgsvägen 6, 506 30 Borås','073589632','Group8cars.Boras@gmail.com');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `storeemployees`
--

LOCK TABLES `storeemployee` WRITE;
/*!40000 ALTER TABLE `storeemployee` DISABLE KEYS */;
INSERT INTO `storeemployee` VALUES (6,1,5),(7,2,4),(8,3,3),(9,4,2),(10,2,4);
/*!40000 ALTER TABLE `storeemployee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping Data for table `suppliers`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'Components Sweden ','16, Bror Nilssons gata, 417 55 Göteborg','06978945612','Components@Sweden ',1);
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-17 19:43:47
