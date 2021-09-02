-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`aluno` (
  `idaluno` INT NOT NULL AUTO_INCREMENT,
  `TP_COR_RACA` INT NOT NULL,
  `TP_SEXO` INT NOT NULL,
  `NU_ANO_NASCIMENTO` INT NOT NULL,
  `NU_MES_NASCIMENTO` INT NOT NULL,
  `NU_DIA_NASCIMENTO` INT NOT NULL,
  `TP_NACIONALIDADE` INT NULL,
  `CO_UF_NASCIMENTO` INT NULL,
  `IN_DEFICIENCIA` INT NOT NULL,
  `TP_ESCOLA_CONCLUSAO_ENS_MEDIO` INT NOT NULL,
  `NU_IDADE` VARCHAR(45) NULL,
  PRIMARY KEY (`idaluno`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`instituicao_ensino_superior`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`instituicao_ensino_superior` (
  `idinstituicao_ensino_superior` INT NOT NULL AUTO_INCREMENT,
  `CO_IES` INT NOT NULL,
  `TP_CATEGORIA_ADMINISTRATIVA` VARCHAR(45) NULL,
  `TP_ORGANIZACAO_ACADEMICA` VARCHAR(45) NULL,
  `CO_UF` VARCHAR(45) NULL,
  PRIMARY KEY (`idinstituicao_ensino_superior`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`curso` (
  `idcurso` INT NOT NULL AUTO_INCREMENT,
  `instituicao_ensino_superior_idinstituicao_ensino_superior` INT NOT NULL,
  `CO_CURSO` VARCHAR(45) NOT NULL,
  `CO_LOCAL_OFERTA` VARCHAR(45) NULL,
  `CO_UF` VARCHAR(45) NULL,
  `CO_MUNICIPIO_NASCIMENTO` VARCHAR(45) NULL,
  `IN_CAPITAL` VARCHAR(45) NULL,
  `NO_CURSO` VARCHAR(45) NOT NULL,
  `TP_SITUACAO` VARCHAR(45) NULL,
  `TP_GRAU_ACADEMICO` VARCHAR(45) NULL,
  `instituicao_ensino_superior_idinstituicao_ensino_superior1` INT NOT NULL,
  PRIMARY KEY (`idcurso`, `instituicao_ensino_superior_idinstituicao_ensino_superior`, `instituicao_ensino_superior_idinstituicao_ensino_superior1`),
  INDEX `fk_curso_instituicao_ensino_superior1_idx` (`instituicao_ensino_superior_idinstituicao_ensino_superior1` ASC) VISIBLE,
  CONSTRAINT `fk_curso_instituicao_ensino_superior1`
    FOREIGN KEY (`instituicao_ensino_superior_idinstituicao_ensino_superior1`)
    REFERENCES `mydb`.`instituicao_ensino_superior` (`idinstituicao_ensino_superior`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`atividade_extra_curricular`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`atividade_extra_curricular` (
  `idatividade_extra_curricular` INT NOT NULL AUTO_INCREMENT,
  `IN_COMPLEMENTAR_ESTAGIO` VARCHAR(45) NULL,
  `IN_COMPLEMENTAR_EXTENSAO` VARCHAR(45) NULL,
  `IN_COMPLEMENTAR_MONITORIA` VARCHAR(45) NULL,
  `IN_COMPLEMENTAR_PESQUISA` VARCHAR(45) NULL,
  `IN_BOLSA_PESQUISA` VARCHAR(45) NULL,
  `IN_BOLSA_MONITORIA` VARCHAR(45) NULL,
  `IN_BOLSA_EXTENSAO` VARCHAR(45) NULL,
  PRIMARY KEY (`idatividade_extra_curricular`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`vaga`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`vaga` (
  `idvaga` INT NOT NULL AUTO_INCREMENT,
  `CO_ALUNO_CURSO` VARCHAR(45) NOT NULL,
  `TP_SITUACAO` VARCHAR(45) NULL,
  `IN_INGRESSO_VESTIBULAR` VARCHAR(45) NULL,
  `IN_INGRESSO_ENEM` VARCHAR(45) NULL,
  `IN_INGRESSO_AVALIACAO_SERIADA` VARCHAR(45) NULL,
  `IN_APOIO_SOCIAL` VARCHAR(45) NULL,
  `TP_SEMESTRE_CONCLUSAO` VARCHAR(45) NULL,
  `TP_SEMESTRE_REFERENCIA` VARCHAR(45) NULL,
  `IN_MATRICULA` VARCHAR(45) NULL,
  `IN_CONCLUINTE` VARCHAR(45) NOT NULL,
  `NU_ANO_INGRESSO` VARCHAR(45) NOT NULL,
  `aluno_idaluno` INT NOT NULL,
  `curso_idcurso` INT NOT NULL,
  `aluno_idaluno1` INT NOT NULL,
  PRIMARY KEY (`idvaga`, `curso_idcurso`, `aluno_idaluno`, `aluno_idaluno1`),
  INDEX `fk_vaga_curso1_idx` (`curso_idcurso` ASC) VISIBLE,
  INDEX `fk_vaga_aluno1_idx` (`aluno_idaluno1` ASC) VISIBLE,
  CONSTRAINT `fk_vaga_curso1`
    FOREIGN KEY (`curso_idcurso`)
    REFERENCES `mydb`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_vaga_aluno1`
    FOREIGN KEY (`aluno_idaluno1`)
    REFERENCES `mydb`.`aluno` (`idaluno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`docente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`docente` (
  `iddocente` INT NOT NULL AUTO_INCREMENT,
  `ID_DOCENTE` VARCHAR(45) NOT NULL,
  `TP_SITUACAO` VARCHAR(45) NOT NULL,
  `TP_ESCOLARIDADE` VARCHAR(45) NULL,
  `TP_REGIME_TRABALHO` VARCHAR(45) NULL,
  `TP_SEXO` VARCHAR(45) NULL,
  `NU_ANO_NASCIMENTO` VARCHAR(45) NULL,
  `NU_MES_NASCIMENTO` VARCHAR(45) NULL,
  `NU_DIA_NASCIMENTO` VARCHAR(45) NULL,
  `NU_IDADE` VARCHAR(45) NULL,
  `TP_COR_RACA` VARCHAR(45) NULL,
  `CO_PAIS_ORIGEM` VARCHAR(45) NULL,
  `TP_NACIONALIDADE` VARCHAR(45) NULL,
  PRIMARY KEY (`iddocente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`docente_has_instituicao_ensino_superior`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`docente_has_instituicao_ensino_superior` (
  `docente_iddocente` INT NOT NULL,
  `instituicao_ensino_superior_idinstituicao_ensino_superior` INT NOT NULL,
  `CO_DOCENTE_IES` VARCHAR(45) NULL,
  PRIMARY KEY (`docente_iddocente`, `instituicao_ensino_superior_idinstituicao_ensino_superior`),
  INDEX `fk_docente_has_instituicao_ensino_superior_instituicao_ensi_idx` (`instituicao_ensino_superior_idinstituicao_ensino_superior` ASC) VISIBLE,
  INDEX `fk_docente_has_instituicao_ensino_superior_docente1_idx` (`docente_iddocente` ASC) VISIBLE,
  CONSTRAINT `fk_docente_has_instituicao_ensino_superior_docente1`
    FOREIGN KEY (`docente_iddocente`)
    REFERENCES `mydb`.`docente` (`iddocente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_docente_has_instituicao_ensino_superior_instituicao_ensino1`
    FOREIGN KEY (`instituicao_ensino_superior_idinstituicao_ensino_superior`)
    REFERENCES `mydb`.`instituicao_ensino_superior` (`CO_IES`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`atividade_extra_curricular_has_aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`atividade_extra_curricular_has_aluno` (
  `atividade_extra_curricular_idatividade_extra_curricular` INT NOT NULL,
  `aluno_idaluno` INT NOT NULL,
  PRIMARY KEY (`atividade_extra_curricular_idatividade_extra_curricular`, `aluno_idaluno`),
  INDEX `fk_atividade_extra_curricular_has_aluno_aluno1_idx` (`aluno_idaluno` ASC) VISIBLE,
  INDEX `fk_atividade_extra_curricular_has_aluno_atividade_extra_cur_idx` (`atividade_extra_curricular_idatividade_extra_curricular` ASC) VISIBLE,
  CONSTRAINT `fk_atividade_extra_curricular_has_aluno_atividade_extra_curri1`
    FOREIGN KEY (`atividade_extra_curricular_idatividade_extra_curricular`)
    REFERENCES `mydb`.`atividade_extra_curricular` (`idatividade_extra_curricular`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atividade_extra_curricular_has_aluno_aluno1`
    FOREIGN KEY (`aluno_idaluno`)
    REFERENCES `mydb`.`aluno` (`idaluno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
