CREATE SCHEMA `brine` ;
INSERT INTO `brine`.`user` (`id`, `password`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES ('1', 'user1', '0', 'user1', 'user', '1', 'gowthamkr18@gmail.com', '0', '1', '2023-05-27 11:19:39.457013');
INSERT INTO `brine`.`user` (`id`, `password`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES ('2', 'user2', '0', 'user2', 'user', '2', 'gowtham.kolekar123@gmail.com', '0', '1', '2023-05-27 11:20:22.904227');


INSERT INTO `brine`.`alert_status` (`id`, `status`, `created_at`, `updated_at`, `is_active`) VALUES ('1', 'Created', '2023-05-27 11:19:39.457013', '2023-05-27 11:19:39.457013', '1');
INSERT INTO `brine`.`alert_status` (`id`, `status`, `created_at`, `updated_at`, `is_active`) VALUES ('2', 'Triggered', '2023-05-27 11:19:39.457013', '2023-05-27 11:19:39.457013', '1');
INSERT INTO `brine`.`alert_status` (`id`, `status`, `created_at`, `updated_at`, `is_active`) VALUES ('3', 'Deleted', '2023-05-27 11:19:39.457013', '2023-05-27 11:19:39.457013', '1');
