-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_eventos
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_eventos` ;

-- -----------------------------------------------------
-- Schema esquema_eventos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_eventos` DEFAULT CHARACTER SET utf8 ;
USE `esquema_eventos` ;

-- -----------------------------------------------------
-- Table `esquema_eventos`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_eventos`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(200) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_eventos`.`eventos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_eventos`.`eventos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `location` VARCHAR(100) NULL,
  `date` DATE NULL,
  `details` TEXT NULL,
  `image` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_eventos_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_eventos_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `esquema_eventos`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
