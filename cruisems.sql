create database cruisems;

use cruisems;

create table personalinfo
(first_name varchar(30) not null,
lastname varchar(30) not null,
password varchar(30) not null,
mobno bigint not null,
usrid varchar(30) primary key not null);

create table admin
(username varchar(30) not null,
password varchar(30) not null);

create table booking
(destination varchar(30),
amount bigint);

insert into booking values
("NewYork",100000,'10:30:00'),
("Miami",120000,'09:00:00'),
("Dubai",130000,'12:00:00'),
("HongKong",110000,'15:00:00'),
("UAE",150000,'18:00:00'),
("London",160000,'22:00:00');

create table customer
(noppl int ,
destiantion varchar(30),
dtedep date,
ttlamt int,
usrid varchar(30),
FOREIGN KEY (usrid) references personalinfo(usrid));

insert into personalinfo values
('rahul','barna','rahul781',9865321441,'rahulbarna00'),
('Ram','Sharma','ram123',9875643210,'ramsharma01'),
('Shyam','Raj','shayam012',9875643298,'shyam0412'),
('Dinesh','Kumar','dinesh031',9813213298,'dinesh123'),
('Deepak','Sharma','deepak322',7815643298,'sharma012'),
('Sanjay','Mishra','Mishra012',9764243298,'sanjay098'),
('Rohit','Sharma','sharma012',9875612348,'sharma9431'),
('Yash','Raj','yashraj812',9432643298,'raj0412'),
('Ayaan','Kagdi','kagdi012',9875783198,'ayaan412'),
('Virat','Khan','virat3212',9856321298,'virat912'),
('miraj','shaikh','miraj012',9842643618,'shaikh931'),
('pranav','sharma','pranav321',7975733298,'pranav52'),
('vinay','kohli','vinay831',7981643298,'vinay7412'),
('navdeep','singh','navdeep01',9876543298,'navdeep0101'),
('rishab','kumar','rishab08',9875723198,'rishab0412'),
('Shyam','kumar','shayam921',9823153298,'shyam9871'),
('manas','merala','manas012',9899883298,'manas12'),
('rohit','kamble','rohit321',9875641998,'rohit412'),
('rahul','sharma','rahul63',7986542131,'rahulshrama0021'),
('sachin','kumar','sachin02',99773312345,'sachin0902');
